#!/usr/bin/env python3
"""
Ship V2 data in the v1 deliverable format (the layout the senior already knows).

work/02-output/*.json (kept)  →  cleaned/<topic>/<slug>__<domain>.md  +  index.md

Same folder layout + frontmatter schema as v1's `cleaned/` + `index.md`, but the
BODY is the clean/structured V2 markdown (no nav/breadcrumb/footer trash) and the
metadata is V2's. career_level is derived from topic+title (entry/mid/senior/
executive), matching v1's tag vocabulary. V2 enrichment (tldr, doc_type,
core_question) is added as bonus frontmatter.

    cv-rag/.venv/bin/python scripts/v2/ship_v1_format.py
"""
from __future__ import annotations
import glob, hashlib, json, re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IN = ROOT / "work" / "02-output"
CLEANED = ROOT / "cleaned"
INDEX = ROOT / "index.md"
TODAY = date.today().isoformat()

LEVEL_ORDER = ["entry", "mid", "senior", "executive"]


def career_level(topic: str, title: str) -> list[str]:
    t = f"{title} {topic}".lower()
    lv = set()
    if any(k in t for k in ["executive", "cto", "cfo", "coo", "vp ", "vice president",
                            "c-suite", "chief ", "director"]):
        lv.add("executive")
    if any(k in t for k in ["senior", "staff", "principal", "lead ", "sr.", "sr "]):
        lv.add("senior")
    if any(k in t for k in ["mid-level", "mid level", "intermediate"]):
        lv.add("mid")
    if any(k in t for k in ["junior", "entry", "first job", "first-job", "graduate",
                            "new grad", "intern", "beginner", "no experience", "no-experience"]):
        lv.add("entry")
    # topic defaults
    lv |= {"executive-resume": {"executive", "senior"}, "senior-level-resume": {"senior"},
           "git-first-job": {"entry"}}.get(topic, set())
    if not lv:
        lv.add("mid")
    return [l for l in LEVEL_ORDER if l in lv]


def yaml_list(items: list) -> str:
    return "".join(f"\n  - {i}" for i in items)


def fm(obj: dict, levels: list[str]) -> str:
    m = obj["metadata"]
    tags = m.get("key_topics") or []
    lines = [
        "---",
        f'title: "{(m.get("title") or "").replace(chr(34), chr(39))}"',
        f'topic: "{m.get("topic")}"',
        f"career_level:{yaml_list(levels)}",
        f'source_url: "{m.get("source_url")}"',
        f'source_domain: "{m.get("source_domain")}"',
        f"word_count: {m.get('word_count')}",
        f"text_to_link_ratio: {m.get('text_to_link_ratio')}",
        f"signal_score: {m.get('signal_score')}",
        "is_curated: false",
        f"tags:{yaml_list(tags)}" if tags else "tags: []",
        f'ingested_at: "{TODAY}"',
        # ── V2 enrichment (bonus, additive) ──
        f'doc_type: "{m.get("doc_type")}"',
        f'core_question: "{(m.get("core_question") or "").replace(chr(34), chr(39))}"',
        f'tldr: "{(m.get("tldr") or "").replace(chr(34), chr(39))}"',
        "---",
    ]
    return "\n".join(lines)


_slug = re.compile(r"[^a-z0-9]+")


def run() -> None:
    if CLEANED.exists():
        import shutil
        shutil.rmtree(CLEANED)
    files = sorted(glob.glob(str(IN / "*.json")))
    by_topic: dict[str, list] = defaultdict(list)
    used: set = set()
    written = 0
    for p in files:
        obj = json.load(open(p, encoding="utf-8"))
        if obj.get("status") != "kept":
            continue
        m = obj["metadata"]
        topic = m.get("topic") or "untagged"
        levels = career_level(topic, m.get("title") or "")
        slug = _slug.sub("-", (m.get("title") or "untitled").lower()).strip("-")[:70] or "page"
        dom = m.get("source_domain") or "src"
        fname = f"{slug}__{dom}.md"
        if (topic, fname) in used:   # disambiguate collisions with a short url hash
            h = hashlib.sha256((m.get("source_url") or "").encode()).hexdigest()[:6]
            fname = f"{slug}__{dom}-{h}.md"
        used.add((topic, fname))
        sub = CLEANED / topic
        sub.mkdir(parents=True, exist_ok=True)
        (sub / fname).write_text(f"{fm(obj, levels)}\n\n{obj.get('markdown','')}", encoding="utf-8")
        by_topic[topic].append((fname, m.get("title") or fname, levels,
                                m.get("signal_score") or 0, m.get("word_count") or 0,
                                m.get("source_domain") or ""))
        written += 1

    # ── index.md (v1 format) ──
    topics = sorted(by_topic)
    total = sum(len(v) for v in by_topic.values())
    out = ["# Cleaned Files Index", "",
           f"**Total files:** {total}  ", f"**Topics:** {len(topics)}  ",
           f"**Generated:** {TODAY}  ", f"**Source:** V2 pipeline (structured + enriched)",
           "", "---", "", "## Table of Contents", ""]
    for t in topics:
        out.append(f"- [{t}](#{t}) ({len(by_topic[t])} files)")
    out += ["", "---", ""]
    for t in topics:
        rows = sorted(by_topic[t], key=lambda r: r[1].lower())
        out += [f"## {t}", "", f"**{len(rows)} files** — `cleaned/{t}/`", "",
                "| File | Title | Career Level | Signal | Words | Source |",
                "|------|-------|--------------|--------|-------|--------|"]
        for fname, title, levels, sig, wc, src in rows:
            ttl = title[:70].replace("|", "\\|")   # truncate first, then escape (no dangling backslash)
            out.append(f"| `{fname}` | {ttl} | {', '.join(levels)} | {sig:.2f} | {wc} | {src} |")
        out += ["", "---", ""]
    INDEX.write_text("\n".join(out), encoding="utf-8")

    print(f"[ship-v1] wrote {written} files → cleaned/  +  index.md ({len(topics)} topics)")


if __name__ == "__main__":
    run()
