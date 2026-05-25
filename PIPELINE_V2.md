---
title: "Pipeline V2 — URL → RAG-ready structured JSON"
date: 2026-05-25
status: spec / agreed, pending build
supersedes: FLOW.md (as-built v1), extends OUTPUT_CONTRACT.md
goal: one URL in → one structured, enriched JSON object out (Firecrawl-exact + RAG intelligence layer)
---

# Pipeline V2

**One URL in → one structured JSON object out.** Body stays verbatim; an LLM adds
a semantic metadata layer on top. Built for ingestion into the hybrid `cv-rag` MCP.

## Core principle

```
  CLEAN  ≠  STRUCTURED  ≠  ENRICHED
  (chrome     (rigid          (LLM semantic
   removed)    heading tree)   metadata on top)
```

- **Body `markdown`** = the article, verbatim, chrome stripped, heading hierarchy normalized. **Never reworded.**
- **`structure`** = a derived overlay (outline + section types) pointing INTO the verbatim body.
- **`metadata` enrichment** = LLM-generated semantic fields that *describe* the body, never *replace* it.

> **The line:** LLM as enricher/annotator = yes. LLM as body-rewriter/summarizer = no.
> The LLM never has write access to `markdown`.

---

## The flow

```
URL
 │
 ▼
┌──────────────────────────────────────────────────────────────────┐
│ STAGE 1 — FETCH                         tool: crawl4ai (+httpx)    │  no LLM
│  • httpx fast-path; fall back to crawl4ai headless Chrome for SPAs │
│  • Politeness: 3 concurrent, 1 rps/domain, 2 retries + backoff     │
│  OUT: rendered HTML, http_status, fetched_at                       │
└──────────────────────────────────────────────────────────────────┘
 │ HTML
 ▼
┌──────────────────────────────────────────────────────────────────┐
│ STAGE 2 — EXTRACT                       tool: trafilatura          │  no LLM
│  trafilatura.bare_extraction(html, output_format="markdown")       │
│  ONE call yields: markdown body + title, author, date,             │
│                   description, language, sitename                  │
│  Fallback chain: trafilatura → readability-lxml → crawl4ai Fit MD  │
│  OUT: markdown + ~80% of metadata fields                           │
└──────────────────────────────────────────────────────────────────┘
 │ markdown + base meta
 ▼
┌──────────────────────────────────────────────────────────────────┐
│ STAGE 3 — NORMALIZE                     tool: regex (~30 lines)    │  no LLM
│  Hygiene only (trafilatura already removed chrome):                │
│   • smart-quotes → ASCII, strip zero-width/nbsp                    │
│   • collapse 3+ blank lines, trim trailing whitespace             │
│  OUT: clean markdown (delete-only edits)                           │
└──────────────────────────────────────────────────────────────────┘
 │
 ▼
┌──────────────────────────────────────────────────────────────────┐
│ STAGE 3.5 — HIERARCHY REPAIR            rules + LLM fallback       │  LLM (rare)
│  Make the body a RIGID H1→H2→H3 tree:                              │
│   • exactly one H1 (title)                                         │
│   • no skipped levels (no H2→H4 jumps)                            │
│   • no empty/orphan headings; ASCII-split headings repaired       │
│  Rules fix ~90%. LLM only relabels heading LEVELS on broken docs. │
│  (LLM never edits prose — heading markers only.)                  │
│  OUT: hierarchically rigid markdown                                │
└──────────────────────────────────────────────────────────────────┘
 │
 ▼
┌──────────────────────────────────────────────────────────────────┐
│ STAGE 4 — ENRICH                        LLM (schema-enforced)     │  LLM (core)
│  LLM reads body, EMITS METADATA ONLY (cannot touch body):         │
│    tldr · entities{primary,aliases} · core_question ·             │
│    doc_type · key_topics · per-section section_type               │
│  Guardrails (see below) make this safe.                            │
│  OUT: enrichment fields + section labels                           │
└──────────────────────────────────────────────────────────────────┘
 │
 ▼
┌──────────────────────────────────────────────────────────────────┐
│ STAGE 5 — STRUCTURE + GATE              tool: pure python          │  no LLM
│  • Parse headings → structure.outline (offsets + header_path)      │
│  • Compute word_count, text_to_link_ratio, signal_score,          │
│    reading_time, content_hash (sha256 of body)                    │
│  • Verdict: status = kept | quarantined, drop_reason              │
└──────────────────────────────────────────────────────────────────┘
 │
 ▼
┌──────────────────────────────────────────────────────────────────┐
│ STAGE 6 — EMIT                          tool: pure python          │  no LLM
│  Assemble final object. Filename = slug(url-path)+"-"+hash8(url).  │
│  Write to output/ (kept + quarantined together; filter on status).│
└──────────────────────────────────────────────────────────────────┘
 │
 ▼
output/<slug>-<hash>.json   →  ready for cv-rag ingest
                                (parent.py → child.py → tag.py → embed.py → upsert.py)
```

---

## The output object

```jsonc
{
  // ─── LLM-ready payload — VERBATIM, hierarchy-normalized ───
  "markdown": "# Career Change to Software Engineer\n\n## Why switch\n\n### Salary impact\n...",

  // ─── metadata: provenance + identity + LLM enrichment ───
  "metadata": {
    // provenance (Stage 1–2, no LLM)
    "source_url":    "https://www.indeed.com/career-advice/...",
    "source_domain": "indeed.com",
    "fetched_at":    "2026-05-25T10:00:00Z",
    "http_status":   200,
    "extractor":     "trafilatura-1.12",

    // content identity (Stage 2 + 5, no LLM)
    "title":         "Career Change to Software Engineer",
    "description":   "...",
    "language":      "en",
    "word_count":    1240,
    "content_hash":  "sha256:abcd…",       // body only → dedupe + change-detect
    "reading_time":  6,
    "author":        null,
    "published_date":null,
    "og_title":      "...",

    // quality signal (Stage 5, computed, NEVER LLM)
    "signal_score":       0.82,
    "text_to_link_ratio": 0.91,
    "extractor_version":  "pipeline-2.0.0",

    // ─── LLM ENRICHMENT (Stage 4, additive — describes body, never replaces) ───
    "tldr":          "50-word abstract used for multi-pass retrieval pre-filter.",
    "entities":      { "primary": "career change to software engineering",
                       "aliases": ["career switch to SWE", "dev career pivot"] },
    "core_question": "How does a non-CS professional transition into software engineering?",
    "doc_type":      "how-to-guide",
    "key_topics":    ["resume", "bootcamp", "portfolio", "salary negotiation"]
  },

  // ─── structure: derived overlay, points INTO verbatim body ───
  "structure": {
    "section_count": 7,
    "max_depth":     3,
    "outline": [
      { "level": 1, "title": "Career Change to Software Engineer",
        "section_type": "title", "header_path": ["Career Change to Software Engineer"],
        "char_start": 0, "char_end": 412 },
      { "level": 2, "title": "Why switch", "section_type": "concept",
        "header_path": ["Career Change to Software Engineer", "Why switch"],
        "char_start": 412, "char_end": 1840 },
      { "level": 3, "title": "Salary impact", "section_type": "example",
        "header_path": ["Career Change to Software Engineer", "Why switch", "Salary impact"],
        "char_start": 980, "char_end": 1840 }
    ]
  },

  // ─── Firecrawl-style outbound links ───
  "links": ["https://...", "https://..."],

  // ─── quality-gate verdict (annotate, don't drop) ───
  "status":      "kept",     // "kept" | "quarantined"
  "drop_reason": null        // null when kept; else a drop-reason value
}
```

---

## LLM enrichment — the guardrails (this is what makes it "good")

| # | Safeguard | Guarantee |
|---|---|---|
| 1 | **Schema-enforced output** (tool-use / `outlines`) | LLM emits only the fixed metadata schema. The body is NOT in its output, so it physically cannot reword/restructure it. |
| 2 | **Faithfulness verification** | Cheap second pass confirms `entities.primary` / `key_topics` actually occur in the body. Hallucinated topic → reject + retry. |
| 3 | **Body-integrity invariant** | `body_in == body_out`, diffed. Any difference → discard enrichment, keep clean-but-unenriched version. LLM has zero write access to `markdown`. |
| 4 | **Right model for the job** | Strong model (Opus/Sonnet-class) for `core_question`/`entities` where quality compounds across every future retrieval. Don't pinch pennies here. |

---

## Why this is the right shape for cv-rag

| RAG mechanism (from research) | Field that feeds it |
|---|---|
| Multi-pass retrieval pre-filter | `metadata.tldr` |
| Entity disambiguation in vector match | `metadata.entities` |
| Answer-engine / query routing | `metadata.core_question` |
| Header-path metadata propagation (fixes ~40% of RAG failures) | `structure.outline[].header_path` |
| Parent-child chunking (parent = H2 section, child = ~200 tok) | rigid `markdown` hierarchy + `outline` |
| Per-corpus filtering / governance | `metadata.source_*` + `source_corpus` (added at ingest) |

---

## Tool stack

| Stage | Tool | Why |
|---|---|---|
| Fetch | crawl4ai + httpx fast-path | JS SPAs + anti-bot; HTTP-first keeps static pages fast |
| Extract | trafilatura | Best OSS DOM-pruning; returns metadata for free in one call |
| Normalize | regex | Trafilatura did heavy lifting; this is hygiene |
| Hierarchy repair | rules + LLM fallback | Deterministic for 90%; LLM only relabels broken heading trees |
| Enrich | LLM (schema-enforced) | The semantic intelligence layer; guarded (above) |
| Structure + gate + emit | pure python | Deterministic, testable, free |

Dependencies install into `cv-rag/.venv` (not system Python — avoids PEP 668).

---

## Explicitly excluded

- **No body summarization / template-rewrite.** `markdown` is verbatim. (The rejected "condense into a template" path.)
- **No raw HTML in the object.** Goes to a sidecar if ever needed for debugging.
- **No semantic-divergence chunking** — our content has headings; header-split wins.
- **No trillion-scale infra** (MinHash LSH, Iceberg, Spark/Ray). Content-hash dedup is enough for a ~500–1000 file corpus.
- **Hidden Context Injection** (invisible `<!-- topic -->` markers) — deferred to an opt-in phase-2 flag; it inserts (invisible) text into the body.
```
