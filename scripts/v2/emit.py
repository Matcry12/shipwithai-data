#!/usr/bin/env python3
"""
Pipeline V2 — Stage 6: emit final OUTPUT_CONTRACT objects.

work/05-enriched/*.json  →  work/02-output/*.json

Deterministic reshape into the Firecrawl-exact contract (see OUTPUT_CONTRACT.md /
PIPELINE_V2.md). Stable schema: every object has every key; null when absent.
Kept + quarantined both land here, distinguished by `status` (filter downstream).

    cv-rag/.venv/bin/python scripts/v2/emit.py
"""
from __future__ import annotations
import argparse, glob, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IN = ROOT / "work" / "05-enriched"
DEFAULT_OUT = ROOT / "work" / "02-output"
PIPELINE_VERSION = "pipeline-2.0.0"

# controlled doc_type vocabulary; hand-written agent values get clamped to it
ALLOWED_DOCTYPES = {"how-to-guide", "listicle", "opinion", "reference",
                    "case-study", "news", "other"}
DOCTYPE_REMAP = {"resume": "reference", "comparison": "reference",
                 "guide": "how-to-guide", "tutorial": "how-to-guide",
                 "review": "opinion", "list": "listicle"}


def normalize_doctype(dt: str | None) -> str | None:
    if dt is None:
        return None
    dt = dt.strip().lower()
    if dt in ALLOWED_DOCTYPES:
        return dt
    return DOCTYPE_REMAP.get(dt, "other")


def to_contract(d: dict) -> dict:
    m = d.get("base_metadata") or {}
    return {
        "markdown": d.get("markdown", ""),
        "metadata": {
            # provenance
            "source_url": d.get("source_url"),
            "source_domain": d.get("source_domain"),
            "topic": d.get("topic"),
            "fetched_at": d.get("fetched_at"),
            "http_status": d.get("http_status"),
            "extractor": d.get("extractor"),
            "extractor_version": PIPELINE_VERSION,
            # content identity
            "title": m.get("title"),
            "description": m.get("description"),
            "language": m.get("language"),
            "word_count": m.get("word_count", d.get("word_count")),
            "content_hash": m.get("content_hash"),
            "reading_time": m.get("reading_time"),
            "author": m.get("author"),
            "published_date": m.get("published_date"),
            "og_title": m.get("og_title"),
            # quality signal
            "signal_score": m.get("signal_score"),
            "text_to_link_ratio": m.get("text_to_link_ratio"),
            # LLM enrichment (null when not enriched / quarantined)
            "tldr": m.get("tldr"),
            "entities": m.get("entities"),
            "core_question": m.get("core_question"),
            "doc_type": normalize_doctype(m.get("doc_type")),
            "key_topics": m.get("key_topics"),
        },
        "structure": d.get("structure", {"section_count": 0, "max_depth": 0, "outline": []}),
        "links": d.get("links", []),
        "status": d.get("status"),
        "drop_reason": d.get("drop_reason"),
        "enrichment_status": d.get("enrichment_status"),
    }


REQUIRED_TOP = {"markdown", "metadata", "structure", "links", "status", "drop_reason"}
REQUIRED_META = {"source_url", "title", "word_count", "content_hash", "signal_score"}


def validate(obj: dict) -> list[str]:
    errs = []
    if not REQUIRED_TOP <= obj.keys():
        errs.append(f"missing top keys: {REQUIRED_TOP - obj.keys()}")
    if not REQUIRED_META <= obj["metadata"].keys():
        errs.append(f"missing meta keys: {REQUIRED_META - obj['metadata'].keys()}")
    if obj["status"] == "kept" and not obj["markdown"].strip():
        errs.append("kept but empty markdown")
    return errs


def run(in_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(glob.glob(str(in_dir / "*.json")))
    status_counts = Counter()
    doctype_counts = Counter()
    enrich_counts = Counter()
    bad = 0
    for p in files:
        d = json.load(open(p, encoding="utf-8"))
        obj = to_contract(d)
        errs = validate(obj)
        if errs:
            bad += 1
            print(f"  ! {Path(p).name}: {errs}")
            continue
        (out_dir / Path(p).name).write_text(
            json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
        status_counts[obj["status"]] += 1
        enrich_counts[obj.get("enrichment_status")] += 1
        if obj["status"] == "kept":
            doctype_counts[obj["metadata"].get("doc_type") or "—"] += 1

    print(f"[emit] wrote {sum(status_counts.values())} objects → {out_dir}  (validation errors={bad})")
    print(f"[emit] status: {dict(status_counts)}")
    print(f"[emit] kept doc_type: {dict(doctype_counts)}")


def main():
    ap = argparse.ArgumentParser(description="Pipeline V2 Stage 6: emit OUTPUT_CONTRACT")
    ap.add_argument("--in", dest="in_dir", default=str(DEFAULT_IN))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args()
    run(Path(a.in_dir), Path(a.out))


if __name__ == "__main__":
    main()
