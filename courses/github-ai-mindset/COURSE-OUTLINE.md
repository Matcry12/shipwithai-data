# Ship with AI — The Junior Developer's Edge in 2026 (course outline)

> **Status:** drafted and shipped — all 10 modules live in this directory; see [`README.md`](README.md).
> This is the design record: a re-architecture of the original GitHub-heavy course into an
> AI-native-first course built around one skill: judgment. The "v1 → v2" mapping below is
> retained to document how the current course was built from the earlier version (now removed).

**Audience:** **non-developers, students, bootcamp grads, and early juniors** building with AI in 2026 — explicitly including people *without* a CS background (the vibe-coding persona). This is locked by the brief; every design choice below serves it.
**Voice:** peer-honest, senior-informed — "here's what's actually true about surviving as a junior right now," not fake-authority checklist advice.
**Through-line:** *AI writes the code now. Your job is to out-judge it — and GitHub is where you prove you can.*
**Shape:** 10 modules across the brief's **3 delivery phases** — Phase 1 = Act 1 (become the judge), Phase 2 = Bridge (apply it on GitHub), Phase 3 = Act 2 (prove it & get hired).
**Length note:** module *count* is not a constraint (per Triết) — content quality and fit to the brief are what matter. Keep individual lessons short.
**Accessibility (tiering):** every lesson is pitched so a *non-developer* can follow it. Deeper CS material is clearly marked **"Going deeper — developer track"** and is optional, so students and career-changers aren't locked out while dev-bound juniors still get the depth.
**Freshness discipline:** body text teaches durable categories; any volatile figure (price, benchmark) lives in a dated callout, never a claim that rots in a month.

**Build risks to manage while drafting:**
1. Freshness ceiling = the corpus. Act 1 facts are only as current as the `github-ai-vibe` slice. Before drafting M4/M6/M7, check corpus coverage (managed agents, current models, GitHub-native AI features?) and supplement from current knowledge where thin — flag anything asserted beyond the corpus so it's auditable.
2. Avoid the staleness trap that bit old M6: no hard prices or single-month benchmark numbers in body text; durable categories only, volatile figures in dated callouts.
3. Source-corpus skew: existing corpus is mostly SEO career-advice blogs (resumefast, socialprachar, quickcv, codelabsacademy). Lead with the judgment/ownership thesis (which the blogs lack); use the corpus only for table-stakes mechanics.

---

## ACT 1 — Become the Judge *(the leverage)*

### Module 1 — The 2026 Shift: Why the Bar Moved
**Objective:** Understand why "I can write code" stopped being the junior value prop, and what replaced it.
- **1.1 The old deal is dead** — AI ate the boilerplate; the "cheap grunt work" value prop collapsed.
- **1.2 The three things AI can't do for you** — judgment, ownership, communication. Why fundamentals matter *more* now, not less.
- **1.3 Asset vs liability** — a junior who ships code they don't understand is dangerous; the new junior *supervises the machine*.
- **1.4 What this does to GitHub** — it's now an audit trail of judgment, not a code portfolio.
- **Action:** Honest self-audit — rate yourself on the three pillars, name your weakest.
- *Grounding: new thesis + old M6's junior-employability thread.*

### Module 2 — Build Your Moat: Enough Understanding to Judge AI
**Objective:** Build just enough of a mental model to tell when AI output is right or wrong — accessible whether or not you have a CS background.
- **2.1 Why understanding is the moat** — you can't judge what you can't follow; true for non-devs and devs alike, and it's what makes you an asset not a liability.
- **2.2 The mental models everyone needs** — what a program/data/the web/storage *actually* are, in plain language; what "correct" and "done" really mean. (no CS degree required)
- **2.3 Following what the machine does** — reading an error message and tracing cause → effect, without panic.
- **2.4 Using AI as a tutor, not an oracle** — make it explain, quiz you, and give you exercises; verify its explanations against primary docs.
- **2.5 (Going deeper — developer track)** the CS layer: data structures, complexity, stack traces, how auth/state really work — optional, for those heading into a developer role.
- **Action:** Pick one thing you currently fake your way through; have AI teach it, then explain it back *without* AI.
- *Grounding: new; the "understanding matters more" claim from M1, made actionable and accessible.*

### Module 3 — Learning in the AI Era: Use It Without Losing Your Edge
**Objective:** Develop the discipline to keep growing when the answer is one prompt away — the defining junior risk of 2026.
- **3.1 The atrophy trap** — outsourcing your thinking means you plateau and get exposed in interviews.
- **3.2 The "struggle first" rule** — attempt before you ask; use AI to *check* your work, not to *skip* the work.
- **3.3 Learning loops that stick** — explain-back, deliberate practice, building from scratch sometimes, spaced review.
- **3.4 Learn in public** — write up what you learned; the cheapest, hardest-to-fake junior signal (and it feeds your GitHub later).
- **Action:** Do one task the hard way first, then compare with AI's approach; publish a short note on what you learned.
- *Grounding: new; honest treatment of the skill-atrophy risk.*

### Module 4 — The Agentic Workflow: Your New Toolset
**Objective:** Understand how AI coding actually works now — as durable categories — and assemble a stack.
- **4.1 The spectrum** — inline autocomplete → chat assist → agentic CLI → cloud/managed agents; what each is *for*.
- **4.2 Picking your stack** — evaluate by category, not brand; cost/value in a dated callout.
- **4.3 Context is everything** — how tools "see" your project; context files (`CLAUDE.md` & friends); context quality = output quality.
- **4.4 The managed-agent shift** — what's new in 2026, and what delegating whole tasks means for a junior.
- **4.5 AI as a comprehension tool** — using agents to *understand an unfamiliar codebase* and read docs, not just generate code (often the highest-value junior use).
- **Action:** Set up one agentic tool on a real repo, run one end-to-end task, note where it helped and where it failed.
- *Grounding: rebuilt from old M6's tool section, de-staled; managed agents from current knowledge, flagged.*

### Module 5 — Vibe Coding Without the Debt: Building Fast
**Objective:** Use AI to build quickly without creating a mess you can't maintain.
- **5.1 Prompting for code that's actually good** — specificity, constraints, worked examples.
- **5.2 Spec-driven development** — spec/tests first, AI implements against them; TDD as a micro-spec.
- **5.3 The build loop** — spec → generate → run → correct, end to end.
- **5.4 The debt trap** — where vibe coding rots: sprawl, no tests, "works but I don't know why."
- **Action:** Scaffold one small feature spec-first; commit the spec *and* the implementation.
- *Grounding: old M6 Lessons 6.5–6.6, expanded.*

### Module 6 — Judgment & Verification: The Differentiator ⭐
**Objective:** Read, test, debug, and trust-but-verify AI output like an engineer, not a copy-paster.
- **6.1 Reading code critically** — how to review code you didn't write.
- **6.2 AI failure modes** — hallucinated APIs, plausible-but-wrong logic, outdated patterns.
- **6.3 Debugging with AI** — reading errors, bisecting a bug, and spotting when AI is looping you in circles instead of fixing it.
- **6.4 Verification as a discipline** — tests, manual checks, edge cases; "does it actually run?"
- **6.5 Security & tech-debt traps** — committed secrets, injection, over-engineering, dependency bloat.
- **6.6 Making verification visible** — commits and PRs that show *what you checked*.
- **Action:** Take an AI-generated snippet, document ≥3 things wrong/risky, write the fix + a test.
- *Grounding: old M6's verify + tech-debt threads, expanded into the course's centerpiece.*

---

## BRIDGE — Apply It on the Platform

### Module 7 — Coding with AI on GitHub: The Real Loop
**Objective:** Run the actual modern dev loop where AI and GitHub meet — issue → branch → PR → review — the way a working team does, not just on your laptop.
- **7.1 The GitHub-native AI surface** — framed by *capability, not vendor*: AI in the editor, assigning an issue to a coding agent, AI-generated PR summaries & reviews, AI in CI/Actions. (GitHub Copilot is *one example* of these, not the lesson — stays brief's "not Copilot-specific" lock.) *(specifics in dated callouts)*
- **7.2 The issue → branch → PR → review loop** — how AI plugs into each step of the workflow a team actually uses.
- **7.3 Letting an agent open a PR** — assign a task/issue to a coding agent, then review its PR like a teammate's. *(managed/cloud agent meets GitHub)*
- **7.4 AI code review, both directions** — using AI to review your own PR before a human sees it, *and* reading AI's review of your code critically *(ties back to M6 judgment)*.
- **7.5 Working with humans** — PR review etiquette, asking good questions, using issues/discussions; the "communication" pillar made concrete (you're hired *into a team*).
- **7.6 Hygiene, IP & data safety** — honest PR descriptions and commit provenance; **never paste secrets or proprietary code into prompts**; whose code is AI output; respecting company AI policies.
- **Action:** Run one full issue → PR → review cycle using an AI agent on a real repo; review and verify its PR before you merge it.
- *Grounding: old M6 tool/workflow threads + current GitHub-platform AI features, flagged where beyond the corpus.*

---

## ACT 2 — Prove It & Get Hired *(the proof surface)*

### Module 8 — GitHub as Your Evidence Locker
**Objective:** Turn GitHub from a code dump into a 2-minute audit trail of judgment.
- **8.1 What the signal is now** — why working code proves less; what survives the AI flood (commits, tests, honest provenance, consistency).
- **8.2 The 30-second recruiter scan** — profile, pinned repos, README *(compressed from old M1)*.
- **8.3 Commits & PRs that show reasoning** — the why-not-what rule; honest AI provenance in commit messages.
- **8.4 Profile & README essentials** — second resume, the skeleton, what to include *(compressed from old M4)*.
- **8.5 The Git you actually need** — branches, meaningful commits, no secrets, as table stakes *(folded from old M2)*.
- **Action:** Run the recruiter scan on yourself + rewrite 3 commits to show reasoning.
- *Grounding: merges old M1 + M4 + M2 essentials.*

### Module 9 — Build Something Real with AI
**Objective:** Scope, build AI-native, and deploy one anchor project you fully understand and can defend.
- **9.1 Scoping for ownership** — a real problem, not a tutorial reconstruction *(from old M3)*.
- **9.2 Building it AI-native** — apply Act 1 (agentic workflow + verification) to a real build.
- **9.3 The quality bar** — tests, README, `.env.example`, deployed live.
- **9.4 The "explain your own code" rule** — never ship what you can't defend in an interview.
- **9.5 (Optional track) Open source when you're ready** — one beginner issue + the contributing flow *(folded from old M5, now optional)*.
- **Action:** Ship one deployed flagship, AI-native, README explaining what you built *and what you judged*.
- *Grounding: old M3 + M2 build essentials + optional M5.*

### Module 10 — Land the Role
**Objective:** Align GitHub/résumé/LinkedIn and walk into interviews able to defend your AI-assisted work.
- **10.1 Close the loop** — GitHub, résumé, LinkedIn must agree *(from old M7)*.
- **10.2 Projects as talking points** — STAR, the narrative arc.
- **10.3 The 2026 interview question** — *"what did the AI do, what did you judge?"* — answering it credibly.
- **10.4 Capstone checklist** — profile, flagship, repos, consistency, interview readiness.
- **Action:** Final capstone — full alignment check + a rehearsed flagship talking point covering its AI-assisted parts.
- *Grounding: old M7 + the AI-interview angle.*

---

## Net change vs the current (v1) course
- AI / judgment goes **1 → 6 modules** (M1–M6) and leads the course.
- New **Module 2 (fundamentals / the moat)** and **Module 3 (learning without atrophy)** — the floor the whole thesis stands on.
- New **bridge Module 7**: the AI + GitHub coding loop (issue → PR → review, agents opening PRs), plus human collaboration and IP/data safety.
- GitHub portfolio mechanics compress to **3 modules** (proof, not spine — Act 2).
- Old M2 (Git fundamentals) → folded into M8 as table stakes.
- Old M5 (Open source) → optional track inside M9, not a standalone module.
- Course grew **7 → 10 modules** — deliberate, for genuine learning value over "micro" branding.

## Gaps now covered (was a review finding)
- Fundamentals (the moat the thesis rests on) → **M2**
- Skill atrophy / learning with AI → **M3**
- Learn in public → **M3.4**
- AI as a comprehension tool → **M4.5**
- Debugging with AI → **M6.3**
- IP / licensing / data-leak honesty → **M7.6**
- Working with humans on a team → **M7.5**

## Matches the locked brief [MANGALAHQ-TBD]
| Brief requirement | How this outline meets it |
|---|---|
| Topic: **GitHub + AI mindset** (not Copilot-specific) | GitHub + AI is the spine of the back half; M7.1 is framed by capability, Copilot named only as one example |
| **AI-assisted vibe coding** | M5 (vibe coding without debt) + M7 (the real AI-on-GitHub loop) are the practical core |
| Audience: junior dev, **non-developer, or student** | Every lesson pitched for non-devs; CS depth quarantined to optional "developer track" sections (M2.5 etc.) |
| Delivered in **3 phases** | Phase 1 = Act 1 (M1–6), Phase 2 = Bridge (M7), Phase 3 = Act 2 (M8–10) |
| **Token-aware: Haiku batch + script** | Production plan: draft lessons via Haiku/Sonnet batch + a script over the per-module outline; Opus reserved for editorial review of the drafts (not inline authoring) |
| Size / "micro" | Relaxed per Triết — count is not a constraint; fit + usefulness are |

## Open structural questions (decide before drafting)
- Merge M2 + M3 into one "Build & Keep Your Edge" module if 10 feels too long?
- Split Module 6 (it's now 6 lessons) into failure-modes vs verification?
- Keep Open Source as a full module instead of a folded optional track?

## Mapping: v1 files → v2 modules
- v1 M1 (Why GitHub) → v2 M8.2
- v1 M2 (Git fundamentals) → v2 M8.5 / M9 essentials
- v1 M3 (Building projects) → v2 M9.1
- v1 M4 (Profile & README) → v2 M8.4
- v1 M5 (Open source) → v2 M9.5 (optional)
- v1 M6 (AI mindset) → exploded into v2 M1–M7 (Act 1 + bridge)
- v1 M7 (Capstone) → v2 M10
