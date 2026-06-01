# Module 7 — Coding with AI on GitHub: The Real Loop

**Objective:** Connect the two halves of this course. You've learned to judge AI's output (Act 1); now learn the actual loop teams use to *build* with AI on GitHub — where the AI writes, you review, and the platform records who decided what. This is the bridge from "I can judge code" to "I can work the way real teams work."

> **Who this is for.** Everyone — including if you've never touched GitHub. Lesson 7.1 gives you the one-minute orientation; nothing here assumes prior experience. The optional "developer track" notes go deeper for those who want them.

---

## Lesson 7.1 — GitHub in One Minute (and Why It's Built for This)

If GitHub is new to you, here's the whole thing in five words: **it's where code lives and changes get reviewed.** The handful of pieces you need:

- **Repository ("repo")** — the project folder, with its full history. Every version ever saved is recoverable. (This is the "save working states" habit from Module 5, automated.)
- **Commit** — one saved change, with a short message explaining *what and why*.
- **Branch** — a safe copy where you (or an AI) can make changes without touching the working version, until they're ready.
- **Issue** — a written description of a task or bug. "Add a login button." "Fix the crash on empty input."
- **Pull request ("PR")** — the proposal: *"here are my changes, here's why, please review before we merge them in."* This is where review happens, comments get left, and the decision is recorded.

Here's why this matters for *this* course: GitHub was built around the idea that **changes get proposed, explained, and reviewed before they count.** That's the exact shape of good AI work — the AI proposes, a human reviews, the reasoning gets written down. The platform that already structured human collaboration around "propose → review → merge" turns out to be the perfect place to supervise a machine. Everything below is that loop.

---

## Lesson 7.2 — The Loop: Issue → Branch → PR → Review

Strip away the tools and the modern AI build loop is five steps. One guide lays out the well-functioning version as a chain *(codegen.com)*:

1. **Task input** — a clear description of the work: what, the acceptance criteria, the scope, the context. (This is an *issue*, written well.)
2. **Context assembly** — the AI pulls what it needs: the codebase, docs, the linked task.
3. **Sandbox execution** — the AI works "in an isolated environment… producing commits and a pull request **without touching the main branch.**" (That's the *branch*, keeping the working version safe.)
4. **PR output** — "the agent opens a pull request with its changes."
5. **Review** — "an AI code review pass runs first… Human review follows for final judgment on architectural decisions and business logic." (That's *you*.)

Now the single most important sentence in this module, because it's where juniors win or lose: **"Quality here is a direct function of input quality"** *(codegen.com)*. The same guide is blunt — most teams set up steps 3 and 5 fine, but "steps one and two are where the work is." Teams with vague inputs are "running an expensive way to generate pull requests they have to rewrite."

This isn't opinion. "A GitHub research study on Copilot adoption found that developers who reported the most productivity gains… shared a common behavior: they spent more time structuring requests before submitting them" *(codegen.com)*. So the highest-leverage skill in the whole loop isn't prompting fast — it's **writing a clear task** (a good issue) before anything runs. That's Module 1's communication pillar, made concrete: the people who win at AI write the spec well.

---

## Lesson 7.3 — Letting an Agent Open a PR

Here's the part that feels like science fiction until you do it once. The GitHub-native coding agent can take a task and run the whole middle of the loop for you. Described capability-first (this is a category — GitHub's Copilot is one example, and tools like Devin and others do the same shape) *(nxcode.io, qodo.ai)*:

> You **assign a GitHub issue to the agent**, "which creates a branch, writes the code, runs tests, and opens a pull request" *(nxcode.io)*.

You go from a written task to a reviewable proposal without typing the code yourself. A working developer describes the real rhythm of it: plan the work first, "ask the coding agent to implement the steps," then "test the code from a functional standpoint, and review the critical code paths in depth" before using the git/GitHub tools to "commit the changes and open a pull request" *(timdeschryver.dev)*. While the agent works, he's reviewing other code or "getting a coffee."

Two things keep this honest, both straight from Act 1:

- **It only suits the right tasks.** This works "for well-defined, scoped tasks" and "struggles with complex, multi-step problems" *(nxcode.io)*. Best fits: "bug fixes with reproducible test cases, refactors with a defined target pattern, migrations with a clear before/after." Keep for yourself: "tasks with evolving requirements or architectural decisions" *(codegen.com)*. (This is Module 4.4, now literal.)
- **The PR is a proposal, not a merge.** Every serious tool in this space "shows diffs before applying changes" and hands "code changes back for review" — "the changes were not merged automatically" *(qodo.ai)*. The agent's PR lands in exactly the spot built for your judgment. You are step 5, and step 5 is not optional.

> *Developer-track note:* you don't need the fancy managed agent to live this loop. Terminal tools (Claude Code, Aider) and IDE agents (Cursor) all "work with Git workflows," show diffs, and can commit and open PRs *(qodo.ai)*. The loop is the same at every rung from Module 4.

---

## Lesson 7.4 — AI Code Review, Both Directions

Review is where this gets genuinely powerful, because in 2026 it runs *both ways*: the AI reviews your code, and you review the AI's.

**The AI reviewing PRs.** GitHub-native review can "review pull requests directly… providing line-by-line feedback and suggestions" *(nxcode.io)*, and teams increasingly run "an AI code review pass first, catching issues at scale," with "human review [for] final judgment" after *(codegen.com)*. You can even build your own — there are full courses on making "a custom GitHub Action that uses AI to automatically review pull requests" *(coursera.org)*. Treat the AI's review the way you'd treat a fast, tireless first-pass reviewer: great at catching the obvious, no judgment about what actually matters.

**You reviewing the AI's PR.** This is where Module 6's checklist comes home — except now it has a *place to live*: the PR. As you review, leave comments, ask the AI to justify itself, and only approve what you understand. The best question to carry into every AI PR, framed as "vibe testing": **"Does this do what I *intended*, not just what I literally instructed?"** *(wearecommunity.io)*.

The reason both directions matter is the one from the whole course: AI review catches *patterns*; human review catches *meaning*. The corpus has a perfect cautionary tale — an AI "optimized" a database query and passed every test, but it quietly broke a monthly financial report three weeks later because it didn't know about an invisible business rule *(wearecommunity.io)*. No automated reviewer catches that. The human who understands the business does. **That gap is your job, and the PR is where you do it.**

---

## Lesson 7.5 — Working With Humans (Not Just Machines)

Even when AI writes the code, software is still a team sport — and GitHub is the team's shared room. A few habits make you the kind of collaborator people trust:

- **Label AI-assisted work.** Mature teams "use tags like `[AI-Generated]` in pull requests to signal to reviewers that the code requires extra scrutiny" *(wearecommunity.io)*. Counterintuitively, *flagging* that AI wrote it earns more trust than hiding it — it shows you know it needs checking (straight from Module 1).
- **Write the PR so a human can judge it fast.** Explain *why*, what you changed from the AI's suggestion, and what you verified. This is the exact "audit trail of judgment" from Module 1.4 — and the raw material for your portfolio in Module 8.
- **Pair on the tricky stuff.** "Reviewing AI output with a teammate is an effective way to spot problems and share insights on the AI's common failure modes" *(wearecommunity.io)*. Asking a senior to look at a sketchy diff isn't weakness; it's how you learn what to look for.
- **Bring a teammate in for the high-stakes paths.** "Ask teammates to review complex or sensitive changes" and "use checklists to ensure all key review points (functionality, security, maintainability) are covered" *(docs.github.com)*.

The throughline: the PR is a conversation, not a delivery chute. The junior who treats review comments as a gift — and can explain every line when asked — is the one who becomes the senior.

---

## Lesson 7.6 — Hygiene, Secrets & IP (Don't Skip This)

This is the short list of ways AI-on-GitHub goes badly wrong, and how not to be a cautionary tale. All of it is grounded in real failures.

**Never commit secrets.** AI "often writes authentication code that includes API keys, passwords, or other credentials directly in the codebase. These secrets should be stored in external configuration files, **not committed to the repository**" *(wearecommunity.io)*. The corpus is full of real cases: "vibe-coded applications with exposed API keys on the frontend, hardcoded credentials" *(ksred.com)*; an AI tool that "literally [left] my access key exposed" in a search cache *(wearecommunity.io)*. The rules, for everyone:

- Secrets go in a separate config/environment file that is **never** committed (kept out via a `.gitignore` list). On GitHub specifically, real credentials live in repository **Secrets** (Settings → Secrets and variables), not in the code *(codelabs.developers.google.com)*.
- A secret pushed to a public repo is **compromised the moment it lands** — bots scan for them in seconds. Rotate it (make a new one), don't just delete the file.
- Add "any secrets hardcoded?" to your verification pass (Module 6.4) *before* you ever commit.

**Watch for the silent-but-dangerous stuff** AI loves to generate: SQL injection (user input pasted straight into a query), and "flawed authentication logic… that appears convincing and works in many cases but contains hidden bypasses" — the kind "automated scanning tools miss" *(wearecommunity.io)*. When auth or payments or user data are involved, that's the "get a security review" line from Module 5.

**Know the IP and data risks.** Two real ones *(wearecommunity.io)*:

- **Copyright/licensing.** Models "trained on open-source code may inadvertently replicate copyrighted functions or breach licensing requirements." Be especially careful pasting AI code into anything you'll publish or sell.
- **What you paste into the AI.** Don't paste secrets, customer data, or proprietary/employer code into a public AI tool — once it's sent, you've lost control of it. (Many tools offer business tiers with data protections and even "IP indemnity" *(nxcode.io)* for exactly this reason — know which tier you're on before pasting anything sensitive.)

None of this requires expertise — it requires a habit: **before you commit or paste, ask "could this leak a secret, someone's data, or someone's copyright?"** That one question prevents most of the disasters in this corpus.

---

## Action — Run the Loop Once, End to End

Pick something tiny and real (a small feature or fix in any project, even a throwaway). Then run the whole loop deliberately:

1. **Write the issue, not just a prompt.** One paragraph: what you want, how you'll know it's done (acceptance criteria), any constraint. Remember — input quality *is* output quality (7.2).
2. **Let AI do the middle.** Have your tool (any rung — agent, IDE, or terminal) work it on a branch and produce a change/PR. Don't hand-write the code.
3. **Review it like step 5.** Run your Module 6 checklist on the diff. Leave at least one comment or question. Ask the AI: *"Does this do what I intended, not just what I said?"*
4. **Run the hygiene check (7.6).** Any secrets? Any blindly-trusted input? Anything you'd be uncomfortable making public?
5. **Write the merge note.** Two sentences: what this does, and what *you* checked or changed. That sentence is the seed of your evidence locker — Module 8.

> **The bridge, crossed:** Act 1 made you someone who can judge AI's output. This module put that judgment inside the loop real teams run — propose, review, record. Act 2 is about making the trail you just created *work for you*: turning every reviewed PR and explained decision into the proof that gets you hired.

---

## Sources Cited

- **codegen.com** — "How to Build Agentic Coding Workflows That Actually Ship" — the five-component loop (task input → context assembly → sandbox execution → PR output → review); "quality is a direct function of input quality"; "steps one and two are where the work is"; the GitHub research finding that top performers spend more time structuring requests; AI review pass first, human review for architecture/business logic; what tasks suit an agent.
- **nxcode.io** — "Cursor vs Claude Code vs GitHub Copilot (2026)" — the GitHub-native coding agent (assign an issue → creates a branch, writes code, runs tests, opens a PR); native line-by-line PR review; best for scoped tasks, struggles with complex multi-step; Copilot as "connective tissue" for team workflows; Enterprise tier IP indemnity.
- **timdeschryver.dev** — "Keep Agentic AI Simple" — a real solo workflow: plan first, let the agent implement, functionally test and review critical code paths, then commit and open a PR via git/GitHub tooling.
- **qodo.ai** — "15 Best AI Coding Assistant Tools (2026)" — tools layer rather than compete; terminal/IDE agents (Claude Code, Aider) work with Git, show diffs before applying; managed agents (Devin) operate before PR review and hand changes back for review, not auto-merged.
- **wearecommunity.io** — "Don't Trust AI-Generated Code" — label AI code `[AI-Generated]` in PRs; secrets belong in external config, not the repo; SQL injection and convincing-but-flawed auth logic that scanners miss; copyright/licensing (IP) risk from training data; pair programming; "vibe testing" — does it do what I *intended*; the optimized-query regression that broke a financial report.
- **ksred.com** — "The Vibe Coding Paradox" — real vibe-coded apps shipped with exposed API keys on the frontend and hardcoded credentials because builders lacked the understanding to spot them.
- **coursera.org** — "AI Code Review Automation with GitHub Actions" — you can build a custom GitHub Action that uses AI to automatically review pull requests.
- **codelabs.developers.google.com** — "GenAI for Dev: GitHub Code Review" — storing real credentials as GitHub repository Secrets (Settings → Secrets and variables → Actions) instead of in code.
