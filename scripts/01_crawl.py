#!/usr/bin/env python3
"""Phase 1: Crawl URLs from search_metadata.json files per topic.

Routing:
  - Medium       → Freedium mirror (bypasses paywall, no browser needed)
  - Reddit       → crawl4ai with auto_tune=True (JS comment expansion built-in)
  - YouTube / LinkedIn / Quora → skipped (no useful text content)
  - Everything else → normal crawl4ai with stealth

Usage:
    python scripts/01_crawl.py                          # all topics
    python scripts/01_crawl.py --topic github-portfolio # single topic
    python scripts/01_crawl.py --dry-run                # show counts, no crawl
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from rich.console import Console
from rich.rule import Rule

from crawl4ai_cli.search import search_urls, save_search_metadata
from crawl4ai_cli.engine import run_job
from crawl4ai_cli.config import SiteConfig, CrawlJobConfig
from crawl4ai_cli.manifest import ManifestCollector
from crawl4ai_cli.writer import write_markdown

QUERIES_FILE = Path(__file__).parent / "01_queries.yaml"
BASE_OUTPUT = Path(__file__).parent.parent / "01-raw"

FREEDIUM_MIRROR = "https://freedium-mirror.cfd"
FREEDIUM_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

SKIP_DOMAINS = {"youtube.com", "youtu.be", "linkedin.com", "quora.com"}

# Domains where following links 1 level deeper yields more on-topic content
DEEP_CRAWL_DOMAINS = {
    # Resume builder blogs
    "zety.com", "enhancv.com", "novoresume.com", "resumelab.com",
    "kickresume.com", "topresume.com", "livecareer.com",
    "resumegenius.com", "resumeworded.com",
    # Career advice hubs
    "themuse.com", "thebalancemoney.com", "thebalancecareers.com",
    "glassdoor.com", "vault.com", "careersidekick.com",
    # Dev career sites
    "dev.to", "hashnode.dev", "hashnode.com",
    # Docs
    "docs.github.com",
}

# Keywords for semantic scoring of linked pages per topic
TOPIC_SCORE_KEYWORDS: dict[str, list[str]] = {
    "github-portfolio":   ["github", "portfolio", "resume", "projects", "open source", "repository"],
    "career-gap":         ["career gap", "employment gap", "resume gap", "returning", "career break"],
    "career-change":      ["career change", "career switch", "bootcamp", "transferable", "non-cs degree"],
    "ats-optimization":   ["ats", "applicant tracking", "resume keywords", "resume scan", "ats friendly"],
    "salary-negotiation": ["salary", "negotiate", "compensation", "offer", "equity", "rsu"],
    "senior-level-resume":["senior", "staff", "principal", "tech lead", "accomplishments", "impact"],
    "executive-resume":   ["cto", "vp", "director", "executive", "leadership", "c-suite"],
    "remote-work-resume": ["remote", "distributed", "async", "work from home", "remote work"],
    "linkedin-profile":   ["linkedin", "profile", "headline", "summary", "open to work"],
    "cover-letter":       ["cover letter", "covering letter", "application letter"],
}

console = Console()


# ── Domain helpers ────────────────────────────────────────────────────────────

def _netloc(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")

def is_skip(url: str) -> bool:
    d = _netloc(url)
    return any(s in d for s in SKIP_DOMAINS)

def is_medium(url: str) -> bool:
    return "medium.com" in _netloc(url)

def is_deep_crawl_worthy(url: str) -> bool:
    d = _netloc(url)
    return any(d == deep or d.endswith("." + deep) for deep in DEEP_CRAWL_DOMAINS)

def url_to_path(url: str, output_dir: Path) -> Path:
    parsed = urlparse(url)
    path_part = re.sub(r"[?#].*", "", parsed.netloc + parsed.path.rstrip("/"))
    return output_dir / (path_part + ".md")


# ── Freedium (Medium) ─────────────────────────────────────────────────────────

def crawl_medium_freedium(url: str, output_dir: Path) -> tuple[bool, int]:
    freedium_url = f"{FREEDIUM_MIRROR}/{url}"
    out_path = url_to_path(url, output_dir)

    if out_path.exists() and len(out_path.read_text().split()) >= 80:
        console.print(f"  [dim]SKIP (exists)[/dim] {url}")
        return True, 0

    try:
        resp = requests.get(freedium_url, headers=FREEDIUM_HEADERS, timeout=30)
        if resp.status_code != 200:
            console.print(f"  [red]FAIL [{resp.status_code}][/red] {url}")
            return False, 0

        soup = BeautifulSoup(resp.text, "html.parser")
        article = (
            soup.find("article")
            or soup.find("div", class_="main-content")
            or soup.find("div", class_="post-content")
            or soup.find("main")
        )
        if not article:
            article = soup.find("body")
            if article:
                for tag in article.find_all(["nav", "header", "footer", "aside", "script", "style"]):
                    tag.decompose()

        if not article:
            console.print(f"  [red]FAIL [no content][/red] {url}")
            return False, 0

        content = md(str(article), heading_style="ATX")
        content = re.sub(r"\n{4,}", "\n\n\n", content).strip()
        wc = len(content.split())

        if wc < 80:
            console.print(f"  [yellow]SKIP [{wc}w short][/yellow] {url}")
            return False, 0

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content + "\n")
        console.print(f"  [green]OK [{wc:>5}w][/green] {url}")
        return True, wc

    except Exception as e:
        console.print(f"  [red]ERR [{e}][/red] {url}")
        return False, 0


# ── Topic loading ─────────────────────────────────────────────────────────────

def load_topics(only: str | None = None) -> dict:
    data = yaml.safe_load(QUERIES_FILE.read_text())
    topics = data["topics"]
    if only:
        if only not in topics:
            console.print(f"[red]Topic '{only}' not found.[/red]")
            sys.exit(1)
        return {only: topics[only]}
    return topics

def load_urls_from_metadata(output_dir: Path) -> list[dict]:
    """Load URLs from existing search_metadata.json (from dry-run)."""
    meta = output_dir / "search_metadata.json"
    if meta.exists():
        return json.loads(meta.read_text()).get("urls", [])
    return []


# ── Main per-topic processor ──────────────────────────────────────────────────

async def process_topic(name: str, cfg: dict, dry_run: bool, force_rescan: bool = False) -> None:
    console.print(Rule(f"[bold cyan]{name}[/bold cyan]"))

    output_dir = BASE_OUTPUT / cfg.get("output_dir", f"01-raw/{name}").split("/")[-1]
    queries: list[str] = cfg["queries"]

    # Load from existing metadata unless --force-rescan
    saved = [] if force_rescan else load_urls_from_metadata(output_dir)
    if saved:
        console.print(f"[dim]Loaded {len(saved)} URLs from existing metadata[/dim]")
        all_urls = [u["url"] for u in saved]
    else:
        results = search_urls(topic=name, query_variants=queries,
                              results_per_query=15, console=console)
        save_search_metadata(results, name, queries, str(output_dir))
        all_urls = [r.url for r in results]

    # Classify URLs
    skip_urls    = [u for u in all_urls if is_skip(u)]
    medium_urls  = [u for u in all_urls if not is_skip(u) and is_medium(u)]
    normal_urls  = [u for u in all_urls if not is_skip(u) and not is_medium(u)]

    deep_urls  = [u for u in normal_urls if is_deep_crawl_worthy(u)]
    shallow_urls = [u for u in normal_urls if not is_deep_crawl_worthy(u)]
    console.print(
        f"  [green]{len(shallow_urls)} shallow[/green]  "
        f"[cyan]{len(deep_urls)} deep[/cyan]  "
        f"[magenta]{len(medium_urls)} medium→freedium[/magenta]  "
        f"[dim]{len(skip_urls)} skipped (YT/LI/Quora)[/dim]"
    )

    if dry_run:
        console.print("[yellow]--dry-run: skipping crawl[/yellow]")
        return

    # ── Freedium pass (Medium) ────────────────────────────────────────────────
    if medium_urls:
        console.print(f"\n[magenta]Freedium pass — {len(medium_urls)} Medium articles[/magenta]")
        ok_m = fail_m = 0
        for i, url in enumerate(medium_urls):
            success, _ = crawl_medium_freedium(url, output_dir)
            if success:
                ok_m += 1
            else:
                fail_m += 1
            if i < len(medium_urls) - 1:
                time.sleep(2.0)
        console.print(f"  Medium: [green]{ok_m} OK[/green]  [red]{fail_m} failed[/red]")

    # ── Normal crawl pass ────────────────────────────────────────────────────
    if normal_urls:
        score_kws = TOPIC_SCORE_KEYWORDS.get(name, [])
        deep_count = sum(1 for u in normal_urls if is_deep_crawl_worthy(u))
        if deep_count:
            console.print(f"  [cyan]{deep_count} URLs → deep crawl (depth=1, best_first)[/cyan]")

        sites = []
        for url in normal_urls:
            if is_deep_crawl_worthy(url):
                sites.append(SiteConfig(
                    url=url,
                    max_depth=1,
                    max_pages=5,
                    domain_only=True,
                    crawl_strategy="best_first",
                    score_keywords=score_kws,
                    content_relevance_threshold=0.3,
                    auto_tune=True,
                    wait_until="domcontentloaded",
                    page_timeout=30,
                    skip_locale_duplicates=True,
                    deduplicate_content=True,
                ))
            else:
                sites.append(SiteConfig(
                    url=url,
                    max_depth=0,
                    max_pages=1,
                    domain_only=False,
                    auto_tune=True,
                    wait_until="domcontentloaded",
                    page_timeout=30,
                    skip_locale_duplicates=True,
                    deduplicate_content=True,
                ))

        job = CrawlJobConfig(
            sites=sites,
            output_dir=str(output_dir),
            delay=1.0,
            concurrency=4,
            pruning_threshold=0.30,
            markdown_format="fit",
            min_word_count=30,
            stealth=True,
            verbose=False,
            generate_manifest=True,
        )

        manifest = ManifestCollector()

        async def on_result(result, site: SiteConfig, depth: int, retries: int) -> None:
            if not result.success:
                err = getattr(result, "error_message", None) or "Unknown error"
                manifest.add_page(url=result.url, filepath=None, depth=depth,
                                  status="failed", retries=retries, error=err)
                return
            filepath, status = write_markdown(
                url=result.url, result=result, output_dir=job.output_dir,
                format=job.markdown_format, depth=depth, min_word_count=job.min_word_count,
            )
            wc = len(str(result.markdown).split()) if result.markdown else 0
            title = (result.metadata or {}).get("title", "")
            manifest.add_page(url=result.url, filepath=filepath, depth=depth,
                              word_count=wc, status=status, title=title, retries=retries)

        all_stats = await run_job(job, on_result=on_result)
        crawled = sum(s.pages_crawled for s in all_stats)
        failed  = sum(s.pages_failed  for s in all_stats)
        console.print(f"  Normal: [green]{crawled} crawled[/green]  [red]{failed} failed[/red] → {output_dir}")


# ── Entry point ───────────────────────────────────────────────────────────────

async def main(only: str | None, dry_run: bool, parallel: int = 3, force_rescan: bool = False) -> None:
    topics = load_topics(only)
    console.print(f"\n[bold]Phase 1 — Crawl[/bold]: {len(topics)} topic(s), {parallel} topics in parallel\n")

    sem = asyncio.Semaphore(parallel)

    async def bounded(name, cfg):
        async with sem:
            await process_topic(name, cfg, dry_run, force_rescan)

    await asyncio.gather(*[bounded(n, c) for n, c in topics.items()])
    console.print(Rule("[bold green]Phase 1 complete[/bold green]"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", metavar="NAME", help="Single topic only")
    parser.add_argument("--dry-run", action="store_true", help="Count URLs, skip crawl")
    parser.add_argument("--force-rescan", action="store_true", help="Re-search SearXNG even if metadata exists")
    args = parser.parse_args()
    asyncio.run(main(only=args.topic, dry_run=args.dry_run, force_rescan=args.force_rescan))
