---
status: in-progress
title: "Implementation plan — clean shipwithai-data and ingest into cv-rag"
date: 2026-05-23
prd: shipwithai-data/PRD_CLEAN_AND_INGEST.md
orchestrator: opus-4.7 (this assistant)
executors: sonnet-4.6 via oh-my-claudecode:executor
reviewer: opus-4.7 via oh-my-claudecode:code-reviewer
update_policy: read-only for executors; orchestrator updates after each agent run
---

# Implementation Plan

This is the orchestrator's tracker. Sonnet executors receive a copy-pasted slice of
their assigned section in their prompt; they do not write back to this file.
Only the orchestrator updates checkboxes, status, and the risk log.

## Agent Assignment Matrix

| Module                          | Owner               | Model       | Depends on        | Status        |
|---------------------------------|---------------------|-------------|-------------------|---------------|
| M1. shipwithai_recrawl          | executor-A          | sonnet-4.6  | —                 | not started   |
| M2. shipwithai_clean            | executor-B          | sonnet-4.6  | M1 output schema  | not started   |
| M3. tag_rules.yaml additions    | orchestrator (opus) | opus-4.7    | —                 | not started   |
| M4. cv-rag/pipeline/clean.py    | orchestrator (opus) | opus-4.7    | —                 | not started   |
| M5. shipwithai_ingest + tests   | executor-C          | sonnet-4.6  | M2, M3, M4        | not started   |
| Final review                    | code-reviewer       | opus-4.7    | M1–M5             | not started   |

**Parallelization plan:**
- Wave 1 (parallel): M1, M3, M4 — independent.
- Wave 2 (parallel): M2 (needs M1 schema), final review of M3 + M4.
- Wave 3: M5 (needs M2 cleaned files, M3 tag rules, M4 modified clean.py).
- Wave 4: final review pass over M1–M5.

## Handoff Contracts

Each executor must read these contracts before starting. The next agent will assume
these invariants hold.

### Contract A — M1 → M2 (recrawled raw files)

- Path: `shipwithai-data/01-raw-v2/<topic>/<source_domain>/<slug>.md`
- Frontmatter (required keys): `source_url`, `topic`, `career_level`, `slug`,
  `source_domain`, `re_crawled_at` (ISO 8601 UTC), `crawler` ("crawl4ai-fit-md"),
  `fetch_status` (200).
- Body: Fit Markdown output, no post-processing.
- Failures: `shipwithai-data/01-raw-v2-failed/<slug>/reason.txt` containing
  `{url, http_status, error, attempt_count}`.

### Contract B — M2 → M5 (cleaned files)

- Path: `shipwithai-data/02-cleaned/<topic>/<source_domain>/<slug>.md`
- Frontmatter (required keys, in addition to Contract A): `word_count`,
  `text_to_link_ratio`, `signal_score`, `cleaner_version` (semver),
  `language` (ISO 639-1).
- Body: cleaned markdown, Prettier-formatted, single H1, no ASCII-split headings,
  no CTA blocks, no link-only/image-only paragraphs.
- Quarantine: `02-quarantine/<reason>/<slug>.md` with `quarantine_reason` in
  frontmatter. Reasons: `too-short | low-link-ratio | not-english | no-h1 | refetch-failed`.
- Report: `02-cleaning-report.json` at corpus root with `{kept, dropped: {reason: [files]}, stats: {...}}`.

### Contract C — M3 (tag rules)

- Path: `cv-rag/pipeline/tag_rules.yaml` (modified).
- Existing keys preserved. New keys appended, alphabetically sorted within each
  group. No mutation of existing tag patterns.

### Contract D — M4 (cv-rag clean.py)

- New optional CLI flag: `--input-dir <path>` defaulting to current behavior.
- No behavioral change when flag is omitted. Existing callers continue to work.

### Contract E — M5 (ingest)

- Reads from `02-cleaned/` (Contract B).
- Writes to Qdrant collections `kb_parents` and `kb_children` (existing).
- Every payload includes `source_corpus: "shipwithai-data"`.
- `chunk_id = sha256(source_url + heading_path + child_index)[:16]` — deterministic.
- Idempotent: second run inserts zero new chunks.

---

## M1 — shipwithai_recrawl

**Owner:** executor-A (Sonnet 4.6)
**Status:** not started

### Steps
- [ ] 1.1 Read all `01-raw/**/*.md` frontmatter; build `[(source_url, topic, career_level, slug)]` list.
- [ ] 1.2 De-duplicate by `source_url` (some URLs may appear under multiple topics — keep first occurrence, log others).
- [ ] 1.3 Implement crawl4ai Fit Markdown fetcher with politeness: 3 concurrent, 1 req/sec/domain, 2 retries (expo backoff).
- [ ] 1.4 On success: write `01-raw-v2/<topic>/<source_domain>/<slug>.md` per Contract A.
- [ ] 1.5 On failure (non-200, timeout, network error): write `01-raw-v2-failed/<slug>/reason.txt`.
- [ ] 1.6 Idempotency: skip URL if output file already exists, unless `--force`.
- [ ] 1.7 Return `RecrawlReport(kept, failed, skipped)` and log it to stdout.

### Validation gates
- [ ] V1.1 Spot-check 5 random `01-raw-v2/` files — no ASCII-split headings present (this is the core regression we're fixing).
- [ ] V1.2 Frontmatter on every output file matches Contract A.
- [ ] V1.3 Failed URLs ≤ 15% of total (per PRD attrition estimate).

### Executor prompt rules
- No retry framework, no config layer, no logging framework. Inline constants.
- No `try/except` swallowing — log and continue, or raise.
- crawl4ai is local; do not import or call anything that hits a paid API.

---

## M2 — shipwithai_clean

**Owner:** executor-B (Sonnet 4.6)
**Status:** not started

### Steps
- [ ] 2.1 Create `shipwithai-data/scripts/cleaning_rules.yaml` with CTA blocklist (~30 patterns), drop thresholds (`min_word_count: 250`, `min_text_to_link_ratio: 0.5`), allowed languages (`["en"]`).
- [ ] 2.2 Implement `markdowncleaner` invocation with the YAML config.
- [ ] 2.3 Custom regex pass: fix ASCII-split headings (`# C\nh\ni` → `# Chi`), collapse 3+ blank lines to 2, strip image-only lines, strip link-only lines.
- [ ] 2.4 Drop-rule filter; quarantine to `02-quarantine/<reason>/`.
- [ ] 2.5 Recompute `word_count`, `text_to_link_ratio`, `signal_score`; attach `cleaner_version`, `language`.
- [ ] 2.6 Prettier `--write` pass over the output directory.
- [ ] 2.7 Emit `02-cleaning-report.json` per Contract B.

### Validation gates
- [ ] V2.1 Sample 20 random cleaned files; no CTAs, no nav, no image-only lines, single H1.
- [ ] V2.2 `02-cleaning-report.json` parseable; counts add up (`kept + sum(dropped) == input_count`).
- [ ] V2.3 Re-running on same input is a no-op (idempotent).

### Executor prompt rules
- Pure functions where possible. No global state.
- All thresholds come from `cleaning_rules.yaml`, never hardcoded.
- No LLM call anywhere in this module.

---

## M3 — tag_rules.yaml additions

**Owner:** orchestrator (Opus 4.7, direct edit)
**Status:** not started

### Steps
- [ ] 3.1 Read current `cv-rag/pipeline/tag_rules.yaml`.
- [ ] 3.2 Inventory shipwithai topics from `01-raw/` directory names.
- [ ] 3.3 Diff against existing tag rules; identify gaps.
- [ ] 3.4 Append new patterns for missing topics (career-gap, career-change, ats-optimization, salary-negotiation, senior-level-resume, executive-resume, remote-work-resume, cover-letter, github-portfolio, linkedin-profile).
- [ ] 3.5 No edits to existing rules.

---

## M4 — cv-rag/pipeline/clean.py modification

**Owner:** orchestrator (Opus 4.7, direct edit)
**Status:** not started

### Steps
- [ ] 4.1 Read current `cv-rag/pipeline/clean.py`; locate input path resolution.
- [ ] 4.2 Add `--input-dir` CLI flag, default to current value.
- [ ] 4.3 Smoke test existing call path still works.

---

## M5 — shipwithai_ingest (+ tests)

**Owner:** executor-C (Sonnet 4.6)
**Status:** not started

### Steps
- [ ] 5.1 Implement orchestrator calling `cv-rag/pipeline/{parent,child,tag,embed,upsert}.py` in order.
- [ ] 5.2 Inject `source_corpus="shipwithai-data"` into every payload at upsert time.
- [ ] 5.3 Deterministic `chunk_id = sha256(source_url + heading_path + child_index)[:16]`.
- [ ] 5.4 Implement `IngestReport(parents, children, skipped)`.

### Tests (per user instruction — only M5 is tested)
- [ ] 5.5 Round-trip test: 3-file fixture → run ingest → `kb_search` filtered query returns expected chunks with `source_corpus="shipwithai-data"`.
- [ ] 5.6 Idempotency test: second run inserts zero new chunks.
- [ ] 5.7 Filter isolation: filter by `source_corpus` returns only that corpus's chunks.
- [ ] 5.8 Co-existence: pre-seeded `cv-kb-clean` chunks unaffected.

### Validation gates
- [ ] V5.1 All 4 tests pass against ephemeral Qdrant.
- [ ] V5.2 Existing cv-rag M6 eval still passes (no regression on prior corpus).

### Executor prompt rules
- Reuse existing `cv-rag/pipeline/` modules unchanged. Do not refactor them.
- Tests assert external behavior only (payload contents, chunk counts), not internal functions.
- Use the existing Qdrant test fixture from `cv-rag/tests/` if present.

---

## Final Review (Wave 4)

**Owner:** oh-my-claudecode:code-reviewer (Opus 4.7)
**Status:** not started

### Checklist
- [ ] R1 No LLM calls anywhere in M1, M2, M3, M4.
- [ ] R2 No retry/config/logging frameworks introduced. No "manager" layer.
- [ ] R3 No half-finished implementations or TODOs left in code.
- [ ] R4 All Contracts (A–E) honored.
- [ ] R5 No mutation of existing cv-rag pipeline modules beyond M4's single flag.
- [ ] R6 No changes to `cv-rag/server/`.

---

## Risk Log

(Orchestrator updates as risks surface.)

| Date       | Risk                                                | Mitigation / Decision                       |
|------------|-----------------------------------------------------|---------------------------------------------|
| 2026-05-23 | Sonnet executors may over-engineer (config layers, retry frameworks) | Quote "no abstractions" rule in every prompt; reviewer pass enforces |
| 2026-05-23 | crawl4ai Fit Markdown may still leave artifacts on some sites | M2 custom regex pass is the safety net; quarantine catches the rest |
| 2026-05-23 | cv-rag Qdrant collection schema may already conflict with `source_corpus` field | M5 executor must verify field is additive before running upsert |

## Deferred Decisions

(Answered later, with evidence.)

- Is cleaned output good enough to ingest directly, or is an LLM rewrite needed? → Answer after V2.1 sample inspection.
- Should existing `cv-kb-clean` chunks be backfilled with `source_corpus`? → Out of scope of this plan; one-line migration when/if needed.

## Change Log

- 2026-05-23 — Plan created. Wave structure defined.
