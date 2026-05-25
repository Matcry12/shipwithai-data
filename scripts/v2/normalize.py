#!/usr/bin/env python3
"""
Pipeline V2 — Stage 3: normalize (deterministic markdown hygiene).

work/01-extracted/*.json  →  work/02-normalized/*.json

Delete-only / normalize-only edits. The body stays the author's text — we do NOT
reword, reorder, or summarize. We only:
  • Unicode-normalize (NFC) and strip zero-width chars + BOM
  • nbsp → space
  • smart quotes → ASCII quotes (dashes left intact for fidelity)
  • drop a tight, evidence-based chrome line-set (uploader widget, byline
    fragments, form-confirmation leaks, stray punctuation-only lines)
  • collapse 3+ blank lines → 1, trim trailing whitespace

Chrome patterns were derived by frequency analysis across the corpus
(report_failures-style scan): lines that recur across many distinct documents
and are not article content. Kept intentionally conservative — when unsure, keep.

    cv-rag/.venv/bin/python scripts/v2/normalize.py
"""
from __future__ import annotations
import argparse, glob, json, re, unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IN = ROOT / "work" / "01-extracted"
DEFAULT_OUT = ROOT / "work" / "02-normalized"
NORMALIZE_VERSION = "normalize-2.0.0"

# zero-width / invisible chars to strip outright
_ZERO_WIDTH = dict.fromkeys(map(ord, "​‌‍⁠﻿"), None)
# smart quotes → ASCII (dashes deliberately NOT converted)
_QUOTES = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"', "″": '"',
}
_QUOTE_TABLE = {ord(k): v for k, v in _QUOTES.items()}

# ── chrome line patterns (evidence-based, conservative) ──
# Each matched against the STRIPPED line. If it matches, the line is dropped.
CHROME_PATTERNS = [
    re.compile(r"^drop your resume here\b.*", re.I),
    re.compile(r"^pdf\s*&\s*docx only\.?\s*max .*file size\.?$", re.I),
    re.compile(r"^thank you for your (enquiry|inquiry|interest|submission|message)\b.*", re.I),
    re.compile(r"^one of our .{0,60}(will be in touch|will contact you|team will)\b.*", re.I),
    re.compile(r"^written by$", re.I),
    re.compile(r"^updated$", re.I),
    # stray punctuation-only artifact lines: a line made only of 1–3 of - . | * _
    re.compile(r"^[-.|*_]{1,3}$"),
]


def _drop_line(stripped: str) -> bool:
    return any(p.match(stripped) for p in CHROME_PATTERNS)


def normalize_body(md: str) -> tuple[str, dict]:
    before_len = len(md)
    # 1. unicode normalize + strip invisibles + nbsp + smart quotes
    md = unicodedata.normalize("NFC", md)
    md = md.translate(_ZERO_WIDTH)
    md = md.replace(" ", " ")
    md = md.translate(_QUOTE_TABLE)

    # 2. line-level: trim trailing ws, drop chrome lines
    dropped = 0
    kept_lines = []
    for line in md.split("\n"):
        line = line.rstrip()
        if _drop_line(line.strip()):
            dropped += 1
            continue
        kept_lines.append(line)

    # 3. collapse 3+ blank lines → 1 blank; trim leading/trailing blanks
    out_lines, blank_run, collapsed = [], 0, 0
    for line in kept_lines:
        if line.strip() == "":
            blank_run += 1
            if blank_run >= 2:
                collapsed += 1
                continue
            out_lines.append("")
        else:
            blank_run = 0
            out_lines.append(line)
    text = "\n".join(out_lines).strip() + "\n"

    stats = {
        "chars_removed": before_len - len(text),
        "lines_dropped": dropped,
        "blank_runs_collapsed": collapsed,
    }
    return text, stats


def run(in_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(glob.glob(str(in_dir / "*.json")))
    processed = skipped = 0
    agg = Counter()
    for p in files:
        d = json.load(open(p, encoding="utf-8"))
        if d.get("status") != "extracted":
            skipped += 1
            continue
        new_md, stats = normalize_body(d["markdown"])
        d["markdown"] = new_md
        d["word_count"] = len(new_md.split())
        d["normalize_stats"] = stats
        d["normalize_version"] = NORMALIZE_VERSION
        (out_dir / Path(p).name).write_text(
            json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        processed += 1
        agg["chars_removed"] += stats["chars_removed"]
        agg["lines_dropped"] += stats["lines_dropped"]
        agg["blank_runs_collapsed"] += stats["blank_runs_collapsed"]

    print(f"[normalize] processed={processed} skipped(non-extracted)={skipped} → {out_dir}")
    print(f"[normalize] totals: chars_removed={agg['chars_removed']} "
          f"lines_dropped={agg['lines_dropped']} blank_runs_collapsed={agg['blank_runs_collapsed']}")


def main():
    ap = argparse.ArgumentParser(description="Pipeline V2 Stage 3: normalize")
    ap.add_argument("--in", dest="in_dir", default=str(DEFAULT_IN))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args()
    run(Path(a.in_dir), Path(a.out))


if __name__ == "__main__":
    main()
