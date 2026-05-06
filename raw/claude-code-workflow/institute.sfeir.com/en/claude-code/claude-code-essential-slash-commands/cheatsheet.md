---
source_url: https://institute.sfeir.com/en/claude-code/claude-code-essential-slash-commands/cheatsheet/
crawl_depth: 0
crawled_at: 2026-05-05T14:36:11Z
word_count: 2255
---

[🏆SFEIR is the **Google Cloud EMEA Training Partner of the Year 2025**](https://institute.sfeir.com/en/training/partnerships/google-cloud)[ 🤝New partnership: Official **GitLab Training**](https://institute.sfeir.com/en/training/partnerships/gitlab)[ 🤖New training: **AI-Augmented Developer**](https://institute.sfeir.com/en/training/ai-augmented-developer)
[🏆SFEIR is the **Google Cloud EMEA Training Partner of the Year 2025**](https://institute.sfeir.com/en/training/partnerships/google-cloud)[ 🤝New partnership: Official **GitLab Training**](https://institute.sfeir.com/en/training/partnerships/gitlab)[ 🤖New training: **AI-Augmented Developer**](https://institute.sfeir.com/en/training/ai-augmented-developer)
Claude Code offers over a dozen slash commands to drive your sessions from the terminal - context management, configuration, memory, diagnostics. This cheatsheet groups each command with its syntax, options, and concrete examples so you can master them without leaving your editor.
The essential slash commands in Claude Code are the primary interaction mechanism with the AI agent directly from your terminal. Claude Code embeds dozens of native slash commands covering configuration, contextual navigation, diagnostics, and memory management. These commands significantly accelerate session management compared to using the tool without shortcuts.
## What are the most commonly used slash commands in Claude Code?
Before diving into the details of each command, here is the quick reference table you can keep at hand. Each row is self-contained: you can read it independently from the rest.  
| Command  | Description  | Usage Example  |  
| --- | --- | --- |  
| `/help`  | Displays general help and the list of available commands  |  `/help` in the Claude Code prompt  |  
| `/init`  | Initializes a CLAUDE.md file at the project root  |  `/init` in a new repository  |  
| `/clear`  | Erases conversation history and frees the context  |  `/clear` after a topic change  |  
| `/compact`  | Compresses the conversation to save tokens  | `/compact "summarize the refactoring"`  |  
| `/cost`  | Displays cumulative session cost in tokens and dollars  |  `/cost` at any time  |  
| `/config`  | Opens or modifies Claude Code configuration  |  `/config` to list settings  |  
| `/model`  | Changes the LLM model used during the session  | `/model claude-sonnet-4-6`  |  
| `/memory`  | Opens the CLAUDE.md file for quick editing  |  `/memory` to add a convention  |  
| `/doctor`  | Diagnoses the installation  | `/doctor`  |  
| `/login`  | Authenticates your session  | `/login`  |  
| `/logout`  | Disconnects your session  | `/logout`  |  
| `/status`  | Displays session status  | `/status`  |  
| `/diff`  | Shows current modifications  | `/diff`  |  
| `/permissions`  | Manages tool permissions  | `/permissions`  |  
| `/bug`  | Reports a bug to Anthropic  | `/bug`  |  
| `/feedback`  | Sends feedback to Anthropic  | `/feedback`  |  
| `/resume`  | Resumes a previous session  | `/resume`  |  
| `/context`  | Visualizes loaded context  | `/context`  |  
| `/plan`  | Creates a structured action plan  | `/plan`  |  
| `/add-dir`  | Adds a directory to context  | `/add-dir ./lib`  |  
| `/mcp`  | Manages MCP servers  | `/mcp`  |  
| `/hooks`  | Manages Claude Code hooks  | `/hooks`  |  
This table covers the most common commands. For advanced usage, check the [complete slash commands reference](https://institute.sfeir.com/en/claude-code/claude-code-essential-slash-commands/command-reference/) which details each available option.
Key takeaway: these 8 commands cover the majority of daily needs - keep this table accessible.
## How to use `/help` to navigate Claude Code?
The `/help` command is the universal entry point. **Type** `/help` in the prompt to display the complete list of commands, keyboard shortcuts, and available options.

```
$ claude
> /help

```

Claude Code then displays a structured summary with each command, its syntax, and a one-line description. In practice, `/help` consumes 0 context tokens since it sends no request to the model.
The `/help` command takes no arguments. It displays the complete list of slash commands, keyboard shortcuts, and documentation links. For details on a specific command, check the online documentation or test it directly.
If you are new to Claude Code, start with the [installation and first launch cheatsheet](https://institute.sfeir.com/en/claude-code/claude-code-installation-and-first-launch/cheatsheet/) before exploring advanced commands. You will find the prerequisites (Node.js 22+, API key) and the startup procedure there.
Key takeaway: `/help` costs nothing in tokens and remains the number one reflex when looking for a command.
## How to initialize a project with `/init`?
The `/init` command automatically generates a `CLAUDE.md` file at the root of your project. This file serves as persistent memory: Claude Code reads it at every session start.

```
$ claude
> /init

```

Claude Code analyzes the repository structure - detected languages, framework, naming conventions - then proposes a pre-filled `CLAUDE.md`. the generated file contains on average 15 to 25 lines of directives adapted to the project.
**Check** the generated content before committing it. You can then refine the instructions with the `/memory` command covered later. To understand the role of this file in depth, check the [CLAUDE.md memory system guide](https://institute.sfeir.com/en/claude-code/claude-code-memory-system-claude-md/tips/).  
| Generated Element  | Typical Content  |  
| --- | --- |  
| Tech stack  | `Node.js 22, TypeScript 5.4, Next.js 15`  |  
| Conventions  | `camelCase for variables, PascalCase for components`  |  
| Project commands  |  `npm run dev`, `npm test`, `npm run build`  |  
| Commit rules  | `Conventional Commits, messages in English`  |  
Specifically, a well-configured `CLAUDE.md` reduces clarification back-and-forth by 30% during the session.
Key takeaway: **run** `/init` on the first use of Claude Code in a project to lay the foundations of persistent memory.
## How to manage context with `/clear` and `/compact`?
Context management is the number one performance factor in Claude Code. Two complementary commands let you maintain control: `/clear` and `/compact`.
###  `/clear` - Start from scratch
**Use** `/clear` when you switch topics or when the context becomes too loaded. This command erases the entire current conversation.

```
> /clear

```

The Claude Opus 4.6 context window is 200,000 tokens. In practice, a development session reaches this limit after 45 to 90 minutes of intensive exchanges. **Launch** `/clear` before switching to a new task to maximize response quality.
###  `/compact` - Compress without losing essentials
The `/compact` command asks the model to summarize the current conversation. You can pass an optional instruction to guide the summary.

```
> /compact
> /compact "keep only the architecture decisions"

```
  
| Command  | Tokens Before  | Tokens After (approx.)  | Info Loss  |  
| --- | --- | --- | --- |  
| `/clear`  | 150,000  | 0  | Total  |  
| `/compact`  | 150,000  | 15,000-30,000  | Minimal  |  
| `/compact "focus X"`  | 150,000  | 10,000-20,000  | Targeted  |  
To dive deeper into context management strategies, **check** the [dedicated context management guide](https://institute.sfeir.com/en/claude-code/claude-code-context-management/cheatsheet/) which covers advanced use cases.
Key takeaway: `/compact` preserves essential history, `/clear` starts from scratch - choose according to your need.
## How to monitor costs with `/cost`?
###  `/cost` - Real-time financial tracking
**Type** `/cost` to display the cumulative cost of the current session. Claude Code breaks down input tokens, output tokens, and the estimated amount in dollars.

```
> /cost
Session cost: $0.42
 Input tokens: 45,230
 Output tokens: 12,890
 Cache read: 128,400
 Cache write: 45,230

```

In practice, the cost of a development session varies depending on the model chosen and exchange intensity. When the session becomes long and responses slow down, it is a sign that the context is filling up. **Launch** `/compact` to compress the conversation.
You will find tips for optimizing your conversations in the [first conversations guide](https://institute.sfeir.com/en/claude-code/claude-code-your-first-conversations/cheatsheet/).
Key takeaway: **check** `/cost` regularly to track your consumption and know when to use `/compact`.
## How to configure Claude Code with `/config`, `/model`, `/login`, and `/logout`?
These four commands control the global configuration of your Claude Code environment.
###  `/config` - General settings
**Open** the configuration with `/config` to access persistent settings.

```
> /config

```

You can modify the theme, default permissions, notification mode, and other preferences. Configuration is stored in `~/.claude/settings.json`.
###  `/model` - Switch models on the fly
**Switch** between models without leaving your session. Specifically, this allows you to choose a less expensive model for simple tasks.

```
> /model claude-sonnet-4-6
> /model claude-opus-4-6
> /model claude-haiku-4-5

```
  
| Model  | Tokens/s (output)  | Relative Cost  | Recommended Usage  |  
| --- | --- | --- | --- |  
| Claude Haiku 4.5  | ~150  | 1x  | Simple tasks, quick questions  |  
| Claude Sonnet 4.6  | ~90  | 5x  | Standard development  |  
| Claude Opus 4.6  | ~40  | 25x  | Complex architecture, heavy refactoring  |  
If you want to dive deeper into model selection based on your tasks, the [slash commands examples](https://institute.sfeir.com/en/claude-code/claude-code-essential-slash-commands/examples/) illustrate concrete scenarios.
###  `/login` and `/logout` - Authentication management
**Run** `/login` to authenticate or switch accounts. The `/logout` command disconnects the current session. Your API tokens and local configurations are not affected by `/logout`.

```
> /login
> /logout

```

For security questions related to authentication and permissions, check the [permissions and security guide](https://institute.sfeir.com/en/claude-code/claude-code-permissions-and-security/cheatsheet/).
Key takeaway: `/model` saves you up to 80% by switching to Haiku for simple tasks.
## How to use `/memory` and undo actions daily?
###  `/memory` - Edit persistent memory
The `/memory` command opens the project's `CLAUDE.md` file in your default editor. **Add** your conventions, style preferences, or business rules so that Claude Code applies them automatically at each session.

```
> /memory
# Opens CLAUDE.md in $EDITOR

```

**Document** your recurring patterns: naming style, test structure, commit conventions. A well-written `CLAUDE.md` improves response relevance from the first exchange.
To get the most from this feature, the [CLAUDE.md memory system guide](https://institute.sfeir.com/en/claude-code/claude-code-memory-system-claude-md/tips/) details best practices for writing.
### Undoing a Claude Code action
To undo an action performed by Claude Code, ask it to use git to revert, or use git commands directly:

```
git checkout -- <file> # Undo changes to a file
git stash # Stash current changes
git reset HEAD~1 # Undo the last commit

```
  
| Action  | Command  | Effect  |  
| --- | --- | --- |  
| Undo a modified file  | `git checkout -- `  | Restores the file  |  
| Stash changes  | `git stash`  | Temporary save  |  
| Erase everything (conversation)  | `/clear`  | Resets context to zero  |  
If you are looking to integrate Claude Code into a Git workflow, the [Git integration guide](https://institute.sfeir.com/en/claude-code/claude-code-git-integration/cheatsheet/) covers the associated versioning commands.
Key takeaway: `/memory` builds lasting project knowledge. To undo modifications, use standard git commands.
## How to diagnose problems with `/doctor`?
The `/doctor` command runs a series of automated checks on your Claude Code environment. **Run it** whenever unexpected behavior occurs.

```
> /doctor

```

`/doctor` checks 6 critical points in under 10 seconds:
  1. API key validity
  2. Network connectivity to Anthropic servers
  3. Installed Node.js version (minimum required: Node.js 18+)
  4. Configuration file integrity `~/.claude/settings.json`
  5. File system access permissions
  6. Installed Claude Code version compatibility

  
| Check  | OK Status  | KO Status - Action  |  
| --- | --- | --- |  
| API Key  | `OK Valid`  |  **Re-run** `/login`  |  
| Network  | `OK Connected`  | Check proxy/VPN  |  
| Node.js  | `OK v22.x`  | Update Node.js  |  
| Config  | `OK Valid JSON`  | Delete and recreate with `/config`  |  
| Permissions  | `OK Read/Write`  | Fix permissions with `chmod`  |  
| Version  | `OK Latest`  |  **Run** `npm update -g @anthropic-ai/claude-code`  |  
Specifically, 90% of problems encountered by developers are resolved by running `/doctor` then following the displayed recommendations. For additional troubleshooting tips, the [first conversations guide](https://institute.sfeir.com/en/claude-code/claude-code-your-first-conversations/tips/) covers common startup errors.
Key takeaway: `/doctor` is your first diagnostic reflex - it identifies the cause in under 10 seconds.
## What keyboard shortcuts accelerate your Claude Code workflow?
Beyond slash commands, Claude Code offers keyboard shortcuts that complement your productivity. Here are the most useful combinations.  
| Shortcut  | Action  | Slash Equivalent  |  
| --- | --- | --- |  
| `Ctrl+C`  | Cancel the current generation  | -  |  
| `Ctrl+L`  | Refresh the screen display (does not reset context)  | -  |  
| `Escape`  | Exit multi-line mode  | -  |  
| `Up arrow`  | Recall the last sent message  | -  |  
| `Tab`  | Autocomplete slash commands  | -  |  
**Press** `Tab` after typing `/` to see the complete list of available commands with autocomplete. In practice, autocomplete reduces command typing time by 60%.
SFEIR Institute offers a [one-day Claude Code training](https://institute.sfeir.com/en/training/claude-code-training/) where you practice these commands on real lab projects. You will learn to chain slash commands and shortcuts to achieve a fluid workflow. To go further, the [AI-Augmented Developer](https://institute.sfeir.com/en/training/ai-augmented-developer/) 2-day training covers integrating Claude Code into a complete CI/CD chain, and the [advanced training](https://institute.sfeir.com/en/training/ai-augmented-developer-advanced/) in one day helps you master complex use cases like multi-agent and automation.
To explore all slash commands in detail with commented use cases, find the [practical slash commands examples](https://institute.sfeir.com/en/claude-code/claude-code-essential-slash-commands/examples/) and the [essential slash commands overview](https://institute.sfeir.com/en/claude-code/claude-code-essential-slash-commands/).
Key takeaway: combine keyboard shortcuts and slash commands to drive Claude Code without ever touching the mouse.
* * *
## Recent articles about Claude
### [Claude Managed Agents: Anthropic's Platform for Production Agent Deployment Anthropic launches Managed Agents: a cloud platform for deploying AI agents in production. Secure sandbox, checkpointing, multi-agent, autonomous sessions lasting hours. Notion, Rakuten, Asana and Sentry already use it.](https://institute.sfeir.com/en/articles/claude-managed-agents-anthropic-production-agent-platform/)### [Claude Code Dream & Auto Dream: Automatic Memory Consolidation After 20 sessions, Auto Memory notes become a mess. Auto Dream solves this by automatically consolidating Claude Code's memory: deduplication, stale entry removal, relative-to-absolute date conversion.](https://institute.sfeir.com/en/articles/claude-code-dream-auto-dream-memory-consolidation/)### [Claude Code Auto Mode: Autonomy Without the Risk Auto Mode in Claude Code eliminates permission interruptions while keeping a safety net. A classifier analyzes every action before execution and blocks destructive operations. The sweet spot between approving everything and letting everything through.](https://institute.sfeir.com/en/articles/claude-code-auto-mode-permissions-autonomy/)
Claude Code Training
### This topic is covered in Module 6 of our Claude Code training
Useful Commands and Tips
1-day training • 60% hands-on labs • Expert instructors
