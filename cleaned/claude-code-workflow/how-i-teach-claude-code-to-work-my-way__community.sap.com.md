---
title: "How I teach Claude Code to work my way"
topic: "claude-code-workflow"
career_level:
  - mid
source_url: "https://community.sap.com/t5/artificial-intelligence-blogs-posts/how-i-teach-claude-code-to-work-my-way/ba-p/14349299"
source_domain: "community.sap.com"
word_count: 4454
text_to_link_ratio: 1.0
signal_score: 0.9413
is_curated: false
tags:
  - Claude Code
  - development workflows
  - code review
  - AI-assisted coding
  - process discipline
ingested_at: "2026-05-25"
doc_type: "opinion"
core_question: "How can developers structure Claude Code workflows with skills to improve code quality and process discipline?"
tldr: "Personal account of using Claude Code with structured skills and workflows to enforce development discipline: feature-dev, brainstorm, and write-plan skills combined into three discovered patterns for effective AI-assisted coding."
---

# How I teach Claude Code to work my way

- Subscribe to RSS Feed
- Mark as New
- Mark as Read
- Bookmark
- Subscribe
- Printer Friendly Page
- Report Inappropriate Content

- SAP Managed Tags
- Artificial Intelligence
- Research and Development
- Agentic AI

## The Problem With "Just Prompting"

Here's what used to happen: I'd open Claude Code, describe what I wanted, and the AI would immediately start writing code. Sometimes it was great. More often, it solved the wrong problem, or solved the right one in a way that clashed with the rest of my codebase. I'd spend more time course-correcting than I saved.

The issue wasn't the AI's coding ability. It was the lack of *process*. When a senior developer tackles a feature, they don't just start typing. They read the existing code, consider the architecture, think about edge cases, maybe sketch something out. I wanted my AI to do the same.

That's what skills are. They're markdown files that define a process: "First explore the codebase, then propose approaches, then get my approval, then write tests, then implement." The AI follows the playbook instead of freestyling.

## My Toolkit

Over the months, I tried a lot of skills. Some became daily habits. Others were interesting experiments that didn't stick. Here's what I actually use:

Skill What It Does

feature-dev | Guided feature development with codebase analysis |
brainstorm | Structured ideation before touching code |
playground-architecture | Interactive architecture visualization |
review-pr | Multi-dimensional PR code review |
playground-brainstorm | Interactive brainstorm explorer |
voice | Voice-to-text interaction for quick input |
write-plan | Detailed step-by-step implementation plans |
pr-adopter | Process and implement PR review feedback |
execute-plan | Execute written plans with checkpoints |
brainstorm-refine | Iterative idea refinement loops |
browser-to-code | Extract context from browser tabs into workflows |
agent-teams | Multi-agent parallel work |
goal-writer | Performance goal drafting |

If I had to pick just one, it's **feature-dev**. It's the thing I reach for most — when I know roughly what I want and need the AI to genuinely understand my codebase before touching anything.

But the interesting part isn't individual skills. It's how they chain together.

## Three Workflows, Discovered by Accident

I didn't plan these. They emerged over weeks of trial and error.

### The Full Pipeline

Early on, I was working on something architecturally complex — a new service with unclear boundaries. I found myself naturally falling into a three-step rhythm:

`/superpowers:brainstorm -> /superpowers:write-plan -> /superpowers:execute-plan`

First, I'd brainstorm with the AI. Not "generate ideas" brainstorming — more like a dialogue. It would ask me questions, I'd clarify my intent, it would propose two or three approaches, and we'd land on a spec document together. Then it would break that spec into tiny implementation steps — two to five minutes each, with exact file paths and code snippets. Then it would execute those steps one by one, spinning up fresh subagents for each task.

The whole thing felt like pair programming with someone who actually reads the brief.

I used this for anything greenfield. Building an auth system from scratch? Full pipeline. New API service? Full pipeline. The brainstorm step alone saved me from building the wrong thing more times than I can count, because it forced me to explain *why* before *how*.

But it's heavy. Three steps, lots of back-and-forth. After about a month, I realized most of my work didn't need that level of ceremony.

### The Tight Loop

So I started skipping the middle step. Instead of brainstorm-plan-execute, I'd just brainstorm and then jump straight into feature-dev:

`/superpowers:brainstorm -> /feature-dev -> (oh wait, new question) -> /superpowers:brainstorm -> /feature-dev`

This works because feature-dev already does its own codebase analysis. And by this point, my `CLAUDE.md`

files — the project instruction files that Claude reads at the start of every session — had gotten detailed enough that the AI already knew my conventions, my gotchas, my architecture. It didn't need a formal written plan anymore. The plan was in the CLAUDE.md.

This became my daily driver. Quick brainstorm to align on the approach, then straight into building. If something unexpected came up during implementation, I'd pop back into a brainstorm, think it through, and dive back in. Some afternoons I'd do five or six of these cycles, redesigning multiple components in one sitting.

### The Review Pipeline

For codebases where I'm reviewing existing code rather than building new stuff, a different pattern emerged:

`/pr-review-toolkit:review-pr -> evaluate findings -> pr-adopter -> implement changes`

Review-PR is clever — it spins up specialized agents that look at security, performance, architecture, and testing in parallel. You get a multi-dimensional review in one shot. But the real gem is pr-adopter. It takes review comments and *evaluates* them before implementing. Is this comment actually valid? Is it high-impact or nitpicky? What's the risk of the suggested change?

That evaluation step is something I used to do manually, and honestly, I wasn't always great at it. Having the AI triage feedback before acting on it prevents a lot of wasted effort on low-value changes.

## Superpowers: The Discipline Layer

The workflows above describe *what* I do. **Superpowers** is the plugin that enforces *how* I do it. It's an open-source collection of skills by Jesse Vincent that adds engineering discipline to Claude Code — and it's the single most important plugin I installed.

What makes Superpowers different from other skill packs is that it doesn't just add capabilities. It adds **constraints**. Three non-negotiable rules — "iron laws" — that the AI must follow no matter what. After ten weeks of using them, I can say with confidence: these constraints are what make AI-assisted development actually reliable.

### Iron Law 1: No Production Code Without a Failing Test First

This is strict Test-Driven Development. The TDD skill enforces a red-green-refactor cycle:

**Red**— Write a test that describes the behavior you want. Run it. Watch it fail.**Green**— Write the*minimum*code to make the test pass. Nothing more.**Refactor**— Clean up, remove duplication, improve names. Tests must stay green.

The rule is absolute: if you write production code before the test, delete it. Don't keep it as reference, don't adapt it. Delete and start fresh from the test.

This sounds extreme, but it solves a real problem with AI coding assistants. Without TDD, the AI tends to write large chunks of code that *look* correct but have subtle bugs. With TDD, every line of production code exists because a test demanded it. The test proves the code works — not a vibes check.

I'll admit I was skeptical at first. Making the AI delete code it just wrote felt wasteful. But after a few sessions, I noticed something: the code that came out of TDD cycles was consistently better — fewer bugs, cleaner interfaces, and easier to refactor later.

### Iron Law 2: No Fixes Without Root Cause Investigation First

The systematic debugging skill enforces a four-phase process:

**Root Cause Investigation**— Read error messages carefully (all of them, including stack traces). Reproduce the issue consistently. Understand*why*it's happening, not just*what*.**Pattern Analysis**— Is this a known pattern? Have similar issues occurred before? What's the broader context?**Hypothesis & Testing**— Form a specific hypothesis. Test it. If it's wrong, form another one. No shotgun debugging.**Implementation**— Only now do you fix it.

The key constraint: you cannot propose a fix until you've completed phase one. No guessing. No "let me just try this real quick." The AI must demonstrate it understands the root cause before touching any code.

This matters because AI assistants love to guess. They'll see an error, pattern-match to something similar they've seen, and suggest a fix that addresses the symptom but not the cause. The debugging skill prevents that by forcing investigation first. After three failed fix attempts, it goes further — it tells the AI to question the architecture, not just the code.

### Iron Law 3: No Completion Claims Without Fresh Verification

The verification skill is deceptively simple: before claiming anything is done, you must run the verification command *in the current message* and show the output. Not "I ran the tests earlier." Not "the tests should pass." Run them now, show the results, prove it.

This catches a surprisingly common failure mode: the AI claiming tests pass based on stale information. Maybe it ran the tests three tool calls ago and things changed since. Maybe it's extrapolating from partial output. The verification skill eliminates that by demanding fresh evidence for every claim.

### How They Work Together

The three iron laws form a cycle. You write a failing test (TDD), implement the fix, debug any issues (systematic debugging), and verify everything passes before calling it done (verification). Skip any step and the chain breaks.

In practice, Superpowers also includes the brainstorming, planning, and execution skills I described in the workflows section. But it's the iron laws that changed how I work. They turned "hope-driven development" — where you hope the AI got it right — into something I can actually trust.

## The Skill That Surprised Me Most: Browser-to-Code

I built this one myself, and I almost didn't mention it because it sounds gimmicky. But it turned out to be genuinely useful, especially in enterprise settings.

The idea is simple: you have a bunch of browser tabs open — a ticket, a design, some API docs — and instead of copy-pasting content into your terminal, you let the AI read those tabs directly.

Under the hood, it uses **chrome-cdp**, a lightweight Chrome DevTools Protocol skill that connects to your browser via WebSocket. It can list your tabs, take screenshots, grab accessibility trees (structured representations of page content), and read HTML. All read-only — it never clicks or navigates in your browser.

The orchestrator skill, **browser-to-code**, wraps this into a workflow:

- It lists your open Chrome tabs
- You pick the relevant ones
- You categorize them — "this is the ticket," "this is the design," "this is reference docs"
- It extracts content from each (screenshots for visual stuff, structured text for everything else)
- It builds a summary and asks you to confirm
- You pick a workflow — brainstorm, plan, debug, or review
- It hands everything off to that skill with the full browser context included

### Where This Really Shines: Enterprise Development

If you've ever worked with SAP systems or similar enterprise software, you know the pain. Your requirements are in ServiceNow. The current UI is in SAP Fiori. The API documentation is in some internal wiki. The BTP cockpit has your service bindings. That's four tabs of critical context that normally you'd have to mentally stitch together.

With browser-to-code, a typical session looks like this: I open my ServiceNow ticket showing the requirements, the Fiori app showing the current UI, and the OData API docs. I run `/browser-to-code`

, select those three tabs, and the AI now has full visibility — the acceptance criteria from the ticket, a screenshot of the current Fiori screen, and the structured API surface. Then I pick "brainstorm" and we're off, designing the solution with all the context right there.

No copy-pasting. No "let me describe what the screen looks like." The AI literally sees it.

This is especially powerful for SAP Fiori or UI5 development where you might have the Business Application Studio open alongside Fiori Elements documentation and a BTP cockpit. Three complex web UIs that the AI can reason about together — something that would take paragraphs to explain in a prompt.

## The Experiments

Not everything became a daily habit. Some skills were worth building even if they didn't stick.

### Voice

For about a week, I went all-in on voice. I built two skills — `listen-once`

for single commands, `voice-conversation`

for continuous dialogue. The idea was to *talk through* ideas before typing them. And honestly, it worked. Speaking ideas aloud is more natural than writing them, especially when you're still fuzzy on what you want.

But the switching cost killed it. Going from voice to text to voice again felt clunky. I kept reaching for the keyboard mid-sentence to reference a file path or a function name. Voice is great for early-stage brainstorming, but the moment you need precision, text wins. I still use it occasionally, but it didn't become a habit.

### Playgrounds: Architecture Explorer and Brainstorm Explorer

These are the skills I'm probably most proud of building. They generate interactive, self-contained HTML files — single-page applications you open in a browser to visually explore your codebase.

The **Architecture Explorer** creates a three-panel layout: a component tree on the left, workflow and data flow diagrams in the center, and a details panel with code snippets and annotations on the right. It supports four diagram views — workflow, data flow, file structure, and sequence diagrams — all generated from a real analysis of your codebase. Click on a component, see its file path, its responsibilities, and the actual interface it exposes. Right-click any element and the AI explains it, lists its dependencies, or suggests improvements — all in real-time.

The **Brainstorm Explorer** takes a different angle. It creates an interactive concept map where you can mark your knowledge level on each topic (know / fuzzy / unknown / explore), draw connections between concepts, and capture ideas that appear as nodes on the canvas. It's designed for the moment when you're dropped into an unfamiliar codebase and need to map what you know, what you don't, and where to dig first. It even generates prompts you can feed back to the AI for deeper exploration.

I used these a lot when onboarding to unfamiliar codebases — especially large monorepos where the architecture isn't obvious from the folder structure alone. The visual map they create is something I'd refer back to weeks later, long after the session that created them. If you work with complex projects, these are worth trying. I even wrote a small MCP bridge that connects the templates with Claude Code and makes them interactive.

### Goal Writer

This one came out of a very specific frustration: writing performance goals for review cycles. Every year, you sit down, stare at a blank document, and try to turn vague aspirations into structured goals with success indicators. It's the kind of task that's not hard, exactly, but it's tedious and easy to do poorly.

So I built a skill for it. The goal-writer first asks about your organization's strategy, then your recent achievements, then your planned work for the coming period. It cross-references all of that and drafts goals that are actually aligned with what your org cares about — each with success indicators at three levels (partly achieved, achieved, exceeded). The structure forces specificity in a way that freeform writing doesn't.

I've only used it twice, but both times it turned a dreaded two-hour task into a thirty-minute conversation. It's the kind of niche skill that doesn't get daily use but absolutely earns its keep when the moment comes.

### CLAUDE.md Management — Keeping Your Project Memory Fresh

I keep saying CLAUDE.md compounds. But there's a problem: as your project evolves, the file can drift. Commands change, architecture shifts, new gotchas appear — and the CLAUDE.md you wrote three weeks ago quietly becomes outdated. The AI follows stale instructions and you wonder why it's doing the wrong thing.

The **CLAUDE.md Management** plugin solves this with two complementary tools. The first is `claude-md-improver`

— a skill that audits your CLAUDE.md files against your actual codebase. It scores each file on a rubric (commands documented? architecture clear? gotchas captured? still current?) and gives you a letter grade from A to F. More importantly, it tells you exactly what's missing or outdated and proposes specific additions as diffs you can approve or reject.

The second is `/revise-claude-md`

— a command you run at the end of a session. It reviews what happened during the conversation — which bash commands were discovered, which patterns were followed, which gotchas were encountered — and proposes updates to your CLAUDE.md. Think of it as a session retrospective that writes itself.

I run the improver every couple of weeks, and `/revise-claude-md`

whenever a session taught me something non-obvious. Together they keep CLAUDE.md from decaying. The difference between a maintained CLAUDE.md and a stale one is the difference between an AI that knows your codebase and one that's guessing.

### Agent Teams

The newest experiment, and the one I'm most excited about. Claude Code has a built-in concept of **subagents** — you can spawn child agents that work independently in the background while the main agent continues. Agent Teams take that a step further: you create a named team, define a shared task list, and spin up multiple agents that pick up tasks, work in parallel, and coordinate through messages.

Here's how it works in practice. You invoke `/agent-teams:team-spawn`

with a preset — say "feature" for parallel feature development, or "review" for multi-dimensional code review. The team lead agent decomposes your task into subtasks with file ownership boundaries (so agents don't step on each other's changes), creates a task list, and spawns teammates. Each teammate claims a task, works on it, marks it done, and checks the list for more work. The lead monitors progress and synthesizes results when everything's done.

What makes this different from just running multiple prompts yourself is the **coordination layer**. Agents can message each other, block on dependencies ("don't start the API tests until the API is built"), and the shared task list gives everyone visibility into what's done and what's left. It's surprisingly close to how a real engineering team operates — just faster.

The coordination overhead is real, and I wouldn't use it for small tasks. But for something like "build this feature across three layers of the stack" or "review this PR from security, performance, and architecture angles simultaneously," it's a genuine force multiplier.

## Claude Code Commands You Should Know

Before we move on, a quick detour. If you're using Claude Code and haven't explored its built-in commands, you're leaving a lot on the table. These aren't skills — they're native features of the CLI, and I use most of them daily.

** /compact** — This one saved me more times than any skill. When your conversation gets long and you start hitting context limits,

`/compact`

compresses prior messages while preserving the essential information. I used it constantly during deep implementation sessions. Don't wait until you get a context error — compact proactively.** /init** — Generates a

`CLAUDE.md`

file for your project by analyzing your codebase. It's the starting point for teaching Claude about your conventions, architecture, and gotchas. I ran this once at the beginning and have been refining the file ever since. That file is arguably the single most impactful thing you can create for your AI workflow.** /review** — Quick code review of your current changes. Less elaborate than the review-pr skill but perfect for a fast sanity check before committing.

** /mcp** — Lists your connected MCP (Model Context Protocol) servers. Essential if you're using skills that rely on external servers, like the playground sync server for real-time AI interaction in the browser.

** /resume** — Picks up where you left off. When you close a session and come back later,

`/resume`

restores the previous conversation so Claude remembers what you were working on. I use this constantly — real work rarely fits into a single session, and without resume you'd have to re-explain the entire context from scratch.**Plan mode** — Not a slash command, but worth mentioning. When you type `plan`

at the start of a prompt (or the AI enters plan mode automatically), Claude switches to read-only exploration. It can read files and search your codebase but won't edit anything until you approve its plan. I use this for anything non-trivial — it's the single biggest guard against the AI changing things you didn't want changed.

** Shift+Tab** — Toggles between different permission modes (plan mode, auto-accept, normal) without typing commands. A small convenience that adds up over hundreds of sessions.

### Claude HUD — Install This First

If you take one thing from this section, make it this: install **Claude HUD**. It's a plugin by Jarrod Watts that adds a persistent status line below your input showing everything you need to know about your session at a glance.

```
[Opus | Pro] █████░░░░░ 45% | my-project git:(main*) | 2 CLAUDE.md | 5h: 25% | ⏱️ 5m
✓ Read ×3 | ✓ Edit ×1 | ⟳ Agent: Exploring auth patterns (12s)
✓ All todos complete (3/3)
```

That context bar alone is worth the install. Before HUD, I'd be deep in a session, spawn a few subagents, and suddenly hit the context limit with no warning. Now I can see the percentage fill up in real-time and `/compact`

before it becomes a problem. The tool activity line shows exactly what Claude is doing — which files it's reading, which agents are running, how long they've been going. The todo progress tracks task completion when you're using structured workflows.

It sounds like a minor quality-of-life improvement. It's not. When you're running multi-agent sessions or deep implementation cycles, having real-time visibility into context usage, active agents, and task progress changes how you work. You make better decisions about when to compact, when to break a session, when to wait for a subagent versus starting something else.

Install it in three commands:

```
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/claude-hud:setup
```

No restart needed. It just works.

## How My Workflow Changed Week by Week

The first two weeks, I just used feature-dev for everything. It was good enough, and I didn't know what else was out there.

Week three, I discovered the brainstorm-plan-execute pipeline and it felt like a revelation. Finally, the AI was *thinking* before coding. I used the full pipeline religiously.

Week four, I got curious about voice and spent a week building and testing voice skills. Fun experiment, partial adoption.

Weeks five and six, I created the playground skills for architecture visualization. These became a go-to for understanding new codebases.

By weeks seven and eight, I'd streamlined. The full three-step pipeline was overkill for most tasks. I dropped write-plan and settled on brainstorm-to-feature-dev as my default loop.

Week nine, I started using git worktrees to keep feature branches isolated. Week ten, I tried agent teams for the first time.

The pattern: **start formal, then streamline.** The full pipeline taught me the value of each step. Once I'd internalized those patterns — always brainstorm first, always verify before calling something done — I could drop the ceremony without losing the discipline.

## Why Some Skills Stick and Others Don't

After a few months, I can see the pattern clearly.

Skills that became habits solve a **recurring pain point**. Feature-dev, brainstorm, review-pr — I need these almost every session. They slot into my existing workflow instead of replacing it, and they have an obvious trigger. "I'm about to build something" means brainstorm. "There's a PR to review" means review-pr. No decision fatigue.

Skills I built but rarely use tend to be too specialized, or they overlap with things other tools already do well. Some required setup that broke my flow — by the time I'd configured everything, I'd lost the context I was trying to preserve.

But here's the thing: even the skills I don't use regularly were worth building. The process of defining a workflow — writing down the steps, thinking about what information flows where — clarifies your thinking. It's like writing documentation that you never read again. The act of writing it was the point.

## What I'd Tell Someone Starting Out

**Brainstorm before you build.** Every time I skipped this step, I paid for it later. Five minutes of structured thinking saves thirty minutes of rework. It's the single highest-leverage habit I picked up.

**Let your workflow evolve.** Don't commit to a rigid process on day one. Start with the full pipeline, understand what each step gives you, then trim what you don't need. Your workflow in month two should look different from month one.

**Invest in CLAUDE.md.** This is the file that tells Claude about your project — conventions, architecture, gotchas. Every lesson I learned went into this file. Over time, it became comprehensive enough that the AI understood my codebase without a formal plan. It compounds in a way that's hard to appreciate until you've done it for a few weeks.

**Build custom skills for things you repeat.** Most skills are just 20-50 lines of markdown. That's twenty minutes of work to encode a process you'd otherwise re-explain every session. If you find yourself giving the same instructions more than twice, make it a skill.

**If you work in enterprise environments, try browser-to-code.** The copy-paste tax between ServiceNow, SAP, Confluence, and your terminal is real. Letting the AI see your browser tabs directly is a genuine quality-of-life improvement.

**Manage your context window.** Long sessions hit limits. I found myself compacting context constantly. It's better to break work into focused sessions than to fight the context ceiling.

## What's Next

Multi-agent teams are where I'm spending my experimental energy now. The idea of decomposing a task into independent pieces and letting multiple agents work simultaneously — that feels like the next productivity jump. The coordination patterns aren't quite there yet, but the foundation is solid.

And browser-to-code has room to grow. Right now it reads individual tabs. Imagine if it could understand the *relationships* — this Jira epic links to those Figma designs which affect these API endpoints. Connected context rather than isolated snapshots.

But honestly, the biggest lesson from last months isn't about any specific skill. It's that **the AI follows a process when you give it one, and freestyles when you don't.** Skills turn freestyling into something structured and repeatable. The AI doesn't just write code — it thinks, plans, reviews, and iterates. And that process, unlike any individual prompt, gets better every time you refine it.

## Links

**Superpowers**(core skills: brainstorm, write-plan, execute-plan, TDD, debugging, verification): github.com/obra/superpowers**Chrome CDP Skill**(browser DevTools Protocol integration): github.com/pasky/chrome-cdp-skill**My Custom Skills**(browser-to-code, goal-writer, architecture explorer, brainstorm explorer): github.tools.sap/Security-Hub/claude-skills**My Custom Skills for non SAP employees**(architecture explorer, brainstorm explorer): https://github.com/Dimi82/claude-playground-explorer**Claude HUD**(session status line — context usage, agent tracking, task progress): github.com/jarrodwatts/claude-hud**CLAUDE.md Management**(audit, score, and update CLAUDE.md files): available via the Claude Code plugin marketplace**Claude Code Workflows**(146 marketplace skills: feature-dev, agent-teams, PR review, and more): available via the Claude Code plugin marketplace

Claude Code is a powerful Agent and now officially available @SAP .

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.
