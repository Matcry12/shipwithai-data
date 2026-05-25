#!/usr/bin/env python3
"""
Pipeline V2 — Stage 3.5: hierarchy repair.

work/02-normalized/*.json  →  work/03-hierarchy/*.json

Make every body a rigid H1 → H2 → H3(+) tree so the chunker can rely on it
(parent = H2 section, child ~200 tok, each chunk inherits its header_path).

Rules (deterministic, fence-aware — never touches inside ``` code blocks):
  1. rejoin ASCII-split headings:  "#\nC\nh\ni..."  → "# Chief..."
  2. drop empty/orphan headings:   "##" with no text
  3. ensure exactly one H1:        prepend "# {title}" if none; demote extra H1s
  4. fix skipped levels:           H1→H3 jump promoted so depth never gaps
Heading TEXT is never reworded; only the leading "#" count and obvious artifacts
change. LLM fallback (gemma4:e4b) is intentionally NOT invoked here — rules cover
the corpus; we measure first and only add the model if evidence shows a need.

    cv-rag/.venv/bin/python scripts/v2/hierarchy.py
"""
from __future__ import annotations
import argparse, glob, json, re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

from structure_gate import clean_title   # same dir; reuse the canonical cleaner

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IN = ROOT / "work" / "02-normalized"
DEFAULT_OUT = ROOT / "work" / "03-hierarchy"
HIERARCHY_VERSION = "hierarchy-2.0.0"

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(\S.*?)[ \t]*$")
EMPTY_HEADING_RE = re.compile(r"^(#{1,6})[ \t]*$")
FENCE_RE = re.compile(r"^\s*```")


def fenced_mask(lines: list[str]) -> list[bool]:
    """True for lines inside ``` fenced code blocks (and the fence lines)."""
    mask, inside = [], False
    for ln in lines:
        if FENCE_RE.match(ln):
            mask.append(True)
            inside = not inside
        else:
            mask.append(inside)
    return mask


def title_from(d: dict) -> str:
    m = d.get("base_metadata") or {}
    t = m.get("title")
    if t and t.strip():
        # strip site-brand suffix so the inserted H1 matches the cleaned title
        return clean_title(t.strip(), m.get("sitename"), d.get("source_domain"))
    # fallback: slug from URL path
    path = urlparse(d.get("source_url", "")).path.rstrip("/")
    last = path.rsplit("/", 1)[-1] if path else ""
    return re.sub(r"[-_]+", " ", last).strip().title() or "Untitled"


def rejoin_ascii_split(lines: list[str]) -> tuple[list[str], int]:
    """Empty heading followed by a run of >=3 single-char lines → one heading."""
    out, i, n = [], 0, 0
    while i < len(lines):
        m = EMPTY_HEADING_RE.match(lines[i])
        if m:
            j, chars = i + 1, []
            while j < len(lines) and len(lines[j].strip()) == 1 and lines[j].strip():
                chars.append(lines[j].strip())
                j += 1
            if len(chars) >= 3:
                out.append(f"{m.group(1)} {''.join(chars)}")
                n += 1
                i = j
                continue
        out.append(lines[i])
        i += 1
    return out, n


def repair(d: dict) -> tuple[str, dict]:
    md = d["markdown"]
    stats = {"ascii_rejoined": 0, "empty_dropped": 0,
             "h1_inserted": False, "h1_demoted": 0, "levels_fixed": 0}

    lines = md.split("\n")

    # Pass 1 — rejoin ASCII-split headings
    lines, stats["ascii_rejoined"] = rejoin_ascii_split(lines)

    # Pass 2 — drop empty headings (outside code fences)
    mask = fenced_mask(lines)
    kept = []
    for ln, fenced in zip(lines, mask):
        if not fenced and EMPTY_HEADING_RE.match(ln):
            stats["empty_dropped"] += 1
            continue
        kept.append(ln)
    lines = kept

    # Pass 3 — ensure exactly one H1
    mask = fenced_mask(lines)
    h1_idx = [i for i, ln in enumerate(lines)
              if not mask[i] and (m := HEADING_RE.match(ln)) and len(m.group(1)) == 1]
    if not h1_idx:
        lines = [f"# {title_from(d)}", ""] + lines
        stats["h1_inserted"] = True
    elif len(h1_idx) > 1:
        for i in h1_idx[1:]:
            m = HEADING_RE.match(lines[i])
            lines[i] = f"## {m.group(2)}"   # demote H1 → H2
            stats["h1_demoted"] += 1

    # Pass 4 — fix skipped levels (first heading forced to H1, no gaps after)
    mask = fenced_mask(lines)
    prev = 0
    for i, ln in enumerate(lines):
        if mask[i]:
            continue
        m = HEADING_RE.match(ln)
        if not m:
            continue
        lvl = len(m.group(1))
        new = 1 if prev == 0 else min(lvl, prev + 1)
        if new != lvl:
            lines[i] = "#" * new + " " + m.group(2)
            stats["levels_fixed"] += 1
        prev = new

    text = "\n".join(lines).strip() + "\n"
    return text, stats


def run(in_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(glob.glob(str(in_dir / "*.json")))
    processed = 0
    agg = Counter()
    no_headings = 0
    for p in files:
        d = json.load(open(p, encoding="utf-8"))
        new_md, stats = repair(d)
        d["markdown"] = new_md
        d["word_count"] = len(new_md.split())
        d["hierarchy_stats"] = stats
        d["hierarchy_version"] = HIERARCHY_VERSION
        (out_dir / Path(p).name).write_text(
            json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        processed += 1
        for k, v in stats.items():
            agg[k] += int(v)
        # flag flat docs (only the single H1, no subsections) for awareness
        if new_md.count("\n#") + new_md.startswith("#") <= 1:
            no_headings += 1

    print(f"[hierarchy] processed={processed} → {out_dir}")
    print(f"[hierarchy] h1_inserted={agg['h1_inserted']}  h1_demoted={agg['h1_demoted']}  "
          f"levels_fixed={agg['levels_fixed']}  empty_dropped={agg['empty_dropped']}  "
          f"ascii_rejoined={agg['ascii_rejoined']}")
    print(f"[hierarchy] flat docs (H1 only, no subsections): {no_headings}")


def main():
    ap = argparse.ArgumentParser(description="Pipeline V2 Stage 3.5: hierarchy repair")
    ap.add_argument("--in", dest="in_dir", default=str(DEFAULT_IN))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args()
    run(Path(a.in_dir), Path(a.out))


if __name__ == "__main__":
    main()
