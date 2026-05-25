#!/usr/bin/env python3
"""Phase 3: Categorize cleaned files into topic folders and write manifest.json.

Reads YAML frontmatter from 02-cleaned/, copies each file into:
  03-categorized/<topic>/<filename>.md

Files with no topic go into 03-categorized/_unclassified/.
Writes 03-categorized/manifest.json with full metadata for all files.

Usage:
    python scripts/03_categorize.py
    python scripts/03_categorize.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

import yaml

CLEANED_DIR  = Path(__file__).parent.parent / "02-cleaned"
CAT_DIR      = Path(__file__).parent.parent / "03-categorized"
MANIFEST_OUT = CAT_DIR / "manifest.json"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Returns ({}, text) if no frontmatter."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4:].lstrip()
    return fm, body


def main(dry_run: bool) -> None:
    md_files = [f for f in CLEANED_DIR.rglob("*.md")
                if f.name != "batch_queue.json"]

    print(f"\nPhase 3 — Categorize: {len(md_files)} files from {CLEANED_DIR}\n")

    stats = {"placed": 0, "unclassified": 0}
    manifest = []

    for src in sorted(md_files):
        text = src.read_text(encoding="utf-8", errors="replace")
        fm, _ = parse_frontmatter(text)

        topic = fm.get("topic") or ""
        topic_dir = topic.strip() if topic.strip() else "_unclassified"

        dest = CAT_DIR / topic_dir / src.name

        # Resolve name collisions by appending parent folder name
        if not dry_run and dest.exists() and dest.resolve() != src.resolve():
            stem = src.stem + f"__{src.parent.name}"
            dest = CAT_DIR / topic_dir / (stem + ".md")

        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)

        if topic_dir == "_unclassified":
            stats["unclassified"] += 1
        else:
            stats["placed"] += 1

        manifest.append({
            "file":              str(dest.relative_to(CAT_DIR)) if not dry_run else str(src.relative_to(CLEANED_DIR)),
            "source_path":       str(src.relative_to(CLEANED_DIR)),
            "title":             fm.get("title", ""),
            "topic":             fm.get("topic", ""),
            "career_level":      fm.get("career_level", []),
            "source_url":        fm.get("source_url", ""),
            "source_domain":     fm.get("source_domain", ""),
            "word_count":        fm.get("word_count", 0),
            "text_to_link_ratio":fm.get("text_to_link_ratio", 0.0),
            "signal_score":      fm.get("signal_score", 0.0),
            "is_curated":        fm.get("is_curated", False),
            "tags":              fm.get("tags", []),
            "ingested_at":       fm.get("ingested_at", ""),
        })

    if not dry_run:
        CAT_DIR.mkdir(parents=True, exist_ok=True)
        MANIFEST_OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    # Summary by topic
    from collections import Counter
    topic_counts = Counter(e["topic"] or "_unclassified" for e in manifest)
    print(f"  {'Topic':<30} {'Files':>6}")
    print(f"  {'-'*30} {'-'*6}")
    for topic, count in sorted(topic_counts.items()):
        print(f"  {topic:<30} {count:>6}")
    print(f"\n  Placed: {stats['placed']}  |  Unclassified: {stats['unclassified']}")
    if not dry_run:
        print(f"  Manifest → {MANIFEST_OUT}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 3: Categorize into topic folders")
    parser.add_argument("--dry-run", action="store_true", help="Show counts, no writes")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
