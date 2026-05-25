---
title: "Quickstart"
topic: "claude-code-workflow"
career_level:
  - mid
source_url: "https://code.claude.com/docs/en/quickstart"
source_domain: "code.claude.com"
word_count: 861
text_to_link_ratio: 1.0
signal_score: 0.6661
is_curated: false
tags:
  - Claude Code
  - installation
  - authentication
  - git operations
  - code changes
  - essential commands
ingested_at: "2026-05-25"
doc_type: "how-to-guide"
core_question: "How do you get started with Claude Code?"
tldr: "Quickstart guide to Claude Code covering installation, login, first session, basic tasks, git operations, and essential commands for beginners."
---

# Quickstart

## Before you begin

Make sure you have:- A terminal or command prompt open
- If you've never used the terminal before, check out the terminal guide

- A code project to work with
- A Claude subscription (Pro, Max, Team, or Enterprise), Claude Console account, or access through a supported cloud provider

This guide covers the terminal CLI. Claude Code is also available on the web, as a desktop app, in VS Code and JetBrains IDEs, in Slack, and in CI/CD with GitHub Actions and GitLab. See all interfaces.

## Step 1: Install Claude Code

To install Claude Code, use one of the following methods:- Native Install (Recommended)
- Homebrew
- WinGet

**macOS, Linux, WSL:**

**Windows PowerShell:**

**Windows CMD:**

If you see

`The token '&&' is not a valid statement separator`

, you're in PowerShell, not CMD. If you see `'irm' is not recognized as an internal or external command`

, you're in CMD, not PowerShell. Your prompt shows `PS C:\`

when you're in PowerShell and `C:\`

without the `PS`

when you're in CMD.Git for Windows is recommended on native Windows so Claude Code can use the Bash tool. If Git for Windows is not installed, Claude Code uses PowerShell as the shell tool instead. WSL setups do not need Git for Windows.Native installations automatically update in the background to keep you on the latest version.

## Step 2: Log in to your account

Claude Code requires an account to use. Start an interactive session with the`claude`

command and you'll be prompted to log in on first use:
For Claude subscription or Console accounts, follow the prompts to complete authentication in your browser. To switch accounts later or re-authenticate, type

`/login`

inside the running session:
You can log in using any of these account types:

- Claude Pro, Max, Team, or Enterprise (recommended)
- Claude Console (API access with pre-paid credits). On first login, a "Claude Code" workspace is automatically created in the Console for centralized cost tracking.
- Amazon Bedrock, Google Vertex AI, or Microsoft Foundry (enterprise cloud providers)

## Step 3: Start your first session

Open your terminal in any project directory and start Claude Code:
You'll see the Claude Code welcome screen with your session information, recent conversations, and latest updates. Type

`/help`

for available commands or `/resume`

to continue a previous conversation.
## Step 4: Ask your first question

Let's start with understanding your codebase. Try one of these commands:
Claude will analyze your files and provide a summary. You can also ask more specific questions:

You can also ask Claude about its own capabilities:

Claude Code reads your project files as needed. You don't have to manually add context.

## Step 5: Make your first code change

Now let's make Claude Code do some actual coding. Try a simple task:
Claude Code will:

- Find the appropriate file
- Show you the proposed changes
- Ask for your approval
- Make the edit

Claude Code always asks for permission before modifying files. You can approve individual changes or enable "Accept all" mode for a session.

## Step 6: Use Git with Claude Code

Claude Code makes Git operations conversational:
You can also prompt for more complex Git operations:

## Step 7: Fix a bug or add a feature

Claude is proficient at debugging and feature implementation. Describe what you want in natural language:
Or fix existing issues:

Claude Code will:

- Locate the relevant code
- Understand the context
- Implement a solution
- Run tests if available

## Step 8: Test out other common workflows

There are a number of ways to work with Claude:**Refactor code**

**Write tests**

**Update documentation**

**Code review**

## Essential commands

Here are the most important commands for daily use:| Command | What it does | Example |
|---|---|---|
`claude` | Start interactive mode | `claude` |
`claude "task"` | Run a one-time task | `claude "fix the build error"` |
`claude -p "query"` | Run one-off query, then exit | `claude -p "explain this function"` |
`claude -c` | Continue most recent conversation in current directory | `claude -c` |
`claude -r` | Resume a previous conversation | `claude -r` |
`/clear` | Clear conversation history | `/clear` |
`/help` | Show available commands | `/help` |
`exit` or Ctrl+D | Exit Claude Code | `exit` |

## Pro tips for beginners

For more, see best practices and common workflows.Be specific with your requests

Be specific with your requests

Instead of: "fix the bug"Try: "fix the login bug where users see a blank screen after entering wrong credentials"

Use step-by-step instructions

Use step-by-step instructions

Break complex tasks into steps:

Let Claude explore first

Let Claude explore first

Before making changes, let Claude understand your code:

Save time with shortcuts

Save time with shortcuts

- Type
`/`

to see all commands and skills - Use Tab for command completion
- Press ↑ for command history
- Press
`Shift+Tab`

to cycle permission modes

## What's next?

Now that you've learned the basics, explore more advanced features:## Getting help

**In Claude Code**: Type`/help`

or ask "how do I…"**Documentation**: You're here! Browse other guides**Community**: Join our Discord for tips and support
