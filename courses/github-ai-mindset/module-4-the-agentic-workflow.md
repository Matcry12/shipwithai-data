# Module 4 — The Agentic Workflow: Your New Toolset

**Objective:** Understand how AI coding tools actually work now — as a few durable *categories*, not a list of brand names — so you can pick a stack, feed it well, and use it for the thing juniors under-use it for: understanding.

> **Who this is for.** Everyone. We name specific tools only as *examples* of categories; the categories are what last. Prices and "which tool is best this month" change constantly — so we quarantine the volatile stuff in a clearly-dated box and spend the lesson on what won't rot.

---

## Lesson 4.1 — The Spectrum: From Autocomplete to Agents

AI coding didn't arrive all at once — it climbed a ladder, and knowing which rung you're on tells you what to expect. One clear telling of the evolution *(ai-tinkerers.cards)*:

- **Before ~2022 — plain autocomplete.** Your editor guessed the next word from syntax rules. No understanding.
- **2022–2023 — AI assistants.** Tools like GitHub Copilot could read context and suggest whole functions, and you could *chat* with them in plain English. The breakthrough was understanding intent, not just syntax.
- **Now — AI agents.** Systems that "handle entire workflows autonomously — design their own execution plans, access tools, and allow human review at key decision points" *(ai-tinkerers.cards)*.

So the durable mental model is **four rungs of autonomy**, and you'll move between them all day:

1. **Inline autocomplete** — finishes your line. Fast, low-stakes, you're fully in control.
2. **Chat assistant** — you ask, it explains or drafts; you copy what you choose. (This is where Module 2's "Ask-Don't-Copy" lives.)
3. **Agentic editor / CLI** — you give it a task and it edits *multiple files*, runs commands, and iterates while you watch and approve.
4. **Managed / cloud agent** — you hand off a *whole task* and it goes away and comes back with a finished result (often a pull request) for you to review.

The key line that separates the top two rungs from the bottom two comes from a guide on agentic workflows: assistants like Copilot and Cursor "operate at the **editor level**, providing suggestions as a developer writes," while agents "operate at the **task level**: you assign a complete piece of work, the agent executes it in a sandboxed environment, and the output is a pull request. The developer isn't in the loop during execution" *(codegen.com)*. As one 2026 comparison put it, the tools "have moved well beyond autocomplete" *(sitepoint.com)*. The higher the rung, the more *judgment* you need on the way out — because you reviewed less on the way in. (That's Module 6.)

---

## Lesson 4.2 — Picking Your Stack (By Category, Not Brand)

Don't ask "what's the best AI tool?" Ask **"best for what, and for whom?"** The honest answer is always *it depends on your workflow* — one guide answers the "best AI for coding" question exactly that way: terminal/complex work, visual editing, or easy inline completions each point to a different tool *(vibewerks.com)*. And note the most experienced users "combine tools rather than choosing one" *(sitepoint.com)*.

Here's the durable map by **what you're trying to do and how technical you are** *(vibecodingacademy.ai, sitepoint.com)*:

| If you are… | You want this category | Examples (early 2026) |
|---|---|---|
| A non-coder building a full app from a description | **Prompt-to-app builder** (handles frontend, database, hosting for you) | Lovable, Bolt, v0, Replit Agent |
| Someone who wants to learn alongside the AI | **Browser IDE + agent** (edit files next to the AI) | Replit Agent |
| Comfortable in a code editor, want deep control | **AI-native IDE** (visual diffs, accept/reject each change) | Cursor |
| Comfortable in a terminal, want max autonomy | **Terminal/CLI agent** (reads whole codebase, runs commands) | Claude Code |
| Want AI inside the editor you already use | **Editor extension** (works across many IDEs) | GitHub Copilot |

A non-developer is best served *low* on the technicality scale (a prompt-to-app builder that "handles the full stack automatically… you describe the product, and it builds the infrastructure") *(vibecodingacademy.ai)*; someone heading into a developer role grows *up* the ladder toward the IDE and CLI agents.

> **⚠️ Dated callout — pricing as of early 2026 (verify before you rely on it).** Editor extensions start cheapest (around $10/mo for the common Pro tier), AI-native IDEs sit around $20/mo, and terminal agents range from ~$20/mo up to $100–200/mo for heavy use. All have free tiers that are *plenty* to start learning. **These numbers move constantly — check the vendor's site.** *(nxcode.io)*

The takeaway that *won't* go stale: start with one tool that matches your level and a free tier, get fluent, and add a second only when you feel a real limit.

---

## Lesson 4.3 — Context Is Everything

Here's the lever that most beginners miss, and it's the single biggest difference between mediocre and great AI output: **the AI is only as good as the context you give it.** It knows everything public and *nothing* about your specific project — your conventions, your structure, how you want things done.

Every serious AI tool now solves this the same way: **a context file.** It goes by different names — `CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, Copilot's `instructions.md` — but as one practitioner notes, "the idea remains the same across the tools" *(timdeschryver.dev)*. Think of it as **a README written for the AI**: a short document, kept in your project, that the tool reads every time so you don't have to re-explain yourself.

A good context file should *(packmind.com)*:

- **Describe the project** — what it is, the core technologies, the structure.
- **State your conventions** — guidelines, style, "we do it this way here."
- **Include the feedback commands** — how to run the tests, the build, the linter (so the AI can check its own work).
- **Contain nothing outdated or contradictory** — stale context is worse than none.

Two practical tips from people who do this daily: you can **ask the AI to write the context file for you**, and you should **review it regularly** — even add the AI's *recurring mistakes* to it so it stops repeating them *(timdeschryver.dev)*. The catch worth remembering: "writing context files is easy; keeping them accurate isn't" *(packmind.com)*. A living context file is one of the highest-return habits in this whole course.

---

## Lesson 4.4 — The Managed-Agent Shift

The newest rung — the **managed or cloud agent** — is the one most worth understanding in 2026, because it changes your job from *typing* to *delegating and reviewing*.

The pattern: instead of sitting beside the AI, you **hand it a whole task**, it works "in a sandboxed environment," and "the output is a pull request" you review — "with human review at defined checkpoints rather than throughout execution" *(codegen.com)*. This is Module 1's "supervise the machine" made literal: you become the person who scopes the work and judges the result, not the one in the weeds.

But — and this is the skill — **not every task suits an agent.** The honest guidance *(codegen.com)*:

- **Good for agents:** work with "clear acceptance criteria, bounded scope, and success conditions that can be verified" — bug fixes with a reproducible test, well-defined refactors, migrations with a clear before/after.
- **Keep for yourself:** "tasks with evolving requirements or architectural decisions that depend on broader organizational context."

Knowing which is which *is* the judgment employers now pay for. A junior who can take an ambiguous goal, **break off the well-scoped pieces an agent can do**, hand them off, and then critically review what comes back — that's the 2026 workflow. We put this exact loop into practice on GitHub in Module 7.

---

## Lesson 4.5 — The Highest-Value Use Juniors Skip: Understanding

Most beginners point AI at one thing: *generate code for me.* They miss the use that's arguably worth more — **using AI to understand.**

Modern agents can "read your entire codebase" and reason across it *(nxcode.io)*; an agentic workflow's first step is literally to "pull relevant context" before doing anything *(codegen.com)*. You can turn that on yourself. Dropped into an unfamiliar project (a new job, an open-source repo, a teammate's code)?

- *"Explain what this project does and how it's structured, like I'm new here."*
- *"Walk me through what happens when a user logs in, file by file."*
- *"What would I need to change to add X, and why there?"*

This is the Module 2 tutor (point AI at *understanding*, not output) and the Module 3 learning habit (it builds your moat instead of eroding it), aimed at the thing juniors find scariest: **someone else's code.** Being able to get oriented in an unfamiliar codebase *fast* is one of the most valuable and least-taught junior skills — and it's exactly what AI is extraordinary at helping with. Use it there first.

---

## Action — One Tool, One Context File, One Real Task

Hands-on, about an hour:

1. **Pick one tool that matches your level** (Lesson 4.2) and its free tier. Non-coder → a prompt-to-app builder. Learning to code → a browser IDE or AI-native editor. Heading toward dev work → an editor extension or terminal agent.
2. **Write a tiny context file** for a real project (even a one-paragraph "here's what this is, here's the stack, here's how to run the tests"). Or ask the AI to draft it, then correct it *(timdeschryver.dev)*.
3. **Run one end-to-end task** — small and well-scoped (Lesson 4.4): add a feature, fix a bug, or just ask it to *explain* an existing project to you (Lesson 4.5).
4. **Write down where it helped and where it failed.** What did it get right? Where did it confidently go wrong? That note is the start of your real-world intuition — and the raw material for Module 6, where we learn to catch the failures.

> **The through-line:** tools and prices churn; the workflow doesn't. You feed the AI context, you choose the right rung of autonomy for the task, and you stay the one who decides what's worth handing off and what's worth understanding yourself.

---

## Sources Cited

- **ai-tinkerers.cards** — "Can AI Really Build Your Next App?" — the evolution of AI coding: pre-2022 rule-based autocomplete → 2022–2023 context-aware AI assistants → current AI agents that plan workflows and allow human review at decision points.
- **codegen.com** — "How to Build Agentic Coding Workflows" — editor-level (Copilot/Cursor) vs. task-level agents (assign a whole task, sandboxed execution, output is a PR, review at checkpoints); what tasks suit an agent (clear acceptance criteria, bounded scope, verifiable) vs. what to keep (evolving requirements, architectural decisions).
- **sitepoint.com** — "Claude Code vs Cursor vs Copilot: The 2026 Developer Comparison" — tools have "moved well beyond autocomplete"; three philosophies (terminal-native agent, AI-native IDE, editor extension); workflow-based selection checklist; "many developers combine tools."
- **vibecodingacademy.ai** — "Vibe Coding for Beginners (2026)" — the categories of tools by what they build and how technical you need to be (Lovable/Bolt/v0 prompt-to-app builders for non-coders; Replit Agent to learn alongside; Cursor for coders; Claude Code for terminal power users).
- **vibewerks.com** — "Vibe Coding Tutorial" — "best AI for coding depends on your workflow" (Claude Code complex/terminal, Cursor visual editing, Copilot easiest inline start).
- **nxcode.io** — "Cursor vs Claude Code vs GitHub Copilot (2026)" — category price points as of early 2026 (extension ~$10, IDE ~$20, terminal agent ~$20–200) with free tiers; agents can read entire codebases.
- **packmind.com** — "Writing AI coding agent context files is easy; keeping them accurate isn't" — context files (`CLAUDE.md`/`AGENTS.md`/`.cursor/rules`); a good setup describes the project, states conventions, includes feedback commands, and stays current.
- **timdeschryver.dev** — "Keep Agentic AI Simple" — the context file is always in the agent's context; the idea is the same across tools; let the AI generate it, review it regularly, and add recurring mistakes to it.
