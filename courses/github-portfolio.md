# Course: GitHub Portfolio That Recruiters Read

**Audience:** developers building a portfolio to back up their resume and LinkedIn
**Format:** 5 modules, ~3 lessons each, micro-course style
**Through-line:** *Your resume claims you can ship. Your GitHub proves it. Optimize the profile-README → pinned-repos → individual-README chain so a recruiter who spends 90 seconds on your profile leaves convinced.*

> Status: outline draft. Primary topic `github-portfolio` (61 articles, 0.86 signal) in `source_corpus=shipwithai-data`. Agents must run `kb_search` (rerank=false) and quote supporting `parent_text` before citing.

---

## Module 1 — Why a Portfolio Beats a Resume Claim
**Objective:** Reframe GitHub as a proof asset, not a code dump.

- The recruiter funnel for technical roles: resume gets the click, LinkedIn confirms identity, GitHub validates skill claims.
- What recruiters actually do on GitHub: scan profile → pinned repos → most-active project → individual README. Total time: 60–120 seconds.
- The portfolio answers one question per visit: *can this person ship something that works without supervision?* Code quality is secondary to clarity of intent.

**Action:** Open your GitHub in a private window. Time yourself reading your own profile like a recruiter — what's the first thing your eye lands on? Is it your strongest work?

## Module 2 — The Profile README That Sells
**Objective:** Build the one-page pitch that lives at the top of your profile.

- The profile README is a special repo named after your username — it renders above your contribution graph and pinned repos.
- Four-block structure: hook (who you are, what you build), stack (tools you actually use), highlights (1–3 projects with one-line value statements), contact (LinkedIn + email).
- Avoid: badge spam, ASCII art, "languages I dabble in" lists, every framework you ever touched. Recruiters read past these.
- Mirror your resume's role keyword in the hook line. Consistency across resume, LinkedIn, and GitHub closes credibility loops.

**Action:** Create or update your `username/username` profile README with the four-block structure — keep it under 200 lines.

## Module 3 — Pinned Repos: Six Slots, Pick Carefully
**Objective:** Curate the six projects that prove you can ship.

- GitHub gives you exactly six pinned repo slots. Treat them as the headline acts of your portfolio.
- Pick projects that satisfy: visible output (demo URL, screenshots), readable code (small surface area), and a clear problem statement.
- Bad pins to avoid: tutorial clones with no original work, broken-build repos, abandoned forks, repos with zero README.
- Order matters: strongest project first (top-left position). Recruiters read left-to-right and stop early.
- If you only have two strong projects, pin two — empty slots beat weak pins.

**Action:** Audit your current pins. For each, ask: would I show this in an interview? Unpin anything you'd hesitate to defend.

## Module 4 — The Individual README That Closes the Loop
**Objective:** Write project READMEs that turn a 30-second scan into a real impression.

- Required sections in order: title + one-line description, live demo link / screenshots, tech stack list, run-locally instructions, design decisions / trade-offs.
- The screenshot or demo GIF in the first 100 lines is the highest-leverage element — recruiters rarely scroll past it.
- "Design decisions" section is what separates senior signal from junior signal. Two paragraphs on *why* you picked Postgres over Redis, or React over Svelte, demonstrates engineering judgment.
- Don't write a wall of text. Bullets, short paragraphs, code blocks for commands.

**Action:** Pick your strongest pinned repo. Rewrite its README to lead with a screenshot/demo and a one-line value statement.

## Module 5 — Contribution Graph & Public Signals
**Objective:** Make the rest of your GitHub presence reinforce the pinned work.

- Contribution graph: not about green every day; about consistent activity across months. Long empty stretches without context read as inactivity.
- Public vs private: keep your strongest work public. Recruiters can't click what they can't see. Move toy projects to private to declutter.
- Issues, PRs, and reviews on other repos count — open-source contributions show collaboration skills the pinned repos cannot demonstrate.
- Don't game commits. Forcing daily green squares with trivial commits is detectable and signals desperation rather than craft.

**Action:** Open your "Contributions" tab. If your last six months show clusters and gaps, write one sentence in your profile README about your current focus to give the gaps context.

---

## Source map
Primary corpus topic: `github-portfolio` (61 articles, 0.86 signal). Supporting topics: `tech-resume` (for the resume-LinkedIn-GitHub triangle), `linkedin-profile`.
