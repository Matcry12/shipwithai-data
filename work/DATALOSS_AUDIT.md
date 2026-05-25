# Data-loss audit

## 1. Count reconciliation

- 01-extracted: 770 (of which status=extracted: 692)
- 02-normalized: 692
- 03-hierarchy: 692
- 04-structured: 692
- 05-enriched: 692
- 02-output: 692  (kept=602, quarantined=90)

**Reconciliation:** PASS — every extracted doc flows through to output

## 2. Body byte-identity: 03-hierarchy → 02-output

Stages 4 (enrich), 5 (gate), 6 (emit) must not alter the body.
- bodies changed after hierarchy: **0** (PASS — body frozen through enrich/gate/emit)


## 3. Word retention: extract → output

Some drop is expected (chrome removal). Big drops are flagged.
- docs compared: 692
- median retention: 1.004
- docs below 80% retention: **0**


## 4. Truncation & empty bodies

- bodies exactly 6000 chars (possible excerpt truncation): **0** (PASS)
- kept docs with empty body: **0** (PASS)
- max body length in output: 345349 chars

## Verdict

**PASS** — no data loss detected; bodies preserved verbatim through enrich/gate/emit, counts reconcile, no truncation.