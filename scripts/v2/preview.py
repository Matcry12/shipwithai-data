#!/usr/bin/env python3
"""Generate a human-readable markdown preview of Stage 1–2 extracted objects.

    cv-rag/.venv/bin/python scripts/v2/preview.py
    cv-rag/.venv/bin/python scripts/v2/preview.py --in work/01-extracted --out work/STAGE12_PREVIEW.md
"""
from __future__ import annotations
import argparse, glob, json, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def build(in_dir: str, out_path: str, excerpt_len: int = 700) -> None:
    src = sorted(glob.glob(os.path.join(in_dir, "*.json")))
    out = [
        "# Stage 1–2 output preview",
        "",
        f"_Generated from `{in_dir}` — {len(src)} files._",
        "",
        "Metadata + body excerpt per object. The full machine object is each `.json`.",
        "",
        "---", "",
    ]
    for p in src:
        d = json.load(open(p, encoding="utf-8"))
        m = d.get("base_metadata", {})
        body = d.get("markdown", "")
        excerpt = body[:excerpt_len].strip()
        out += [
            f"## {m.get('title') or '(no title)'}",
            "",
            f"- **file:** `{os.path.basename(p)}`",
            f"- **source_url:** {d['source_url']}",
            f"- **domain / topic:** {d['source_domain']} / {d['topic']}",
            f"- **status:** `{d['status']}`  |  **http:** {d['http_status']}  |  "
            f"**fetch:** {d['fetch_method']}  |  **extractor:** {d['extractor']}",
            f"- **word_count:** {d['word_count']}  |  **links:** {len(d['links'])}",
            f"- **author:** {m.get('author')}  |  **date:** {m.get('published_date')}  |  "
            f"**language:** {m.get('language')}",
            f"- **description:** {m.get('description')}",
            "",
            "**Body excerpt:**",
            "",
            "```markdown",
            excerpt,
            "…" if len(body) > excerpt_len else "",
            "```",
            "",
            "---", "",
        ]
    Path(out_path).write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {out_path} ({os.path.getsize(out_path)} bytes, {len(src)} objects)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_dir", default=str(ROOT / "work" / "01-extracted"))
    ap.add_argument("--out", default=str(ROOT / "work" / "STAGE12_PREVIEW.md"))
    ap.add_argument("--excerpt", type=int, default=700)
    a = ap.parse_args()
    build(a.in_dir, a.out, a.excerpt)


if __name__ == "__main__":
    main()
