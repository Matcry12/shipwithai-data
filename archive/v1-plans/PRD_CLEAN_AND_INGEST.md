---
status: needs-triage
title: "Clean shipwithai-data corpus and ingest into cv-rag Hybrid RAG MCP"
author: synthesized from grilling session
date: 2026-05-23
related:
  - shipwithai-data/PLAN.md
  - shipwithai-data/COMPLETION_STATUS.md
  - cv-rag/PRD_KB_INGEST.md
  - cv-rag/CLAUDE.md
labels: [needs-triage, corpus, rag, ingest, cleaning]
---

# PRD: Clean shipwithai-data and Ingest into cv-rag Hybrid RAG MCP

## Problem Statement

The `shipwithai-data/` corpus was crawled and partially processed through phases 1–5
(raw → cleaned → categorized → frequency → priority), producing 260 articles across
10 CV-writing topics and 4 career levels. Six micro-course drafts exist in
`06-microcourses/`, but their quality is limited by an underlying problem:
**`02-cleaned/` is not actually clean**. It carries YAML frontmatter but the body
still contains crawl4ai output artifacts (ASCII-split headings like `# C\nh\ni`),
marketing CTAs, link-only lines, navigation blocks, and image-link garbage.

When this corpus is consumed by an LLM for drafting course modules, the model wastes
context on noise, sees five sources stating the same thing without deduplication, and
has no provenance trail to verify any claim. Course drafts come out generic and
hard to audit.

A separate concern: the user explicitly does not trust "throw 30 files at an LLM,
get a wiki" bulk-synthesis approaches (STORM-style / LLM-Wiki). They have already
built a Hybrid RAG MCP in `cv-rag/` (BM25 + dense + reranker, Qdrant, no LLM in the
indexing pipeline) and want this corpus ingested into that existing system so it
serves both end-user CV assistance and internal course drafting from a single
auditable index.

## Solution

A two-stage pipeline owned by `shipwithai-data/`:

1. **Clean stage** — re-crawl all 260 `source_url` values from existing
   `01-raw/` frontmatter using crawl4ai with Fit Markdown mode (upstream fix
   for the ASCII-split heading and boilerplate problems). Pipe the output
   through `markdowncleaner` with a hand-maintained CTA blocklist, a small
   custom regex pass for residual crawl4ai-specific bugs, a drop-rule filter,
   and a final Prettier formatting pass. Quarantine files that fail any drop
   rule with an explicit reason. No LLM in this pipeline — deterministic,
   re-runnable, diffable.

2. **Ingest stage** — pass the cleaned corpus into `cv-rag/`'s existing pipeline
   (`parent.py → child.py → tag.py → embed.py → upsert.py`) which already
   produces a Hybrid RAG index (BM25 + dense bge-small + bge-reranker-v2-m3)
   in Qdrant. Preserve `topic` and `career_level` in each chunk's payload so
   the cv-rag MCP's existing `kb_search` tool can filter per curriculum cell
   without any changes to the server. Course drafting then runs as
   per-cell filtered retrieval against the same index that serves the end-user
   CV assistant — one index, two consumers.

Bulk LLM synthesis (STORM / LLM-Wiki), GraphRAG, LightRAG, and RAPTOR are all
explicitly out of scope. Recent benchmarks show GraphRAG often underperforms
hybrid RAG on real tasks; the user's fixed taxonomy (10 topics × 4 levels)
does not benefit from entity-graph approaches; and adding an LLM to the
indexing path violates the user's stated determinism requirement.

## User Stories

1. As a course author, I want the cleaned corpus to contain only article body
   text — no nav, no CTAs, no image links, no ASCII-split headings — so that
   downstream consumers do not waste context on noise.
2. As a course author, I want every cleaned file to carry the original `topic`
   and `career_level` frontmatter, so that I can issue per-cell filtered
   queries at draft time.
3. As a course author, I want to query the cv-rag MCP for "career-change senior"
   content and get back ranked chunks with citations, so that I can draft one
   lesson at a time without reading the full corpus.
4. As a course author, I want every retrieved chunk to come back with a
   `source_url`, so that any claim in a drafted lesson can be traced to its
   origin.
5. As a course author, I want re-running the clean stage on the same source
   URLs to produce the same output, so that I can rebuild the index from
   scratch without drift.
6. As an end-user of the CV assistant, I want the assistant to also benefit
   from this corpus, so that one ingestion serves two products.
7. As a kb maintainer, I want a `02-cleaning-report.json` after each run
   summarizing kept files, quarantined files (with reasons), and per-file
   diff stats, so that I can audit cleaning quality without reading every
   file.
8. As a kb maintainer, I want quarantined files to live in `02-quarantine/`
   organized by drop reason (too-short, low-link-ratio, not-english,
   no-h1, refetch-failed), so that I can spot-check whether the drop rules
   are calibrated correctly.
9. As a kb maintainer, I want the cleaning stage to skip files whose
   `source_url` returned a non-200 HTTP status on re-crawl, so that dead
   links naturally fall out of the corpus instead of being salvaged with
   inconsistent quality.
10. As a kb maintainer, I want the CTA blocklist to live in a version-controlled
    YAML file, so that I can add patterns over time without changing code.
11. As a kb maintainer, I want the drop thresholds (min word count, min
    text-to-link ratio) to live in the same YAML config, so that I can tune
    them without forking the cleaner.
12. As a kb maintainer, I want ingestion to be idempotent by content hash, so
    that re-ingesting the cleaned corpus does not duplicate chunks in Qdrant.
13. As a kb maintainer, I want ingested chunks tagged with
    `source_corpus: "shipwithai-data"` in their payload, so that I can filter,
    audit, or roll back this corpus without touching the original
    `cv-kb-clean/` chunks already in the index.
14. As a developer, I want `shipwithai_recrawl` and `shipwithai_clean` to be
    separate deep modules, so that one can be re-run without the other when
    iterating on cleaning rules.
15. As a developer, I want the ingest orchestrator to reuse `cv-rag/pipeline/`
    modules unchanged (parent, child, tag, embed, upsert), so that improvements
    to the indexing pipeline stay in one place.
16. As a developer, I want `shipwithai_ingest` to have end-to-end tests
    covering: cleaned file in → chunks in Qdrant with correct payload filters
    out, so that I can refactor the pipeline confidently.
17. As an evaluator, I want existing cv-rag eval runs (deterministic M6) to
    remain unaffected when this corpus is ingested, so that retrieval
    regression detection on the existing corpus still works.
18. As a course author, I want the re-crawl politeness defaults
    (3 concurrent requests, 1 req/sec per domain, 2 retries) baked in, so
    that I do not have to think about rate limits or bans.
19. As a kb maintainer, I want the cleaner to recompute `word_count`,
    `text_to_link_ratio`, and `signal_score` after stripping, so that
    downstream filters use values that reflect actual content not original
    boilerplate.
20. As a kb maintainer, I want a `re_crawled_at` and `cleaner_version` field
    added to frontmatter, so that I can detect stale files and re-clean
    selectively as cleaning rules improve.

## Implementation Decisions

### Modules

- **`shipwithai_recrawl`** (new) — owns re-crawl. Reads `source_url` from
  existing `01-raw/**/*.md` frontmatter. Uses crawl4ai with Fit Markdown
  mode. Writes to `01-raw-v2/<topic>/<source_domain>/<slug>.md` preserving
  the original frontmatter plus `re_crawled_at`. Idempotent on URL hash;
  re-running skips already-fetched files unless `--force` is passed. Quarantines
  non-200 responses to `01-raw-v2-failed/` with a `reason.txt`.
  Politeness defaults: 3 concurrent, 1 req/sec/domain, 2 retries with
  exponential backoff.

- **`shipwithai_clean`** (new) — owns the post-crawl cleaning pipeline.
  Reads from `01-raw-v2/`. Applies in order:
  1. `markdowncleaner` with YAML config (`scripts/cleaning_rules.yaml`)
     — CTA blocklist (~30 patterns), duplicate headline removal,
     encoding fix (smart quotes, nbsp, zero-width chars), drop link-only
     and image-only lines.
  2. Custom regex pass — fix ASCII-split headings, collapse 3+ blank
     lines to 2.
  3. Drop-rule filter — `word_count < 250 OR text_to_link_ratio < 0.5
     OR language != "en" OR no H1 detected` → move to
     `02-quarantine/<reason>/`.
  4. Frontmatter re-attach with preserved fields plus recomputed
     `word_count`, `text_to_link_ratio`, `signal_score`, and new
     `cleaner_version`, `language`.
  5. Prettier `--write` over the output directory.
  Output: `02-cleaned/<topic>/<source_domain>/<slug>.md`,
  `02-quarantine/<reason>/<slug>.md`, `02-cleaning-report.json`.

- **`shipwithai_ingest`** (new) — thin orchestrator that points `cv-rag`'s
  existing pipeline modules at `shipwithai-data/02-cleaned/`. Calls in order:
  `parent → child → tag → embed → upsert`. Adds `source_corpus:
  "shipwithai-data"` to each chunk's Qdrant payload. Idempotent by
  deterministic `chunk_id` derived from `(source_url, heading_path,
  child_index)`. Re-runs do not duplicate.

- **`cv-rag/pipeline/clean.py`** (modify) — accept an additional input root
  via CLI flag so the same module can process either the original
  `cv-kb-clean/` corpus or `shipwithai-data/02-cleaned/`. No behavior change
  for existing callers.

- **`cv-rag/pipeline/tag_rules.yaml`** (modify) — add tag mappings for any
  shipwithai topics not already represented (career-gap, career-change,
  ats-optimization, salary-negotiation, senior-level-resume, executive-resume,
  remote-work-resume, cover-letter, github-portfolio, linkedin-profile). Tag
  inheritance from parent to child stays as-is.

### Interfaces

- `shipwithai_recrawl.run(input_dir, output_dir, *, force=False, concurrency=3,
  per_domain_rps=1.0, max_retries=2)` → writes files, returns
  `RecrawlReport(kept: int, failed: list[FailedUrl], skipped: int)`.
- `shipwithai_clean.run(input_dir, output_dir, quarantine_dir, *,
  rules_path)` → writes files, returns `CleanReport(kept: int, dropped:
  dict[reason, list[file]], stats: dict)`.
- `shipwithai_ingest.run(cleaned_dir, *, qdrant_url, source_corpus_tag)` →
  returns `IngestReport(parents: int, children: int, skipped: int)`.

### Schema additions

- New chunk payload field in Qdrant: `source_corpus: str` (values:
  `"cv-kb-clean"`, `"shipwithai-data"`). Existing chunks get backfilled
  with `"cv-kb-clean"` on the next pipeline run.
- New frontmatter fields in `02-cleaned/`: `re_crawled_at` (ISO
  timestamp), `cleaner_version` (semver), `language` (ISO 639-1).

### What we are NOT doing

- No LLM in the cleaning pipeline.
- No bulk LLM synthesis (STORM / LLM-Wiki / canonical article generation).
- No GraphRAG, LightRAG, or RAPTOR.
- No changes to `cv-rag/server/`. The existing `kb_search` tool already
  supports payload filters, which is how course drafting will query per
  cell.
- No changes to existing eval suite or M6 acceptance criteria.

## Testing Decisions

A good test for this work asserts external behavior — given a known input
file, the cleaner produces the expected output file with the expected
frontmatter and content rules, and a known cleaned file flows through
ingest to produce a known set of chunks with correct Qdrant payload fields.
Tests do not depend on internal helper functions or implementation
details. They use small fixture corpora (3–5 files) committed to the repo,
not the full 260-file corpus.

**Modules with tests (per user instruction): `shipwithai_ingest` only.**

End-to-end tests for `shipwithai_ingest`:
- **Round-trip test:** Given a 3-file fixture in `tests/fixtures/cleaned/`,
  run `shipwithai_ingest.run()` against a local ephemeral Qdrant instance
  (docker-compose or in-process), then query `kb_search` with
  `filters={"topic": "career-change", "career_level": "senior"}` and assert
  the expected chunks come back, with `source_corpus="shipwithai-data"` in
  the payload.
- **Idempotency test:** Run ingest twice. Assert the second run produces
  zero new chunks (chunk_id collision detection).
- **Filter isolation test:** Pre-seed Qdrant with one cv-kb-clean chunk
  and one shipwithai-data chunk. Assert a filtered query for
  `source_corpus="shipwithai-data"` returns only the shipwithai chunk.
- **Co-existence test:** Assert ingesting shipwithai-data does not mutate or
  remove any pre-existing cv-kb-clean chunks.

`shipwithai_recrawl` and `shipwithai_clean` are not tested per user
instruction — they will be validated by reading the `02-cleaning-report.json`
and spot-checking output files manually.

Prior art for tests: `cv-rag/tests/eval/run_eval.py` already exercises the
full pipeline against a fixture corpus and asserts retrieval-quality
properties. New ingest tests will follow the same shape (fixture in,
property assertions out), reusing the existing Qdrant test fixture if one
exists.

## Out of Scope

- Course module drafting itself. This PRD only delivers a clean corpus and
  an indexed corpus. The course drafter is a separate piece of work that
  consumes the kb via `kb_search` filtered per curriculum cell.
- Any changes to `cv-rag/server/main.py` or `cv-rag/server/search.py`.
- Bulk LLM rewriting of cleaned content into canonical articles.
- Entity graph extraction (GraphRAG / LightRAG).
- Hierarchical summarization (RAPTOR).
- A web UI for browsing the cleaned corpus or quarantine bin.
- Backfilling `source_corpus` on existing cv-kb-clean chunks — that's a
  separate one-line migration if and when it's needed.
- Time-based TTL or refresh policy for ingested chunks.
- Automated re-crawl on a schedule.

## Further Notes

- Cost is approximately zero. crawl4ai is local. markdowncleaner and
  Prettier are local. Qdrant is local via the existing docker-compose.
  Only API-cost spend in this entire plan happens later, at course
  drafting time, when a drafter LLM reads retrieved chunks (estimated
  ~$2 for the full 40-module curriculum at Sonnet rates).
- Expected corpus attrition from re-crawl: 5–15% of source URLs (dead
  links, paywalls, Cloudflare blocks). This is acceptable; the cleaning
  report will list them explicitly.
- The MCP server has no graph component. If a future need for relational
  queries emerges (e.g. "which CV principles apply across topics X and Y?"),
  revisit GraphRAG/LightRAG then — not now.
- `cv-rag/PRD_KB_INGEST.md` describes the live search-and-ingest
  fallback path. That work is orthogonal and complementary: this PRD
  bulk-ingests the shipwithai corpus once; the other PRD handles
  individual URL ingest on demand. Both write into the same Qdrant index
  and both benefit from the same payload schema.
- The deferred decision "is the cleaned data good enough to ingest
  directly, or do we need an LLM rewrite step in between?" is to be
  answered empirically: run cleaning, sample 20 random cleaned files,
  judge by eye. Only revisit if quality is visibly insufficient after
  inspecting real output.
