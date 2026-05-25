"""
M1 — shipwithai_recrawl.

Re-crawl every source_url found in 01-raw/**/*.md frontmatter using crawl4ai
with Fit Markdown mode (PruningContentFilter). Writes to 01-raw-v2/ mirroring
the input directory layout. Failures land in 01-raw-v2-failed/<slug>/reason.txt.

Deterministic, no LLM. Idempotent on output paths unless --force is passed.

Politeness defaults (baked in, per PRD): 3 concurrent, ~1 req/sec/domain via
crawl4ai's MemoryAdaptiveDispatcher rate limiter, 2 retries with backoff.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import yaml
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher, RateLimiter
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


CRAWLER_TAG = "crawl4ai-fit-md"
CONCURRENCY = 3
PER_DOMAIN_DELAY_SEC = 1.0
MAX_RETRIES = 2


@dataclass
class SourceEntry:
    source_url: str
    topic: str
    source_domain: str
    slug: str
    rel_subpath: Path  # path relative to 01-raw root, used to mirror layout
    original_frontmatter: dict


@dataclass
class RecrawlReport:
    kept: int = 0
    failed: int = 0
    skipped: int = 0
    duplicates_dropped: int = 0
    failures: list[dict] = field(default_factory=list)

    def __str__(self) -> str:
        return (
            f"RecrawlReport(kept={self.kept}, failed={self.failed}, "
            f"skipped={self.skipped}, duplicates_dropped={self.duplicates_dropped})"
        )


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Empty dict if no frontmatter."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    fm_block = text[4:end]
    body = text[end + 5 :]
    fm = yaml.safe_load(fm_block) or {}
    if not isinstance(fm, dict):
        return {}, text
    return fm, body


def _dump_frontmatter(fm: dict, body: str) -> str:
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n" + body


def discover_sources(input_root: Path) -> list[SourceEntry]:
    """Walk 01-raw and build SourceEntry per markdown file with a source_url."""
    entries: list[SourceEntry] = []
    for md in sorted(input_root.rglob("*.md")):
        rel = md.relative_to(input_root)
        parts = rel.parts
        if len(parts) < 3:
            continue  # expected topic/domain/.../file.md
        topic = parts[0]
        source_domain = parts[1]
        slug = md.stem
        raw_text = md.read_text(encoding="utf-8", errors="replace")
        fm, _ = _parse_frontmatter(raw_text)
        url = fm.get("source_url")
        if not url:
            continue
        entries.append(
            SourceEntry(
                source_url=url,
                topic=topic,
                source_domain=source_domain,
                slug=slug,
                rel_subpath=rel,
                original_frontmatter=fm,
            )
        )
    return entries


def dedupe_by_url(
    entries: list[SourceEntry], log: list[str]
) -> tuple[list[SourceEntry], int]:
    seen: dict[str, SourceEntry] = {}
    duplicates = 0
    for e in entries:
        if e.source_url in seen:
            duplicates += 1
            kept = seen[e.source_url]
            log.append(
                f"DUP url={e.source_url} kept={kept.topic}/{kept.slug} "
                f"dropped={e.topic}/{e.slug}"
            )
            continue
        seen[e.source_url] = e
    return list(seen.values()), duplicates


def output_path_for(entry: SourceEntry, output_root: Path) -> Path:
    return output_root / entry.rel_subpath


def failure_path_for(entry: SourceEntry, failed_root: Path) -> Path:
    # group failures by slug under a directory so reason.txt sits beside the
    # slug; if the same slug appears in multiple topics they'd collide, so
    # include topic in the dir name
    return failed_root / f"{entry.topic}__{entry.slug}" / "reason.txt"


def write_success(entry: SourceEntry, fit_md: str, output_root: Path) -> None:
    fm = dict(entry.original_frontmatter)
    fm["topic"] = entry.topic
    fm["source_domain"] = entry.source_domain
    fm["slug"] = entry.slug
    fm["re_crawled_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    fm["crawler"] = CRAWLER_TAG
    fm["fetch_status"] = 200
    out = output_path_for(entry, output_root)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_dump_frontmatter(fm, fit_md), encoding="utf-8")


def write_failure(
    entry: SourceEntry,
    failed_root: Path,
    http_status: int | None,
    error: str,
    attempt_count: int,
) -> dict:
    path = failure_path_for(entry, failed_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "url": entry.source_url,
        "http_status": http_status,
        "error": error,
        "attempt_count": attempt_count,
        "topic": entry.topic,
        "slug": entry.slug,
    }
    path.write_text(json.dumps(record, indent=2), encoding="utf-8")
    return record


async def crawl_batch(entries: list[SourceEntry]) -> dict[str, object]:
    """Crawl every entry once. Returns {source_url: crawl4ai_result}."""
    md_gen = DefaultMarkdownGenerator(content_filter=PruningContentFilter())
    run_config = CrawlerRunConfig(
        markdown_generator=md_gen,
        cache_mode=CacheMode.BYPASS,
        excluded_tags=["nav", "header", "footer", "aside", "form"],
        remove_overlay_elements=True,
        remove_consent_popups=True,
        process_iframes=True,
        remove_forms=True,
        exclude_social_media_links=True,
        word_count_threshold=10,
        scan_full_page=True,
        verbose=False,
    )
    dispatcher = MemoryAdaptiveDispatcher(
        max_session_permit=CONCURRENCY,
        memory_threshold_percent=85.0,
        rate_limiter=RateLimiter(
            base_delay=(PER_DOMAIN_DELAY_SEC, PER_DOMAIN_DELAY_SEC + 0.5),
            max_retries=MAX_RETRIES,
        ),
    )

    results_by_url: dict[str, object] = {}
    urls = [e.source_url for e in entries]
    browser_config = BrowserConfig(headless=True)
    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun_many(
            urls=urls, config=run_config, dispatcher=dispatcher
        )
        if not isinstance(results, list):
            results = [results]
        for r in results:
            url = getattr(r, "url", "") or ""
            results_by_url[url] = r
    return results_by_url


def extract_fit_markdown(result) -> str | None:
    md = getattr(result, "markdown", None)
    if md is None:
        return None
    fit = getattr(md, "fit_markdown", None)
    if fit:
        return fit
    # fallback: raw_markdown is better than nothing for our diagnostics
    raw = getattr(md, "raw_markdown", None)
    return raw


async def run(
    input_root: Path,
    output_root: Path,
    failed_root: Path,
    *,
    force: bool = False,
    limit: int | None = None,
) -> RecrawlReport:
    report = RecrawlReport()

    log: list[str] = []
    entries = discover_sources(input_root)
    print(f"discovered {len(entries)} entries with source_url", file=sys.stderr)

    entries, duplicates = dedupe_by_url(entries, log)
    report.duplicates_dropped = duplicates
    print(f"unique URLs: {len(entries)} (dropped {duplicates} duplicates)", file=sys.stderr)

    # Idempotency: skip entries whose output already exists, unless --force
    to_crawl: list[SourceEntry] = []
    for e in entries:
        out = output_path_for(e, output_root)
        if out.exists() and not force:
            report.skipped += 1
        else:
            to_crawl.append(e)
    print(f"to crawl: {len(to_crawl)} (skipped {report.skipped} existing)", file=sys.stderr)

    if limit is not None:
        to_crawl = to_crawl[:limit]
        print(f"limit applied: crawling first {len(to_crawl)}", file=sys.stderr)

    if not to_crawl:
        for line in log:
            print(line, file=sys.stderr)
        return report

    output_root.mkdir(parents=True, exist_ok=True)
    failed_root.mkdir(parents=True, exist_ok=True)

    # Group by domain so we crawl one domain's URLs before moving on — keeps
    # per-domain RPS naturally low even though concurrency is global
    by_domain: dict[str, list[SourceEntry]] = defaultdict(list)
    for e in to_crawl:
        host = urlparse(e.source_url).netloc.lower()
        by_domain[host].append(e)

    for host, group in by_domain.items():
        print(f"crawling {len(group)} URLs from {host}", file=sys.stderr)
        results_by_url = await crawl_batch(group)
        for entry in group:
            result = results_by_url.get(entry.source_url)
            if result is None:
                rec = write_failure(
                    entry, failed_root,
                    http_status=None,
                    error="no result returned from crawl4ai",
                    attempt_count=MAX_RETRIES + 1,
                )
                report.failed += 1
                report.failures.append(rec)
                continue
            success = getattr(result, "success", False)
            status_code = getattr(result, "status_code", None)
            if not success:
                err = getattr(result, "error_message", "unknown error")
                rec = write_failure(
                    entry, failed_root,
                    http_status=status_code,
                    error=str(err),
                    attempt_count=MAX_RETRIES + 1,
                )
                report.failed += 1
                report.failures.append(rec)
                continue
            fit_md = extract_fit_markdown(result)
            if not fit_md or not fit_md.strip():
                rec = write_failure(
                    entry, failed_root,
                    http_status=status_code,
                    error="empty fit_markdown",
                    attempt_count=1,
                )
                report.failed += 1
                report.failures.append(rec)
                continue
            write_success(entry, fit_md, output_root)
            report.kept += 1

    for line in log:
        print(line, file=sys.stderr)
    return report


def main() -> None:
    here = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="M1 — re-crawl shipwithai source URLs")
    parser.add_argument("--input", default=str(here / "01-raw"), help="path to 01-raw root")
    parser.add_argument("--output", default=str(here / "01-raw-v2"), help="path to 01-raw-v2 root")
    parser.add_argument("--failed", default=str(here / "01-raw-v2-failed"), help="path to failed-URL dir")
    parser.add_argument("--force", action="store_true", help="re-crawl even if output exists")
    parser.add_argument("--limit", type=int, default=None, help="cap number of URLs crawled (for testing)")
    args = parser.parse_args()

    report = asyncio.run(
        run(
            Path(args.input),
            Path(args.output),
            Path(args.failed),
            force=args.force,
            limit=args.limit,
        )
    )
    print(str(report))


if __name__ == "__main__":
    main()
