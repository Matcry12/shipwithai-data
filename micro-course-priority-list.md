# Top 5-10 Micro-course Priorities

## #1 — Cover Letter for Mid-Level Engineers

* Search demand signal: high
* Data coverage: 24 cleaned articles in [cleaned/cover-letter/](https://github.com/Matcry12/shipwithai-data/tree/main/cleaned/cover-letter) (only 5 tagged mid-level — thinnest cell in the entire dataset)
* Target audience: mid-level engineers (3–7 years) preparing for lateral moves or promotions
* Suggested angle: "The one-paragraph technical pitch — skip the template, write the decision you owned"
* Top 5 keywords: letter, cover, company, job, software
* Why prioritize: Highest gap score in the dataset (0.167, count=5). Mid-level devs are the most active job-seekers but have almost no targeted guidance — every generic resource is written for entry or executive level.

---

## #2 — Executive Resume Framing for Mid-Level Engineers

* Search demand signal: medium
* Data coverage: 79 cleaned articles in [cleaned/executive-resume/](https://github.com/Matcry12/shipwithai-data/tree/main/cleaned/executive-resume) (only 8 tagged mid-level)
* Target audience: mid-level engineers approaching senior or staff roles
* Suggested angle: "Impact framing vs strategy framing — write toward the next level without misrepresenting current scope"
* Top 5 keywords: resume, engineering, experience, skills, management
* Why prioritize: Strong total file count but near-zero mid-level coverage (gap score 0.111, count=8). Mid-level devs routinely imitate executive resume styles prematurely, which reads as overreach to hiring managers.

---

## #3 — LinkedIn Profile for Mid-Level Engineers

* Search demand signal: high
* Data coverage: 33 cleaned articles in [cleaned/linkedin-profile/](https://github.com/Matcry12/shipwithai-data/tree/main/cleaned/linkedin-profile) (only 8 tagged mid-level)
* Target audience: mid-level engineers who rely on referrals but are missing inbound recruiter interest
* Suggested angle: "Treat your LinkedIn summary like a README — stack, scale, what you shipped"
* Top 5 keywords: linkedin, skills, profile, headline, engineer
* Why prioritize: Tied for second-highest gap (0.111, count=8). LinkedIn is increasingly the first filter before a resume is ever requested, and mid-level-specific guidance is almost absent from the knowledge base.

---

## #4 — Claude Code Workflow on Your CV

* Search demand signal: medium
* Data coverage: 46 cleaned articles in [cleaned/claude-code-workflow/](https://github.com/Matcry12/shipwithai-data/tree/main/cleaned/claude-code-workflow) (only 9 tagged mid-level)
* Target audience: student devs and mid-level engineers entering first jobs or switching to AI-augmented teams
* Suggested angle: "Git × Claude Code for first PR — how to quantify AI-assisted output honestly"
* Top 5 keywords: code, claude, coding, developers, context
* Why prioritize: AI workflow is uniquely relevant to this team and almost absent from generic CV advice. Both entry and mid levels are sparse (gap score 0.100, count=9). This topic differentiates students entering the job market right now.

---

## #5 — Senior Cover Letters: From Applying to Being Recruited

* Search demand signal: high
* Data coverage: 24 cleaned articles in [cleaned/cover-letter/](https://github.com/Matcry12/shipwithai-data/tree/main/cleaned/cover-letter) (only 12 tagged senior)
* Target audience: senior engineers (7+ years) pivoting companies or re-entering the market
* Suggested angle: "Frame the letter as narrowing optionality for the reader, not selling yourself"
* Top 5 keywords: letter, cover, company, job, software
* Why prioritize: Gap score 0.092 after 1.2× senior weighting (count=12). Senior devs disproportionately underinvest in cover letters because they've relied on referrals — a strategy that breaks down at new companies or career pivots.

---

## #6 — Git for First Job

* Search demand signal: high
* Data coverage: 63 cleaned articles in [cleaned/git-first-job/](https://github.com/Matcry12/shipwithai-data/tree/main/cleaned/git-first-job) (only 14 tagged mid-level)
* Target audience: student devs preparing for their first dev job; bootcamp grads
* Suggested angle: "Your first PR — commit hygiene, branch naming, and how open source contributions read to a hiring team"
* Top 5 keywords: code, branch, commit, changes, review
* Why prioritize: Git is a universal requirement for every dev role, yet mid-level-targeted content is sparse (gap score 0.067, count=14). A foundational micro-course that applies across all 12 topic clusters as a prerequisite.

---

## #7 — Career Change Into Dev: Lead With Domain, Not Credentials

* Search demand signal: medium
* Data coverage: 63 cleaned articles in [cleaned/career-change/](https://github.com/Matcry12/shipwithai-data/tree/main/cleaned/career-change) (only 16 tagged mid-level)
* Target audience: mid-level career changers — bootcamp grads, domain experts moving into engineering roles
* Suggested angle: "A former nurse writing healthcare software has a differentiator — most CVs bury it"
* Top 5 keywords: resume, skills, career, job, experience
* Why prioritize: High-empathy topic with a clear underserved audience (gap score 0.059, count=16). Many team members mentor career changers or were career changers themselves, making this easy to validate and produce.

---

## Honourable Mentions

| Rank | Topic | Level | Gap Score | Notes |
|------|-------|-------|-----------|-------|
| #8 | linkedin-profile | senior | 0.042 | Logical follow-on to #3 — build it second |
| #9 | salary-negotiation | mid | 0.048 | High-value but adjacent to CV writing; consider standalone module |
| #10 | github-portfolio | mid | 0.045 | 91 files but median word count is lowest in the set — shallow coverage |

---

## What to Build Next

After closing these gaps, the next investment should be a **mobile engineer track** — mobile-specific CV patterns (app store metrics, binary size, crash rates as resume bullets) appear in none of the current topic clusters despite being a named team segment.
