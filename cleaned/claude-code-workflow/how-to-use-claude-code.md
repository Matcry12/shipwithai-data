---
title: "How to Use Claude Code (Beginner Guide)"
topic: "claude-code-workflow"
career_level:
  - senior
  - executive
source_url: "https://www.builder.io/blog/how-to-use-claude-code"
source_domain: "www.builder.io"
word_count: 3451
text_to_link_ratio: 0.9263
signal_score: 1.0
is_curated: false
tags:
  - remote
  - open-source
  - senior
  - executive
ingested_at: "2026-05-05"
---

#### Claude Code
# How to Use Claude Code (Beginner Guide)
#### March 4, 2026
#### Written By [Vishwas Gopinath](https://www.builder.io/blog/authors/vishwas-gopinath)
Most developers hear about Claude Code, install it, type a vague prompt, get a mediocre result, and conclude it's overhyped. But Claude Code gets productive fast once you get the basics right.
This Claude Code tutorial walks through everything from installation to making your first real code change. You'll learn how to use Claude Code as a CLI tool, configure your project so Claude follows your rules, and build the workflow that turns a chatbot into a coding partner.
If you're new to Claude Code, [What is Claude Code](https://www.builder.io/blog/what-is-claude-code) covers the big picture before you start here.
## What is Claude Code and how is it different from other AI coding tools?
Claude Code is Anthropic's agentic coding tool that reads your entire codebase, edits files, and runs commands through natural language prompts. It's available across the terminal CLI, VS Code, JetBrains IDEs, a desktop app, and the web. It reasons across multiple files and executes multi-step tasks autonomously while you review and approve each change.
Say you need to add email validation to a signup form. You type that as a prompt.
Claude Code finds the relevant files across your project, plans the changes, shows you a diff, and applies the edits after you approve. It runs tests, commits code, and creates pull requests. All from a single prompt.
So how is this different from other AI coding tools? [Most AI coding tools](https://www.builder.io/blog/best-ai-tools-2026) now offer agent modes, multi-file editing, and plugin ecosystems. The features overlap significantly. The difference is the default workflow and where you spend your time. [Cursor](https://www.builder.io/blog/cursor-vs-claude-code) optimizes for an IDE-first experience. Claude Code optimizes for giving the AI more autonomy to work through a task while you review at a higher level. The choice comes down to how you prefer to work with AI.
## What do you need before installing Claude Code?
You need a Claude Pro subscription ($20/month) or higher, a terminal application, and a computer running macOS, Linux, or Windows 11. The Pro plan provides enough usage for most beginners. Git is strongly recommended as a safety net for reviewing and rolling back AI-generated changes.
### System requirements
Claude Code runs on macOS (Intel and Apple Silicon), Linux (Ubuntu 22.04+, Debian 12+), and Windows 11 (natively or via WSL2, Windows Subsystem for Linux). You need a terminal like the built-in Terminal on macOS, PowerShell on Windows, or any major terminal on Linux. On Windows, use PowerShell specifically. Git Bash has compatibility issues.
Git is optional for installation. Strongly recommended as a safety net for reviewing and rolling back changes.
Node.js 18+ is only needed for npm-based workflows. The native installer doesn't require it.
### Pricing and plans
The Pro plan at $20/month ($17/month billed annually) is enough for learning and light daily use. Anthropic doesn't publish exact message limits, but allocations reset every 5 hours with no overage fees. There's also a weekly cap on total usage, so heavy sessions across multiple days can hit a ceiling even if each 5-hour window has room.
If you hit rate limits regularly, Max plans offer more capacity. Max 5x ($100/month) gives 5x the Pro allowance, and Max 20x ($200/month) gives 20x.
For API-style billing, the [Console](https://console.anthropic.com/) charges per token. It auto-creates a "Claude Code" workspace for cost tracking. Team plans start at $25/seat/month (Standard, or $20 annually) with Premium seats at $150/seat/month ($100 annually) for 5x the usage. Both tiers include Claude Code.
Start with Pro. Upgrade when you know your usage patterns.
## How do you install Claude Code step by step?
Install Claude Code by running `curl -fsSL  | bash` on macOS or Linux, or `irm  | iex` in Windows PowerShell. Verify with `claude --version`, then run `claude` in any project directory to authenticate through your browser. The native installer auto-updates.
Install commands by platform:
**macOS and Linux (including WSL):**

```
curl -fsSL <https://claude.ai/install.sh> | bash
```

**Windows PowerShell:**

```
irm <https://claude.ai/install.ps1> | iex
```

**Windows CMD:**

```
curl -fsSL <https://claude.ai/install.cmd> -o install.cmd && install.cmd && del install.cmd
```

You can also install via Homebrew (`brew install --cask claude-code`) or WinGet (`winget install Anthropic.ClaudeCode`). These methods require manual updates. The native installer auto-updates.
After installation, verify it worked:
If the `claude` command isn't found, restart your terminal. PATH issues after installation are the most common problem. If something still looks off, a fresh reinstall usually fixes it.
**Authentication** is browser-based. Run `claude` in any project directory, and your default browser opens to [claude.ai](http://claude.ai/) for a one-time sign-in. Return to the terminal, and you're authenticated. Credentials are stored locally in `~/.claude/` so you won't need to log in every session.
Several older tutorials and AI-generated articles still recommend `npm install -g @anthropic-ai/claude-code`. That method is no longer in the [official docs](https://code.claude.com/docs/en/quickstart). Use the native installer.
## How do you start your first Claude Code session?
Start a Claude Code session by running `claude` in your project directory. Begin with an exploratory prompt like "what does this project do?" to let Claude analyze your codebase. Then try a small edit. Claude will show proposed changes and ask for your approval before modifying anything.
Navigate to your project and launch Claude:

```
cd ~/projects/my-app
claude

```

You'll see a welcome screen showing your working directory, the model in use, and hints for getting started. The interface is a conversational prompt. Type your message, hit Enter.
Start by exploring your codebase:

```
what does this project do?
```

Claude reads your files, summarizes the stack, and describes the architecture. Follow up with more focused questions:

```
what are the main modules?
```

Or reference a file directly with the `@` symbol:

```
@src/App.tsx explain what this component does
```

These are the essential Claude Code commands you'll use daily:  
| Command  | What it does  | /help  | Lists all available commands  |  
| --- | --- |  
| /clear  | Resets conversation, same project  |  
| /compact  | Compresses history while keeping key context  |  
| /model  | Shows available models to choose from  |  
| /plan  | Enters Plan Mode for read-only research  |  
| /resume  | Continues a previous session  |  
| /init  | Generates a starter CLAUDE.md from your project  |  
Keyboard shortcuts worth memorizing: Tab for completion, Up arrow for history, `?` for all shortcuts, `/` to see all commands, `!` to run a terminal command and feed the output back to Claude, Esc to stop Claude mid-action.
**Making your first code change.** Give Claude a prompt with a file reference:

```
Update the header text in @src/pages/Home.tsx to say 'Welcome to My App'
```

Claude shows the proposed diff and asks for approval. Say yes, and the file updates. Then validate:

```
git diff
```

Claude Code also has built-in checkpoints. Every edit creates a snapshot you can roll back to with Esc+Esc or `/rewind`. Checkpoints only track Claude's file edits though. For bash commands and external changes, Git gives you the full picture.
**About the permission system.** Claude asks before every file edit and shell command by default. This feels slow at first. Few developers on Hacker News have described it as "drive you insane" levels of friction but it also prevents disasters.
You can customize permissions with `/permissions` to allowlist safe commands like `npm run lint` or `git commit`. This cuts the approval prompts for trusted operations while keeping guardrails for everything else. There's also `--dangerously-skip-permissions` which bypasses all approval prompts. The name is intentionally scary. It lets Claude run any command and edit any file without asking. Only consider this after a few months of daily use when you fully understand what Claude Code can and will do to your codebase. Use it at your own risk.
## How do you configure your project with CLAUDE.md?
CLAUDE.md is a markdown file at your project root that tells Claude Code how your project works. Think of it as onboarding documentation for your AI teammate. Run `/init` to generate a starter version, then add your build commands, code style rules, and architectural decisions. Keep it concise. Bloated files cause Claude to ignore your instructions.
A CLAUDE.md gives Claude your conventions upfront. It follows your rules reliably across every session. Skip it, and Claude guesses. Sometimes right, often wrong.
Run `/init` inside a Claude Code session. Claude analyzes your project, detects build systems, test frameworks, and code patterns, then generates a starter CLAUDE.md. Review the output and trim aggressively. Most of what `/init` generates is information Claude can already discover by reading your code.
A good CLAUDE.md looks like this:

```
# Tech Stack

- Frontend: React 19, TypeScript, Vite
- Backend: Node.js, Express
- Testing: Vitest (frontend), Jest (backend)

# Commands

- `npm run dev` -- Start dev server
- `npm test` -- Run all tests
- `npm run lint` -- Lint check

# Code Style

- Use ES modules (import/export), never CommonJS (require)
- Functional components only, no class components
- Prefer named exports over default exports

# Workflow

- Create feature branches before changes
- Run tests before every commit
- Keep PRs focused on a single concern
```

Anthropic's [best practices docs](https://code.claude.com/docs/en/best-practices) say it well. "For each line, ask: Would removing this cause Claude to make mistakes? If not, cut it." Over-specified CLAUDE.md files are a common beginner mistake. When the file gets too long, Claude loses track of the important rules buried inside.
Early benchmarks reinforce this. A study found that LLM-generated context files (like those from `/init`) slightly decreased task completion rates, while developer-written files improved results by only 4% on average. Both increased agent costs by over 20%.
**What to include:** Bash commands Claude can't guess, code style rules that differ from language defaults, test instructions, repo etiquette (branch naming, PR conventions), architectural decisions, and common gotchas.
**What to leave out:** Anything Claude can figure out from reading code, standard language conventions it already knows, detailed API documentation (link to docs instead), and information that changes frequently.
As Boris Cherny (Claude Code's creator) put it, "There is no one right way to use Claude Code. Everyone's setup is different." Your CLAUDE.md will evolve as you learn what Claude needs reminding about.
**Treat CLAUDE.md as a living document.** Review it when your stack changes, when you add dependencies, or when a new model release handles things differently. A stale [CLAUDE.md](http://claude.md/) causes more problems than having none at all. Outdated file paths, deprecated patterns, or legacy tech listed prominently mislead Claude into errors that are hard to trace back to the file.
**File locations:** `~/.claude/CLAUDE.md` for global preferences that apply everywhere, `./CLAUDE.md` at your project root for team-shared rules (check it into git), and `CLAUDE.local.md` for personal overrides you want to gitignore.
For a deeper dive, check out [How to Write a Good CLAUDE.md File](https://www.builder.io/blog/claude-md-guide).
## What is the best workflow for using Claude Code effectively?
When you're starting out with Claude Code, a simple four-step workflow keeps you in control. Explore (read files in Plan Mode), Plan (outline the approach), Code (implement with approval), and Commit (review diffs and commit). Planning is the most important step. Without a plan, Claude jumps straight into writing code and you lose the chance to shape the approach before files start changing. Activate Plan Mode with Shift+Tab to let Claude research and think without touching anything. Use `/clear` between unrelated tasks to keep context focused.
The workflow as a diagram:
**Explore:** Press Shift+Tab twice to enter Plan Mode. Claude reads files and answers questions without touching anything. Ask it to understand the authentication flow, map out the database schema, or trace how a request moves through your app.
**Plan:** Still in Plan Mode, ask Claude to create an implementation plan. Review it, refine it, then proceed.
**Code:** Switch back to Normal Mode and let Claude implement. It follows its plan, shows diffs, and asks for approval at each step.
**Commit:** Review with `git diff`. Run tests. Commit with a descriptive message.
Skip Plan Mode for small, obvious fixes. A typo correction or a single-line config change doesn't need a research phase. Use it when you're uncertain about the approach, when the change touches multiple files, or when you're working in unfamiliar code.
The practice that pays off most, per Anthropic's own [best practices docs](https://code.claude.com/docs/en/best-practices), is giving Claude a way to verify its work. Tests, screenshots, expected outputs. If Claude can run `npm test` and see green, it self-corrects. Give it verification criteria, and it handles the feedback loop for you.
### When do you clear, compact, or start fresh?
Context management defines your Claude Code experience. The default context window is 200,000 tokens (with 1 million tokens available in beta for Sonnet and Opus). As the window fills with conversation history, file contents, and command outputs, Claude's performance degrades. Claude auto-compacts when it gets close to the limit by clearing older tool outputs and summarizing the conversation, but proactive management works better.
Use `/clear` between unrelated tasks. If you just finished a bug fix and want to add a feature, clear first. The old context actively hurts the new task.
Use `/compact` when you're deep into a long task and don't want to lose your place. It compresses the conversation while preserving code patterns, file states, and key decisions. You can add focus instructions like `/compact Focus on the API changes`.
Start a fresh session entirely (quit and re-run `claude`) after two failed correction attempts. If Claude keeps producing the wrong output despite corrections, the context is polluted with failed approaches. A clean session with a better prompt almost always outperforms a long session with accumulated mistakes.
## What happens when you outgrow one agent?
Everything in this guide assumes you're one developer working with one Claude Code session. That's the right way to start. But at some point you'll hit the ceiling.
You'll want to run a refactor in one terminal while building a feature in another. You'll open three Claude Code sessions, each needing its own git worktree, its own dev server, and its own share of your laptop's CPU. Meanwhile your designer is pinging you on Slack with spacing feedback and your PM wants to verify the acceptance criteria on the feature branch. Neither of them can see or touch the code directly.
This is the exact problem [Builder.io](https://www.builder.io/) was built to solve.
Builder.io is an agentic development platform that runs 20+ agents in parallel, each in its own cloud container with a full dev environment and browser preview. Everything runs in the cloud. Each branch gets its own preview. Your laptop stays free.
The parallel agents handle throughput. The collaborative workspace handles everything else. Your whole team works together:
  * **Designers** propose layout changes directly in the branch using a visual canvas connected to your real components
  * **PMs** verify acceptance criteria in live previews
  * **QA** validates before the PR even reaches you
  * **You** review architecture and merge clean, validated code


Assign tasks from Slack or Jira. Agents create branches and open PRs automatically. Team members validate in real-time. You get back fully-reviewed code. Everything is shareable with a link.
Claude Code makes you fast as a solo developer. [Builder.io makes your whole team fast](https://www.builder.io/).
## How do you use Claude Code in VS Code?
Install the Claude Code extension from the VS Code marketplace by searching for "Claude Code" in the Extensions view (Cmd+Shift+X on macOS, Ctrl+Shift+X on Windows/Linux). The extension provides the full Claude Code experience inside your IDE with inline diffs, @-mentions, Plan Mode, and conversation history.
Claude Code started as a terminal tool, and the CLI remains the most complete interface. A few features like [MCP](https://www.builder.io/blog/model-context-protocol) server configuration, the `!` bash shortcut, and some slash commands are CLI-only. For everything else, the VS Code extension works the same way. If you prefer staying in your editor, start with the extension.
The extension is published by Anthropic. Once installed, click the Spark icon in the top-right corner of the editor or the Claude Code label in the bottom-right status bar to open the Claude Code panel. It also works in Cursor since Cursor supports VS Code extensions.
**When to use which:**
  * **Terminal CLI:** If you prefer a command-line workflow, or need MCP server setup, the `!` bash shortcut, and advanced slash commands
  * **VS Code extension:** If you prefer an IDE-integrated experience. Handles multi-file edits, Plan Mode, Git workflows, code explanations, and everything else


The JetBrains plugin covers IntelliJ, PyCharm, WebStorm, GoLand, and other JetBrains IDEs. Open it with Cmd+Esc (Mac) or Ctrl+Esc (Windows/Linux). There's also a desktop app with visual diff review, app preview for running your dev server directly in the desktop, and connectors for GitHub, Slack, Linear, and Notion. The web version at claude.ai/code requires zero installation.
Same subscription across every surface.
## What mistakes do Claude Code beginners make?
The five most common beginner mistakes are running mixed-topic sessions without `/clear`, correcting Claude repeatedly instead of starting fresh, skipping CLAUDE.md configuration, not committing code before asking for large changes, and writing vague prompts. Treat Claude Code as a capable but non-deterministic collaborator that needs clear instructions and regular checkpoints.
**Mistake 1: Kitchen sink sessions.** You start with a bug fix, then ask about an unrelated feature, then go back to the bug. Claude's context fills with irrelevant information and performance tanks. Fix: run `/clear` between unrelated tasks. Every time.
**Mistake 2: Correcting Claude in circles.** Claude does something wrong. You correct it. Still wrong. You correct again. Now the context is polluted with three failed attempts. Fix: after two failed corrections, `/clear` and write a better initial prompt. Incorporate what you learned about what went wrong. A clean start with a precise prompt beats iterating on a confused session.
**Mistake 3: Skipping CLAUDE.md**. Claude guesses at your conventions when there's no CLAUDE.md. Wrong import style. Wrong test runner. Wrong branch naming. Run `/init` in your first session and refine the output. Ten minutes of setup saves hours of corrections.
**Mistake 4: Not using safety nets before big changes.** Claude proposes a multi-file refactor. You accept. Something breaks. Claude Code has built-in checkpoints you can roll back to with Esc+Esc or `/rewind`, and those handle most situations. For extra safety on large refactors, run `git commit -m "checkpoint before Claude refactor"` first. Git catches everything checkpoints don't, like bash commands and external changes. Also review diffs carefully.
**Mistake 5: Vague prompts.** "Make this better" gives Claude nothing to work with. "Reduce duplication in @src/utils/date.ts and keep the public API unchanged" gives it constraints, scope, and a file reference. Fix: be specific about what you want, what file it's in, and what constraints apply. Treat Claude like a senior engineer who's new to your codebase. Give it the context it needs.
## FAQ
**Q: Do I need a paid Claude subscription to use Claude Code?**
**A:** Yes. Claude Code requires a Claude Pro subscription ($20/month) or a Console account with API billing. Pro is enough for learning and light daily use. There's no free tier.
**Q: Is my code sent to Anthropic's servers when using Claude Code?**
**A:** Claude Code sends your prompts and relevant file content to Anthropic's API for processing. It reads files as needed but doesn't upload your entire codebase at once. The context window holds the current conversation and files Claude has actively read. Check [Anthropic's data handling policies](https://www.anthropic.com/privacy) for retention and privacy details.
**Q: How does Claude Code handle large codebases?**
**A:** Claude Code reads files on demand, one at a time as needed. It uses a context window to hold the current conversation, files it has read, and command outputs. Keep context focused by referencing specific files with `@` and running `/clear` between unrelated tasks. [Subagents](https://www.builder.io/blog/subagents) can handle investigation tasks that require reading many files while keeping your main session clean.
**Q: Can I use Claude Code with VS Code and the terminal at the same time?**
**A:** Yes. The VS Code extension and terminal CLI use the same subscription and can run simultaneously. Many developers use the terminal for multi-file tasks and VS Code for focused edits. Sessions are independent.
**Q: What is the difference between Claude Code and regular Claude chat?**
**A:** Claude Code is an agentic tool that reads your local files, runs terminal commands, and makes code changes with your approval. Regular Claude chat runs in a browser and works with pasted text only. Claude Code is designed for development workflows; Claude chat is for general conversation and analysis.
## Get started
Claude Code becomes productive once you nail three fundamentals. A clean install with the right subscription. A concise CLAUDE.md that teaches Claude your project's conventions. And the discipline to follow the Explore-Plan-Code-Commit workflow. Every other skill (Plan Mode, context management, VS Code integration) builds on that foundation.
Pick the topic that matters most, dig in, and build something. The best way to learn Claude Code is to use it on a real project.
![](https://cdn.builder.io/api/v1/pixel?apiKey=YJIGb4i01jvw0SRdL5Bt)
[ Build in Claude Code.  Ship as a team in Builder. Builder 2.0 lets you push your branch and hand off design review, PM feedback, and QA to the rest of your team Try for free ](https://www.builder.io/signup)![](https://cdn.builder.io/api/v1/pixel?apiKey=YJIGb4i01jvw0SRdL5Bt)
Continue Reading
[ AI10 MIN Announcing Builder 2.0: Collaborative Coding with Claude and Codex WRITTEN BYSteve Sewell April 8, 2026 ](https://www.builder.io/blog/builder-2-0)[ AI6 MIN When Enterprise AI Development Gets Real: Five Friction Points, Five Fixes WRITTEN BYAmy Cross April 7, 2026 ](https://www.builder.io/blog/five-friction-points-five-fixes)[ Design8 MIN How to Use Figma's Remote MCP WRITTEN BYAlice Moore April 3, 2026 ](https://www.builder.io/blog/figma-remote-mcp)
