# Module 4 — The Individual README That Closes the Loop

A recruiter opens your repo. They have 30 seconds. What they see in those first few scrolls determines whether they tab back to the candidate list or forward your profile to the hiring manager. Your project README is that moment — and most developers waste it.

This module covers the five sections every project README needs, the single highest-leverage element you can add in the next hour, and the one section that separates a senior signal from a junior one.

---

## Lesson 4.1 — The Five Required Sections, In Order

A README without a clear structure forces the reader to hunt. Hunting creates friction. Friction ends consideration. The fix is a predictable order that answers the reader's questions before they ask them.

**The sequence:**

1. **Title + one-line description.** The project name and a single sentence stating what it does and who it is for. "A CLI tool that syncs Notion databases to local Markdown files for offline reading." No marketing language, no adjectives. One claim, falsifiable by the code below it.

2. **Live demo / screenshots.** A link to the deployed app, or screenshots, or a GIF. This comes second — not buried at the bottom.

3. **Tech stack.** A short list: framework, language, database, major libraries. Be specific. "React 19 with TypeScript, Express.js, PostgreSQL 15" communicates more than "React, Node, Database"[^1]. Recruiters and hiring engineers scan this list to confirm you use tools relevant to the role they are filling.

4. **Run locally.** Step-by-step commands to clone and start the project. Assume the reader has never seen your repo before. List every required environment variable, even if the value is obvious. "A reviewer who can run your project quickly is far more likely to remember you."[^2] If something takes more than five minutes to set up, document why.

5. **Design decisions.** Why you made the non-obvious architectural choices.

This order matches how a reader's attention moves: first orientation, then proof, then context, then signal, then depth. Flipping it — putting installation before the description — forces the reader to work for information they need at the top.

"The README is where most developers fail. They either write nothing or write a wall of text that nobody will read."[^3]

Keep paragraphs short. Use bullets for lists. Use code blocks for every shell command and environment variable.

**Action:** Open one of your pinned repos right now. Check whether these five sections exist in this order. If any are missing or out of sequence, reorder and fill the gap before moving to the next lesson.

---

## Lesson 4.2 — The Screenshot Rule: First 100 Lines, Every Time

There is one change that produces more return than any other single README edit: put a screenshot or demo GIF above the fold, within the first 100 lines of the file.

"Include screenshots, GIFs, or videos that demonstrate your project in action. This helps potential users visualize what they can achieve using your code."[^4]

Placement matters because GitHub renders the README in a fixed viewport. A reader who sees a screenshot in the first scroll does not need to imagine what the project looks like. A reader who scrolls past 80 lines of installation steps before seeing anything visual has already disengaged.

The demo asset tier, from lowest to highest impact:

- **Screenshot** — good. Shows the real UI, proves deployment.
- **GIF** — better. Shows interaction flow, not just a static state.
- **Working live demo link** — best. "Screenshots are fine. Videos are better. Working demos are best."[^5]

Deploy to Vercel, Netlify, or Render — all free for personal projects. A broken or missing demo link is worse than no link at all, so if you cannot maintain a live deployment, fall back to a high-quality GIF. Either way, it belongs near the top.

For layout, avoid stacking screenshots in a single column — it makes the README feel like a photo dump. A 2×2 Markdown table of demo images reads better and keeps the file scannable.[^6]

"Show don't tell: screenshots prove your design skills. GIFs prove your interactions work."[^7]

**Action:** Pick your strongest project. If the README does not have a screenshot or GIF in the first 100 lines, capture one today and add it. Commit the change, then visit the repo as a logged-out user to see exactly what a recruiter sees.

---

## Lesson 4.3 — Design Decisions: The Section That Signals Seniority

Everything covered so far — title, demo, stack, run instructions — is table stakes. A junior and a senior can both write those four sections. The fifth section, design decisions, is where the gap becomes visible.

A design decisions section answers one question: why did you make the non-obvious choices you made?

"Your architecture decisions: why did you choose PostgreSQL over MongoDB? Why serverless functions instead of a traditional server? Why JWT authentication instead of sessions? These decisions show how you think."[^7]

This is the difference between listing tools and demonstrating judgment. Anyone can write "I used PostgreSQL." Fewer write "I chose PostgreSQL over MongoDB because the relationships between users, projects, and tasks were well-defined and benefited from foreign key constraints and ACID transactions." The second version makes your reasoning legible — it shows you evaluated the alternative, understood the trade-off, and made a deliberate choice.

Two or three decisions is enough. Choose ones that were genuinely non-obvious: a caching layer added after profiling a slow query, a webhook approach chosen over polling, a monorepo adopted for a specific reason. Skip decisions that had only one sensible answer.

Also include what you would do differently. "What you'd do differently: demonstrates learning about type safety across the stack and code organization."[^7] Admitting what you got wrong feels risky — but it reads as intellectual honesty, not weakness.

"Include a README with setup instructions, design decisions, and trade-offs."[^3]

A README with a genuine design decisions section does two things simultaneously: it proves you can build, and it proves you can think. That combination is what moves a profile from the "maybe" pile to the interview queue.

**Action:** For your primary portfolio project, write a design decisions section with two or three entries. For each: state the decision, name the alternative you considered, and explain why you chose what you chose in two to three sentences. Add a single "what I would do differently" note at the end.

---

## Module Summary

A project README is not documentation for users — it is a first interview for reviewers. The five sections (title + one-line, live demo, tech stack, run locally, design decisions) give a reader everything they need to orient, evaluate, and remember your work without touching the code. Placing a screenshot or demo GIF in the first 100 lines removes the single largest reason readers disengage early. And a design decisions section converts a list of tools into evidence of judgment — the quality that distinguishes a senior candidate from a junior one on paper. Together, these three practices turn a 30-second scan into a real impression.

## Sources

[^1]: frontendmentor.io
[^2]: codelabsacademy.com
[^3]: dev.to
[^4]: www.codingtemple.com
[^5]: byagentai.com
[^6]: bstefanski.com
[^7]: www.frontendmentor.io
