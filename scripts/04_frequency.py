#!/usr/bin/env python3
"""Phase 4: Frequency analysis — topic × career level cross-table + gap scoring.

Reads 03-categorized/manifest.json and produces:
  04-frequency/frequency_report.md   — human-readable table + gap analysis
  04-frequency/frequency_report.json — machine-readable data for Phase 5

Usage:
    python scripts/04_frequency.py
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

MANIFEST    = Path(__file__).parent.parent / "03-categorized" / "manifest.json"
OUT_DIR     = Path(__file__).parent.parent / "04-frequency"
REPORT_MD   = OUT_DIR / "frequency_report.md"
REPORT_JSON = OUT_DIR / "frequency_report.json"

LEVELS = ["entry", "mid", "senior", "executive"]


def main() -> None:
    records = json.loads(MANIFEST.read_text())
    print(f"\nPhase 4 — Frequency analysis: {len(records)} files\n")

    # ── Count files per (topic, career_level) ─────────────────────────────────
    topics: set[str] = set()
    # counts[topic][level] = set of file paths (to avoid double-counting)
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    word_counts: dict[str, list[int]] = defaultdict(list)

    for rec in records:
        topic = rec.get("topic", "").strip()
        if not topic:
            continue
        topics.add(topic)
        levels = rec.get("career_level") or []
        if not levels:
            # Count as general (all levels)
            for lv in LEVELS:
                counts[topic][lv] += 1
        else:
            for lv in levels:
                if lv in LEVELS:
                    counts[topic][lv] += 1
        wc = rec.get("word_count", 0)
        if wc:
            word_counts[topic].append(wc)

    sorted_topics = sorted(topics)

    # ── Gap score: 1 / (count + 1), normalized per column ────────────────────
    # Higher = more sparse = bigger gap
    gap_scores: dict[str, dict[str, float]] = {}
    for topic in sorted_topics:
        gap_scores[topic] = {}
        for lv in LEVELS:
            c = counts[topic].get(lv, 0)
            gap_scores[topic][lv] = round(1 / (c + 1), 4)

    # ── Top 10 sparse cells ───────────────────────────────────────────────────
    cells = []
    for topic in sorted_topics:
        for lv in LEVELS:
            cells.append({
                "topic": topic,
                "level": lv,
                "count": counts[topic].get(lv, 0),
                "gap_score": gap_scores[topic][lv],
            })
    cells.sort(key=lambda x: (-x["gap_score"], x["topic"], x["level"]))
    top_gaps = cells[:10]

    # ── Word count stats per topic ────────────────────────────────────────────
    wc_stats: dict[str, dict] = {}
    for topic in sorted_topics:
        wcs = sorted(word_counts.get(topic, [0]))
        total = sum(wcs)
        median = wcs[len(wcs) // 2] if wcs else 0
        wc_stats[topic] = {
            "min": min(wcs) if wcs else 0,
            "median": median,
            "max": max(wcs) if wcs else 0,
            "total": total,
            "files": len(wcs),
        }

    # ── Build markdown report ─────────────────────────────────────────────────
    lines = [
        "# Phase 4 — Frequency Report\n",
        f"**Files analysed:** {len(records)}  |  "
        f"**Topics:** {len(sorted_topics)}  |  "
        f"**Levels:** entry / mid / senior / executive\n\n",
        "## Topic × Career Level Cross-Table\n\n",
    ]

    # Header
    col = 28
    lines.append(f"| {'Topic':<{col}} | {'Entry':>6} | {'Mid':>6} | {'Senior':>7} | {'Executive':>9} | {'Total':>6} |\n")
    lines.append(f"|{'-'*(col+2)}|{'-'*8}|{'-'*8}|{'-'*9}|{'-'*11}|{'-'*8}|\n")

    for topic in sorted_topics:
        row_counts = [counts[topic].get(lv, 0) for lv in LEVELS]
        total = sum(row_counts)
        lines.append(
            f"| {topic:<{col}} | {row_counts[0]:>6} | {row_counts[1]:>6} | "
            f"{row_counts[2]:>7} | {row_counts[3]:>9} | {total:>6} |\n"
        )

    # Word count table
    lines += [
        "\n## Word Count Distribution per Topic\n\n",
        f"| {'Topic':<{col}} | {'Files':>6} | {'Min':>6} | {'Median':>7} | {'Max':>6} | {'Total':>8} |\n",
        f"|{'-'*(col+2)}|{'-'*8}|{'-'*8}|{'-'*9}|{'-'*8}|{'-'*10}|\n",
    ]
    for topic in sorted_topics:
        s = wc_stats[topic]
        lines.append(
            f"| {topic:<{col}} | {s['files']:>6} | {s['min']:>6} | "
            f"{s['median']:>7} | {s['max']:>6} | {s['total']:>8,} |\n"
        )

    # Top gaps
    lines += [
        "\n## Top 10 Sparse Cells (Biggest Gaps)\n\n",
        f"| {'#':>3} | {'Topic':<{col}} | {'Level':<10} | {'Count':>6} | {'Gap Score':>10} |\n",
        f"|{'-'*5}|{'-'*(col+2)}|{'-'*12}|{'-'*8}|{'-'*12}|\n",
    ]
    for i, cell in enumerate(top_gaps, 1):
        lines.append(
            f"| {i:>3} | {cell['topic']:<{col}} | {cell['level']:<10} | "
            f"{cell['count']:>6} | {cell['gap_score']:>10.4f} |\n"
        )

    # ── Write outputs ─────────────────────────────────────────────────────────
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("".join(lines), encoding="utf-8")

    json_out = {
        "topics": sorted_topics,
        "levels": LEVELS,
        "counts": {t: dict(counts[t]) for t in sorted_topics},
        "gap_scores": gap_scores,
        "word_count_stats": wc_stats,
        "top_gaps": top_gaps,
        "total_files": len(records),
    }
    REPORT_JSON.write_text(json.dumps(json_out, indent=2), encoding="utf-8")

    # Print summary to console
    print(f"  {'Topic':<30} {'Entry':>6} {'Mid':>6} {'Senior':>7} {'Executive':>10} {'Total':>6}")
    print(f"  {'-'*30} {'-'*6} {'-'*6} {'-'*7} {'-'*10} {'-'*6}")
    for topic in sorted_topics:
        row = [counts[topic].get(lv, 0) for lv in LEVELS]
        print(f"  {topic:<30} {row[0]:>6} {row[1]:>6} {row[2]:>7} {row[3]:>10} {sum(row):>6}")

    print(f"\n  Top gaps:")
    for cell in top_gaps[:5]:
        print(f"    {cell['topic']:<30} {cell['level']:<10} count={cell['count']}  gap={cell['gap_score']:.3f}")

    print(f"\n  Report → {REPORT_MD}")
    print(f"  JSON   → {REPORT_JSON}\n")


if __name__ == "__main__":
    main()
