# Course: Claude Code & AI-Assisted Coding Workflow

**Audience:** developers adopting AI coding assistants (Claude Code, Copilot, Cursor) as a daily tool
**Format:** 5 modules, ~3 lessons each, micro-course style
**Through-line:** *AI assistants change which work is leverage and which is busywork. The developers who get ahead in 2026 are the ones who know what to delegate, what to write themselves, and how to catch the assistant's mistakes before they ship.*

> Status: outline draft. Primary topic `claude-code-workflow` (40 articles, 0.87 signal) in `source_corpus=shipwithai-data`. Agents must run `kb_search` (rerank=false) and quote supporting `parent_text` before citing.

---

## Module 1 — Why AI-Assisted Coding Changes the Job
**Objective:** Separate the hype from the structural shift so you can decide what to actually change in your workflow.

- The real productivity gain is not "writing code faster" — it's "spending less time on boilerplate so you can spend more on design and review."
- What AI does well: scaffolding, refactoring across many files, writing tests for existing code, summarizing unfamiliar codebases.
- What it does poorly: novel architectural decisions, debugging non-obvious failure modes, anything requiring deep context about your specific system.
- Hiring signal shift: "uses AI assistants" is no longer a differentiator. "Uses them with judgment" is.

**Action:** Audit your last week of coding. List five tasks that an AI assistant could have handled and five it could not. The gap is your starting point.

## Module 2 — Setup and Sane Defaults
**Objective:** Configure Claude Code (or your assistant of choice) so it earns its keep instead of getting in your way.

- Install and authenticate the CLI / IDE extension. Confirm it can read your project files and run terminal commands in the project directory.
- Set up project-level instructions: a `CLAUDE.md` (or equivalent) that names your stack, your conventions, and the things the assistant should never do.
- Decide on permission mode: prompt-on-every-tool is safest, but auto-approve for read-only operations saves real time after you trust the setup.
- Connect the tools that matter: language server (for accurate jump-to-def), git, your test runner. Skip MCP servers you won't actually use.

**Action:** Create a `CLAUDE.md` (or your assistant's equivalent) in one of your active repos. List your stack, naming conventions, and at least three "don't do this" rules.

## Module 3 — The Daily Loop: When to Delegate, When to Write Yourself
**Objective:** Build the instinct for which tasks belong with the assistant.

- Delegate freely: boilerplate, test scaffolding, type definitions, formatting, multi-file rename or refactor, summarizing unfamiliar files.
- Hold the pen yourself: anything that affects production data, anything where the failure mode is silent corruption, anything you'd be embarrassed to ship without understanding.
- Prompt structure that works: give context, name the constraint, show one example of acceptable output, ask for the diff before you accept it.
- When the assistant produces a 200-line change, your job is review, not "looks good, ship it." Trust speeds up over time; never trust faster than you can verify.

**Action:** Pick one boilerplate task you'd normally do by hand (e.g., add error handling to five functions in a file). Delegate it with a precise prompt and a constraint. Review the diff line by line before accepting.

## Module 4 — Code Review with AI: Self-Review and PR Review
**Objective:** Use the assistant to make your code review faster and your own PRs cleaner.

- Self-review before you push: ask the assistant to read your diff, flag obvious bugs, suggest edge cases. Catch what reviewers would catch.
- For incoming PRs: have the assistant summarize what the PR does, list risks, identify untested branches. Speeds up the boring parts so you focus on judgment calls.
- What AI review misses: domain-specific invariants, performance regressions that depend on prod data shape, security concerns rooted in business logic.
- Treat AI review as a first pass, never a final pass. The human still owns approval.

**Action:** Before your next PR, paste the diff into Claude Code and ask: "What would a senior reviewer flag here?" Address whatever it finds before pushing.

## Module 5 — Putting Claude Code on Your Resume
**Objective:** Communicate AI-assisted skill to hiring managers without sounding like marketing copy.

- "Familiar with AI coding assistants" reads as generic. "Refactored a 4,000-line Python service to async using Claude Code, reduced p95 latency 35%" reads as a hire signal.
- The strong line is always: tool + concrete task + measurable outcome. The assistant is the multiplier, not the headline.
- In the interview: be ready to describe a task where you delegated to the assistant, what went wrong, and what you did to catch it. Hiring managers care about your judgment, not the assistant's output.
- LinkedIn signal: pin a project that visibly used AI assistance in its commit history or README. Don't hide it; don't oversell it.

**Action:** Rewrite one bullet on your resume to follow the formula `tool + task + measurable outcome`, naming the AI assistant explicitly. Verify the number is real before publishing.

---

## Source map
Primary corpus topic: `claude-code-workflow` (40 articles, 0.87 signal). Supporting topics: `tech-resume` and `linkedin-profile` (for Module 5).
