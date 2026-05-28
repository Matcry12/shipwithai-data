# Course: Remote Job Hunt for Tech Roles

**Audience:** developers, engineers, and tech-adjacent professionals targeting remote or hybrid roles
**Format:** 5 modules, ~3 lessons each, micro-course style (short lessons + one action per lesson)
**Through-line:** *Remote hiring is a different funnel. The resume signals you can do the work alone. The application proves you communicate async. The interview tests both — and the offer is closed by remote-aware negotiation.*

> Status: outline draft. Every talking point traces to a doc in the `cv-rag` corpus (`source_corpus=shipwithai-data`, primary topic `remote-work-resume`). Sources cited by domain per lesson; agents must run `kb_search` (rerank=false) and quote the supporting `parent_text` before citing.

---

## Module 1 — How Remote Hiring Differs (and What That Means for Your Resume)
**Objective:** Understand the remote-hiring funnel so you stop applying like an in-office candidate.

- The remote ATS is the same ATS — but with extra filters. Recruiters add "remote," "distributed," "async," and time-zone terms as required keywords.
- "Remote experience" is now a screened qualification — not a perk. Most rejections at the resume stage come from missing remote-specific signals, not missing skills.
- Time-zone and location signals matter. Listing "Remote" without specifying time zone or country forces the recruiter to guess — and most won't.

**Action:** Open your current resume and count how many times "remote," "distributed," "async," or a time-zone keyword appears. If zero, that's the first gap to close.

## Module 2 — The Remote-Ready Resume
**Objective:** Rewrite the resume to surface remote signals the ATS and the recruiter both look for.

- Add `(Remote)` or `Remote Position` next to job titles or location. Make remote experience scannable in the first pass, not buried in bullets.
- Highlight remote-relevant skills as a named cluster: async communication (Slack, Notion), task management (Jira, Linear), virtual collaboration (Zoom, Loom), self-direction.
- Lead with outcomes that prove you ship without supervision — across time zones, with minimal handholding, with measurable results.
- Add a one-line "remote experience" summary line in your About / Summary block: "X years across N time zones, fully distributed teams" — recruiters search for this.

**Action:** Pick one current or recent role. Rewrite the location to include `(Remote)`, add three remote-relevant tools to the Skills block, and rewrite one bullet to demonstrate solo ownership with a number.

## Module 3 — The Remote Cover Letter and Application Package
**Objective:** Send an application that proves you communicate well in writing.

- The cover letter is a writing sample. For remote roles, hiring managers read it as proof you can communicate async without ambiguity.
- Address the remote angle directly in the opening: where you live, what hours you work, what time zones you have collaborated across.
- Show, don't tell, async skills: link to a Loom intro, a public Notion doc, a GitHub README — anything that demonstrates you produce clear written/recorded artifacts on demand.
- Customize per-company: cite their async tooling stack and at least one named team practice (e.g., "I saw your handbook section on default-public docs — that matches how I work").

**Action:** Draft a cover letter opening for one real remote posting that names your location, primary working hours, and one async artifact you can link to.

## Module 4 — The Remote Interview Loop
**Objective:** Prepare for the screens, take-homes, and pairing sessions that remote teams use to vet you.

- Setup matters. Camera at eye level, clean background, wired ethernet or strong Wi-Fi, headset mic — technical glitches read as "won't be reliable remotely."
- Async take-home tests are the new norm for remote roles. Treat them as deliverables: write a README, explain trade-offs, show you can document a decision without anyone in the room.
- Live pairing rounds test verbal clarity under pressure. Practice thinking out loud — narrate every decision, ask clarifying questions, do not go silent.
- Behavioral questions skew toward async self-management: "Tell me about a time you blocked yourself for a day — what unblocked you?" Have specific stories ready.

**Action:** Record a 90-second Loom answering: "How do you stay productive working remotely?" Watch it back. If you cringe at silences or filler words, do it again until it lands.

## Module 5 — Closing the Remote Offer
**Objective:** Negotiate compensation, location terms, and working agreement so the role works long-term.

- Remote compensation often comes with geographic pay bands. Ask explicitly: "What's the band for my location, and is there a single-band remote-anywhere option?"
- Equipment, home office stipend, co-working budget, internet reimbursement — these are real line items at most remote-first companies. Ask for the full list before signing.
- Working agreement: confirm core overlap hours, expected response times for async messages, and on-call expectations in writing.
- Get the remote-policy commitment in your offer letter or employment agreement, not just verbally. "Remote-first" companies sometimes shift to hybrid or RTO — a written term gives you leverage if that happens.

**Action:** Write a one-page document listing every benefit you'll ask about before accepting your next remote offer — comp band, equipment, stipends, core hours, and policy permanence. Save it for your next negotiation.

---

## Source map (for drafting)
Primary corpus topic: `remote-work-resume` (61 articles, signal 0.93). Supporting topics: `linkedin-optimization` (for the remote-on-LinkedIn angle), `cover-letter` (for the remote application section), `salary-negotiation` (for Module 5).

Re-pull citations with:
```
kb_search(query="...", filters={"source_corpus": "shipwithai-data"}, rerank=false, k=8)
```
