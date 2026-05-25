#!/usr/bin/env python3
"""
Pipeline V2 — Stage 1 (fetch) + Stage 2 (extract).

seed_urls.jsonl  →  work/01-extracted/<slug>-<hash>.json   (partial objects)

Stage 1 FETCH:   crawl4ai end-to-end. Headless Chrome renders every page (JS
                 SPAs + anti-bot), parallelized via arun_many +
                 MemoryAdaptiveDispatcher + RateLimiter (native concurrency,
                 memory back-pressure, per-domain politeness, retries).
Stage 2 EXTRACT: trafilatura.bare_extraction on the rendered HTML → markdown +
                 rich metadata (title/author/date/description). Fallback:
                 trafilatura → readability-lxml.

Fully LLM-free and deterministic. Downstream stages (normalize, hierarchy,
enrich, structure, gate, emit) consume these partial objects.

Run with the cv-rag venv:
    cv-rag/.venv/bin/python scripts/v2/fetch_extract.py --limit 5
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urljoin

import trafilatura
from lxml import html as lxml_html

try:
    from readability import Document as ReadabilityDocument
except Exception:  # pragma: no cover
    ReadabilityDocument = None

# ─────────────────────────── config ───────────────────────────
STAGE_VERSION = "fetch-extract-2.0.0"
MIN_EXTRACT_WORDS = 50          # below this after all fallbacks → extract-failed
DEFAULT_CONCURRENCY = 4         # parallel browser sessions (max_session_permit)
PER_DOMAIN_MIN_DELAY = 1.0
PER_DOMAIN_MAX_DELAY = 2.0
MAX_RETRIES = 2
PAGE_TIMEOUT_MS = 45000

ROOT = Path(__file__).resolve().parents[2]   # shipwithai-data/
DEFAULT_SEED = ROOT / "seed_urls.jsonl"
DEFAULT_OUT = ROOT / "work" / "01-extracted"


# ─────────────────────────── model ───────────────────────────
@dataclass
class ExtractRecord:
    source_url: str
    source_domain: str
    topic: str
    fetched_at: str
    http_status: int
    fetch_method: str          # "crawl4ai" | "failed"
    extractor: str             # "trafilatura-2.0" | "readability" | "none"
    markdown: str
    base_metadata: dict
    links: list
    word_count: int
    status: str                # "extracted" | "fetch-failed" | "extract-failed"
    error: str | None = None


# ─────────────────────────── helpers ───────────────────────────
_slug_re = re.compile(r"[^a-z0-9]+")


def make_filename(url: str) -> str:
    path = urlparse(url).path.rstrip("/")
    last = path.rsplit("/", 1)[-1] if path else urlparse(url).netloc
    slug = _slug_re.sub("-", last.lower()).strip("-")[:60] or "page"
    h = hashlib.sha256(url.encode()).hexdigest()[:8]
    return f"{slug}-{h}.json"


def word_count(text: str) -> int:
    return len(text.split()) if text else 0


def extract_links(html_text: str, base_url: str, limit: int = 200) -> list:
    try:
        tree = lxml_html.fromstring(html_text)
    except Exception:
        return []
    out, seen = [], set()
    for a in tree.iter("a"):
        href = a.get("href")
        if not href:
            continue
        absu = urljoin(base_url, href)
        if not absu.startswith("http") or absu in seen:
            continue
        seen.add(absu)
        out.append(absu)
        if len(out) >= limit:
            break
    return out


def run_trafilatura(html_text: str, url: str) -> tuple[str, dict, list] | None:
    """(markdown, base_metadata, in_article_links) or None if extraction too thin.

    Three calls on purpose:
      • extract(output_format="markdown") for the clean body — bare_extraction does
        NOT honor markdown output (it leaves `text` empty in trafilatura 2.0), and
        we keep include_links=False so the body has no inline URL clutter.
      • extract(output_format="html", include_links=True) for the article subtree,
        from which we parse ONLY in-article links (no site nav/footer chrome).
      • extract_metadata() for title/author/date/description.
    Never pass favor_precision=True — it prunes whole article bodies to None.
    """
    try:
        md = trafilatura.extract(
            html_text,
            url=url,
            output_format="markdown",
            include_tables=True,
            include_comments=False,
        )
    except Exception:
        return None
    if not md or word_count(md) < MIN_EXTRACT_WORDS:
        return None
    md = md.strip()

    # in-article links only: parse <a> from the extracted article HTML subtree
    links: list = []
    try:
        article_html = trafilatura.extract(
            html_text, url=url, output_format="html",
            include_links=True, include_comments=False,
        )
        if article_html:
            links = extract_links(article_html, url)
    except Exception:
        pass

    meta: dict = {}
    try:
        m = trafilatura.extract_metadata(html_text)
        if m is not None:
            meta = {
                "title": getattr(m, "title", None),
                "author": getattr(m, "author", None),
                "published_date": getattr(m, "date", None),
                "description": getattr(m, "description", None),
                "sitename": getattr(m, "sitename", None),
                "hostname": getattr(m, "hostname", None),
                "language": getattr(m, "language", None),
                "categories": getattr(m, "categories", None),
                "tags": getattr(m, "tags", None),
            }
    except Exception:
        pass
    return md, meta, links


def run_readability(html_text: str, url: str) -> tuple[str, dict, list] | None:
    if ReadabilityDocument is None:
        return None
    try:
        doc = ReadabilityDocument(html_text)
        title = doc.short_title()
        summary_html = doc.summary(html_partial=True)
    except Exception:
        return None
    res = run_trafilatura(summary_html, url)
    if res is None:
        return None
    md, meta, links = res
    if not meta.get("title"):
        meta["title"] = title
    return md, meta, links


def extract_record(seed: dict, html_text: str, status_code: int, method: str) -> ExtractRecord:
    url = seed["source_url"]
    domain = seed.get("source_domain") or urlparse(url).netloc.replace("www.", "")
    topic = seed.get("topic", "")
    fetched_at = datetime.now(timezone.utc).isoformat()

    extractor = "none"
    res = run_trafilatura(html_text, url)
    if res is not None:
        extractor = "trafilatura-2.0"
    else:
        res = run_readability(html_text, url)
        if res is not None:
            extractor = "readability"

    if res is None:
        return ExtractRecord(
            source_url=url, source_domain=domain, topic=topic,
            fetched_at=fetched_at, http_status=status_code, fetch_method=method,
            extractor="none", markdown="", base_metadata={},
            links=[], word_count=0,
            status="extract-failed", error="all extractors below threshold",
        )

    md, meta, links = res
    return ExtractRecord(
        source_url=url, source_domain=domain, topic=topic,
        fetched_at=fetched_at, http_status=status_code, fetch_method=method,
        extractor=extractor, markdown=md, base_metadata=meta,
        links=links, word_count=word_count(md),
        status="extracted",
    )


def fetch_failed_record(seed: dict, status_code: int, error: str) -> ExtractRecord:
    url = seed["source_url"]
    domain = seed.get("source_domain") or urlparse(url).netloc.replace("www.", "")
    return ExtractRecord(
        source_url=url, source_domain=domain, topic=seed.get("topic", ""),
        fetched_at=datetime.now(timezone.utc).isoformat(),
        http_status=status_code, fetch_method="failed", extractor="none",
        markdown="", base_metadata={}, links=[], word_count=0,
        status="fetch-failed", error=error,
    )


# ─────────────────────────── driver ───────────────────────────
def load_seed(path: Path, limit: int | None) -> list[dict]:
    rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    return rows[:limit] if limit else rows


async def run(args) -> None:
    from crawl4ai import (
        AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode,
        MemoryAdaptiveDispatcher, RateLimiter,
    )

    seed_rows = load_seed(Path(args.seed), args.limit)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # map url → seed, and skip already-extracted unless --force
    by_url = {s["source_url"]: s for s in seed_rows}
    todo = []
    skipped = 0
    for s in seed_rows:
        if (out_dir / make_filename(s["source_url"])).exists() and not args.force:
            skipped += 1
            continue
        todo.append(s["source_url"])

    print(f"[fetch-extract] seed={len(seed_rows)} todo={len(todo)} skipped={skipped} "
          f"→ {out_dir} (sessions={args.concurrency})")
    if not todo:
        print("[fetch-extract] nothing to do.")
        return

    run_cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        wait_until="domcontentloaded",
        page_timeout=PAGE_TIMEOUT_MS,
        remove_overlay_elements=True,
        stream=True,
    )
    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=85.0,
        max_session_permit=args.concurrency,
        rate_limiter=RateLimiter(
            base_delay=(PER_DOMAIN_MIN_DELAY, PER_DOMAIN_MAX_DELAY),
            max_delay=30.0,
            max_retries=MAX_RETRIES,
        ),
    )

    counts: dict[str, int] = {}
    done = 0
    async with AsyncWebCrawler(config=BrowserConfig(headless=True, verbose=False)) as crawler:
        async for res in await crawler.arun_many(urls=todo, config=run_cfg, dispatcher=dispatcher):
            seed = by_url.get(res.url) or {"source_url": res.url}
            if res.success and res.html:
                # crawl4ai reports the first hop's code (e.g. 308 on redirect);
                # on success the page rendered, so normalize non-2xx to the final 200.
                status = getattr(res, "status_code", 200) or 200
                if not (200 <= status < 300):
                    status = 200
                rec = extract_record(seed, res.html, status, "crawl4ai")
            else:
                rec = fetch_failed_record(
                    seed, getattr(res, "status_code", 0) or 0,
                    getattr(res, "error_message", None) or "crawl4ai fetch failed",
                )
            out_path = out_dir / make_filename(seed["source_url"])
            out_path.write_text(json.dumps(asdict(rec), ensure_ascii=False, indent=2))
            counts[rec.status] = counts.get(rec.status, 0) + 1
            done += 1
            if done % 10 == 0 or done == len(todo):
                print(f"  …{done}/{len(todo)}  {counts}")

    print(f"[fetch-extract] done: {counts}")


def main():
    p = argparse.ArgumentParser(description="Pipeline V2 Stage 1+2: crawl4ai fetch + trafilatura extract")
    p.add_argument("--seed", default=str(DEFAULT_SEED))
    p.add_argument("--out", default=str(DEFAULT_OUT))
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY,
                   help="parallel browser sessions (max_session_permit)")
    p.add_argument("--force", action="store_true", help="re-fetch even if output exists")
    args = p.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
