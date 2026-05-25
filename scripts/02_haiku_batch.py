#!/usr/bin/env python3
"""Phase 2b: Resolve ambiguous metadata fields via claude CLI (parallel).

Reads batch_queue.json written by 02_extract_metadata.py, calls the
`claude` CLI for each file in parallel, then patches frontmatter in
the corresponding 02-cleaned/ files.

Usage:
    python scripts/02_haiku_batch.py
    python scripts/02_haiku_batch.py --dry-run      # show counts, no calls
    python scripts/02_haiku_batch.py --concurrency 8
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

CLEANED_DIR  = Path(__file__).parent.parent / "02-cleaned"
BATCH_QUEUE  = CLEANED_DIR / "batch_queue.json"
BATCH_RESULT = CLEANED_DIR / "batch_results.json"

MODEL      = "claude-haiku-4-5-20251001"
MAX_TOKENS = 256

SYSTEM_PROMPT = """\
You are a resume content classifier. Given a snippet of a web article about CV/resume writing, extract:
1. title: a short descriptive title (max 80 chars), inferred from content if no H1 present
2. topic: the single best-fit topic from this list:
   resume-basics, resume-formatting, work-experience, skills-section, education-section,
   projects-section, github-portfolio, open-source-contributions, cover-letter, linkedin-profile,
   career-gap, career-change, salary-negotiation, ats-optimization, job-search-strategy,
   interview-prep, senior-level-resume, executive-resume, remote-work-resume
3. career_level: array of applicable levels from [entry, mid, senior, executive].
   entry=0-2yrs/junior/new grad, mid=2-7yrs/IC, senior=7+yrs/staff/lead, executive=director/VP/C-suite.
   Include all that apply. If the content is general/all-levels, return all four.

Respond ONLY with valid JSON: {"title": "...", "topic": "...", "career_level": ["..."]}"""


def build_user_message(snippet: str, existing_fields: dict) -> str:
    hints = []
    if existing_fields.get("title"):
        hints.append(f"Existing title hint: {existing_fields['title']}")
    if existing_fields.get("topic"):
        hints.append(f"Existing topic hint: {existing_fields['topic']}")
    if existing_fields.get("career_level"):
        hints.append(f"Existing career_level hint: {existing_fields['career_level']}")
    hint_block = "\n".join(hints)
    return f"{hint_block}\n\nArticle snippet:\n{snippet[:3000]}"


def estimate_cost(items: list[dict]) -> float:
    # ~500 input tokens per item (system cached + snippet), ~60 output tokens
    # Haiku Batch: $0.125/1M input, $0.625/1M output (50% batch discount)
    n = len(items)
    input_cost  = (n * 500 / 1_000_000) * 0.125
    output_cost = (n * 60  / 1_000_000) * 0.625
    return round(input_cost + output_cost, 4)


def patch_frontmatter(file_path: Path, updates: dict) -> None:
    """Patch title, topic, career_level in an existing YAML frontmatter block."""
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return

    end = text.find("\n---", 3)
    if end == -1:
        return

    fm_raw  = text[3:end]
    body    = text[end + 4:]

    import yaml
    fm = yaml.safe_load(fm_raw) or {}

    if updates.get("title") and not fm.get("title"):
        fm["title"] = updates["title"]
    if updates.get("topic") and not fm.get("topic"):
        fm["topic"] = updates["topic"]
    if updates.get("career_level") and not fm.get("career_level"):
        fm["career_level"] = updates["career_level"]

    # Reserialise — keep field order
    ordered_keys = [
        "title", "topic", "career_level", "source_url", "source_domain",
        "word_count", "text_to_link_ratio", "signal_score", "is_curated",
        "tags", "ingested_at",
    ]
    lines = ["---"]
    for k in ordered_keys:
        if k not in fm:
            continue
        v = fm[k]
        if isinstance(v, list):
            if v:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{k}: []")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, float):
            lines.append(f"{k}: {v}")
        elif isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            safe = str(v).replace('"', '\\"')
            lines.append(f'{k}: "{safe}"')
    lines.append("---")

    file_path.write_text("\n".join(lines) + "\n" + body, encoding="utf-8")


async def classify_one(item: dict, sem: asyncio.Semaphore) -> tuple[str, dict | None]:
    """Call `claude -p` for a single item, return (path, parsed_json | None)."""
    prompt = f"{SYSTEM_PROMPT}\n\n{build_user_message(item['snippet'], item['fields'])}"
    async with sem:
        proc = await asyncio.create_subprocess_exec(
            "claude", "-p", prompt,
            "--model", MODEL,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL,
        )
        stdout, _ = await proc.communicate()
        raw = stdout.decode().strip()

    # Extract JSON from response (may have surrounding text)
    match = __import__("re").search(r'\{[^{}]+\}', raw, __import__("re").DOTALL)
    if not match:
        return item["path"], None
    try:
        return item["path"], json.loads(match.group())
    except json.JSONDecodeError:
        return item["path"], None


async def run_all(items: list[dict], concurrency: int) -> dict:
    sem = asyncio.Semaphore(concurrency)
    tasks = [classify_one(item, sem) for item in items]
    results = {}
    done = 0
    for coro in asyncio.as_completed(tasks):
        path, parsed = await coro
        done += 1
        if parsed:
            results[path] = parsed
            print(f"  [{done}/{len(items)}] OK  {Path(path).name}")
        else:
            print(f"  [{done}/{len(items)}] WARN no JSON  {Path(path).name}")
    return results


def main(dry_run: bool, concurrency: int) -> None:
    if not BATCH_QUEUE.exists():
        print(f"No batch queue found at {BATCH_QUEUE}")
        print("Run 02_extract_metadata.py first.")
        sys.exit(1)

    items: list[dict] = json.loads(BATCH_QUEUE.read_text())
    print(f"\nPhase 2b — claude CLI: {len(items)} files, concurrency={concurrency}\n")

    if dry_run:
        print("--dry-run: no calls made.")
        return

    results = asyncio.run(run_all(items, concurrency))

    # Save raw results
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    BATCH_RESULT.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nResults saved → {BATCH_RESULT}")

    # Patch frontmatter in 02-cleaned files
    patched = 0
    for item in items:
        raw_path = Path(item["path"])
        try:
            rel = raw_path.relative_to(CLEANED_DIR.parent / "01-raw")
            cleaned_path = CLEANED_DIR / rel
        except ValueError:
            continue
        if not cleaned_path.exists():
            continue
        updates = results.get(item["path"], {})
        if updates:
            patch_frontmatter(cleaned_path, updates)
            patched += 1

    print(f"Patched {patched} files in {CLEANED_DIR}")
    print("Phase 2b complete — ready for Phase 3.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 2b: metadata resolution via claude CLI")
    parser.add_argument("--dry-run", action="store_true", help="Show counts, no calls")
    parser.add_argument("--concurrency", type=int, default=5, help="Parallel claude calls (default: 5)")
    args = parser.parse_args()
    main(dry_run=args.dry_run, concurrency=args.concurrency)
