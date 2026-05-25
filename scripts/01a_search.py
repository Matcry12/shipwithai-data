#!/usr/bin/env python3
"""Phase 1a: Search SearXNG for new topics → export URLs for review.

Outputs per topic:
    01-raw/<topic>/urls_to_review.json   — structured URL list for review
    01-raw/<topic>/search_metadata.json  — raw SearXNG metadata

After running, review the JSON with Claude, approve/remove/add URLs,
then run 01b_crawl.py to crawl the approved list.

Usage:
    python scripts/01a_search.py                         # all topics in YAML
    python scripts/01a_search.py --topic git-first-job   # single topic
    python scripts/01a_search.py --topics git-first-job claude-code-workflow
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import yaml
from rich.console import Console
from rich.table import Table
from rich.rule import Rule

from crawl4ai_cli.search import search_urls, save_search_metadata

QUERIES_FILE = Path(__file__).parent / "01_queries.yaml"
BASE_OUTPUT  = Path(__file__).parent.parent / "01-raw"

SKIP_DOMAINS = {"youtube.com", "youtu.be", "linkedin.com", "quora.com"}

DEEP_CRAWL_DOMAINS = {
    "zety.com", "enhancv.com", "novoresume.com", "resumelab.com",
    "kickresume.com", "topresume.com", "livecareer.com",
    "resumegenius.com", "resumeworded.com",
    "themuse.com", "thebalancemoney.com", "thebalancecareers.com",
    "glassdoor.com", "vault.com", "careersidekick.com",
    "dev.to", "hashnode.dev", "hashnode.com", "docs.github.com",
    "shipwithai.io",
}

console = Console()


def _netloc(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def classify_url(url: str) -> str:
    d = _netloc(url)
    if any(s in d for s in SKIP_DOMAINS):
        return "skip"
    if "medium.com" in d:
        return "medium"
    if any(d == deep or d.endswith("." + deep) for deep in DEEP_CRAWL_DOMAINS):
        return "deep"
    return "shallow"


def load_topics(names: list[str] | None = None) -> dict:
    data = yaml.safe_load(QUERIES_FILE.read_text())
    topics = data["topics"]
    if names:
        missing = [n for n in names if n not in topics]
        if missing:
            console.print(f"[red]Unknown topics: {missing}[/red]")
            sys.exit(1)
        return {n: topics[n] for n in names}
    return topics


def search_topic(name: str, cfg: dict) -> list[dict]:
    queries: list[str] = cfg["queries"]
    output_dir = BASE_OUTPUT / cfg.get("output_dir", f"01-raw/{name}").split("/")[-1]
    output_dir.mkdir(parents=True, exist_ok=True)

    console.print(f"\n[cyan]Searching:[/cyan] {name} ({len(queries)} queries)")
    results = search_urls(topic=name, query_variants=queries,
                          results_per_query=15, console=console)
    save_search_metadata(results, name, queries, str(output_dir))

    seen_domains: set[str] = set()
    urls: list[dict] = []

    # Seed URLs — always approved, always deep
    for seed in cfg.get("seed_urls", []):
        d = _netloc(seed)
        seen_domains.add(d)
        urls.append({
            "url":            seed,
            "domain":         d,
            "suggested_type": "deep",
            "approved":       True,
            "source":         "seed",
            "notes":          "hardcoded seed — bypasses review",
        })

    # SearXNG results — deduplicated per domain
    for r in results:
        url = r.url
        d   = _netloc(url)
        if d in seen_domains:
            continue
        seen_domains.add(d)
        ctype = classify_url(url)
        urls.append({
            "url":            url,
            "domain":         d,
            "suggested_type": ctype,
            "approved":       ctype != "skip",
            "source":         "searxng",
            "notes":          "",
        })

    review_path = output_dir / "urls_to_review.json"
    review_path.write_text(json.dumps({
        "topic":        name,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "urls":         urls,
    }, indent=2))

    return urls


def print_table(name: str, urls: list[dict]) -> None:
    console.print(Rule(f"[bold]{name}[/bold]"))
    t = Table(show_header=True, header_style="bold magenta")
    t.add_column("#",        width=4,  justify="right")
    t.add_column("Type",     width=8)
    t.add_column("Source",   width=8)
    t.add_column("Domain",   width=30)
    t.add_column("URL",      no_wrap=False)

    type_color = {"deep": "cyan", "shallow": "green", "medium": "magenta", "skip": "dim"}
    for i, u in enumerate(urls, 1):
        color = type_color.get(u["suggested_type"], "white")
        approved_marker = "" if u["approved"] else " [dim](skip)[/dim]"
        t.add_row(
            str(i),
            f"[{color}]{u['suggested_type']}[/{color}]",
            u["source"],
            u["domain"],
            u["url"] + approved_marker,
        )
    console.print(t)
    approved = sum(1 for u in urls if u["approved"])
    console.print(f"  Total: {len(urls)}  |  Approved: {approved}  |  Skipped: {len(urls)-approved}\n")


def main(names: list[str] | None) -> None:
    topics = load_topics(names)
    console.print(f"\n[bold]Phase 1a — Search[/bold]: {len(topics)} topic(s)\n")

    for name, cfg in topics.items():
        urls = search_topic(name, cfg)
        print_table(name, urls)

    console.print(Rule("[bold green]Phase 1a complete[/bold green]"))
    console.print("\nReview the tables above, then edit urls_to_review.json in each topic folder.")
    console.print("Run [bold]python scripts/01b_crawl.py[/bold] to crawl approved URLs.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 1a: Search → export URLs for review")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--topic",  metavar="NAME", help="Single topic")
    group.add_argument("--topics", metavar="NAME", nargs="+", help="Multiple topics")
    args = parser.parse_args()

    names = [args.topic] if args.topic else args.topics
    main(names)
