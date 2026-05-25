#!/usr/bin/env python3
"""
Pipeline V2 — data-loss audit.

Traces every doc across stages and proves the pipeline didn't silently drop
article content. Writes work/DATALOSS_AUDIT.md.

Checks:
  1. count reconciliation across stage dirs
  2. body byte-identity 03-hierarchy → 02-output  (stages 4/5/6 must NOT touch body)
  3. word retention extract → output (flag big drops beyond intentional chrome)
  4. no truncation to the 6000-char enrichment excerpt; no empty kept bodies

    cv-rag/.venv/bin/python scripts/v2/audit_dataloss.py
"""
from __future__ import annotations
import glob, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
W = ROOT / "work"
EXTRACT, NORM, HIER, STRUCT, ENR, OUT = (
    W / "01-extracted", W / "02-normalized", W / "03-hierarchy",
    W / "04-structured", W / "05-enriched", W / "02-output")
RETENTION_FLOOR = 0.80      # below this word-retention → flag for review


def load(d: Path, name: str):
    p = d / name
    return json.load(open(p, encoding="utf-8")) if p.exists() else None


def wc(s: str) -> int:
    return len((s or "").split())


def main() -> None:
    lines = ["# Data-loss audit", ""]

    # ── 1. count reconciliation ──
    counts = {p.name: len(glob.glob(str(p / "*.json"))) for p in
              [EXTRACT, NORM, HIER, STRUCT, ENR, OUT]}
    out_files = sorted(glob.glob(str(OUT / "*.json")))
    kept = [f for f in out_files if json.load(open(f))["status"] == "kept"]
    extracted_ok = [f for f in glob.glob(str(EXTRACT / "*.json"))
                    if json.load(open(f)).get("status") == "extracted"]
    lines += ["## 1. Count reconciliation", "",
              f"- 01-extracted: {counts['01-extracted']} (of which status=extracted: {len(extracted_ok)})",
              f"- 02-normalized: {counts['02-normalized']}",
              f"- 03-hierarchy: {counts['03-hierarchy']}",
              f"- 04-structured: {counts['04-structured']}",
              f"- 05-enriched: {counts['05-enriched']}",
              f"- 02-output: {counts['02-output']}  (kept={len(kept)}, quarantined={counts['02-output']-len(kept)})",
              ""]
    recon_ok = (len(extracted_ok) == counts["02-normalized"] == counts["03-hierarchy"]
                == counts["04-structured"] == counts["05-enriched"] == counts["02-output"])
    lines.append(f"**Reconciliation:** {'PASS — every extracted doc flows through to output' if recon_ok else 'FAIL — counts diverge!'}")
    lines.append("")

    # ── 2. body byte-identity hierarchy → output ──
    body_changed = []
    truncated = []
    empty_kept = []
    retentions = []
    for f in out_files:
        name = Path(f).name
        out = json.load(open(f))
        out_body = out.get("markdown", "")
        h = load(HIER, name)
        if h is not None and h.get("markdown", "") != out_body:
            body_changed.append(name)
        # truncation check: enrichment excerpt was 6000 chars; ensure long docs kept full body
        if len(out_body) == 6000:
            truncated.append(name)
        if out["status"] == "kept" and not out_body.strip():
            empty_kept.append(name)
        # retention extract → output
        ex = load(EXTRACT, name)
        if ex and ex.get("markdown"):
            ewc = wc(ex["markdown"])
            if ewc > 0:
                retentions.append((wc(out_body) / ewc, name, ewc, wc(out_body)))

    lines += ["## 2. Body byte-identity: 03-hierarchy → 02-output", "",
              "Stages 4 (enrich), 5 (gate), 6 (emit) must not alter the body.",
              f"- bodies changed after hierarchy: **{len(body_changed)}** "
              f"{'(PASS — body frozen through enrich/gate/emit)' if not body_changed else '(FAIL)'}",
              ""]
    if body_changed[:5]:
        lines += [f"  - {n}" for n in body_changed[:5]]

    # ── 3. word retention extract → output ──
    retentions.sort()
    low = [r for r in retentions if r[0] < RETENTION_FLOOR]
    import statistics
    med = statistics.median([r[0] for r in retentions]) if retentions else 0
    lines += ["", "## 3. Word retention: extract → output", "",
              "Some drop is expected (chrome removal). Big drops are flagged.",
              f"- docs compared: {len(retentions)}",
              f"- median retention: {med:.3f}",
              f"- docs below {RETENTION_FLOOR:.0%} retention: **{len(low)}**", ""]
    if low:
        lines.append("| retention | extract_wc | out_wc | file |")
        lines.append("|---|---|---|---|")
        for ratio, name, ewc, owc in low[:25]:
            lines.append(f"| {ratio:.2f} | {ewc} | {owc} | {name} |")
    lines.append("")

    # ── 4. truncation / empty ──
    lines += ["## 4. Truncation & empty bodies", "",
              f"- bodies exactly 6000 chars (possible excerpt truncation): **{len(truncated)}** "
              f"{'(PASS)' if not truncated else '(REVIEW)'}",
              f"- kept docs with empty body: **{len(empty_kept)}** "
              f"{'(PASS)' if not empty_kept else '(FAIL)'}",
              f"- max body length in output: {max((len(json.load(open(f)).get('markdown','')) for f in out_files), default=0)} chars",
              ""]
    if truncated[:5]:
        lines += [f"  - {n}" for n in truncated[:5]]

    # ── verdict ──
    verdict = "PASS" if (recon_ok and not body_changed and not empty_kept and not truncated) else "REVIEW"
    lines += ["## Verdict", "",
              f"**{verdict}** — "
              + ("no data loss detected; bodies preserved verbatim through enrich/gate/emit, "
                 "counts reconcile, no truncation." if verdict == "PASS"
                 else "see flagged items above.")]

    (W / "DATALOSS_AUDIT.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"recon_ok={recon_ok} body_changed={len(body_changed)} "
          f"low_retention(<{RETENTION_FLOOR})={len(low)} truncated={len(truncated)} empty_kept={len(empty_kept)}")
    print(f"median_retention={med:.3f}  → work/DATALOSS_AUDIT.md  VERDICT={verdict}")


if __name__ == "__main__":
    main()
