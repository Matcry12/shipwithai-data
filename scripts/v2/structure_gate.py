#!/usr/bin/env python3
"""
Pipeline V2 — Stage 5: structure overlay + quality gate.

work/03-hierarchy/*.json  →  work/04-structured/*.json

Deterministic, no LLM. Adds the `structure` overlay (the chunker's map) and the
quality verdict. Annotates `status`; never deletes a file.

  • structure.outline  — every heading with level, title, header_path (ancestor
                         chain), char_start/char_end (span incl. subsections),
                         and a rule-based section_type baseline.
  • metadata (computed) — word_count, text_to_link_ratio, reading_time,
                         signal_score, content_hash (sha256 of body), language
                         (stopword heuristic), cleaned title (site suffix removed).
  • status/drop_reason — kept | quarantined  (too-short / not-english /
                         low-signal / no-h1).

    cv-rag/.venv/bin/python scripts/v2/structure_gate.py
"""
from __future__ import annotations
import argparse, glob, hashlib, json, math, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IN = ROOT / "work" / "03-hierarchy"
DEFAULT_OUT = ROOT / "work" / "04-structured"
STRUCTURE_VERSION = "structure-gate-2.0.0"

# ── quality thresholds ──
MIN_WORD_COUNT = 200
MIN_SIGNAL_SCORE = 0.30
NOT_ENGLISH_RATIO = 0.03      # below this stopword ratio (with enough words) = not English
EN_LANGUAGE_RATIO = 0.08      # at/above this = label "en"

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(\S.*?)[ \t]*$")
FENCE_RE = re.compile(r"^\s*```")
LINK_RE = re.compile(r"\[[^\]]*\]\([^)]+\)")

STOPWORDS = {
    "the","a","an","and","or","but","if","then","of","to","in","on","for","with",
    "as","by","at","from","is","are","was","were","be","been","being","this","that",
    "these","those","it","its","you","your","we","our","they","their","he","she",
    "his","her","i","me","my","do","does","did","have","has","had","not","no","can",
    "will","would","should","could","about","into","than","so","what","when","how",
    "which","who","there","here","more","most","some","any","all","also","just",
}

# rule-based section_type from heading keywords
SECTION_RULES = [
    ("intro",   re.compile(r"\b(introduction|overview|what is|why)\b", re.I)),
    ("step",    re.compile(r"\b(step|how to|guide|process|getting started)\b", re.I)),
    ("example", re.compile(r"\b(example|sample|template|case study)\b", re.I)),
    ("faq",     re.compile(r"\b(faq|frequently asked|questions)\b", re.I)),
    ("tips",    re.compile(r"\b(tip|best practice|do's|dont|mistake)\b", re.I)),
    ("summary", re.compile(r"\b(conclusion|summary|takeaway|final|wrap)\b", re.I)),
]


def section_type(title: str, level: int) -> str:
    if level == 1:
        return "title"
    for name, rx in SECTION_RULES:
        if rx.search(title):
            return name
    return "content"


def clean_title(title: str | None, sitename: str | None, domain: str | None) -> str | None:
    """Strip a trailing brand suffix like ' - SEEK' / ' | Indeed.com'.

    The title's brand suffix often differs from the metadata sitename (e.g. title
    says 'SEEK' but sitename is 'SEEK Limited'), so we match the trailing segment's
    first word against sitename OR domain, and only strip short (<=4 word) segments.
    """
    if not title:
        return title
    t = title.strip()
    m = re.search(r"\s*[-|–—]\s*([^-|–—]{1,40})\s*$", t)
    if m:
        seg = m.group(1).strip()
        first = re.split(r"\W+", seg.lower())[0] if seg else ""
        hay = f"{sitename or ''} {domain or ''}".lower()
        if first and len(seg.split()) <= 4 and first in hay:
            t = t[:m.start()].strip()
    return t or title.strip()


def build_outline(md: str) -> list[dict]:
    """Headings with level, title, header_path, char span, section_type."""
    lines = md.split("\n")
    # offsets of each line start
    offsets, pos = [], 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1  # +1 for the '\n'

    inside = False
    raw = []   # (line_idx, level, title, char_start)
    for i, ln in enumerate(lines):
        if FENCE_RE.match(ln):
            inside = not inside
            continue
        if inside:
            continue
        m = HEADING_RE.match(ln)
        if m:
            raw.append((i, len(m.group(1)), m.group(2).strip(), offsets[i]))

    outline, stack = [], []   # stack of (level, title)
    for k, (idx, level, title, cstart) in enumerate(raw):
        # char_end = start of next heading with level <= this level, else EOF
        cend = len(md)
        for (idx2, lvl2, _t2, cstart2) in raw[k + 1:]:
            if lvl2 <= level:
                cend = cstart2
                break
        while stack and stack[-1][0] >= level:
            stack.pop()
        header_path = [t for (_l, t) in stack] + [title]
        stack.append((level, title))
        outline.append({
            "level": level, "title": title, "section_type": section_type(title, level),
            "header_path": header_path, "char_start": cstart, "char_end": cend,
        })
    return outline


def compute_metrics(md: str) -> dict:
    words = md.split()
    wc = len(words)
    lower = [w.strip(".,;:!?\"'()[]").lower() for w in words]
    stop = sum(1 for w in lower if w in STOPWORDS)
    stop_ratio = stop / wc if wc else 0.0

    link_chars = sum(len(m) for m in LINK_RE.findall(md))
    ttl_ratio = (len(md) - link_chars) / len(md) if md else 0.0

    length_score = min(wc / 600.0, 1.0)
    prose_score = min(stop_ratio / 0.30, 1.0)
    pipe_pen = min(md.count("|") / max(len(md), 1) * 50, 0.5)
    signal = max(0.0, min(1.0, 0.5 * length_score + 0.5 * prose_score - pipe_pen))

    return {
        "word_count": wc,
        "stopword_ratio": round(stop_ratio, 4),
        "text_to_link_ratio": round(ttl_ratio, 4),
        "reading_time": max(1, math.ceil(wc / 200)),
        "signal_score": round(signal, 4),
        "content_hash": "sha256:" + hashlib.sha256(md.encode("utf-8")).hexdigest(),
    }


def gate(md: str, metrics: dict) -> tuple[str, str | None]:
    wc = metrics["word_count"]
    sr = metrics["stopword_ratio"]
    if not re.search(r"^#\s+\S", md, re.M):
        return "quarantined", "no-h1"
    if wc < MIN_WORD_COUNT:
        return "quarantined", "too-short"
    if wc > 100 and sr < NOT_ENGLISH_RATIO:
        return "quarantined", "not-english"
    if metrics["signal_score"] < MIN_SIGNAL_SCORE:
        return "quarantined", "low-signal"
    return "kept", None


def run(in_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(glob.glob(str(in_dir / "*.json")))
    kept = 0
    reasons = Counter()
    for p in files:
        d = json.load(open(p, encoding="utf-8"))
        md = d["markdown"]
        meta = d.setdefault("base_metadata", {})

        meta["title"] = clean_title(meta.get("title"), meta.get("sitename"), d.get("source_domain"))
        metrics = compute_metrics(md)
        meta.update({
            "word_count": metrics["word_count"],
            "reading_time": metrics["reading_time"],
            "signal_score": metrics["signal_score"],
            "text_to_link_ratio": metrics["text_to_link_ratio"],
            "content_hash": metrics["content_hash"],
            "language": "en" if metrics["stopword_ratio"] >= EN_LANGUAGE_RATIO else "unknown",
        })
        d["word_count"] = metrics["word_count"]

        outline = build_outline(md)
        d["structure"] = {
            "section_count": len(outline),
            "max_depth": max((o["level"] for o in outline), default=0),
            "outline": outline,
        }

        status, reason = gate(md, metrics)
        d["status"] = status
        d["drop_reason"] = reason
        d["structure_version"] = STRUCTURE_VERSION

        (out_dir / Path(p).name).write_text(
            json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        if status == "kept":
            kept += 1
        else:
            reasons[reason] += 1

    total = len(files)
    print(f"[structure-gate] processed={total} kept={kept} quarantined={total-kept} → {out_dir}")
    print(f"[structure-gate] quarantine reasons: {dict(reasons)}")


def main():
    ap = argparse.ArgumentParser(description="Pipeline V2 Stage 5: structure + gate")
    ap.add_argument("--in", dest="in_dir", default=str(DEFAULT_IN))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args()
    run(Path(a.in_dir), Path(a.out))


if __name__ == "__main__":
    main()
