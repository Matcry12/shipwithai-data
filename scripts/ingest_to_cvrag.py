"""
Ingest shipwithai-data/01-raw/ into the cv-rag Qdrant knowledge base.

Steps:
  1. Strip YAML frontmatter from 01-raw/ files → staging/input/
  2. clean.py  → staging/data/_processed/ + manifest.jsonl
  3. parent.py → staging/data/parents.jsonl
  4. child.py  → staging/data/children.jsonl
  5. tag.py    → staging/data/parents_tagged.jsonl + children_tagged.jsonl
  6. embed.py  → staging/data/embeddings/
  7. upsert.py → Qdrant kb_parents / kb_children (additive, idempotent)

Run from repo root:
    cd /home/matcry/Documents/Knowledge
    .venv/bin/python shipwithai-data/scripts/ingest_to_cvrag.py
Or directly with the cv-rag venv:
    /home/matcry/Documents/Knowledge/cv-rag/.venv/bin/python \
        shipwithai-data/scripts/ingest_to_cvrag.py
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────

REPO = Path(__file__).resolve().parent.parent.parent   # .../Knowledge
RAW_DIR     = REPO / "shipwithai-data" / "01-raw"
STAGING_DIR = REPO / "shipwithai-data" / "pipeline-staging"
INPUT_DIR   = STAGING_DIR / "input"     # frontmatter-stripped source files
DATA_DIR    = STAGING_DIR / "data"      # clean.py output (manifest + _processed)

PIPELINE_DIR = REPO / "cv-rag" / "pipeline"
PYTHON       = REPO / "cv-rag" / ".venv" / "bin" / "python"

# Topics to skip — not CV/resume content
EXCLUDED_TOPICS = {"claude-code-workflow"}

# ── YAML frontmatter stripping ─────────────────────────────────────────────

_FM_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def strip_frontmatter(text: str) -> str:
    return _FM_RE.sub("", text, count=1).lstrip("\n")


# ── Step 1: copy 01-raw/ → staging/input/, stripping frontmatter ───────────

def prepare_input():
    if INPUT_DIR.exists():
        shutil.rmtree(INPUT_DIR)
    INPUT_DIR.mkdir(parents=True)

    total = skipped = 0
    for src in sorted(RAW_DIR.rglob("*.md")):
        parts = src.relative_to(RAW_DIR).parts
        if len(parts) < 3:
            continue                       # need <topic>/<domain>/<file>
        topic = parts[0]
        if topic in EXCLUDED_TOPICS:
            skipped += 1
            continue

        dest = INPUT_DIR / src.relative_to(RAW_DIR)
        dest.parent.mkdir(parents=True, exist_ok=True)
        raw = src.read_text(encoding="utf-8", errors="replace")
        dest.write_text(strip_frontmatter(raw), encoding="utf-8")
        total += 1

    print(f"[step 1] prepared {total} files, skipped {skipped} (excluded topics)", flush=True)


# ── Step runner ────────────────────────────────────────────────────────────

def run(label: str, cmd: list[str | Path]) -> None:
    print(f"\n[{label}] {' '.join(str(c) for c in cmd)}", flush=True)
    result = subprocess.run(cmd, capture_output=False)
    if result.returncode != 0:
        print(f"[{label}] FAILED (exit {result.returncode})", file=sys.stderr)
        sys.exit(result.returncode)


# ── Main ───────────────────────────────────────────────────────────────────

def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("=== shipwithai → cv-rag ingestion ===")
    print(f"  raw:     {RAW_DIR}")
    print(f"  staging: {STAGING_DIR}")
    print(f"  qdrant:  localhost:6333")

    prepare_input()

    run("clean",  [PYTHON, PIPELINE_DIR / "clean.py",
                   "--input",  INPUT_DIR,
                   "--output", DATA_DIR])

    run("parent", [PYTHON, PIPELINE_DIR / "parent.py",
                   "--data", DATA_DIR])

    run("child",  [PYTHON, PIPELINE_DIR / "child.py",
                   "--data", DATA_DIR])

    run("tag",    [PYTHON, PIPELINE_DIR / "tag.py",
                   "--data",  DATA_DIR,
                   "--rules", PIPELINE_DIR / "tag_rules.yaml"])

    run("embed",  [PYTHON, PIPELINE_DIR / "embed.py",
                   "--data", DATA_DIR])

    run("upsert", [PYTHON, PIPELINE_DIR / "upsert.py",
                   "--data", DATA_DIR])

    print("\n=== done — new chunks added to kb_parents / kb_children ===")


if __name__ == "__main__":
    main()
