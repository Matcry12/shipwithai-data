# Course: Resume & ATS Mastery for Tech Roles

**Audience:** students, bootcamp grads, career-changers, and juniors entering tech
**Format:** 7 modules, ~3 lessons each, micro-course style (short lessons + one action per lesson)
**Through-line:** *The ATS is the gate. Pass it cleanly, then write the resume that earns a recruiter's "yes" in 8 seconds.*

> Status: outline draft. Every talking point traces to a doc in the `cv-rag` corpus (`source_corpus=shipwithai-data`). Sources cited by domain per lesson; pull full text via `kb_search` before writing prose.

---

## Module 1 — How ATS Actually Works
**Objective:** Understand the digital gatekeeper before trying to beat it.

- The pipeline: parse → keyword match → auto-filter → rank → store. Only top-ranked resumes reach a human *(uppl.ai, scale.jobs)*
- The numbers: ~98% of Fortune 500 use ATS; 88% of employers admit ATS filters out qualified candidates; ~75% of resumes get rejected for missing keywords *(scale.jobs, taggd.in)*
- What ATS *can't* do: read context, recognize synonyms, evaluate quality of achievements, understand transferable skills — your job is to compensate *(scale.jobs)*

**Action:** paste your current resume into a plain-text editor; if the layout breaks, the ATS sees the same mess.

## Module 2 — Resume Structure That Passes
**Objective:** Build a resume the parser reads cleanly the first time.

- The non-negotiable sections in order: Header → Summary → Skills → Experience → Projects → Education *(blog.scale.jobs/tech-resume)*
- Formatting rules: single column, standard fonts (Arial/Calibri/Times), 10–12pt, 0.5–1in margins, .docx or text-based PDF, no tables/columns/text-boxes/graphics/headers/footers *(wahresume.com, huntr.co, jogosoccer.com)*
- Standard headers only — "Work Experience" not "My Journey"; consistent dates (`January 2021` not `Jan '21`); contact info in the body, never in a header/footer *(scale.jobs, huntr.co)*

**Action:** rebuild your resume from a blank single-column template using only the six standard sections.

## Module 3 — Bullets That Signal Impact
**Objective:** Replace "responsible for" with proof of value.

- The shift: responsibilities → achievements. *"Responsible for managing social media"* → *"Grew followers 45% across 5 platforms in 6 months"* *(resumly.ai)*
- The formula: **STAR/PAR** (Situation/Task → Action → Result) — every bullet is a mini-story with a quantified outcome *(resumly.ai, datacamp.com)*
- Quantify with the bottom line: money (revenue/savings), time (hours saved, latency reduced), people (team size, users served), rankings/recognition. ≈ symbol is fine when exact numbers aren't available *(ptechpartners.com)*
- Strong action verbs by category — Led/Orchestrated/Spearheaded (leadership), Architected/Engineered/Automated (technical), Reduced/Increased/Optimized (growth). Avoid "Responsible for" / "Assisted with" *(resumly.ai, eliteresumes.co)*

**Action:** rewrite five "responsible for" bullets using `action verb + what + how + measurable result`.

## Module 4 — Keywords & Tailoring per Job
**Objective:** Mirror the job description's language so the ATS *and* the recruiter see a match.

- Where keywords live in a JD: required skills, responsibilities (action verbs live here), preferred qualifications, tools/systems, even the mission statement *(x0pa.com)*
- The 5-step tailor: scan JD → split into skills vs. experience → mirror exact phrasing → place in summary + skills + experience → spell-check *(x0pa.com, hipcv.com)*
- Use *exact* terms ("customer support" ≠ "customer assistance"); include long-form + acronym ("Enterprise Resource Planning (ERP)"); put the literal job title in your headline — said to make you ~10× more likely to get an interview *(wahresume.com, x0pa.com)*
- Target 10–20 keywords; keyword density ~0.5–2%; **never stuff** — both ATS and humans detect it *(x0pa.com, taggd.in)*

**Action:** pick one real job posting, extract 15 keywords, and inject them naturally into your summary + skills + top experience entry.

## Module 5 — The Cover Letter That Earns a Read
**Objective:** Add the context your resume can't carry.

- Structure: header → addressed greeting (find a name — `Dear Ms. Smith`, not "To Whom It May Concern") → hook → body (your fit + their pain points) → call to action → professional sign-off → save as PDF *(resumeway.com, upwork.com)*
- The hook in line one: lead with a relevant achievement or alignment with the company's mission — never "I am writing to express my interest…" *(resumeway.com, resumewriter.sg)*
- The body answers one question: *what value will you bring*? Address the company's pain points; quantify; mirror JD keywords; keep it to one page / 3–4 short paragraphs *(resumewriter.sg, upwork.com)*

**Action:** write the opening paragraph for one real application using the "hook from line one" formula.

## Module 6 — LinkedIn That Matches Your Resume
**Objective:** Make recruiters who search find you, and make the profile they land on confirm your resume.

- Headline = your tagline. Front-load the role keyword (only ~60–80 chars show on mobile); use separators (`|`); include one achievement; skip clichés like "hard-working" *(ohhmybrand.com)*
- About section: hook → core skills with tools/keywords woven in → quantified achievements → call to action. 8–12 keywords, first-person voice, short paragraphs *(ohhmybrand.com)*
- Experience: standard job titles (translate quirky internal titles in parentheses), achievement bullets that match your resume, 3–5 keywords per role *(ohhmybrand.com)*
- Profile hygiene: photo + banner, custom URL, "Open to Work" toggle on, Featured section pinned, complete every section to maximize discoverability *(freecodecamp.org, linkedfusion.io, dev.to)*

**Action:** rewrite your headline using `Role | Specialty | Stack/Achievement` and align your About hook with your resume summary.

## Module 7 (Capstone) — One Tailored Application Packet
**Objective:** Run the full pipeline on one real job, end to end.

- Pick one role you'd actually accept → run the JD keyword extraction → tailor the resume (Modules 2–4) → write the cover letter (Module 5) → align LinkedIn (Module 6).
- Self-check: paste the resume into plain text — does it parse? Does the job title appear in the headline? Are the top 10 JD keywords present? Is every bullet STAR-quantified?
- Submit, then track: where you applied, when, and whether you got a response. The funnel is the feedback loop.

**Capstone deliverable:** one job application packet (ATS-parseable resume + tailored cover letter + matching LinkedIn) ready to send today.

---

## Source map (for drafting)
Primary corpus topics feeding this course, all 100% in our slice (`source_corpus=shipwithai-data`):
`ats-optimization`, `resume-writing`, `tech-resume`, `senior-level-resume`, `action-verbs`, `cover-letter`, `linkedin-profile`, `linkedin-optimization`. Career-gap is referenced only as a cross-link, not a citation.

Re-pull citations with:
```
kb_search(query="...", filters={"source_corpus": "shipwithai-data", "topic": "<topic>"}, k=5)
```
