#!/usr/bin/env python3
"""Scan Stage 1–2 outputs, report fetch/extract failures, and suggest a recrawl
strategy per failure (e.g. Freedium for Medium paywalls).

    cv-rag/.venv/bin/python scripts/v2/report_failures.py

Writes:
  • work/RECRAWL_FAILURES.md   — human-readable report grouped by strategy/domain
  • work/recrawl_failed.jsonl  — machine list (url, domain, status, strategy) for a
                                 targeted recrawl pass
"""
from __future__ import annotations
import glob, json, os
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
IN_DIR = ROOT / "work" / "01-extracted"

# Medium-hosted publications that share the paywall (Freedium bypasses these)
MEDIUM_HOSTS = {
    "medium.com", "towardsdatascience.com", "betterprogramming.pub",
    "levelup.gitconnected.com", "uxdesign.cc", "javascript.plainenglish.io",
    "python.plainenglish.io", "blog.bitsrc.io", "itnext.io",
}


def is_medium(domain: str) -> bool:
    d = domain.lower().replace("www.", "")
    return d in MEDIUM_HOSTS or d.endswith(".medium.com") or d == "medium.com"


def suggest_strategy(domain: str, http_status: int, status: str) -> tuple[str, str]:
    """Return (strategy_key, human_note)."""
    if is_medium(domain):
        return ("freedium", "Medium paywall → refetch via https://freedium.cfd/<url>")
    if http_status in (401, 402, 403):
        return ("anti-bot", "Blocked → retry with stealth UA / undetected browser; "
                            "if paywalled, try a reader proxy")
    if http_status in (404, 410):
        return ("dead", "Dead link (404/410) → drop from corpus")
    if http_status in (429,):
        return ("rate-limited", "429 → slow down, retry later with longer per-domain delay")
    if http_status >= 500:
        return ("server-error", "5xx → transient; retry later")
    if status == "extract-failed":
        return ("render-retry", "Fetched but extractor found no body → retry with "
                                 "wait_until=networkidle + delay_before_return, or it's a "
                                 "non-article page (drop)")
    if status == "fetch-failed":
        return ("fetch-retry", "No HTML after retries → timeout/JS; retry with longer "
                               "page_timeout, or site needs JS interaction")
    return ("investigate", "Unknown — inspect manually")


def main() -> None:
    files = sorted(glob.glob(str(IN_DIR / "*.json")))
    total = len(files)
    ok = 0
    failures = []  # dicts
    for p in files:
        d = json.load(open(p, encoding="utf-8"))
        if d.get("status") == "extracted":
            ok += 1
            continue
        domain = d.get("source_domain") or urlparse(d["source_url"]).netloc.replace("www.", "")
        strat, note = suggest_strategy(domain, d.get("http_status", 0), d.get("status", ""))
        failures.append({
            "source_url": d["source_url"], "source_domain": domain,
            "topic": d.get("topic", ""), "http_status": d.get("http_status", 0),
            "status": d.get("status", ""), "error": d.get("error"),
            "strategy": strat, "note": note, "file": os.path.basename(p),
        })

    # group by strategy
    by_strat: dict[str, list] = defaultdict(list)
    for f in failures:
        by_strat[f["strategy"]].append(f)

    # ── machine list ──
    (ROOT / "work" / "recrawl_failed.jsonl").write_text(
        "\n".join(json.dumps(f, ensure_ascii=False) for f in failures), encoding="utf-8")

    # ── markdown report ──
    out = [
        "# Recrawl failure report — Stage 1–2",
        "",
        f"- **total objects:** {total}",
        f"- **extracted OK:** {ok}  ({ok*100//total if total else 0}%)",
        f"- **failed:** {len(failures)}",
        "",
        "## Failures by recrawl strategy",
        "",
        "| strategy | count | what to do |",
        "|---|---|---|",
    ]
    strat_notes = {
        "freedium": "Refetch Medium URLs via `https://freedium.cfd/<url>`",
        "anti-bot": "Stealth/undetected browser retry; reader proxy if paywalled",
        "render-retry": "Refetch with `wait_until=networkidle` + delay; else drop",
        "fetch-retry": "Longer timeout / JS retry",
        "rate-limited": "Slow down, retry later",
        "server-error": "Transient 5xx, retry later",
        "dead": "404/410 — drop from corpus",
        "investigate": "Manual inspection",
    }
    for strat in sorted(by_strat, key=lambda s: -len(by_strat[s])):
        out.append(f"| `{strat}` | {len(by_strat[strat])} | {strat_notes.get(strat,'')} |")
    out += ["", "---", ""]

    for strat in sorted(by_strat, key=lambda s: -len(by_strat[s])):
        items = by_strat[strat]
        out += [f"## `{strat}` — {len(items)} ({items[0]['note']})", ""]
        # group by domain within strategy
        by_dom: dict[str, list] = defaultdict(list)
        for f in items:
            by_dom[f["source_domain"]].append(f)
        for dom in sorted(by_dom, key=lambda d: -len(by_dom[d])):
            out.append(f"### {dom} ({len(by_dom[dom])})")
            for f in by_dom[dom]:
                out.append(f"- [{f['status']}/{f['http_status']}] {f['source_url']}")
            out.append("")
        out.append("---")
        out.append("")

    (ROOT / "work" / "RECRAWL_FAILURES.md").write_text("\n".join(out), encoding="utf-8")
    print(f"objects={total} ok={ok} failed={len(failures)}")
    for strat in sorted(by_strat, key=lambda s: -len(by_strat[s])):
        print(f"  {strat:14} {len(by_strat[strat])}")
    print("→ work/RECRAWL_FAILURES.md  +  work/recrawl_failed.jsonl")


if __name__ == "__main__":
    main()
