# Module 9 — Build Something Real with AI

**Objective:** Take everything from the course — judgment, verification, the GitHub loop, the evidence locker — and aim it at *one* thing: a single anchor project you scoped, built AI-native, deployed live, and can fully defend. This is the module where the whole course becomes a thing you can point at.

> **Who this is for.** Everyone who's ready to *build*, not just learn — students, career-changers, juniors, non-devs. You don't need to be able to write every line yourself. You need to be able to *own* every decision. We'll show you how to scope a build so that's actually true.

---

## Lesson 9.1 — Scoping for Ownership

Before you write a single prompt, you make the most important decision of the whole project: **what to build.** Get this right and everything downstream gets easier. Get it wrong and no amount of clean code will save it.

**Start with a problem, not a technique.** The single best framing comes from a guide on student projects: *"The strongest AI projects begin with a question, not a technique. 'I want to build an image classifier' is a technique. 'I want to help students with visual impairments navigate our school's website' is a problem"* *(figma.com)*. Problems give a project "a reason to exist beyond the grade" — and, crucially, "they also make your documentation, your presentation, and your demo exponentially easier to explain." A problem you actually care about is a project you'll actually be able to talk about in an interview. That's not a coincidence; it's the whole point.

**This is the line between a real project and a tutorial.** The difference, the same source notes, "is usually the data. Tutorials use clean, pre-processed datasets. Real projects use messy, incomplete, sometimes contradictory data" *(figma.com)*. A tutorial reconstruction proves you can follow steps. A real project — your problem, your messy data, your decisions — proves you can *think*. Module 8's red-flag list put "only tutorial projects" at the top for exactly this reason: rebuild something *original* *(authenticjobs.com)*.

**Scope it small enough to actually finish.** The most common beginner mistake: "they try to build their dream startup on day one. The first project should be small enough to complete" — and "a working simple app is worth more than an unfinished complex one" *(vibecodingacademy.ai)*. One real, finished, deployed thing beats three abandoned ambitious ones. And depth beats breadth: "the real learning comes from depth rather than breadth… build them thoroughly, iterating and improving until they work reliably" *(firecrawl.dev)*.

**Write down the scope before you build.** This is Module 4's agentic discipline applied to your own project: a good task definition is "a structured description of the work, including acceptance criteria, scope constraints, and relevant context… This is where most implementations are weakest" *(codegen.com)*. Five minutes writing *what does "done" look like, what's in, what's explicitly out* will save you hours — and it's the same artifact you'll hand the AI in 9.2.

> **The scoping test:** Can you say, in one sentence, *what problem this solves and for whom*? If you can't, you're not ready to build yet — you're ready to think a little more. That sentence becomes your README's first line and your interview opener.

---

## Lesson 9.2 — Building It AI-Native

Now build it — and build it the way the whole course has been preparing you for. This isn't "type every line yourself" (that's not 2026) and it isn't "accept whatever the AI emits" (that's the hangover, Module 5). It's the supervised loop.

**Feed it the context you wrote.** Remember the iron law from Module 4 and Module 7: with agents, *"quality here is a direct function of input quality"* *(codegen.com)*. Your scope from 9.1, a context file (`CLAUDE.md` / `AGENTS.md` / `.cursor/rules`), your README and design patterns as the AI's starting context *(docs.github.com)* — that's the input. Garbage in, garbage out has never been more literally true.

**Prompt for the result, then iterate.** Describe the end you want, not the steps: a *strong* prompt is "Build a web app where I can add daily habits, mark them complete each day, and see a 7-day streak counter," not "build me an app for tracking things" *(vibecodingacademy.ai)*. Then refine through conversation — "rarely will the first output be exactly what you want. That is normal and expected" *(vibecodingacademy.ai)*. This is Module 5's "describe the experience, not the implementation," now aimed at a real build.

**Work the loop, not the keyboard.** A practitioner's honest description of the modern workflow: *"Instead of writing code, and writing code, and writing code, I now delegate this task to the coding agent, while I can give more attention to more critical aspects… After the feature is complete I test the code from a functional standpoint, and I review the critical code paths in depth"* *(timdeschryver.dev)*. Note what he still does himself: **the architectural decisions and the deep review of critical paths.** He treated his UI components "as an external dependency… I only look at the public API, not the internals" — a deliberate judgment call about *where* to spend his attention, not a blanket "trust everything." That selective rigor is the skill.

**Verify as you go — this is Module 6, live.** Every feature the AI produces gets the verification pass: does it do what you intended, does it follow your conventions, and — non-negotiable — does it pass the security smell test (no hardcoded secrets, inputs validated, not just the happy path)? *(docs.github.com)*. AI "misses security vulnerabilities, performance issues, edge cases; your judgment is the final defense" *(frontendmentor.io)*. You are not done when it runs. You're done when you've *checked* it.

> **The through-line, in motion:** building AI-native means you moved up to the architect's chair — you scope, you direct, you verify, you decide where to look hard. The AI does the typing. *You* do the judging. That division of labor is the entire course, finally applied to something real.

---

## Lesson 9.3 — The Quality Bar

A project isn't an anchor project until it clears a real bar. Here's the checklist that separates "I made a thing" from "I shipped a thing someone could use." None of it requires you to write more code — it requires you to *finish*.

**It's deployed and live.** A live URL beats a localhost screenshot every time — Module 8's recruiters "absolutely click through" *(text2resume.com)*, and "nothing deployed" is a portfolio red flag *(authenticjobs.com)*. The good news: deployment is nearly free and nearly instant now. Many builder tools deploy with one click; standalone projects go up on free hosting "in under two minutes from a GitHub repository" *(vibecodingacademy.ai)*. *"Your first live project, something real that other people can visit, changes how you think about building. Do not skip this step"* *(vibecodingacademy.ai)*.

> **⚠️ Dated callout — deploy targets as of early 2026 (verify before relying on it).** Free hosting that deploys straight from a GitHub repo includes Vercel and Netlify; prompt-to-app builders like Lovable deploy to a live URL automatically, and Bolt connects to Netlify/Vercel *(vibecodingacademy.ai, getmocha.com)*. Specific tools and free-tier limits change constantly — check the vendor's current site. The durable point: **deploying is no longer the hard part. Not deploying is just a choice.**

**It has a README that shows judgment.** Straight from Module 8: not just "how to run it," but *what problem it solves*, *one decision you made and why*, and *what you changed from the AI's suggestion* *(authenticjobs.com)*. The README is where your invisible thinking becomes visible.

**Your secrets are not in the repo.** This is Module 7.6, and it's table stakes: API keys and passwords never get committed. The standard convention is to keep real secrets in an untracked `.env` file (and in your host's environment/secrets settings for the live deploy), while committing a `.env.example` that lists the *names* of the variables needed with placeholder values — so someone can run your project without ever seeing your keys. "Exposed API keys" is a named portfolio red flag *(authenticjobs.com)*; a clean `.env.example` is the quiet signal that you know better.

**It works for someone who isn't you.** The most underrated quality check: *"Your project isn't done until someone who didn't build it has tried to use it. Watch them. Don't explain. Take notes on where they get stuck"* *(figma.com)*. Twenty minutes of watching one real person surfaces more than a week of solo testing — and it's exactly the user-empathy that the red-flag list calls "product thinking."

**Tests, where they earn their place.** From Module 6.6: a meaningful test on the part that matters proves you "think about correctness," and it's a green flag reviewers notice. You don't need 100% coverage on a portfolio project. You need a test that shows you know *why* tests exist.

---

## Lesson 9.4 — The "Explain Your Own Code" Rule

This is the rule that governs everything else, and it's worth stating as bluntly as the sources do. Module 8 introduced the gatekeeper; here it becomes the law of the build:

> *"Portfolio projects should demonstrate your understanding, not AI's capabilities. If you can't explain it thoroughly in a technical interview, you shouldn't include it."* *(frontendmentor.io)*

And the sharpest version of the test: *"Can you rebuild the core functionality from scratch without AI? If not, you don't understand it well enough to claim it as your work"* — that rebuild ability is "your interview insurance" *(frontendmentor.io)*. The same source warns of the exact failure mode to avoid: *"Building projects you can't explain in interviews"* and *"Can't explain your code in pull requests"* are critical warning signs — and the fix is always the same: **manual rebuild required** *(frontendmentor.io)*.

Here's the liberating flip side, though. The standard isn't "you wrote every line." It's "you understand and can defend every decision." A backend-minded builder can hand-build the API and vibe-code the dashboard, *as long as they can explain both and rebuild the core.* The bright line the whole field keeps drawing: **"Your portfolio doesn't define your skill level. Your ability to explain and rebuild that portfolio does"** *(frontendmentor.io)*.

So build with this as your real-time filter: at every feature, ask *could I explain this to an interviewer, and rebuild the heart of it without the AI?* If yes — keep going, fast. If no — slow down and learn it now, while it's cheap, not in the interview, where it's fatal. This is Module 3's whole thesis ("learn, don't just generate") cashed at the moment it matters most.

---

## Lesson 9.5 — (Optional Track) Open Source When You're Ready

This lesson is optional and a stretch goal — your deployed anchor project (9.1–9.4) is the priority. But once you have one thing you're proud of and can defend, a single contribution to *someone else's* project is one of the highest-signal moves available to a junior, because it proves the one thing a solo repo can't: that you can work inside code you didn't write, on a team you didn't pick.

The career guides quietly agree. "Contribute to open-source projects" sits right alongside "build 3–5 real projects on GitHub" on the how-to-land-the-job lists *(tripleten.com)*, and contributing "can increase your visibility and showcase your passion" to hiring managers *(datacamp.com)*. It's collaboration evidence — the green-flag extra Module 8 pointed at.

**The beginner flow, lightly:**

1. **Find one small, well-scoped issue.** Look for repositories that tag beginner-friendly work (commonly labeled `good first issue` or `help wanted`). Pick something *bounded* — a doc fix, a small bug, a tiny feature — the same "clear acceptance criteria, bounded scope" rule from Module 4.
2. **Use AI to understand the codebase first.** This is Module 4.5's highest-value use: point the AI at the unfamiliar repo and ask it to explain the structure and walk you through the relevant files before you change anything. Getting oriented in someone else's code, fast, is exactly what AI is extraordinary at — and exactly what makes open source feel approachable.
3. **Work the loop you already know (Module 7).** Fork it, make a focused change on a branch, verify it (their tests, their conventions), and open a pull request that explains *what* and *why* — and honestly labels any AI assistance.
4. **Respect that it's their house.** Read their contributing guide, match their style, and accept that maintainers may ask for changes. Handling review feedback gracefully is itself the collaboration skill on display.

You don't have to do this to finish the course. But the junior who has *one* merged contribution to a real project has an interview story most applicants simply don't.

---

## Action — Ship One Flagship

This is the capstone build. Don't aim for impressive — aim for *finished, deployed, and defensible.* Over a few focused sessions:

1. **Scope it (9.1).** Write the one sentence: *what problem, for whom.* Pick something small, real, and yours — not a tutorial reconstruction. Note explicitly what's in and what's out.
2. **Build it AI-native (9.2).** Feed the AI your scope and context. Prompt for the result, iterate, and *verify every feature* (Module 6) — especially the security smell test. Make the architectural calls yourself.
3. **Clear the quality bar (9.3).** Deploy it to a live URL. Write the judgment-showing README. Add a `.env.example` and confirm no secrets are committed. Have one person who isn't you try it, and watch where they get stuck.
4. **Pass the explain test (9.4).** Walk through it out loud as if to an interviewer. Anything you can't explain or rebuild, learn it now — or cut it.
5. **(Optional) One open-source PR (9.5)** if you've got momentum.

When you're done you'll have the single most valuable thing a junior can own in 2026: **a live, original project you fully understand, built the way the industry now builds, with a GitHub trail that proves you did the judging.**

> **The through-line, made real:** "AI writes the code now; your job is to out-judge it — and GitHub is where you prove you can." This module is where you *did* it — one project, scoped by you, built with AI under your supervision, verified by your judgment, deployed for the world, and defensible in any room. Module 10 takes this flagship and walks it into the interview.

---

## Sources Cited

- **figma.com** — "AI Project Ideas for College Students" — start with a problem, not a technique; the problem makes documentation and demos far easier to explain; the tutorial-vs-real-project line is the data (messy, real); document decisions as you go; "your project isn't done until someone who didn't build it has tried to use it" — watch them, don't explain.
- **vibecodingacademy.ai** — "Vibe Coding for Beginners (2026)" — pick a manageable first project (don't build your dream startup on day one); a working simple app beats an unfinished complex one; specific prompts beat vague ones; iterate through conversation; deploy your first project (one-click / Vercel / Netlify, under two minutes from a GitHub repo) — "do not skip this step."
- **frontendmentor.io** — "AI Coding Assistants for Beginners" — portfolio projects must demonstrate *your* understanding; the rebuild-from-scratch test is your interview insurance; "can't explain your code in pull requests" → manual rebuild required; AI misses security/perf/edge cases — your judgment is the final defense; "your portfolio doesn't define your skill level, your ability to explain and rebuild it does."
- **codegen.com** — "How to Build Agentic Coding Workflows" — a strong task input (acceptance criteria, scope constraints, context) is where most implementations are weakest; "quality is a direct function of input quality."
- **firecrawl.dev** — "11 AI Agent Projects You Can Build Today" — depth over breadth; build a couple of projects thoroughly until they work reliably; the goal is applications others can actually use.
- **timdeschryver.dev** — "Keep Agentic AI Simple" — the modern workflow: delegate the typing to the agent, spend attention on critical aspects; test functionally and review critical code paths in depth; selective rigor (treat stable components as an external dependency) then commit and open a PR.
- **docs.github.com** — "Review AI-generated code" — verify context and intent ("does this solve the right problem? does it follow our conventions?"); use your README/docs/PRs as context for the AI.
- **authenticjobs.com** — "How to Become a Vibe Coder (2026)" — build original projects, not just tutorials; "nothing deployed" and "exposed API keys" are portfolio red flags; READMEs should document why/what-changed; disclose and own AI use.
- **text2resume.com** — "Vibe Coding Your Way to Your First Dev Job" — recruiters click project links; a deployed working project beats localhost.
- **getmocha.com** — "Best AI App Builder 2026" — prompt-to-app builders and where they deploy (Supabase/Netlify/Vercel); shipping a real, deployed product vs. an undeployable mockup.
- **tripleten.com** — "Best Entry-Level Tech Jobs Safe from AI" — "build 3–5 real projects on GitHub" and "contribute to open-source projects" on the how-to-land-the-job list.
- **datacamp.com** — "How to Learn AI From Scratch (2026)" — contributing to open-source projects increases visibility with hiring managers; share your work or your skills stay locked in the box.
