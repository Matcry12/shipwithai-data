#!/usr/bin/env python3
"""
Ship the remaining 3 v1 deliverables from V2 data:

  raw/<topic>/<slug>__<domain>.md          (V2 extracted bodies, pre-clean)
  keyword-frequency-analysis.md            (top key_topics/entities per topic)
  micro-course-priority-list.md            (topics ranked by coverage + signal)

    cv-rag/.venv/bin/python scripts/v2/ship_v1_extras.py
"""
from __future__ import annotations
import glob, json, re, shutil
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXTRACT = ROOT / "work" / "01-extracted"
OUT = ROOT / "work" / "02-output"
RAW = ROOT / "raw"
TODAY = date.today().isoformat()
_slug = re.compile(r"[^a-z0-9]+")


def slugify(s: str, n: int = 70) -> str:
    return _slug.sub("-", (s or "untitled").lower()).strip("-")[:n] or "page"


# ───────────────────────── raw/ ─────────────────────────
def build_raw() -> int:
    if RAW.exists():
        shutil.rmtree(RAW)
    n = 0
    used: set = set()
    for p in sorted(glob.glob(str(EXTRACT / "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        if d.get("status") != "extracted":
            continue
        m = d.get("base_metadata") or {}
        topic = d.get("topic") or "untagged"
        dom = d.get("source_domain") or "src"
        slug = slugify(m.get("title") or Path(p).stem)
        fname = f"{slug}__{dom}.md"
        if (topic, fname) in used:
            import hashlib
            h = hashlib.sha256((d.get("source_url") or "").encode()).hexdigest()[:6]
            fname = f"{slug}__{dom}-{h}.md"
        used.add((topic, fname))
        sub = RAW / topic
        sub.mkdir(parents=True, exist_ok=True)
        fm = (f"---\nsource_url: \"{d.get('source_url')}\"\n"
              f"source_domain: \"{dom}\"\ntopic: \"{topic}\"\n"
              f"extractor: \"{d.get('extractor')}\"\nfetched_at: \"{d.get('fetched_at')}\"\n"
              f"word_count: {d.get('word_count')}\nstage: \"raw-extracted\"\n---\n\n")
        (sub / fname).write_text(fm + d.get("markdown", ""), encoding="utf-8")
        n += 1
    return n


# ───────────── load kept V2 docs ─────────────
def load_kept() -> list[dict]:
    out = []
    for p in sorted(glob.glob(str(OUT / "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        if d.get("status") == "kept":
            out.append(d)
    return out


# ───────── keyword-frequency-analysis.md ─────────
STOP_TAGS = {"resume", "cv", "guide", "tips", "career"}


def build_keyword_analysis(docs: list[dict]) -> None:
    by_topic: dict[str, Counter] = defaultdict(Counter)
    by_topic_ent: dict[str, Counter] = defaultdict(Counter)
    doctypes: dict[str, Counter] = defaultdict(Counter)
    for d in docs:
        m = d["metadata"]
        t = m.get("topic") or "untagged"
        for kt in (m.get("key_topics") or []):
            by_topic[t][kt.strip().lower()] += 1
        ent = (m.get("entities") or {}).get("primary")
        if ent:
            by_topic_ent[t][ent.strip().lower()] += 1
        doctypes[t][m.get("doc_type") or "—"] += 1

    out = ["# Keyword & Topic Frequency Analysis", "",
           f"**Generated:** {TODAY}  ", f"**Source:** V2 enrichment (key_topics + entities) over {len(docs)} kept articles",
           "", "Top topic tags and primary entities per topic, aggregated from the LLM",
           "enrichment layer (not raw text frequency).", "", "---", ""]
    for t in sorted(by_topic):
        out += [f"## {t}", "",
                f"_{sum(doctypes[t].values())} articles · doc types: "
                + ", ".join(f"{k} {v}" for k, v in doctypes[t].most_common()) + "_", "",
                "**Top key_topics:**", "",
                "| Keyword | Count |", "|---|---|"]
        for kw, c in by_topic[t].most_common(25):
            out.append(f"| {kw} | {c} |")
        out += ["", "**Top primary entities:**", ""]
        out += [f"- {e} ({c})" for e, c in by_topic_ent[t].most_common(10)]
        out += ["", "---", ""]
    (ROOT / "keyword-frequency-analysis.md").write_text("\n".join(out), encoding="utf-8")


# ───────── micro-course-priority-list.md ─────────
TOPIC_AUDIENCE = {
    "git-first-job": "student devs preparing for their first job",
    "github-portfolio": "junior devs building a portfolio for job hunting",
    "claude-code-workflow": "devs adopting AI-assisted coding workflows",
    "career-change": "professionals switching into tech",
    "career-gap": "people returning to work after a break",
    "ats-optimization": "job seekers optimizing resumes for ATS",
    "executive-resume": "senior/executive candidates",
    "senior-level-resume": "senior engineers advancing their careers",
    "salary-negotiation": "devs negotiating offers and raises",
    "remote-work-resume": "candidates targeting remote roles",
    "linkedin-profile": "devs optimizing their professional brand",
    "cover-letter": "applicants writing targeted cover letters",
}


def build_priority_list(docs: list[dict]) -> None:
    stats: dict[str, dict] = defaultdict(lambda: {"n": 0, "sig": 0.0, "words": 0, "kw": Counter()})
    for d in docs:
        m = d["metadata"]
        t = m.get("topic") or "untagged"
        s = stats[t]
        s["n"] += 1
        s["sig"] += m.get("signal_score") or 0
        s["words"] += m.get("word_count") or 0
        for kt in (m.get("key_topics") or []):
            s["kw"][kt.strip().lower()] += 1
    # rank by coverage (n) then avg signal
    ranked = sorted(stats.items(), key=lambda kv: (kv[1]["n"], kv[1]["sig"] / max(kv[1]["n"], 1)), reverse=True)
    counts = [s["n"] for _, s in ranked]
    hi = max(counts); lo = min(counts)

    def demand(n: int) -> str:
        if n >= lo + (hi - lo) * 0.66: return "high"
        if n >= lo + (hi - lo) * 0.33: return "medium"
        return "low"

    out = ["# Top Micro-course Priorities", "",
           f"**Generated:** {TODAY}  ", f"**Source:** V2 corpus ({len(docs)} structured+enriched articles)",
           "", "Ranked by data coverage (article count) and average signal quality.", "", "---", ""]
    for i, (t, s) in enumerate(ranked, 1):
        avg_sig = s["sig"] / max(s["n"], 1)
        top_kw = [k for k, _ in s["kw"].most_common(5)]
        out += [f"## #{i} — {t}", "",
                f"- **Search demand signal:** {demand(s['n'])} ({s['n']} articles crawled)",
                f"- **Data coverage:** {s['n']} cleaned articles in `cleaned/{t}/` ({s['words']:,} words total)",
                f"- **Avg signal score:** {avg_sig:.2f}",
                f"- **Target audience:** {TOPIC_AUDIENCE.get(t, 'devs')}",
                f"- **Top keywords:** {', '.join(top_kw)}",
                f"- **Why prioritize:** strong coverage ({s['n']} articles) at {avg_sig:.2f} avg signal "
                f"makes this a well-supported micro-course candidate.",
                "", "---", ""]
    (ROOT / "micro-course-priority-list.md").write_text("\n".join(out), encoding="utf-8")


def main():
    docs = load_kept()
    n_raw = build_raw()
    build_keyword_analysis(docs)
    build_priority_list(docs)
    print(f"[ship-extras] raw/={n_raw} files | keyword-frequency-analysis.md | micro-course-priority-list.md")


if __name__ == "__main__":
    main()
