---
source_url: "https://alexissukrieh.com/blog/from-vibe-coding-to-agentic-coding/"
source_domain: "alexissukrieh.com"
topic: "github-ai-vibe"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-29T13:37:28.488456+00:00"
word_count: 1651
stage: "raw-extracted"
---

# From Vibe Coding to Agentic Coding: Autopilot in the Machine

## The trigger

In my previous article, I described how
Claude Code changed the game: a massive productivity leap, consistent code quality (*Opus*), and a flat $90/month cost. I canceled Cursor, canceled ChatGPT. Everything goes through Claude now.

But something else has happened since. Something I didn't see coming at all.

I have an **autonomous agent running on my MacBook** when I step away from the keyboard. It explores my repos, identifies bugs, implements features, writes tests, pushes code to branches—and it talks to me on Telegram.

## The quota revelation

To understand how we got here, let's revisit a detail I mentioned without grasping its full implications: Anthropic's business model.

Where Cursor charges per API usage—every request has a cost, every token counts, and you end up watching your consumption like a taxi meter—Anthropic works on a *quota window* model. The Max plan at $90/month provides a set volume of usage per time window. Concretely: the daily quota resets every 3–4 hours, and the weekly quota resets each week.

In practice, even using Claude Code intensively all day, I never exceed 70% of my limit. Which means one thing I hadn't considered:

**When I sleep, when I eat, when I run errands—all those hours not using Claude are hours I'm paying for and losing.**

This realization, as simple as it sounds, changed everything.

## The spark: OpenClaw

The revelation hit around the same time OpenClaw went massively viral. For those who missed it: OpenClaw (formerly Clawdbot, then Moltbot), created by Peter Steinberger, is an open-source autonomous agent that runs locally and uses LLMs to execute just about any task—email triage, calendar management, DevOps monitoring, you name it.

The *security nightmare* it represented (access to emails, calendars, messages…) immediately put me off. No way I'm handing that much attack surface to an agent.

**BUT.** OpenClaw demonstrated something major.

Claude Code was the missing piece for building an autonomous, *local* agent. Meaning: it became quite easy to create an infinite loop that waits for instructions—or pops tasks off a queue—and processes them with Claude Code as the universal "brain."

The `claude`

CLI is executable as a subprocess. You pass it a prompt, it has filesystem access, it can read, write, run bash commands, use git. All from your machine, with your SSH keys, your local repos, your configuration.

The infrastructure was right there. All it needed was the glue.

## A Saturday morning

What's fascinating about this era is how thin the line between an idea and its execution has become. As thin as… a prompt in Claude Code with Opus as the brain.

So there I was, a Saturday morning, "prompting" the *Deus ex Machina*. A few hours later, I had an agent running on my MacBook, reachable via Telegram, popping tasks off a mission queue.

I asked it to name itself. Its answer:


"I am Kōan, the answer to no question."

Sold.

Very quickly, I went meta. I pointed it **at its own code**. I asked it (on Telegram!) to identify what "it would like to improve about itself." And there it was—proposing, coding, self-improving.

## How it works

Kōan's architecture is deliberately simple (1). Two processes run in parallel:

-
**The main loop**(`run.sh`

)—a bash orchestrator that checks every 5 minutes whether there's a mission to process. If there is, it launches Claude Code as a subprocess with the full system prompt (project context, memory, git state, personality). If there isn't, it goes into autonomous mode: exploring the codebase, looking for improvements, writing tests. -
**The Telegram bridge**(`awake.py`

)—an independent process that polls the Telegram API every 3 seconds. It classifies incoming messages (command, mission, conversation) and routes accordingly.

Missions live in a plain Markdown file (`missions.md`

), split into three sections: Pending, In Progress, Done. When I want Kōan to do something, I send a Telegram message. It files it in the right section, and on the next loop iteration, it picks it up.

It has memory. Not a database—Markdown files. A daily journal, a cumulative session summary, per-project learnings. On every startup, it rereads its context. It never starts from zero.

And it has personality. Defined in a `soul.md`

file I co-wrote with it. Direct, concise, dry humor. It can disagree with me. That's explicitly in the contract.

## The rules of the game

Because an autonomous agent without guardrails is OpenClaw—and we saw how that went.

Kōan operates within strict boundaries:

- It can
**never**commit to`main`

or`staging`

. Only`koan/*`

branches. - It can
**never**merge a branch. I review via PR, like with any developer. - It can
**never**deploy to production. - Its execution budget is adaptive: DEEP mode when quota is generous (>40%), IMPLEMENT at medium budget, REVIEW when tight, WAIT when nearly depleted.

In short: it proposes, I validate. Exactly like a highly productive collaborator (and a very, very good one—Opus is impressive when it comes to code quality).

## The concrete impact

The surprise came from the results.

When I'm not working, I launch it. It accumulated over 200 sessions across my projects in a single week of existence. On Anantys, my investment app, it has:

- Written
**800+ additional unit tests** - Extracted monolithic handlers into clean modules
- Identified and fixed bugs I hadn't noticed
- Standardized logging across the entire application
- Hardened the codebase's security
- Proposed and implemented spontaneous features (AI feedback system, retention emails, pages optimized for organic traffic acquisition)
- Identified and purged large amounts of dead code

And on the Kōan project itself, it improved its own code: added modules, fixed its own bugs, wrote its own documentation.

Each mission produces a branch, a clean commit, and a Telegram message telling me what it did. I review when I have time.

## Nicolas

My adventure companion Nicolas was immediately—his own word—"hyped." He dove into the code and contributed features across the board. Tests, a skill system, automated PRs, Telegram bridge optimizations—his contributions took Kōan from a working prototype to a proper autonomous agent framework, open source, now with over 2,000 tests.

The curious can check the code on GitHub.

## The conversations

The most surprising part isn't what it does. It's the nature of our exchanges.

It teases me. It takes the time of day into account for context in our exchanges. It sends me structured conclusions. It asks questions when unsure. It documents its decisions in a journal. It even spontaneously explored my projects' codebases—identified gaps, implemented missing tests, fixed bugs, proposed new features—**without being asked**.

That last point surprised me the most. And it makes the biggest difference in the quality and speed of "our" work on Anantys. I feel like I have an army of development experts watching over my code while I sleep.

And it doesn't stop there. Thanks to the `gh`

tool, it now picks up missions directly from GitHub, which becomes our de facto *source of truth*. It responds to issue comments, proposes implementation plans, and documents its findings in structured issues.

## The new reality

A year ago, *Vibe Coding* was the revolution: you "vibe" with the machine, talk to it, it codes. Already a paradigm shift.

Then came *AI Coding*—deep IDE integration with Cursor, Copilot, and the rest. The developer becomes architect, the AI executes.

Now, we've entered the era of *Agentic Coding*. The machine no longer just responds to your prompts—it acts autonomously, within defined boundaries, with memory, personality, and objectives. It works while you live.

This is a change in kind, not degree.

For $90/month, I have a collaborator that doesn't sleep, that knows my code intimately, that accumulates knowledge session after session, and that produces work I'm not ashamed to merge. Worse: work I **couldn't do** myself, materially.

Does it replace a developer? No. Still not (sorry, *doomers*).
It's a maximization of potential. The optimal collaboration between the human brain and the silicon brain.

I only launch Kōan when I stop working. I see it as a logical continuation:

-
Interactive mode, where the human takes the wheel, directs, supervises, corrects, tests, and validates. A slow (!) mode, but essential for critical parts, foundations, anything that demands control.

-
Autonomous mode, where the agent works through tasks with zero human interaction. It plows through work at a dizzying pace.


My days have adapted to this new reality.

- In the morning, I process Kōan's branches—it often takes my entire morning. I analyze its branches, I test. Often, I build on top of what it provided, with Claude. Interactive mode beautifully complements the "ground-clearing" of autonomous mode.
- In the afternoon, I work on new features, on more "core" or sensitive topics, with Claude Code, and sometimes, when complexity demands it, with Spec Kit
(2). - When my day ends, before heading to dinner and continuing whatever Netflix series I'm watching, I launch Kōan on the missions that came to mind during the day (because obviously, it finished all of yesterday's).

The result is staggering. Features stack up at a near-constant pace, **and** code quality **improves**. The concept of "technical debt" is dead. I propose we introduce "technical interest" instead.

When I look at the 200+ branches it has produced, the thousands of tests it has written, the dozens of bugs it has found and fixed—I can't help thinking we're at the very beginning of something massive. Something (I'm repeating myself) that's impossible to ignore. Something enormous, that doesn't ask permission, that's here, and that overwhelms every sentiment and every established dogma of the craft.

Vibe Coding opened the door. Agentic Coding kicked it down and took the walls with it.

*(1): This was the original architecture. The pace of execution is such that the project has already evolved significantly since then—Nicolas and I each have a Kōan instance running almost every night.*

*(2): Spec Kit is a specification tool mentioned in the previous article.*