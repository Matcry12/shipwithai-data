## Triết — Rebuild crawl→clean pipeline: URL → structured, RAG-ready JSON

**Original notes:** The v1 "cleaned" folder was still basically raw (chrome, broken
headings, no structure). Rebuild the pipeline so one URL in produces one
structured, enriched, LLM/RAG-ready object out (Firecrawl-exact shape). Feed the
result into the existing Hybrid RAG MCP (`cv-rag`). Engines: crawl4ai (fetch) +
trafilatura (extract) + spawned Haiku (enrich, to spare local hardware) with
gemma4:e4b as local fallback. Token: deterministic stages = $0; enrichment via
spawned Haiku agents (no API key).

### Why this task matters (Context)

The micro-course corpus (task 1.14) was crawled but never truly *structured* —
"clean" only meant chrome-stripped, not retrieval-ready. A RAG index built on a
flat wall of text retrieves poorly (no heading paths, no semantic metadata). This
rebuild produces a hierarchically-rigid, semantically-enriched corpus so the
hybrid RAG (`cv-rag`) can retrieve precisely and cite sources.

**Consumer:** the `cv-rag` MCP (CV assistant + course drafter). Both query one
Qdrant index; the course drafter filters by `source_corpus`.

### Output contract (per URL)

Firecrawl-exact JSON: `markdown` (verbatim, chrome-free, rigid H1→H2→H3) +
`metadata` (provenance + identity + quality + LLM enrichment) + `structure`
(outline with `header_path` + char offsets) + `links` + `status`/`drop_reason`.
Spec: `PIPELINE_V2.md`, `OUTPUT_CONTRACT.md`.

### Pipeline breakdown (6 stages + render)

#### Stage 1–2 — Fetch + Extract  (`scripts/v2/fetch_extract.py`)
* crawl4ai parallel headless fetch (`arun_many` + MemoryAdaptiveDispatcher + RateLimiter)
* trafilatura extraction → markdown body + title/author/date/description
* **Result:** 692/770 extracted OK (90%); failures logged for recrawl
* **Output:** `work/01-extracted/*.json`

#### Stage 3 — Normalize  (`scripts/v2/normalize.py`)
* smart-quotes→ASCII, strip zero-width/nbsp, collapse blanks, drop evidence-based chrome lines
* **Result:** 848 chrome/artifact lines dropped, 0 real-content loss (verified)
* **Output:** `work/02-normalized/*.json`

#### Stage 3.5 — Hierarchy repair  (`scripts/v2/hierarchy.py`)
* rigid H1→H2→H3: insert missing H1 from title, demote extra H1, fix skipped levels, drop empty headings, rejoin ASCII-split
* **Result:** 471 H1 inserted, 338 levels fixed, 90 empty dropped, 0 ASCII-split (gone with trafilatura)
* **Output:** `work/03-hierarchy/*.json`

#### Stage 4 — LLM enrich  (`scripts/v2/enrich.py`)
* per-doc metadata: tldr, entities{primary,aliases}, core_question, doc_type, key_topics
* **Engine: spawned Haiku** (24 agents, 3 parallel waves) — cloud, zero local load; gemma4:e4b local fallback
* guardrails: schema-enforced, faithfulness-checked, body never touched
* **Result:** 602/602 enriched, 0 rejected after tuning
* **Output:** `work/05-enriched/*.json`

#### Stage 5 — Structure overlay + quality gate  (`scripts/v2/structure_gate.py`)
* `structure.outline` (level, title, header_path, char span, section_type); metrics (signal_score, content_hash, language, reading_time); verdict kept|quarantined
* **Result:** 602 kept / 90 quarantined (79 too-short, 9 low-signal, 2 not-english)
* **Output:** `work/04-structured/*.json`

#### Stage 6 — Emit OUTPUT_CONTRACT  (`scripts/v2/emit.py`)
* assemble final Firecrawl-exact object; doc_type clamped to controlled vocab
* **Output:** `work/02-output/*.json` (692: 602 kept + 90 quarantined)

#### Stage 6b — Render human-readable markdown  (`scripts/v2/render_md.py`)
* YAML frontmatter + body per article, by topic, + `INDEX.md` catalog
* **Output:** `work/06-markdown/<topic>/<slug>.md` + `INDEX.md`

### Deliverables to commit

1. `scripts/v2/` — the 8-script pipeline (fetch_extract, normalize, hierarchy, structure_gate, enrich, emit, render_md, preview, report_failures, audit_dataloss)
2. `PIPELINE_V2.md` + `OUTPUT_CONTRACT.md` — the spec
3. `seed_urls.jsonl` — 771-URL input seed
4. `work/02-output/` — final structured JSON (machine format)
5. `work/06-markdown/` — human-readable mirror + `INDEX.md`
6. Reports — `work/DATALOSS_AUDIT.md`, `work/RECRAWL_FAILURES.md`, `work/recrawl_failed.jsonl`

### Token strategy (cost control)

* crawl4ai + trafilatura + all deterministic stages → **$0** (local)
* enrichment → **spawned Haiku** agents (no API key, runs in cloud, ~$ negligible vs 6.7h local gemma)
* gemma4:e4b → local fallback, validated, kept for offline/small re-runs
* body is never sent for rewriting — only a 6000-char excerpt for metadata extraction

### What you decide vs what needs alignment

| You decide | Need alignment |
| --- | --- |
| Pipeline stages, engines, file layout | Final `source_corpus` tag name for cv-rag |
| Quality-gate thresholds (word floor 200, signal 0.30) | Whether to recover the 78 fetch failures |
| Enrichment schema fields | Whether quarantined 90 should be revisited |

### Definition of Done (DoD)

* [x] 6-stage pipeline built, each stage one reproducible CLI
* [x] 602 kept structured+enriched objects in `work/02-output/`
* [x] Human-readable mirror in `work/06-markdown/` + INDEX
* [x] Data-loss audit PASS (0 body changes post-hierarchy, 0 content loss)
* [ ] Ingested into cv-rag Qdrant (Stage 14) — pending
* [ ] Co-existence + eval verified against existing `cv-kb-clean` corpus — pending

---

### Progress tracker (2026-05-25)

#### ✅ Done
- Stages 1–2 fetch+extract: 692/770 OK; failures in `work/recrawl_failed.jsonl`
- Stage 3 normalize: 848 chrome lines dropped, 0 content loss (verified corpus-wide)
- Stage 3.5 hierarchy: rigid H1→H2→H3; 471 H1 inserted, code fences preserved
- Stage 4 enrich: 602/602 via spawned Haiku (24 agents), schema + faithfulness enforced
- Stage 5 structure+gate: 602 kept / 90 quarantined; outline+header_path computed
- Stage 6 emit + 6b render: 692 JSON + 692 markdown, doc_type vocab clamped
- Data-loss audit: PASS — bodies byte-identical hierarchy→output, median retention 1.004

#### ⏳ Next
- [ ] Stage 14 — ingest into cv-rag (parent→child→tag→embed→upsert, `source_corpus` + header_path metadata)
- [ ] Co-existence check + eval vs `cv-kb-clean`
- [ ] (optional) Recrawl pass — networkidle retry for ~20 JS fails; drop junk URLs

#### Notes
- v1 pipeline + data archived under `archive/` (superseded by this rebuild)
- Intermediate stage dirs (`work/01`–`05`, `enrich_*`) are regenerable — gitignored
