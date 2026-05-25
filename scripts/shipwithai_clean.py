"""
M2 — shipwithai_clean.

Reads 01-raw-v2/<topic>/<domain>/.../<slug>.md, applies deterministic cleaning
(line-drop patterns from cleaning_rules.yaml, regex passes, drop-rule filter),
recomputes metrics, re-attaches frontmatter, formats with Prettier, and writes:

  02-cleaned/<topic>/<domain>/.../<slug>.md  — kept files
  02-quarantine/<reason>/<topic>__<slug>.md  — dropped files (one per reason)
  02-cleaning-report.json                    — kept / dropped / stats

No LLM. Idempotent — re-runs fully overwrite outputs.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


# ---------------------------------------------------------------------------
# Frontmatter helpers (same shape used in M1 — kept tiny and duplicated; no
# shared utils module yet because there is only one other caller)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    fm = yaml.safe_load(text[4:end]) or {}
    body = text[end + 5 :]
    if not isinstance(fm, dict):
        return {}, text
    return fm, body


def dump_frontmatter(fm: dict, body: str) -> str:
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True) + "---\n\n" + body


# ---------------------------------------------------------------------------
# Line-level cleaning
# ---------------------------------------------------------------------------

# Standalone image lines: ![alt](url) — same as cv-rag/pipeline/clean.py
_RE_IMAGE_LINE = re.compile(r"^\s*!\[.*?\]\(.*?\).*$")
_RE_IMAGE_LINK_LINE = re.compile(r"^\s*\[?\s*!\[.*?\]\(.*?\)\s*\]?\(?.*?\)?\s*$")

# Any markdown link span — used to measure link char density
_RE_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")

# Defensive: ASCII-split single-letter heading lines (`# C` followed by `h`,`i`...).
# Fit Markdown should have eliminated these; keep the detector to be safe.
_RE_ASCII_SPLIT_HEADING = re.compile(r"^\s*#{1,6}\s+[A-Za-z]\s*$")

# Empty headings (`#`, `##`, ... with no text) — source-HTML artifact from
# sites that emit empty <hN></hN> for layout. Drop the marker so the body that
# follows isn't visually disconnected.
_RE_EMPTY_HEADING = re.compile(r"^\s*#{1,6}\s*$")

# Common English stopwords for the cheap language heuristic
_EN_STOPWORDS = {
    "the", "and", "of", "to", "in", "a", "is", "that", "for", "on", "with",
    "as", "are", "be", "by", "this", "or", "from", "it", "an", "but", "not",
    "you", "your", "we", "our", "they", "their", "have", "has", "will",
    "can", "if", "when", "what", "how", "all", "more", "than", "at", "into",
    "about", "which", "also", "do", "does",
}


def _is_high_link_density(line: str) -> bool:
    """True if >80% of line chars are inside [text](url) bracketed text."""
    n = len(line)
    if n == 0:
        return False
    link_chars = sum(len(m.group(1)) for m in _RE_LINK.finditer(line))
    return link_chars / n > 0.8


def _is_link_only_line(line: str) -> bool:
    """Line is just one or more links separated by whitespace / punctuation."""
    stripped = line.strip()
    if not stripped:
        return False
    # remove all [text](url) spans; if what's left is whitespace or trivial, drop
    leftover = _RE_LINK.sub("", stripped).strip(" \t·•|-—–")
    return len(leftover) <= 3 and len(stripped) > 4


def clean_body(body: str, rules: dict) -> str:
    """Apply line-drop patterns + regex passes. Returns cleaned body string."""
    cta_patterns = [re.compile(p, re.IGNORECASE) for p in rules.get("cta_line_patterns", [])]
    noise_lines = {n.lower() for n in rules.get("noise_lines", [])}

    lines = body.splitlines()
    kept: list[str] = []

    for line in lines:
        stripped = line.strip()

        # 1. image-only / image-link-only lines
        if _RE_IMAGE_LINE.match(line) or _RE_IMAGE_LINK_LINE.match(line):
            continue

        # 2. CTA / boilerplate patterns from YAML
        if any(p.match(line) for p in cta_patterns):
            continue

        # 3. trivial noise lines (single-word gallery cruft)
        if stripped.lower() in noise_lines:
            continue

        # 4. high-link-density lines (nav/menu fragments)
        if len(stripped) > 10 and _is_high_link_density(stripped):
            continue
        if _is_link_only_line(stripped):
            continue

        # 5. ASCII-split heading remnants (defensive; should not occur)
        if _RE_ASCII_SPLIT_HEADING.match(stripped):
            continue

        # 6. empty headings (`###` with no text) — bare structure markers
        if _RE_EMPTY_HEADING.match(stripped):
            continue

        kept.append(line.rstrip())

    # collapse 3+ consecutive blanks to 2
    collapsed: list[str] = []
    blanks = 0
    for line in kept:
        if line.strip() == "":
            blanks += 1
            if blanks <= 2:
                collapsed.append(line)
        else:
            blanks = 0
            collapsed.append(line)

    return "\n".join(collapsed).strip() + "\n"


# ---------------------------------------------------------------------------
# Metrics + drop rules
# ---------------------------------------------------------------------------

def compute_metrics(body: str) -> dict:
    lines = body.splitlines()
    word_count = 0
    heading_count = 0
    has_h1 = False
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("# "):
            has_h1 = True
            heading_count += 1
            continue
        if s.startswith("#"):
            heading_count += 1
            continue
        word_count += len(s.split())

    total_chars = len(body)
    link_chars = sum(len(m.group(1)) for m in _RE_LINK.finditer(body))
    ratio = (total_chars - link_chars) / total_chars if total_chars else 0.0

    # crude English check — fraction of body words that are common English stopwords
    body_words = [w.lower() for line in lines if not line.strip().startswith("#")
                  for w in re.findall(r"[a-zA-Z']+", line)]
    if body_words:
        stopword_hits = sum(1 for w in body_words if w in _EN_STOPWORDS)
        stopword_ratio = stopword_hits / len(body_words)
    else:
        stopword_ratio = 0.0

    single_char_lines = len(_RE_SINGLE_CHAR_LINE.findall(body))
    cookie_table_lines = len(_RE_COOKIE_TABLE_LINE.findall(body))

    return {
        "word_count": word_count,
        "heading_count": heading_count,
        "has_h1": has_h1,
        "text_to_link_ratio": round(ratio, 4),
        "stopword_ratio": round(stopword_ratio, 4),
        "single_char_line_count": single_char_lines,
        "cookie_table_line_count": cookie_table_lines,
    }


def signal_score(metrics: dict, is_curated: bool) -> float:
    score = metrics["text_to_link_ratio"]
    if is_curated:
        score += 0.2
    hc = metrics["heading_count"]
    wc = metrics["word_count"]
    if hc > 0 and wc / hc > 100:
        score += 0.1
    return round(max(0.0, min(1.0, score)), 4)


_RE_SINGLE_CHAR_LINE = re.compile(r"^[A-Za-z]$", re.MULTILINE)
_RE_COOKIE_TABLE_LINE = re.compile(
    r"^\s*[-*+]\s+(Cookie|Duration|Description|This cookie|The cookie|"
    r"Cloudflare|YouTube|LinkedIn|Google\s+recaptcha)\b",
    re.IGNORECASE | re.MULTILINE,
)


def drop_reason(metrics: dict, rules: dict) -> str | None:
    d = rules["drop"]
    if metrics["word_count"] < d["min_word_count"]:
        return "too-short"
    if metrics["text_to_link_ratio"] < d["min_text_to_link_ratio"]:
        return "low-link-ratio"
    if d.get("require_h1", True) and not metrics["has_h1"]:
        return "no-h1"
    if metrics.get("single_char_line_count", 0) >= d.get("max_single_char_lines", 10):
        return "ascii-split-body"
    if metrics.get("cookie_table_line_count", 0) >= d.get("max_cookie_table_lines", 20):
        return "excessive-cookie-table"
    if d.get("english_only", True):
        if metrics["stopword_ratio"] < d["english_stopword_ratio_min"]:
            return "not-english"
    return None


# ---------------------------------------------------------------------------
# Curated domain list — mirrors cv-rag/pipeline/clean.py CURATED
# ---------------------------------------------------------------------------

CURATED = {
    "hbr.org", "career.berkeley.edu", "themuse.com", "www.themuse.com",
    "indeed.com", "www.indeed.com", "askamanager.org", "www.askamanager.org",
    "ca.topresume.com", "interviewing.io", "resources.biginterview.com",
    "extendedstudies.ucsd.edu", "www.cmu.edu", "www.bls.gov", "www.naceweb.org",
    "www.onetonline.org", "www.payscale.com", "www.pon.harvard.edu",
    "www.roberthalf.com", "www.shrm.org", "hired.com", "www.levels.fyi",
}


# ---------------------------------------------------------------------------
# Per-file processing
# ---------------------------------------------------------------------------

def process_file(
    src: Path,
    input_root: Path,
    output_root: Path,
    quarantine_root: Path,
    rules: dict,
) -> dict:
    rel = src.relative_to(input_root)
    parts = rel.parts
    topic = parts[0] if parts else "unknown"
    source_domain = parts[1] if len(parts) > 1 else "unknown"
    slug = src.stem

    raw = src.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(raw)
    cleaned = clean_body(body, rules)
    metrics = compute_metrics(cleaned)
    reason = drop_reason(metrics, rules)

    is_curated = source_domain in CURATED

    if reason:
        qpath = quarantine_root / reason / f"{topic}__{slug}.md"
        qpath.parent.mkdir(parents=True, exist_ok=True)
        qfm = dict(fm)
        qfm.update({
            "quarantine_reason": reason,
            "word_count": metrics["word_count"],
            "text_to_link_ratio": metrics["text_to_link_ratio"],
            "heading_count": metrics["heading_count"],
            "stopword_ratio": metrics["stopword_ratio"],
            "language": "en" if metrics["stopword_ratio"] >= rules["drop"]["english_stopword_ratio_min"] else "unknown",
            "cleaner_version": rules["cleaner_version"],
        })
        qpath.write_text(dump_frontmatter(qfm, cleaned), encoding="utf-8")
        return {
            "kept": False,
            "src": str(rel),
            "topic": topic,
            "source_domain": source_domain,
            "slug": slug,
            "reason": reason,
            "word_count": metrics["word_count"],
            "text_to_link_ratio": metrics["text_to_link_ratio"],
        }

    # kept file
    out_path = output_root / rel
    out_path.parent.mkdir(parents=True, exist_ok=True)
    new_fm = dict(fm)
    new_fm.update({
        "topic": topic,
        "source_domain": source_domain,
        "slug": slug,
        "word_count": metrics["word_count"],
        "text_to_link_ratio": metrics["text_to_link_ratio"],
        "heading_count": metrics["heading_count"],
        "is_curated": is_curated,
        "signal_score": signal_score(metrics, is_curated),
        "language": "en",
        "cleaner_version": rules["cleaner_version"],
        "cleaned_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    })
    out_path.write_text(dump_frontmatter(new_fm, cleaned), encoding="utf-8")
    return {
        "kept": True,
        "src": str(rel),
        "out": str(out_path.relative_to(output_root)),
        "topic": topic,
        "source_domain": source_domain,
        "slug": slug,
        "word_count": metrics["word_count"],
        "text_to_link_ratio": metrics["text_to_link_ratio"],
        "signal_score": new_fm["signal_score"],
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run(
    input_root: Path,
    output_root: Path,
    quarantine_root: Path,
    report_path: Path,
    rules_path: Path,
    *,
    run_prettier: bool = True,
) -> dict:
    rules = yaml.safe_load(rules_path.read_text(encoding="utf-8"))

    # Wipe outputs so re-runs are clean (idempotent in the strong sense)
    if output_root.exists():
        shutil.rmtree(output_root)
    if quarantine_root.exists():
        shutil.rmtree(quarantine_root)
    output_root.mkdir(parents=True)
    quarantine_root.mkdir(parents=True)

    all_files = sorted(input_root.rglob("*.md"))
    print(f"processing {len(all_files)} files from {input_root}", file=sys.stderr)

    kept: list[dict] = []
    dropped_by_reason: dict[str, list[dict]] = defaultdict(list)

    for src in all_files:
        rec = process_file(src, input_root, output_root, quarantine_root, rules)
        if rec["kept"]:
            kept.append(rec)
        else:
            dropped_by_reason[rec["reason"]].append(rec)

    if run_prettier and kept:
        print(f"running prettier on {output_root}", file=sys.stderr)
        result = subprocess.run(
            ["npx", "--yes", "prettier", "--write", "--prose-wrap=preserve", str(output_root)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"prettier exit {result.returncode}: {result.stderr[:500]}", file=sys.stderr)

    report = {
        "input_root": str(input_root),
        "output_root": str(output_root),
        "quarantine_root": str(quarantine_root),
        "rules_path": str(rules_path),
        "cleaner_version": rules["cleaner_version"],
        "kept": len(kept),
        "dropped": {r: [f["src"] for f in files] for r, files in dropped_by_reason.items()},
        "dropped_counts": {r: len(files) for r, files in dropped_by_reason.items()},
        "total_input": len(all_files),
        "stats": {
            "kept_word_count_total": sum(r["word_count"] for r in kept),
            "kept_word_count_avg": (
                sum(r["word_count"] for r in kept) // len(kept) if kept else 0
            ),
        },
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main() -> None:
    here = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="M2 — clean shipwithai re-crawled corpus")
    parser.add_argument("--input", default=str(here / "01-raw-v2"))
    parser.add_argument("--output", default=str(here / "02-cleaned"))
    parser.add_argument("--quarantine", default=str(here / "02-quarantine"))
    parser.add_argument("--report", default=str(here / "02-cleaning-report.json"))
    parser.add_argument("--rules", default=str(here / "scripts" / "cleaning_rules.yaml"))
    parser.add_argument("--no-prettier", action="store_true")
    args = parser.parse_args()

    report = run(
        Path(args.input),
        Path(args.output),
        Path(args.quarantine),
        Path(args.report),
        Path(args.rules),
        run_prettier=not args.no_prettier,
    )

    counts = report["dropped_counts"]
    drop_str = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    print(
        f"kept={report['kept']}, dropped={sum(counts.values())} ({drop_str}), "
        f"total={report['total_input']}"
    )


if __name__ == "__main__":
    main()
