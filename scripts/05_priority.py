#!/usr/bin/env python3
"""Phase 5: Rank topic × career-level gaps and write priority_list.md via claude CLI.

Ranking formula:
    priority_score = gap_score × team_relevance_weight

Team relevance weights (skews mid-senior dev team):
    entry     0.6
    mid       1.0
    senior    1.2
    executive 0.4

Usage:
    python scripts/05_priority.py
    python scripts/05_priority.py --dry-run   # print ranked list, skip claude narrative
"""
from __future__ import annotations

import argparse
import asyncio
import json
import subprocess
from pathlib import Path

FREQ_JSON  = Path(__file__).parent.parent / "04-frequency" / "frequency_report.json"
OUT_DIR    = Path(__file__).parent.parent / "05-priority"
OUT_MD     = OUT_DIR / "priority_list.md"

TEAM_WEIGHTS = {
    "entry":     0.6,
    "mid":       1.0,
    "senior":    1.2,
    "executive": 0.4,
}

TOP_N = 10  # ranked cells to include in narrative


def rank_gaps(data: dict) -> list[dict]:
    ranked = []
    for topic in data["topics"]:
        for level in data["levels"]:
            count      = data["counts"].get(topic, {}).get(level, 0)
            gap_score  = data["gap_scores"].get(topic, {}).get(level, 0.0)
            weight     = TEAM_WEIGHTS.get(level, 1.0)
            priority   = round(gap_score * weight, 4)
            ranked.append({
                "topic":          topic,
                "level":          level,
                "count":          count,
                "gap_score":      gap_score,
                "team_weight":    weight,
                "priority_score": priority,
            })
    ranked.sort(key=lambda x: -x["priority_score"])
    return ranked


def build_prompt(ranked: list[dict], freq_data: dict) -> str:
    top = ranked[:TOP_N]
    wc_stats = freq_data.get("word_count_stats", {})

    rows = "\n".join(
        f"  {i+1}. {r['topic']} × {r['level']} — "
        f"count={r['count']}, gap={r['gap_score']:.3f}, "
        f"weight={r['team_weight']}, priority={r['priority_score']:.3f}"
        for i, r in enumerate(top)
    )

    topic_summary = "\n".join(
        f"  {t}: {s['files']} files, median {s['median']} words"
        for t, s in wc_stats.items()
    )

    return f"""You are a curriculum designer for a developer-focused CV writing micro-course.

The audience is an internal dev team: Node.js, Java, Mobile, and AI engineers across all career levels (intern to executive). The team skews mid-to-senior.

Below is a ranked list of content gaps in our CV-writing knowledge base (topic × career level pairs with the fewest resources, weighted by team relevance):

{rows}

Topic file counts and content depth:
{topic_summary}

Write a concise 1-page priority list document (markdown) with:
1. A brief intro (2-3 sentences) explaining the methodology
2. Top 5-7 micro-course recommendations, each with:
   - Title (actionable, audience-specific)
   - Target level(s)
   - Why it's a priority (1-2 sentences linking gap data to team needs)
   - Suggested content angle (what makes this different from generic CV advice)
3. A short "honourable mentions" section for gaps #6-10
4. One closing sentence on what to build next after these

Be specific and practical. Avoid generic advice. Write for developers who are skeptical of CV writing tips."""


async def call_claude(prompt: str) -> str:
    proc = await asyncio.create_subprocess_exec(
        "claude", "-p", prompt,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
    )
    stdout, _ = await proc.communicate()
    return stdout.decode().strip()


def main(dry_run: bool) -> None:
    if not FREQ_JSON.exists():
        print(f"frequency_report.json not found at {FREQ_JSON}")
        print("Run 04_frequency.py first.")
        return

    data   = json.loads(FREQ_JSON.read_text())
    ranked = rank_gaps(data)

    print("\nPhase 5 — Priority ranking\n")
    print(f"  {'#':>3}  {'Topic':<30} {'Level':<10} {'Count':>6} {'Priority':>9}")
    print(f"  {'-'*3}  {'-'*30} {'-'*10} {'-'*6} {'-'*9}")
    for i, r in enumerate(ranked[:TOP_N], 1):
        print(f"  {i:>3}  {r['topic']:<30} {r['level']:<10} {r['count']:>6} {r['priority_score']:>9.4f}")

    if dry_run:
        print("\n--dry-run: skipping claude narrative.")
        return

    print("\nGenerating priority_list.md via claude CLI...")
    prompt   = build_prompt(ranked, data)
    narrative = asyncio.run(call_claude(prompt))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(narrative, encoding="utf-8")
    print(f"\nWritten → {OUT_MD}\n")
    print(narrative[:800] + ("\n..." if len(narrative) > 800 else ""))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 5: Priority micro-course topic list")
    parser.add_argument("--dry-run", action="store_true", help="Print ranking, skip claude narrative")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
