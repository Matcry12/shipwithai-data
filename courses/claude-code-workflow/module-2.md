# Module 2 — Setup and Sane Defaults

**Objective:** Configure Claude Code (or your assistant of choice) so it earns its keep from the first session.

---

## Lesson 1 — Install, Authenticate, and Verify

Getting the tool running is a five-minute job. Skipping verification is where most beginners lose an hour later.

### Installation

The recommended path for macOS and Linux is the native installer:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

On Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

Homebrew and WinGet also work but require manual updates. "The native installer auto-updates"[^1], so prefer it unless your environment forces otherwise. On Windows, use PowerShell, not Git Bash — "Git Bash has compatibility issues."[^1]

After installation, confirm the binary is on your PATH: `claude --version`. If the command is not found, restart your terminal — PATH issues are the most common post-install problem[^1].

### Authentication

"Authentication is browser-based. Run `claude` in any project directory, and your default browser opens to claude.ai for a one-time sign-in. Credentials are stored locally in `~/.claude/` so you won't need to log in every session."[^1]

### IDE Extension

"Install the Claude Code extension from the VS Code marketplace by searching for 'Claude Code' in the Extensions view. The extension provides the full Claude Code experience inside your IDE with inline diffs, @-mentions, Plan Mode, and conversation history."[^1] It also works in Cursor. For JetBrains IDEs, a separate plugin is available.

Before trusting the assistant with real work, confirm it can read files and run terminal commands. Ask it to list your project's top-level files. If it fails, debug now rather than mid-task.

**Action:** Install Claude Code with the native installer, run `claude --version`, open a project directory, and ask Claude to list the top-level files. Once it responds correctly, file-read and authentication are confirmed.

---

## Lesson 2 — Project Instructions with `CLAUDE.md`

The single highest-leverage configuration step is a `CLAUDE.md` file. Without it, the assistant guesses your conventions every session.

### What It Does

"`CLAUDE.md` is a markdown file at your project root that tells Claude Code how your project works. Think of it as onboarding documentation for your AI teammate." "A `CLAUDE.md` gives Claude your conventions upfront. It follows your rules reliably across every session. Skip it, and Claude guesses. Sometimes right, often wrong."[^1]

"CLAUDE.md is a special file that Claude reads at the start of every conversation. Include Bash commands, code style, and workflow rules. This gives Claude persistent context it can't infer from code alone."[^2]

### Generate a Starter, Then Trim

Run `/init` inside a session. "Claude analyzes your project, detects build systems, test frameworks, and code patterns, then generates a starter CLAUDE.md."[^1] A well-configured file "reduces clarification back-and-forth by 30% during the session."[^3]

After generation, trim aggressively using this test: *"Would removing this cause Claude to make mistakes?"* If not, cut it. "Bloated CLAUDE.md files cause Claude to ignore your actual instructions."[^2]

### What to Include and What to Exclude

Include: Bash commands Claude cannot guess, code style rules that differ from defaults, testing instructions, repository etiquette, and architectural decisions specific to your project[^2].

Exclude: anything Claude can infer from reading code, standard language conventions, detailed API docs, and file-by-file codebase descriptions[^2]. Self-evident rules like "write clean code" waste context and dilute what actually matters.

Structure the content around three layers: the What (stack, structure), the Why (architectural decisions), and the How (your working preferences)[^4]. "Commit it to version control so your entire team benefits. When coding standards evolve, update the file."[^4]

**Action:** Run `/init` in your main project. Delete every line that passes the "would Claude figure this out anyway?" test. Add one naming convention, one never-do rule, and your test runner command. Commit the file.

---

## Lesson 3 — Permissions, Tool Integrations, and Selective MCP

With installation and project memory in place, the last layer is controlling what the assistant is allowed to do and what external systems it can reach.

### Permission Modes

By default, Claude Code asks for approval before any system-modifying action. "This is safe but tedious. After the tenth approval you're not really reviewing anymore, you're just clicking through."[^2]

Three ways to reduce friction:

- **Auto mode** — "a separate classifier model reviews commands and blocks only what looks risky: scope escalation, unknown infrastructure, or hostile-content-driven actions."[^2]
- **Permission allowlists** — permit specific safe tools like `npm run lint` or `git commit`[^2]. Right for commands you have already watched run cleanly.
- **Sandboxing** — OS-level isolation that restricts filesystem and network access, letting Claude work freely within defined boundaries[^2].

Start in prompt-on-every-tool mode. After a few sessions of watching the assistant's behavior, add allowlists for read-only and low-risk commands. Reserve auto mode for longer autonomous tasks where you have reviewed the plan first.

### Connect Git and Your Test Runner

If you use GitHub, install the `gh` CLI — "Claude knows how to use it for creating issues, opening pull requests, and reading comments. Without `gh`, Claude can still use the GitHub API, but unauthenticated requests often hit rate limits."[^2] Include your exact test runner command in `CLAUDE.md`. The assistant cannot close the feedback loop on a code change if it cannot run tests.

### MCP Servers — Connect What You Use, Skip the Rest

"With MCP servers, you can ask Claude to implement features from issue trackers, query databases, analyze monitoring data, integrate designs from Figma, and automate workflows."[^2] "MCP server support means Claude Code can be extended with external tools and data sources, making it adaptable to unusual workflows."[^5]

The discipline is restraint. Each registered server adds latency and tool-call noise to every session. Connect a server only when you will use it in most sessions. Register with:

```bash
claude mcp add <name> <command> <args>
claude mcp list
```

[^6]

**Action:** Run one full task in prompt-on-every-tool mode, watching every approval request. Identify two commands safe to allowlist and add them to `.claude/settings.json`. Then register one MCP server you will actually use and verify with `claude mcp list`.

---

## Module Summary

A properly configured Claude Code setup has three layers: installation verified against actual file-read and terminal-command capability; a lean `CLAUDE.md` that tells the assistant only what it cannot infer from code; and a permission model that starts conservative and relaxes deliberately as trust is established. MCP servers extend capability but should be added one at a time, only for tools used in most sessions. These defaults take under an hour to configure and pay compounding returns across every session that follows.

## Sources

[^1]: builder.io
[^2]: code.claude.com
[^3]: institute.sfeir.com
[^4]: codewithmukesh.com
[^5]: cosmicjs.com
[^6]: blog.gitbutler.com
