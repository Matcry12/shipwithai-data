## Triết — Crawl + clean keywords data → micro-course priority list

**Original notes:** Phases: (1) Continue crawl + add new Git/GitHub topic, (2) Clean .md files with metadata, (3) Categorize by topic folder, (4) Frequency analysis, (5) Priority list of top 5-10 micro-course topics. Output: 5 deliverables in `shipwithai-data/` (folder decided by Triết). Material for 1.25 (Leonard MangalaHQ course). Token: Haiku batch + script

### Why this task matters (Context)

Leonard is auditing MangalaHQ courses (1.25) and proposing a tighter, focused structure. To know which courses to prioritize, we need data — not opinions. Your crawl provides search demand signals.

This data also seeds the future micro-course strategy: small, AI-augmented courses for student devs entering first jobs (CV writing, Git, Excel, etc.).

**Consumer:** Leonard (task 1.25) — will use your priority list to decide course strategy. Sprint 03+ will execute building micro-courses based on your priority ranking.

### 5 Phases breakdown

#### Phase 1 — Continue crawl + add new Git/GitHub topic (Day 1-5)

* Continue existing crawl pipeline (CC, CV topics from Sprint 01)

* Add NEW topic: **Git/GitHub for first-job devs**

* Suggested search queries to crawl:

  * "git rebase tutorial", "git merge vs rebase"

  * "first PR open source", "github workflow"

  * "git for beginners", "git × AI / Claude Code"

  * Common Git mistakes & how to fix

* Source pages: tutorials, blog posts, Stack Overflow Q&A, official docs

* **Output:** Raw .md files in `shipwithai-data/raw/git/` (+ existing `cc/`, `cv/` folders)

#### Phase 2 — Clean .md files with metadata (Day 3-9)

* Build cleaning script (regex + heuristics handles 80% + Haiku for hard cases)

* For each raw .md file:

  * Remove navigation, footer, ads, irrelevant content

  * Extract main content only

  * Add front-matter metadata at top:

    ```
    ---
    source_url: https://...
    crawl_date: 2026-05-XX
    topic_tags: [git, beginner]
    summary: 1-line summary
    keywords: [keyword1, keyword2, ...]
    ---
    ```

* **Output:** Cleaned .md files in `shipwithai-data/cleaned/`

#### Phase 3 — Categorize by topic folder (Day 8-10)

* Organize cleaned .md files into folders by topic:

  ```
  shipwithai-data/cleaned/
    git/
    cv-writing/
    cc/  (Claude Code)
    [other topics if any]/
  ```

* Build `index.md` manifest listing all cleaned files with metadata

* **Output:** Folder tree + `index.md`

#### Phase 4 — Frequency analysis (Day 10-12)

* For each topic, analyze:

  * Most frequent keywords (top 20-50)

  * Most common questions / pain points

  * Coverage depth (do we have enough data for that topic?)

* **Output:** `keyword-frequency-analysis.md` with tables/charts

#### Phase 5 — Priority list of top 5-10 micro-course topics (Day 11-12)

* This is the **final consumer-facing output** for Leonard

* Based on phase 4 analysis + strategic fit, rank topics by:

  * **High demand** (keyword frequency signal)

  * **Good coverage** (enough data to build a course)

  * **Strategic fit** (target = student devs entering first job)

* **Output format** (`micro-course-priority-list.md`):

  ```
  # Top 5-10 Micro-course Priorities
  ```

  ## `#1 — [Topic name]`

  * `Search demand signal: high / medium / low`

  * `Data coverage: N cleaned articles in cleaned/[topic]/`

  * `Target audience: e.g., "student devs preparing for first job"`

  * `Suggested angle: e.g., "Git × Claude Code for first PR"`

  * `Top 5 keywords: [keyword1, keyword2, ...]`

  * `Why prioritize: 1-2 sentences`

  ## `#2 — [Topic name]`

  `...`

### 5 deliverables to commit (in `shipwithai-data/`)

1. `raw/` — original crawled .md files

2. `cleaned/` — refined .md files with metadata

3. `index.md` — manifest of all cleaned files

4. `keyword-frequency-analysis.md` — analysis report

5. `micro-course-priority-list.md` — **final output for Leonard**

### Token strategy (cost control — important)

* Crawl4AI engine handles crawling → no Claude tokens

* Cleaning script with regex + heuristics handles 80% of work → no LLM tokens

* Use **Haiku** (cheaper model) for: front-matter generation, summaries, batch cleaning

* Reserve **Sonnet** only for hard cases where Haiku struggles

* **Workflow:** Sample 10-20 files first → validate cleaning prompt → batch the rest

* Estimated budget: ~30% of monthly Claude token budget

### What you decide vs what needs Leonard alignment

| You decide                                | Need Leonard alignment                                  |
| ----------------------------------------- | ------------------------------------------------------- |
| Folder structure under `shipwithai-data/` | If you want to add NEW topics beyond Git (Day 1-2 ping) |
| Git topic search queries                  | Final priority criteria weighting                       |
| Cleaning script implementation            | Confirm output format meets Leonard's needs             |
| Priority ranking methodology              | —                                                       |

### Definition of Done (DoD)

All 5 deliverables committed in `shipwithai-data/` + 1-page summary post in Telegram with link to `micro-course-priority-list.md` (so Leonard can pick it up for 1.25).

---

### Progress tracker (2026-05-05)

#### ✅ Done
- Phase 1 — Crawled 12 topics (10 CV + `git-first-job` + `claude-code-workflow`) → 773 cleaned files
- Phase 2 — YAML frontmatter metadata extracted for all files (deterministic + claude CLI batch)
- Phase 3 — All files categorized into topic folders, 0 unclassified
- Phase 4 — Frequency cross-table (topic × career level) + gap scoring → `04-frequency/frequency_report.md`
- Phase 5 — Priority ranking narrative → `05-priority/priority_list.md`
- New pipeline: `01a_search.py` (search → review JSON) + `01b_crawl.py` (crawl approved URLs) with human-in-the-loop URL approval

#### ✅ All deliverables complete (2026-05-05)
- [x] `index.md` — 773-file markdown manifest with topic sections and per-file metadata table
- [x] `micro-course-priority-list.md` — at repo root (matches spec name exactly)
- [x] `keyword-frequency-analysis.md` — top 30 keywords + domain phrases per topic, extracted from article content
- [ ] Telegram summary post — draft below, send manually to Leonard

#### Folder naming note
Task spec uses flat names (`raw/`, `cleaned/`). We use numbered prefixes (`01-raw/`, `02-cleaned/`, etc.) for pipeline ordering clarity. Align with Leonard if he has a preference.
