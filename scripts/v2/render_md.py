#!/usr/bin/env python3
"""
Pipeline V2 — Stage 6b: render human-readable markdown.

work/02-output/*.json  →  work/06-markdown/<topic>/<slug>.md   (+ INDEX.md)

The JSON objects are the machine format; this produces a browsable markdown
mirror: YAML frontmatter (all metadata + enrichment) followed by the verbatim
body. Kept docs go under their topic; quarantined go under _quarantined/<reason>.
INDEX.md is a catalog grouped by topic with one-line tldrs.

    cv-rag/.venv/bin/python scripts/v2/render_md.py
"""
from __future__ import annotations
import argparse, glob, json
from collections import defaultdict
from pathlib import Path

try:
    import yaml
    def dump_yaml(d): return yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100)
except Exception:
    def dump_yaml(d):
        lines = []
        for k, v in d.items():
            if isinstance(v, (list, dict)):
                lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
            elif v is None:
                lines.append(f"{k}: null")
            elif isinstance(v, str) and (":" in v or '"' in v or "'" in v):
                lines.append(f'{k}: {json.dumps(v, ensure_ascii=False)}')
            else:
                lines.append(f"{k}: {v}")
        return "\n".join(lines) + "\n"

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IN = ROOT / "work" / "02-output"
DEFAULT_OUT = ROOT / "work" / "06-markdown"


def frontmatter(obj: dict) -> dict:
    m = obj["metadata"]
    fm = {
        "title": m.get("title"),
        "source_url": m.get("source_url"),
        "source_domain": m.get("source_domain"),
        "topic": m.get("topic"),
        "doc_type": m.get("doc_type"),
        "author": m.get("author"),
        "published_date": m.get("published_date"),
        "fetched_at": m.get("fetched_at"),
        "language": m.get("language"),
        "word_count": m.get("word_count"),
        "reading_time": m.get("reading_time"),
        "signal_score": m.get("signal_score"),
        "status": obj.get("status"),
        "core_question": m.get("core_question"),
        "tldr": m.get("tldr"),
        "key_topics": m.get("key_topics"),
        "entities": m.get("entities"),
        "content_hash": m.get("content_hash"),
    }
    return {k: v for k, v in fm.items() if v is not None}


def run(in_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(glob.glob(str(in_dir / "*.json")))
    index: dict[str, list] = defaultdict(list)   # topic -> [(title, relpath, doc_type, wc, tldr)]
    kept = quar = 0

    for p in files:
        obj = json.load(open(p, encoding="utf-8"))
        m = obj["metadata"]
        name = Path(p).stem + ".md"
        if obj.get("status") == "kept":
            topic = m.get("topic") or "untagged"
            sub = out_dir / topic
            rel = f"{topic}/{name}"
            kept += 1
        else:
            reason = obj.get("drop_reason") or "other"
            sub = out_dir / "_quarantined" / reason
            rel = f"_quarantined/{reason}/{name}"
            quar += 1
        sub.mkdir(parents=True, exist_ok=True)

        body = obj.get("markdown", "")
        doc = f"---\n{dump_yaml(frontmatter(obj))}---\n\n{body}"
        (sub / name).write_text(doc, encoding="utf-8")

        if obj.get("status") == "kept":
            index[m.get("topic") or "untagged"].append(
                (m.get("title") or name, rel, m.get("doc_type") or "—",
                 m.get("word_count") or 0, m.get("tldr") or ""))

    # INDEX.md catalog
    lines = ["# Corpus index", "",
             f"_{kept} kept articles across {len(index)} topics "
             f"({quar} quarantined under `_quarantined/`)._", ""]
    for topic in sorted(index):
        items = sorted(index[topic], key=lambda x: x[0].lower())
        lines.append(f"## {topic}  ({len(items)})")
        lines.append("")
        for title, rel, dt, wc, tldr in items:
            tldr_s = (tldr[:140] + "…") if len(tldr) > 140 else tldr
            lines.append(f"- [{title}]({rel}) — `{dt}`, {wc}w" + (f"  \n  {tldr_s}" if tldr_s else ""))
        lines.append("")
    (out_dir / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"[render-md] wrote {kept} kept + {quar} quarantined → {out_dir}")
    print(f"[render-md] topics: {len(index)}  | catalog: {out_dir/'INDEX.md'}")


def main():
    ap = argparse.ArgumentParser(description="Pipeline V2 Stage 6b: render human-readable markdown")
    ap.add_argument("--in", dest="in_dir", default=str(DEFAULT_IN))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args()
    run(Path(a.in_dir), Path(a.out))


if __name__ == "__main__":
    main()
