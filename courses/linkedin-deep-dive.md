# Course: LinkedIn Deep Dive for Tech Professionals

**Audience:** working tech professionals, job seekers, and career-builders who already have a resume but want LinkedIn to generate inbound opportunities
**Format:** 5 modules, ~3 lessons each, micro-course style (short lessons + one action per lesson)
**Through-line:** *LinkedIn is a keyword-indexed database, not a social feed. Optimize for search first, narrative second, engagement third — and recruiters come to you.*

> Status: outline draft. Every talking point traces to a doc in the `cv-rag` corpus (`source_corpus=shipwithai-data`). Sources cited by domain per lesson; pull full text via `kb_search` before writing prose.

---

## Module 1 — Headline & Photo: Your Search Result
**Objective:** Make recruiters who search find you, and make the result look click-worthy.

- The headline is the highest-weighted searchable field. 220 chars total, but only ~60–80 visible on mobile — front-load the role keyword.
- The formula: `Role | Specialty / Stack | Outcome or Target`. Strip filler ("hard-working," "passionate"). Every word is either a keyword or a value claim.
- Headline must mirror the role keyword on your resume — consistency is what verifies you're the right person when a recruiter cross-checks.
- Photo, banner, and name field: profiles with photos receive significantly more views. Use a professional photo, a banner that signals your domain, and your real name (not pseudonyms or emojis).

**Action:** Rewrite your headline with `Role | Specialty | Target` and front-load the most-searched term.

## Module 2 — The About Section: Keywords Wrapped in Narrative
**Objective:** Convert your largest text block into a keyword-dense, human-readable pitch.

- 2,600 characters available. The first three lines on mobile show before "See more" — make them count.
- Weave 8–12 keywords into a short narrative. The algorithm scans for keyword density here; humans read for substance.
- Four-block structure: **hook** (target role + value), **skills/tools** (named tech, frameworks, domain terms), **quantified achievements** (pull from resume), **call to action** (what you want next).
- First-person voice ("I built…" not "Responsible for building…"). Short paragraphs. Echo the resume summary on key terms.

**Action:** Write the three-line hook that opens your About section — name your target role, primary skill, and one quantified achievement.

## Module 3 — Experience, Skills & Endorsements
**Objective:** Make every role entry rank in search and read as proof of competence.

- Each Experience entry gets 2,000 chars. Use them like resume bullets: action verb + what + how + measurable result.
- Job titles carry significant search weight. If your actual title is non-standard ("Pod Lead," "Growth Hacker"), append the industry equivalent in parens: `Pod Lead (Engineering Manager)`.
- Skills section: pin 3 top skills, list 50 max but prioritize the keywords that match your target role. Endorsements add weight; ask peers and managers for the skills you most want to rank for.
- Consistency rule: titles, dates, employers must match your resume exactly. Achievement phrasing can differ but the facts cannot.

**Action:** Audit one role entry — add the standard title in parens if yours is unusual, and rewrite the top bullet using `verb + what + measurable result`.

## Module 4 — Featured, Recommendations & Profile Completeness
**Objective:** Turn the discoverability signals you don't see into ones that work for you.

- Featured section: pin your resume PDF, a portfolio link, and 1–2 work samples. Most profiles leave this empty — it's free real estate.
- Custom URL: change `linkedin.com/in/abc-xyz-1234` to `linkedin.com/in/yourname`. Shareable, professional, takes 60 seconds.
- Recommendations: 2–3 strong ones from former managers or colleagues outperform 10 vague ones. Draft a starter for the person writing yours.
- Profile completeness directly affects how often LinkedIn's recommendation algorithm surfaces you. Every section filled in moves you up.

**Action:** Pin your resume PDF to Featured and change your URL to your name — both before closing the browser tab.

## Module 5 — Open to Work, Visibility, and the Recruiter Inbound Loop
**Objective:** Configure the settings that put you in front of recruiters who are actively searching.

- Turn on "Open to Work." Two visibility modes: **All members** (public green frame, max reach, current employer sees it) vs **Recruiters only** (LinkedIn Recruiter users only — discreet, targets the searches that matter most).
- Fill in target job titles, locations, and work arrangements. Recruiters filter by all three; missing fields = missing matches.
- Profile settings: ensure your profile is set to public for search engines so recruiters can find you via Google, not just LinkedIn-internal search.
- The feedback loop: after enabling visibility, track who views your profile. View patterns tell you which keywords are working and which need tuning.

**Action:** Enable "Open to Work" (pick visibility), fill in all three filter fields (titles, locations, arrangements), and verify your profile is public.

---

## Source map (for drafting)
Primary corpus topics feeding this course, all 100% in our slice (`source_corpus=shipwithai-data`):
`linkedin-profile`, `linkedin-optimization`.

Re-pull citations with:
```
kb_search(query="...", filters={"source_corpus": "shipwithai-data", "topic": "<topic>"}, k=5)
```
