#!/usr/bin/env python3
"""Phase 1b: Crawl approved URLs from urls_to_review.json.

Reads the approved URL list produced by 01a_search.py (after your review),
then crawls each URL using the same routing logic as the original 01_crawl.py:
  - medium   → Freedium mirror
  - deep     → depth=1, max_pages=5, best_first + semantic scoring
  - shallow  → depth=0, single page

Usage:
    python scripts/01b_crawl.py                          # all topics with review files
    python scripts/01b_crawl.py --topic git-first-job   # single topic
    python scripts/01b_crawl.py --topics git-first-job claude-code-workflow
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from rich.console import Console
from rich.rule import Rule

from crawl4ai_cli.engine import run_job
from crawl4ai_cli.config import SiteConfig, CrawlJobConfig
from crawl4ai_cli.manifest import ManifestCollector
from crawl4ai_cli.writer import write_markdown

QUERIES_FILE = Path(__file__).parent / "01_queries.yaml"
BASE_OUTPUT  = Path(__file__).parent.parent / "01-raw"

FREEDIUM_MIRROR  = "https://freedium-mirror.cfd"
FREEDIUM_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

TOPIC_SCORE_KEYWORDS: dict[str, list[str]] = {
    "github-portfolio":      ["github", "portfolio", "resume", "projects", "open source", "repository"],
    "career-gap":            ["career gap", "employment gap", "resume gap", "returning", "career break"],
    "career-change":         ["career change", "career switch", "bootcamp", "transferable", "non-cs degree"],
    "ats-optimization":      ["ats", "applicant tracking", "resume keywords", "resume scan", "ats friendly"],
    "salary-negotiation":    ["salary", "negotiate", "compensation", "offer", "equity", "rsu"],
    "senior-level-resume":   ["senior", "staff", "principal", "tech lead", "accomplishments", "impact"],
    "executive-resume":      ["cto", "vp", "director", "executive", "leadership", "c-suite"],
    "remote-work-resume":    ["remote", "distributed", "async", "work from home", "remote work"],
    "linkedin-profile":      ["linkedin", "profile", "headline", "summary", "open to work"],
    "cover-letter":          ["cover letter", "covering letter", "application letter"],
    "git-first-job":         ["git", "github", "pull request", "commit", "branch", "merge", "rebase", "workflow"],
    "claude-code-workflow":  ["claude", "claude code", "ai coding", "ai pair programming", "agentic", "llm", "copilot"],
}

console = Console()


def _netloc(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def url_to_path(url: str, output_dir: Path) -> Path:
    parsed   = urlparse(url)
    path_part = re.sub(r"[?#].*", "", parsed.netloc + parsed.path.rstrip("/"))
    return output_dir / (path_part + ".md")


# ── Freedium (Medium) ─────────────────────────────────────────────────────────

def crawl_medium_freedium(url: str, output_dir: Path) -> tuple[bool, int]:
    freedium_url = f"{FREEDIUM_MIRROR}/{url}"
    out_path     = url_to_path(url, output_dir)

    if out_path.exists() and len(out_path.read_text().split()) >= 80:
        console.print(f"  [dim]SKIP (exists)[/dim] {url}")
        return True, 0

    try:
        resp = requests.get(freedium_url, headers=FREEDIUM_HEADERS, timeout=30)
        if resp.status_code != 200:
            console.print(f"  [red]FAIL [{resp.status_code}][/red] {url}")
            return False, 0

        soup    = BeautifulSoup(resp.text, "html.parser")
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
        wc      = len(content.split())

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


# ── Crawl approved URLs for one topic ────────────────────────────────────────

async def crawl_topic(name: str, output_dir: Path, approved_urls: list[dict]) -> None:
    console.print(Rule(f"[bold cyan]{name}[/bold cyan]"))

    medium_urls  = [u for u in approved_urls if u["suggested_type"] == "medium"]
    deep_urls    = [u for u in approved_urls if u["suggested_type"] == "deep"]
    shallow_urls = [u for u in approved_urls if u["suggested_type"] == "shallow"]

    console.print(
        f"  [green]{len(shallow_urls)} shallow[/green]  "
        f"[cyan]{len(deep_urls)} deep[/cyan]  "
        f"[magenta]{len(medium_urls)} medium→freedium[/magenta]"
    )

    # ── Freedium pass ────────────────────────────────────────────────────────
    if medium_urls:
        console.print(f"\n[magenta]Freedium pass — {len(medium_urls)} Medium articles[/magenta]")
        ok_m = fail_m = 0
        for i, u in enumerate(medium_urls):
            success, _ = crawl_medium_freedium(u["url"], output_dir)
            ok_m += success
            fail_m += not success
            if i < len(medium_urls) - 1:
                time.sleep(2.0)
        console.print(f"  Medium: [green]{ok_m} OK[/green]  [red]{fail_m} failed[/red]")

    # ── Normal crawl pass ────────────────────────────────────────────────────
    normal_urls = deep_urls + shallow_urls
    if not normal_urls:
        return

    score_kws = TOPIC_SCORE_KEYWORDS.get(name, [])
    sites = []
    for u in normal_urls:
        url  = u["url"]
        if u["suggested_type"] == "deep":
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
        wc    = len(str(result.markdown).split()) if result.markdown else 0
        title = (result.metadata or {}).get("title", "")
        manifest.add_page(url=result.url, filepath=filepath, depth=depth,
                          word_count=wc, status=status, title=title, retries=retries)

    all_stats = await run_job(job, on_result=on_result)
    crawled   = sum(s.pages_crawled for s in all_stats)
    failed    = sum(s.pages_failed  for s in all_stats)
    console.print(f"  Normal: [green]{crawled} crawled[/green]  [red]{failed} failed[/red] → {output_dir}")


# ── Entry point ───────────────────────────────────────────────────────────────

async def main(names: list[str] | None) -> None:
    data   = yaml.safe_load((Path(__file__).parent / "01_queries.yaml").read_text())
    topics = data["topics"]

    if names:
        missing = [n for n in names if n not in topics]
        if missing:
            console.print(f"[red]Unknown topics: {missing}[/red]")
            return
        topics = {n: topics[n] for n in names}

    console.print(f"\n[bold]Phase 1b — Crawl[/bold]: {len(topics)} topic(s)\n")

    tasks = []
    for name, cfg in topics.items():
        output_dir  = BASE_OUTPUT / cfg.get("output_dir", f"01-raw/{name}").split("/")[-1]
        review_file = output_dir / "urls_to_review.json"

        if not review_file.exists():
            console.print(f"[yellow]SKIP {name}[/yellow] — urls_to_review.json not found. Run 01a_search.py first.")
            continue

        review      = json.loads(review_file.read_text())
        approved    = [u for u in review["urls"] if u.get("approved", False)]

        if not approved:
            console.print(f"[yellow]SKIP {name}[/yellow] — no approved URLs.")
            continue

        console.print(f"  {name}: {len(approved)} approved URLs")
        tasks.append(crawl_topic(name, output_dir, approved))

    if tasks:
        await asyncio.gather(*tasks)

    console.print(Rule("[bold green]Phase 1b complete[/bold green]"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 1b: Crawl approved URLs")
    group  = parser.add_mutually_exclusive_group()
    group.add_argument("--topic",  metavar="NAME", help="Single topic")
    group.add_argument("--topics", metavar="NAME", nargs="+", help="Multiple topics")
    args   = parser.parse_args()

    names = [args.topic] if args.topic else args.topics
    asyncio.run(main(names))
