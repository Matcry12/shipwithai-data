---
title: "Claude Code Tutorial for Beginners - Complete 2026 Guide to AI Coding"
topic: "claude-code-workflow"
career_level:
  - senior
  - executive
source_url: "https://codewithmukesh.com/blog/claude-code-for-beginners"
source_domain: "codewithmukesh.com"
word_count: 4767
text_to_link_ratio: 0.9018
signal_score: 0.9018
is_curated: false
tags:
  - remote
  - open-source
  - senior
  - executive
ingested_at: "2026-05-05"
---

[ #claude ](https://codewithmukesh.com/categories/claude) [ ](https://codewithmukesh.com/courses/claude-code-for-dotnet-developers/)
#  Claude Code Tutorial for Beginners - Complete 2026 Guide to AI Coding 
22 min read
Jan 20, 2026  Jan 15, 2026 · Updated Jan 20, 2026 
41.4K views
#### [ .NET Web API Course  Zero to Hero Series  Master .NET Web API development from scratch. Learn to build production-ready APIs with Clean Architecture, best practices, and real-world patterns.  20+ Chapters 5,000+ Developers Highly Rated Start Learning  ](https://codewithmukesh.com/courses/dotnet-webapi-zero-to-hero/#join-course)
I don’t write code by hand anymore. And no, I’m not exaggerating.
For the past few months, I’ve been using **Claude Code** as my primary coding companion, and it has fundamentally changed how I build software. Whether I’m scaffolding a new .NET Web API, debugging a tricky race condition, or refactoring a legacy codebase - Claude is right there in my terminal, reasoning through problems like a senior engineer sitting next to me.
But here’s the thing: most developers I talk to either haven’t heard of Claude Code, or they’ve tried it once and didn’t realize its true potential. They treat it like a fancy autocomplete. It’s not.
**Claude Code is a full-fledged agentic coding assistant** that can read your entire codebase, understand your architecture, plan multi-step implementations, and execute them - all while respecting your coding standards.
In this guide, I’ll show you how to get started with Claude Code in under 15 minutes. We’ll cover installation, the magic of `CLAUDE.md`, Plan Mode, context management, and I’ll give you an honest comparison with GitHub Copilot and Cursor.
![Claude Code terminal interface showing AI powered coding assistant in action](https://codewithmukesh.com/_astro/cover.D2JpsSzF_1v6Tbc.webp)
Let’s get into it.
## What is Claude Code? (2026 Overview)
[Claude Code](https://claude.ai/download) is [Anthropic’s](https://anthropic.com) **terminal-native AI coding assistant** built on top of Claude (the same model powering [claude.ai](https://claude.ai)). Unlike traditional code completion tools that suggest snippets as you type, Claude Code operates as an **agentic system** - meaning it can:
  * Read and understand your entire project structure
  * Search through files, grep for patterns, and analyze dependencies
  * Plan complex implementations before writing any code
  * Execute multi-file changes while respecting your conventions
  * Run shell commands, tests, and build processes
  * Learn your project’s rules through a `CLAUDE.md` file


Think of it as having a senior developer in your terminal who never gets tired, never forgets your coding standards, and can hold 200,000 tokens of context in memory.
> Claude Code launched in **February 2025** and reached general availability in **May 2025**. By November 2025, it hit $1 billion in annualized revenue - that’s how fast developers are adopting it.
![Claude Code official download page on claude.ai showing installation options](https://codewithmukesh.com/_astro/website.BXBP3Cuz_1QvnNh.webp)
## Claude Code vs GitHub Copilot vs ChatGPT vs Cursor - Quick Comparison
Before we dive in, let’s address the elephant in the room. You’ve probably used GitHub Copilot, ChatGPT, or heard about Cursor. How does Claude Code stack up?  
| Feature  | Claude Code  | GitHub Copilot  | ChatGPT/Codex  | Cursor  |  
| --- | --- | --- | --- | --- |  
| **Primary Interface**  | Terminal (CLI)  | IDE Plugin  | Web/API  | Full IDE (VS Code fork)  |  
| **Context Window**  | 200,000 tokens  | ~8,000 tokens (practical)  | 128,000 tokens  | Project-aware  |  
| **Approach**  | Agentic, multi-step reasoning  | Autocomplete, snippets  | Conversational, iterative  | Multi-file refactoring  |  
| **Best For**  | Architecture, debugging, explanations  | Fast completions, boilerplate  | Brainstorming, exploration  | Large refactors, IDE comfort  |  
| **Learning Curve**  | Medium  | Low  | Low  | Low  |  
| **Pricing**  | $20-200/month (Claude subscription)  | $0-39/month  | $20-200/month (ChatGPT Plus/Pro)  | $20-40/month  |  
**My honest take:**
  * **[GitHub Copilot](https://github.com/features/copilot)** is fantastic for autocomplete and writing boilerplate fast. It’s the easiest to adopt and lives right in your IDE.
  * **[ChatGPT/Codex](https://chat.openai.com)** excels at brainstorming, exploring ideas, and conversational problem-solving. When you need to think through an approach before touching code, it’s a great sparring partner.
  * **[Cursor](https://cursor.com)** shines when you’re doing multi-file refactoring and want a familiar VS Code experience with AI baked in.
  * **Claude Code** wins when you need **reasoning**. When you want the AI to understand _why_ your code is structured a certain way, plan before executing, and explain its decisions.


For .NET developers working on complex architectures (Clean Architecture, microservices, domain-driven design) - Claude Code’s ability to hold massive context and reason through dependencies is a game-changer.
If you’re a .NET developer looking to level up your skills, these resources pair perfectly with Claude Code:
#### [ .NET Developer Roadmap  The complete guide to becoming a proficient .NET developer - from fundamentals to advanced architecture patterns.  ](https://codewithmukesh.com/blog/dotnet-developer-roadmap/)
#### [ 20+ Tips from a Senior .NET Developer  Hard-won lessons and practical advice for writing better .NET code - perfect for training Claude on your coding standards.  ](https://codewithmukesh.com/blog/20-tips-from-a-senior-dotnet-developer/)
### My Journey Through AI Coding Tools
Let me share how I ended up here - and why I believe the future isn’t about picking ONE tool.
I started with **GitHub Copilot** like most developers. It’s decent for basic code changes and generation - no complaints there. The autocomplete is snappy, and it genuinely speeds up boilerplate work. But as I used it for larger tasks, I wasn’t happy with the context it maintained. It felt like explaining the same architectural decisions over and over. The AI would suggest patterns that contradicted what I’d just built two files ago. And the developer experience? Despite being integrated directly into the IDE, something about the back-and-forth never clicked for me when I needed deeper reasoning.
Then came **Codex**. I’d had a ChatGPT subscription for a long time, but I never realized it included Codex access - pleasant surprise. When I discovered it, I went all in. For JavaScript and frontend work, I could see real success. The conversational interface made it easy to iterate on ideas. I even used it to improve [FullStackHero](https://fullstackhero.net/) - refactoring modules, cleaning up patterns, and it actually did a solid job understanding the .NET ecosystem.
But when I tested **Claude Code** , I was genuinely impressed.
It wasn’t just about code generation. Claude understood my codebase structure, respected my workflow, and grasped my requirements in a way the others didn’t. When I described a feature, it would ask clarifying questions about edge cases I hadn’t considered. When I pointed it at a bug, it would trace through the call stack and identify the root cause - not just patch the symptom. The Blazor skills? Surprisingly strong. It could reason through component hierarchies, understand the render lifecycle, handle cascading parameters correctly, and suggest patterns that actually made sense for Blazor development. For complex .NET work - Clean Architecture, domain-driven design, multi-project solutions - Claude Code’s ability to hold context across dozens of files is unmatched.
### The Real Lesson: Use Every Tool for What It’s Best At
Here’s what I’ve learned after months of experimentation: **the goal isn’t to choose one tool and abandon the rest.** Each tool has its strengths, and the smartest developers use them together.
Here’s my current setup:
  * **Claude Code** - My primary tool for complex implementations, debugging, architectural decisions, and anything that requires deep codebase understanding. When I need the AI to _think_ before it acts, Claude is where I go.
  * **GitHub Copilot** - Still in my workflow for quick autocomplete and commit message generation. It’s fast, it’s inline, and for small completions it’s hard to beat.
  * **ChatGPT** - My go-to for brainstorming ideas, exploring approaches before I write code, and rubber-ducking problems. Sometimes I just need to think out loud with an AI that isn’t tied to my codebase.


The tools complement each other. Copilot for speed. ChatGPT for exploration. Claude Code for depth.
**Don’t fall into the trap of tribal loyalty to one tool.** The AI landscape is evolving fast, and the developers who win are the ones who adapt their toolkit to the task at hand.
That said, for the core work of building software - understanding requirements, planning implementations, writing production code, and debugging complex issues - Claude Code has become my daily driver. And trust me, there are a lot of ways to supercharge your Claude experience beyond the basics. I’ll be covering advanced patterns, custom commands, and productivity hacks in upcoming articles.
For now, let’s get you set up.
## Claude Code Installation - Get Running in 5 Minutes
Let’s get Claude Code installed. You’ll need:
  * A Claude subscription (Pro at $20/month minimum)
  * Node.js (for the npm installation method)
  * A terminal (Command Prompt, PowerShell, or your IDE’s integrated terminal)


### CLI vs Desktop vs Cloud - Pick Your Flavor
Here’s something most tutorials skip: Claude Code isn’t just a CLI tool. You have **three ways** to access it:
  1. **CLI (Terminal)** - The original experience. Runs directly in your terminal alongside your code.
  2. **Desktop App** - A standalone application with a dedicated window and UI.
  3. **Cloud (claude.ai)** - Browser-based access, works anywhere including mobile.


**I use all three.** And honestly, that’s the productivity hack nobody talks about.
Here’s my setup:
  * **CLI for intense coding sessions** - When I’m deep in backend work, implementing features, or debugging complex issues, I run Claude in my terminal. It’s lightweight, fast, and stays out of the way. The CLI just feels more responsive when you’re in the zone.
  * **Desktop for general development** - The desktop app is convenient when I want Claude in a separate window. But fair warning - it’s more memory intensive than the CLI. During really long sessions, I’ve noticed it can get sluggish or act a bit weird. If you’re on a machine with limited RAM, stick with the CLI.
  * **Cloud and mobile app for brainstorming** - This is my go-to when I’m away from my dev machine. Thinking through architecture during a commute? Sketching out an approach before I sit down to code? I use the **[Claude Android app](https://play.google.com/store/apps/details?id=com.anthropic.claude)** on my phone - it’s smoother than the browser and works great for quick back-and-forth conversations. The web version at [claude.ai](https://claude.ai) is there when I’m on a different machine without the CLI installed.


The beauty is they all share your Claude subscription. Same account, same usage limits, different interfaces for different contexts.
For this guide, we’ll focus on the **CLI installation** - it’s the most powerful option for developers and the one you’ll use for serious coding work.
### Windows Installation
The official PowerShell script can be finicky. Here’s the reliable approach using npm:
**Step 1: Install Node.js (if you don’t have it)**
Head to [nodejs.org](https://nodejs.org), download the LTS version, and run the installer.
Verify the installation:

```


node -v


```

You should see a version number like `v22.x.x`.
**Step 2: Install Claude Code via npm**

```


npm install -g @anthropic-ai/claude-code


```

**Step 3: Launch Claude Code**

```

claude

```

On first run, you’ll:
  1. Choose your theme (dark mode, obviously)
  2. Connect your Anthropic account
  3. Trust the current directory


![Claude Code first run setup screen showing theme selection and account connection](https://codewithmukesh.com/_astro/first-run.Dv3ZOG8-_ZoBfkl.webp)
### macOS / Linux Installation
You have more options here:

```

# Using Homebrew (recommended for macOS)


brew install --cask claude-code


# Or using the official installer


curl -fsSL https://claude.ai/install.sh | bash


```

Then simply run `claude` in your terminal.
![Claude Code running inside terminal with command prompt ready for input](https://codewithmukesh.com/_astro/terminal.DwE9yM1v_ctLzQ.webp)
## CLAUDE.md File - How to Configure Claude Code for Your Project
Here’s where Claude Code becomes truly powerful.
The `CLAUDE.md` file is a Markdown file at the root of your project that **onboards Claude onto your codebase**. Every time you start a Claude session in that directory, the contents of this file are injected into context automatically.
Think of it as writing instructions for a new developer joining your team - except this developer has perfect memory and follows instructions precisely.
### What to Put in CLAUDE.md
Structure your `CLAUDE.md` around three layers:
  1. **The What** - Your tech stack, project structure, key packages
  2. **The Why** - The purpose of each component, architectural decisions
  3. **The How** - How you want Claude to work with the project


Here’s an example for a .NET Web API project:

```

# CLAUDE.md - MyApp API


## Tech Stack


- .NET 9, ASP.NET Core Minimal APIs


- Entity Framework Core with PostgreSQL


- MediatR for CQRS


- FluentValidation for request validation


## Project Structure


- `src/MyApp.Api/` - Entry point, endpoints, middleware


- `src/MyApp.Application/` - Use cases, handlers, DTOs


- `src/MyApp.Domain/` - Entities, value objects, domain events


- `src/MyApp.Infrastructure/` - EF Core, external services


## Commands


- Build: `dotnet build`


- Test: `dotnet test`


- Run: `dotnet run --project src/MyApp.Api`


## Coding Standards


- Use primary constructors for dependency injection


- Always pass CancellationToken to async methods


- Validation goes in FluentValidation validators, not handlers


- Never hardcode connection strings or secrets


## Workflow Rules


- ALWAYS create a git branch before making changes


- Run `dotnet test` after every implementation


- Keep commits atomic and focused


```

### Creating CLAUDE.md Automatically
You can ask Claude to generate this file for you:

```

Analyze this codebase and create a CLAUDE.md file that covers:


1. Tech stack and dependencies


2. Project structure and purpose of each folder


3. Build/test/run commands


4. Coding conventions you observe


5. Workflow rules I should follow


Use progressive disclosure - keep the main file concise and link to


detailed docs in a /docs folder if needed.

```

Claude will scan your project, identify patterns, and create a comprehensive `CLAUDE.md`. You can then refine it based on your preferences.
> **Pro Tip:** Treat `CLAUDE.md` as a living document. Commit it to version control so your entire team benefits. When coding standards evolve, update the file.
### Does It Actually Work?
Let me show you. After setting up `CLAUDE.md` with a rule that says “always create a git branch before making changes,” I asked Claude to fix a bug:

```

There's a bug where clicking on the calendar doesn't set the correct


time for the new event. The time shown in the modal doesn't match


where I clicked.

```

Claude found the bug in a TSX file, but before implementing the fix, **it asked to create a new branch first** - exactly as instructed in my `CLAUDE.md`.
That’s the power of this file. Claude respects your workflow.
## Claude Code Plan Mode - Think Before You Code
Here’s a mistake I see developers make with AI coding tools: they jump straight into implementation without planning.
Claude Code has a **Plan Mode** specifically designed to prevent this. When you’re in Plan Mode, Claude can only:
  * Read files
  * Search and grep through code
  * Browse the web for documentation
  * Ask you clarifying questions


It **cannot** write, modify, or execute anything. It’s forced to think first.
### How to Enter Plan Mode
Press `Shift + Tab` twice to cycle to Plan Mode - you’ll see the indicator in the bottom left corner of the prompt.
> **Windows users:** If `Shift + Tab` only toggles between Edit and Auto-accept modes, try `Alt + M` instead. There’s a known issue on some Windows setups where Plan Mode is skipped in the cycle.
![Claude Code Plan Mode indicator showing read-only mode in bottom left corner](https://codewithmukesh.com/_astro/plan-mode.BpnReoC1_U2Rs1.webp)
### When to Use Plan Mode
Use Plan Mode when:
  * Starting a new feature with multiple components
  * Making architectural changes
  * You’re not 100% sure about the approach
  * Working on an unfamiliar codebase


### A Real Example
Let’s say I want to build a chore management app. Instead of vibe-coding with a vague prompt like “make me a chore app,” I enter Plan Mode and write:

```

Build a chore management app with these requirements:


- Calendar view similar to Outlook


- Add/remove chores


- Recurring schedules


- Assign chores to team members


- Manage team members


Ask me questions to clarify requirements, tech stack preferences,


engineering constraints, and architecture decisions.

```

Claude will now ask targeted questions:
  * “Should this be React, Vue, or another framework?”
  * “Local storage or a backend database?”
  * “Do you need authentication?”
  * “Any specific UI library preferences?”


After I answer, Claude generates a detailed implementation plan:
  * Project structure
  * Data models
  * Component breakdown
  * Implementation phases
  * Key design decisions


**This is like pair programming with a senior engineer.** You discuss the approach, agree on the plan, and only then do you execute.
If I see something I disagree with (like Claude choosing JavaScript instead of TypeScript), I can say:

```

Use TypeScript instead of JavaScript.

```

Claude regenerates the plan. Once I’m satisfied, I approve it and Claude starts implementing - now with a clear roadmap.
#### [ .NET Claude Kit  Free  Open-source Claude Code companion with 47 skills and 10 specialist agents  ](https://codewithmukesh.com/resources/dotnet-claude-kit)
## Claude Code Context Window - How It Understands Your Codebase
One thing that sets Claude Code apart is its **200,000-token context window**. For perspective:
  * GitHub Copilot practically uses around 8,000 tokens
  * GPT-4 Turbo supports 128,000 tokens
  * Claude Code can hold roughly **150,000 words** of code and conversation in memory


This means Claude can genuinely understand large codebases. I’ve used it on .NET solutions with 50+ projects, and it navigates them effectively.
### How Context Works
When you start a session, Claude doesn’t load your entire codebase into memory immediately. Instead, it:
  1. Reads your `CLAUDE.md` file
  2. Scans the project structure
  3. Loads files on-demand as needed
  4. Maintains conversation history


If you’re working on a specific feature, Claude will read the relevant files, understand the dependencies, and keep that context as you iterate.
### Managing Context
Context can fill up during long sessions. Here are some tips:
**Clear conversation history:** Type `/clear` to reset the conversation while keeping your `CLAUDE.md` context.
**Use subagents for isolated tasks:** When Claude spawns a subagent (a focused task), it gets its own context. This prevents bloating your main session.
**Keep CLAUDE.md concise:** Since `CLAUDE.md` is loaded into every session, don’t dump your entire documentation there. Keep it focused and link to external files for details.
## Claude Code Hooks - Automate Your Workflow
Hooks let you run custom actions at specific points in Claude’s workflow. They’re event-driven:
  * **PreToolUse** - Runs before Claude uses a tool (like before writing a file)
  * **PostToolUse** - Runs after a tool completes
  * **Stop** - Runs when Claude finishes a task


For example, you could set up a hook to automatically run your linter after every file edit, or validate a deployment script before execution.

```

# Access the hooks interface


/hooks

```

Hooks are powerful for teams that want to enforce quality gates automatically. I’ll cover them in depth in a follow-up article.
## Claude Code Custom Commands - Create Your Own Shortcuts
You can create custom commands to streamline repetitive tasks. These live in the `.claude/commands/` folder as Markdown files.
For example, create `.claude/commands/test.md`:

```

Run all tests for the solution and report any failures.


If tests fail, analyze the error and suggest fixes.


$ARGUMENTS

```

Now you can type `/test` in Claude, and it executes your predefined prompt.
Some ideas for custom commands:
  * `/pr` - Create a pull request with a structured description
  * `/review` - Review the current changes for code quality
  * `/migrate` - Generate an EF Core migration


I’ll do a deep dive on custom commands in the next article. They’re a productivity multiplier once you get the hang of them.
## Claude Code Pricing 2026 - Plans and Rate Limits Explained
Claude Code access comes with your Claude subscription. Here’s the breakdown:  
| Plan  | Price  | Claude Code Access  | Usage  |  
| --- | --- | --- | --- |  
| **Free**  | $0  | No access  | -  |  
| **Pro**  | $20/month  | Yes  | ~45 messages per 5-hour window  |  
| **Max 5x**  | $100/month  | Yes  | ~225 messages per 5-hour window  |  
| **Max 20x**  | $200/month  | Yes  | ~900 messages per 5-hour window  |  
**My recommendation:** Start with the Pro plan at $20/month. It’s enough for most individual developers. If you’re using Claude Code all day for heavy development, consider Max 5x.
For teams, there’s a Teams plan with centralized billing and admin dashboards - useful for tracking usage across developers.
> **No per-message overage fees** - you get a fixed allocation per time window, and it resets. No surprise bills.
### What Happens When You Hit the Rate Limit?
This is something every Claude Code user experiences eventually - you’re in the zone, shipping features, and suddenly Claude says it needs to wait.
Here’s what actually happens:
  1. **You get a warning** - Claude will tell you that you’re approaching your usage limit for the current window.
  2. **Requests slow down or pause** - Once you hit the limit, Claude won’t process new prompts until the window resets.
  3. **The 5-hour window resets** - Your allocation refreshes every 5 hours. If you hit the limit at 2 PM, you’ll get a fresh allocation around 7 PM.


**How to manage this:**
  * **Break work into sessions.** If you’re on Pro, plan your heavy Claude Code sessions around the 5-hour windows. Don’t burn through 45 messages on small tasks.
  * **Use Plan Mode strategically.** Planning consumes fewer resources than execution. Do your thinking in Plan Mode, then execute efficiently.
  * **Batch your requests.** Instead of asking Claude to fix one file, then another, then another - describe the full scope and let it handle multiple files in one go.
  * **Know when to upgrade.** If you’re consistently hitting limits before lunch, Max 5x at $100/month gives you 5x the headroom. For all-day coding, Max 20x is worth it.


I’ve been on Max 5x for months, and I rarely hit the ceiling. But when I was on Pro, I learned to be strategic - mornings for heavy implementation, afternoons for review and planning.
## 6 Claude Code Tips From a Power User
After using Claude Code extensively, here are my top tips - lessons learned from real projects, not theory.
### 1. Talk to Claude Like a Senior Engineer
Be clear, specific, and direct. You don’t need to be overly polite or use corporate speak - just state the facts.
**Instead of:**

```

Could you please help me with maybe adding some validation


to the user input if that's not too much trouble?

```

**Try:**

```

Add FluentValidation to the CreateUserCommand.


Validate: Email is required and valid format,


Name is required and max 100 chars.

```

Claude responds better to specific, actionable instructions. Treat it like a capable colleague who needs clear requirements, not hand-holding.
### 2. Commit Early, Commit Often
This one has saved me countless times. Before you pile on more prompts, **commit your working state**.
AI can introduce regressions. Claude might fix one bug and accidentally break something else. If you’ve committed after each successful change, rolling back is trivial:

```


git diff HEAD~1  # See what changed


git checkout HEAD~1 -- src/file.cs  # Restore specific file


```

I commit after every meaningful change Claude makes. It takes seconds and gives you a safety net.
### 3. Review the Code - Always
Claude is a teammate, not a replacement for code review. I’ve seen Claude:
  * Add dependencies I didn’t ask for
  * Use patterns that don’t match my architecture
  * Write code that works but isn’t idiomatic


Check its work like you would any pull request. Read the diff, understand the changes, and push back if something doesn’t look right.
### 4. Use Plan Mode for Anything Non-Trivial
If a task touches more than 2-3 files or involves any architectural decisions, start in Plan Mode. The upfront planning saves hours of back-and-forth later.
I’ve learned this the hard way - jumping straight into implementation with a vague prompt leads to Claude making assumptions. Those assumptions compound, and suddenly you’re three files deep into an approach you don’t want.
Plan first. Execute with confidence.
### 5. Invest in Your CLAUDE.md
A well-crafted `CLAUDE.md` pays dividends across every single session. Every minute you spend refining it saves you from repeating yourself later.
Things worth adding:
  * Your naming conventions
  * Patterns you always use (Result pattern, MediatR, etc.)
  * Patterns you **never** want (no repository pattern, no AutoMapper, etc.)
  * How you structure commits and branches


The more specific your `CLAUDE.md`, the less you’ll fight Claude on style decisions.
### 6. Don’t Be Afraid to Say “No”
Claude will suggest approaches. Sometimes they’re great. Sometimes they’re not what you want.
Push back. Say “No, use X instead” or “I don’t like this approach because Y.” Claude is designed to iterate. It won’t get offended, and it’ll adapt to your preferences.
The best results come from a back-and-forth dialogue, not blind acceptance of the first suggestion.
## Claude Code FAQ - Common Issues and Solutions
Here are the questions I get asked most often about Claude Code.
### How to Fix npm Install Permission Errors
Don’t use `sudo npm install -g`. Instead, fix npm’s permissions:

```


mkdir ~/.npm-global


npm config set prefix '~/.npm-global'


export PATH=~/.npm-global/bin:$PATH


```

Add that last line to your `.bashrc` or `.zshrc` to make it permanent. Then run the install again without sudo.
On Windows, run your terminal as Administrator for the initial install, or use the native installer instead of npm.
### Why Doesn’t Claude Code Understand My Project Structure?
This usually means Claude hasn’t read enough context. Try:
  1. **Create a`CLAUDE.md` file** - This is the single biggest improvement you can make.
  2. **Explicitly tell Claude to explore** - Say “Read the project structure and understand the architecture before making changes.”
  3. **Point Claude to key files** - “Look at `src/Application/` to understand how we structure commands and handlers.”


Claude doesn’t automatically read every file. It reads on-demand. Guide it to the important parts.
### How to Prevent Claude Code From Making Unwanted Changes
This happens. Claude sometimes “improves” code while fixing something else. A few ways to prevent this:
  * **Be explicit about scope** - “Only modify the `UserService` class. Don’t touch anything else.”
  * **Add rules to`CLAUDE.md`** - “Never refactor code unless explicitly asked.”
  * **Use Plan Mode** - Review the plan before Claude executes. If you see unrelated changes, tell it to remove them.


And always: commit before asking Claude to make changes. Easy rollback.
### What to Do When Claude Code Forgets Earlier Instructions
Long sessions can exhaust context. When this happens:
  1. **Type`/clear`** - This resets the conversation but keeps your `CLAUDE.md` loaded.
  2. **Start a new session** - Close and reopen Claude Code. Fresh context.
  3. **Summarize before continuing** - After `/clear`, paste a brief summary: “We’re building X. We’ve completed Y. Next step is Z.”


For very long tasks, I break them into multiple sessions intentionally. Each session has focused scope.
### How to Stop Claude Code From Suggesting Unwanted Patterns
Put your preferences in `CLAUDE.md`. Be explicit:

```

## Patterns We Use


- MediatR for CQRS


- Result<T> pattern for error handling


- FluentValidation for all request validation


## Patterns We DON'T Use (Never suggest these)


- Repository pattern (we use EF Core directly)


- AutoMapper (we write explicit mappings)


- Exceptions for control flow


```

Claude follows these rules reliably once they’re documented.
### Is My Code Sent to Anthropic’s Servers?
Yes - Claude Code sends your code to Anthropic’s API for processing. This is how it works.
However, Anthropic has stated that data from Claude Pro/Max subscriptions is **not used to train models**. If you’re working on sensitive code, check your company’s AI usage policy and Anthropic’s terms of service.
For enterprise needs, there’s a Teams plan with additional compliance features.
### Can I Use Claude Code Offline?
No. Claude Code requires an internet connection to communicate with Anthropic’s API. There’s no offline mode.
If you’re working in an air-gapped environment, Claude Code isn’t an option - you’ll need to look at local LLM solutions.
#### [ Claude Code for .NET Developers  From Setup to Multi-Agent Teams  Master AI powered .NET development with Claude Code. Learn CLAUDE.md, Plan Mode, MCP servers, hooks, skills, and multi-agent workflows to 10x your productivity.  8+ Hours 11 Lessons All Levels Start Learning  ](https://codewithmukesh.com/courses/claude-code-for-dotnet-developers/#join-course)
## What’s Next? - The Complete Claude Code Series
This was just the beginning. I’m building a **complete Claude Code series** for .NET developers - taking you from beginner to mass productivity.
Here’s what’s coming:
### CLAUDE.md Mastery
  * **The Perfect CLAUDE.md for .NET Developers** - My exact template for Clean Architecture, Minimal APIs, and enterprise .NET projects. Copy-paste ready.
  * **Everything You Need to Know About CLAUDE.md** - Deep dive into progressive disclosure, team sharing, and advanced patterns.


### Core Features
  * **Understanding Plan Mode** - When to use it, when to skip it, and how to get the most out of planning sessions.
  * **Understanding Subagents in Claude Code** - How Claude spawns focused tasks, context isolation, and multi-agent patterns.
  * **Skills in Claude Code** - Build custom slash commands that 10x your workflow. I’ll share my personal `/pr`, `/review`, and `/migrate` commands.


### Advanced (Coming Soon)
  * **Hooks** - Automate linting, testing, and deployment validation
  * **MCP (Model Context Protocol)** - Connect Claude to Jira, GitHub, databases, and Slack
  * **YOLO Mode & Context Management** - When to go fast, and how to handle massive codebases


**This series will be the most comprehensive Claude Code resource for .NET developers on the internet.** No fluff, just practical patterns you can use tomorrow.
If you want to be notified when these drop, **subscribe to my newsletter** below. I send out .NET and developer productivity content every week - no spam, just value.
* * *
**What are your thoughts on AI coding assistants?** Are you using Copilot, Cursor, or something else? Let me know in the comments - I’m curious how other developers are integrating AI into their workflows.
Happy Coding :)
### Share this Article
Help others discover this content
Copy
Want to reach 7,100+ .NET developers? [See sponsorship options](https://codewithmukesh.com/sponsor). 
### Continue Reading
Handpicked articles you might enjoy 
[![Anatomy of a Claude Code Session - What Happens Under the Hood](https://codewithmukesh.com/_astro/cover.DAynEDS3_Z1KKAOK.webp) Anatomy of a Claude Code Session - What Happens Under the Hood Mar 26, 2026 Read  ](https://codewithmukesh.com/blog/anatomy-claude-code-session/)[![Plan Mode in Claude Code - Think Before You Build with AI](https://codewithmukesh.com/_astro/cover.CJzIkNLJ_2wlpYJ.webp) Plan Mode in Claude Code - Think Before You Build with AI Feb 25, 2026 Read  ](https://codewithmukesh.com/blog/plan-mode-claude-code/)[![Anatomy of the .claude Folder - Every File Explained \(2026\)](https://codewithmukesh.com/_astro/cover.C6WWa4e0_Z1q26BB.webp) Anatomy of the .claude Folder - Every File Explained (2026) Apr 7, 2026 Read  ](https://codewithmukesh.com/blog/anatomy-of-the-claude-folder/)
##  What's your Feedback? 
Do let me know your thoughts around this article. 
Popular Articles
  1. [ 1  The Ultimate .NET Developer Roadmap 2026 - AI, Backend, Blazor...  ](https://codewithmukesh.com/blog/dotnet-developer-roadmap/)
  2. [ 2  Essential AWS Services Every .NET Developer Should Master!  ](https://codewithmukesh.com/blog/essential-aws-services-for-dotnet-developers/)
  3. [ 3  Claude Code Tutorial for Beginners - Complete 2026 Guide to...  ](https://codewithmukesh.com/blog/claude-code-for-beginners/)
  4. [ 4  GitHub Actions CI/CD Pipeline for Deploying .NET Web API to...  ](https://codewithmukesh.com/blog/github-actions-deploy-dotnet-webapi-to-amazon-ecs/)
  5. [ 5  Choosing the Best AWS Compute Service for your .NET Solution...  ](https://codewithmukesh.com/blog/best-aws-compute-service-for-your-dotnet-solution/)


FREE Developer Resources
[ Clean Architecture Template  .NET 10 production-ready starter  ](https://codewithmukesh.com/resources/clean-architecture-template)[ Interview Questions PDF  100 scenario-based questions  ](https://codewithmukesh.com/resources/dotnet-webapi-interview-questions)[ .NET Claude Kit  47 skills for Claude Code + .NET  ](https://codewithmukesh.com/resources/dotnet-claude-kit)
On This Page
Weekly .NET tips, free 
Subscribe Free 
Get weekly .NET + AI tips
###  You're in! 
Welcome to the crew.
Check your inbox and confirm to get Tuesday's issue 
[ ](https://mail.google.com/mail/u/0/#search/from%3Acodewithmukesh) [ ](https://outlook.live.com/mail/0/inbox) [ ](https://mail.yahoo.com/)
Every Tuesday: benchmarks, architecture insights, and production tips that never make it to the blog. 
Continue reading 
##  Every Tuesday, one email. 
.NET tips, benchmarks, and architecture insights. Straight from production. 
Exclusive benchmarks
7,100+ developers · Free forever · No spam  [ Preview an issue → ](https://codewithmukesh.com/newsletter)
Search articles Type to start searching
No results found Try different keywords
Searching...
`↑``↓` navigate `↵` select
Powered by Orama
We value your privacy
Accept All  Essentials Only 
![codewithmukesh](https://codewithmukesh.com/favicon.svg)
codewithmukesh
codewithmukesh.com
Not now
