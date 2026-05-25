# shipwithai-data — CV Micro-Course Build Plan

**Course:** Leonard MangalaHQ CV Writing Course (1.25)
**Audience:** Internal dev team — Node.js, Java, Mobile, AI engineers — all career levels
**Goal:** 5–10 micro-course topics derived from a cleaned, categorized CV-writing corpus
**Output directory:** `/home/matcry/Documents/Knowledge/shipwithai-data/`
**Estimated Haiku Batch cost:** $0.10–0.30

---

## Deliverables

| # | Deliverable | Path |
|---|---|---|
| 1 | Raw crawled `.md` files (cv-kb-clean + Git/GitHub) | `shipwithai-data/01-raw/` |
| 2 | Cleaned `.md` files with metadata frontmatter | `shipwithai-data/02-cleaned/` |
| 3 | Topic-categorized folder structure | `shipwithai-data/03-categorized/<topic>/` |
| 4 | Frequency analysis report | `shipwithai-data/04-frequency/frequency_report.md` + `.json` |
| 5 | Priority micro-course topic list | `shipwithai-data/05-priority/priority_list.md` |

---

## Phase 1 — Crawl + Expand Topics

**Tool:** `crawl4ai_cli` (existing, at `/home/matcry/Documents/crawl4AI`)
**Source corpus:** `cv-kb-clean/` (~1558 `.md` files, existing CV-writing crawl)
**Search engine:** SearXNG (replaces DuckDuckGo — better result quality, no rate limits)

### ⚠️ Prerequisite: Update Search Tool to SearXNG

Before running any crawl, update `crawl4ai_cli` to use SearXNG instead of DDG:
- Locate the DDG search call in `crawl4ai_cli` (likely `crawl4ai_cli/search.py`)
- Replace with SearXNG HTTP API call (`GET /search?q=...&format=json`)
- Configure SearXNG instance URL (self-hosted or public instance)
- Verify with a test query before Phase 1 run

**This must be done and verified before Phase 1 starts.**

### Tasks

- Copy `cv-kb-clean/` content into `01-raw/`
- Define expanded topic list + search queries (see below)
- For each topic: run SearXNG queries → triage URLs → crawl with `crawl4ai_cli`
- Output raw `.md` files into `01-raw/<topic>/`

### Expanded Topics + Search Queries

Each topic gets 3–5 search query variants to maximize coverage across career levels:

| Topic | Example Queries |
|---|---|
| `github-portfolio` | "how to showcase github on resume", "github profile for developers cv", "open source contributions resume" |
| `career-gap` | "resume gap explanation developer", "returning to tech after career gap cv" |
| `career-change` | "career change to software engineer resume", "non-cs degree developer cv" |
| `ats-optimization` | "ATS resume tips developer", "applicant tracking system resume keywords tech" |
| `salary-negotiation` | "salary negotiation software engineer", "how to negotiate offer developer" |
| `senior-level-resume` | "senior engineer resume examples", "staff engineer cv tips", "10 years experience resume" |
| `executive-resume` | "CTO resume examples", "VP engineering cv", "engineering director resume" |
| `remote-work-resume` | "remote developer resume tips", "distributed team experience cv" |
| *(+ any topics from Phase 4 gap analysis)* | |

> Topics and queries can be updated in `scripts/01_queries.yaml` before running — re-runnable anytime.

**Output:** `01-raw/` — `.md` files organized by topic subfolder

---

## Phase 2 — Clean + Metadata Extraction

**Strategy:** Deterministic pre-filter first, Haiku Batch only for ambiguous files.

### Metadata Schema (YAML frontmatter on each `.md`)

```yaml
---
title: "..."                    # page/section title
topic: "..."                    # controlled vocabulary (see Topics below)
career_level:                   # list — one file can cover multiple levels
  - entry                       # 0–2 years, first job, new grad
  - mid                         # 2–7 years, individual contributor
  - senior                      # 7–12 years, tech lead / staff
  - executive                   # 12+ years, director / VP / C-suite
source_url: "..."               # original crawled URL
source_domain: "..."            # e.g. resumelab.com
word_count: 0                   # computed
text_to_link_ratio: 0.0         # computed (quality signal)
signal_score: 0.0               # computed (0.0–1.0)
is_curated: false               # manual flag for hand-picked sources
tags: []                        # freeform additional tags
ingested_at: "YYYY-MM-DD"
---
```

### Controlled Topic Vocabulary (initial)

```
resume-basics
resume-formatting
work-experience
skills-section
education-section
projects-section
github-portfolio
open-source-contributions
cover-letter
linkedin-profile
career-gap
career-change
salary-negotiation
ats-optimization
job-search-strategy
interview-prep
```

### Extraction Logic

| Field | Method |
|---|---|
| `word_count`, `text_to_link_ratio` | Deterministic (count words, links) |
| `source_url`, `source_domain` | From filename / existing manifest |
| `title` | H1 heading if present, else Haiku |
| `topic` | Folder path if encoded, else keyword rules, else Haiku |
| `career_level` | Keyword rules (see below), else Haiku |
| `signal_score` | Deterministic formula (same as cv-rag) |
| `tags` | Keyword rules |

### Career Level Keyword Rules (auto-infer, no Haiku)

```
entry:     entry-level, new grad, first job, 0-2 years, junior, internship, fresh graduate
mid:       mid-level, 2-5 years, 3-7 years, individual contributor, associate
senior:    senior, staff, 7+ years, 10+ years, tech lead, principal, architect
executive: director, VP, C-suite, executive, head of, 15+ years, leadership
```

**Pre-filter rule:** If `topic` AND `career_level` can both be inferred deterministically → skip Haiku. Estimated 40–60% of files skip Haiku entirely.

**Haiku Batch prompt (for ambiguous files):**
- Send: system prompt (cached) + first 500 tokens of file
- Return: JSON `{"title": "...", "topic": "...", "career_level": [...]}`
- Model: `claude-haiku-4-5-20251001`
- Mode: Batch API (50% discount)

**Output:** `02-cleaned/` — same files with frontmatter prepended, low-quality files dropped (word_count < 200 or text_to_link_ratio < 30%)

---

## Phase 3 — Categorize by Topic Folder

**Tool:** Python script (reads `topic` from Phase 2 frontmatter)

```
03-categorized/
├── resume-basics/
├── github-portfolio/
├── cover-letter/
├── ats-optimization/
├── career-gap/
└── ...
```

Files with multiple topics go into the primary topic folder (first listed). A `manifest.json` lists all files with their full metadata for downstream use.

**Output:** `03-categorized/<topic>/<filename>.md` + `manifest.json`

---

## Phase 4 — Frequency Analysis

**Tool:** Python script (reads `manifest.json` from Phase 3)

**Metrics computed:**

1. **Topic × career level cross-table** — file count per cell
2. **Word count distribution per topic** — min, median, max, total
3. **Gap score per (topic, career_level) cell** — `1 / (count + 1)`, normalized
4. **Top 10 sparse cells** — ranked by gap score

**Output:** `04-frequency/frequency_report.md` (human-readable) + `frequency_report.json` (machine-readable)

Sample table format:
```
| Topic               | Entry | Mid | Senior | Executive | Total |
|---------------------|-------|-----|--------|-----------|-------|
| resume-basics       |  42   |  38 |   12   |     2     |  94   |
| github-portfolio    |   8   |   6 |    3   |     0     |  17   |
| salary-negotiation  |   2   |   4 |    8   |     5     |  19   |
| career-gap          |   5   |   3 |    1   |     0     |   9   |
```

---

## Phase 5 — Priority Micro-Course Topic List

**Tool:** Python rank script → Haiku writes narrative

**Ranking formula:**

```
priority_score = gap_score × team_relevance_weight
```

**Team relevance weights (manual, set once):**

| Career level | Weight |
|---|---|
| entry | 0.6 |
| mid | 1.0 |
| senior | 1.2 |
| executive | 0.4 |

*(Your team skews mid–senior developers. Adjust if needed.)*

**Script output:** ranked `(topic, career_level)` pairs with scores → fed to Haiku

**Haiku prompt:** takes ranked list + frequency data → writes `priority_list.md` as a human-readable 1-page doc with rationale for each top topic.

**Output:** `05-priority/priority_list.md`

---

## Scripts to Build

| Script | Phase | Description |
|---|---|---|
| `scripts/01_copy_raw.sh` | 1 | Copy cv-kb-clean into 01-raw, crawl Git/GitHub URLs |
| `scripts/02_extract_metadata.py` | 2 | Deterministic metadata + Haiku Batch for ambiguous |
| `scripts/02_haiku_batch.py` | 2 | Haiku Batch API calls, reads queue, writes results |
| `scripts/03_categorize.py` | 3 | Move files into topic folders, write manifest.json |
| `scripts/04_frequency.py` | 4 | Cross-tab analysis, gap scoring, report generation |
| `scripts/05_priority.py` | 5 | Rank + call Haiku for narrative priority_list.md |

---

## Token Cost Estimate

| Step | Files | Input tokens | Output tokens | Cost (Batch) |
|---|---|---|---|---|
| Phase 2 Haiku (ambiguous only, ~50%) | ~780 | ~624K | ~117K | ~$0.49 |
| Phase 5 Haiku (1 call, ranked list) | 1 | ~2K | ~800 | ~$0.003 |
| **Total** | | | | **~$0.50** |

---

## Open Questions

- [ ] Triết to confirm topic vocabulary — add/remove topics before Phase 2
- [ ] Triết to adjust team relevance weights in Phase 5 if seniority mix changes
- [ ] Git/GitHub crawl target URLs — to be decided before Phase 1 run
