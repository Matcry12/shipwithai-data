---
source_url: https://cuong.io/blog/2025/06/09-a-commit-message-prompt
crawl_depth: 0
crawled_at: 2026-05-05T14:26:31Z
word_count: 493
---

Here is a prompt you can use to generate a commit message with a LLM. I wrote this prompt for Claude Code, but it’s generic enough that you should be able to use it with other LLMs.
## The Prompt

```

Your task is to help the user to generate a commit message and commit the changes using git.


## Guidelines

- DO NOT add any ads such as "Generated with [Claude Code](https://claude.ai/code)"
- Only generate the message for staged files/changes
- Don't add any files using `git add`. The user will decide what to add. 
- Follow the rules below for the commit message.


## Format

```
<type>:<space><message title>

<bullet points summarizing what was updated>
```

## Example Titles

```
feat(auth): add JWT login flow
fix(ui): handle null pointer in sidebar
refactor(api): split user controller logic
docs(readme): add usage section
```

## Example with Title and Body

```
feat(auth): add JWT login flow

- Implemented JWT token validation logic
- Added documentation for the validation component
```

## Rules

* title is lowercase, no period at the end.
* Title should be a clear summary, max 50 characters.
* Use the body (optional) to explain *why*, not just *what*.
* Bullet points should be concise and high-level.

Avoid

* Vague titles like: "update", "fix stuff"
* Overly long or unfocused titles
* Excessive detail in bullet points

## Allowed Types

| Type     | Description                           |
| -------- | ------------------------------------- |
| feat     | New feature                           |
| fix      | Bug fix                               |
| chore    | Maintenance (e.g., tooling, deps)     |
| docs     | Documentation changes                 |
| refactor | Code restructure (no behavior change) |
| test     | Adding or refactoring tests           |
| style    | Code formatting (no logic change)     |
| perf     | Performance improvements              |


```

## Usage
### Claude Code
  * Create a file called `~/.claude/commands/gen-commit-msg.md`
  * Copy the content from [git-commit-message.md](https://raw.githubusercontent.com/thecodecentral/prompt-library/refs/heads/main/general/git-commit-message.md) into that file
  * Go the directory where you want to commit your changes
  * Run `claude`
  * Inside of Claude Code, type `/user:gen-commit-msg`


That’s it.
Also see [Slash Commands](https://docs.anthropic.com/en/docs/claude-code/cli-usage#slash-commands).
### Claude Code - One-Liner
I wish Anthropic will add an option so that even in non-interactive mode, Claude Code can still prompt for additional permissions. For now, you need to open the REPL to generate a commit message.
If you are brave enough to allow Claude Code to run the commit command, you can use the following to generate a message and commit in one line:

```
cat ~/.claude/commands/gen-commit-msg.md | claude --allowedTools 'Bash(git commit -m:*)'
```

Personally, I prefer to review the commit message so I don’t use this one-liner.
If you run into this error:
_Error: Raw mode is not supported on the current process.stdin, which Ink uses as input stream by default._
You need to run claude at least once in the current directory and grant permission.
## Conlusion
This prompt can also be used with Cursor or GitHub Copilot.
See


Loading comments…
