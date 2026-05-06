---
source_url: https://www.deployhq.com/blog/how-to-use-git-with-claude-code-understanding-the-co-authored-by-attribution
title: "How to Use Git with Claude Code: Commands, Commits and Tips"
crawl_depth: 0
crawled_at: 2026-05-05T14:26:31Z
word_count: 2303
---

# How to Use Git with Claude Code: Commands, Commits and Tips
By Facundo F · Updated on 12th April 2026
[AI](https://www.deployhq.com/blog/category/ai), [Devops & Infrastructure](https://www.deployhq.com/blog/category/devops-infrastructure), [Git](https://www.deployhq.com/blog/category/git), and [News](https://www.deployhq.com/blog/category/news)
![How to Use Git with Claude Code: Commands, Commits and Tips](https://blog.deployhq.com/attachment/fef0dc94-bc3a-40e8-8f04-2f282349520f/thumb1400.jpg)
Claude Code turns your terminal into a Git-aware coding partner. It reads your repository history, understands diffs, generates context-aware commit messages, resolves merge conflicts, and creates pull requests — all through natural language. This guide covers the practical Git operations you can perform with Claude Code, from everyday commits to advanced workflows, and how to integrate everything into an automated deployment pipeline with [DeployHQ](https://www.deployhq.com).
## Setting Up Git with Claude Code
### Install Claude Code
Ensure you have Node.js 18 or higher installed, then install Claude Code globally:

```
npm install -g @anthropic-ai/claude-code

```

### Authenticate and Verify Git Integration
Launch Claude Code in your terminal inside any Git repository:

```
cd /path/to/your/project
claude

```

Follow the prompts to authenticate with your Anthropic account. Once inside, verify Git integration works by typing a natural language request:

```
Show me what files have changed

```

Claude reads your working tree, staged changes, and recent history automatically. No additional Git plugins or configuration are required — if `git` is available in your PATH, Claude Code will use it.
## Essential Git Operations with Claude Code
This is where Claude Code shines in day-to-day development. Rather than memorising flags and options, you describe what you want in plain English.
### Creating Commits
Claude analyses your staged changes and recent commit history to generate messages that match your project's conventions. A few example prompts:
  * **"Commit these auth changes"** — Claude inspects the diff, identifies it as authentication-related, and writes a descriptive message 
  * **"Create a commit following conventional commits"** — Claude formats the message as `feat:`, `fix:`, `refactor:`, etc., based on the actual changes 
  * **"Commit with a detailed body explaining the security implications"** — Claude adds a multi-line body explaining why the change was made 


If you use [Conventional Commits](https://deployhq.com/blog/conventional-commits-a-standardized-approach-to-commit-messages), add a rule to your project's `CLAUDE.md` file and Claude will follow that format automatically for every commit.
### Resolving Merge Conflicts
Instead of manually editing conflict markers, describe the situation:
  * **"Help me resolve these merge conflicts on the feature branch"** — Claude reads the conflicting files, understands both sides, and proposes a resolution 
  * **"Resolve the conflicts in src/auth.ts keeping our version of the login timeout"** — Claude applies your preference while integrating non-conflicting changes from the other branch 
  * **"Show me what's conflicting and explain each conflict"** — Claude breaks down each conflict with context about what each side changed and why 


Claude handles rebase conflicts the same way. During an interactive rebase, if conflicts arise at any step, you can ask Claude to resolve them while preserving the intent of both change sets.
### Managing Branches
Branch operations become conversational:
  * **"Create a feature branch for the new payment integration"** — Claude runs `git checkout -b feature/payment-integration` (or your team's naming convention if specified in CLAUDE.md) 
  * **"Which branches have unmerged work?"** — Claude lists branches with their last commit dates and descriptions 
  * **"Delete all branches that have been merged into main"** — Claude identifies safe-to-delete branches and removes them 
  * **"Switch to the branch that has the auth refactor"** — Claude finds the right branch by searching commit messages and branch names 


### Working with Pull Requests
Claude Code integrates with GitHub's CLI (`gh`) to create and manage pull requests:
  * **"Create a PR for this feature branch with a summary of changes"** — Claude analyses all commits on the branch, generates a title and description covering the what and why, and opens the PR 
  * **"Update the PR description with the latest changes"** — Claude amends the description after additional commits 
  * **"What feedback is on my open PR?"** — Claude fetches review comments and summarises them 


For tips on structuring effective PRs, see our guide to [the perfect pull request](https://deployhq.com/blog/the-perfect-pull-request-best-practices-for-collaborative-development).
### Searching Git History
Git archaeology is one of Claude Code's strongest capabilities. Many engineers at Anthropic report this as one of the most valuable features:
  * **"Find when the login timeout was changed from 30 minutes to 15"** — Claude searches through commit diffs to pinpoint the exact commit 
  * **"What commits touched the auth module this week?"** — Claude filters history by path and date range 
  * **"Why was the caching layer redesigned in v2.1?"** — Claude reads commits, PR descriptions, and code comments to reconstruct the reasoning 
  * **"Who changed the deployment config last and what did they change?"** — Claude traces authorship through `git log` and `git blame`
  * **"What changes made it into the v1.2.3 release?"** — Claude compares tags and summarises the changelog 


### Rebasing and Cherry-Picking
For more advanced Git workflows:
  * **"Rebase this branch onto main and squash the WIP commits"** — Claude performs the rebase, identifies which commits are work-in-progress, and squashes them into logical units 
  * **"Cherry-pick the database migration fix from the hotfix branch"** — Claude identifies the specific commit and applies it to your current branch 
  * **"Clean up my commit history before merging — squash the fixup commits"** — Claude performs an interactive rebase, combining related commits 


## Advanced Git Workflows
### Git Worktrees with Claude Code
Git worktrees let you check out multiple branches simultaneously in separate directories. Claude Code can work within worktrees for parallel development:
  * **"Set up a worktree for the hotfix branch in ../hotfix-dir"** — Claude creates the worktree and switches context 
  * **"Compare my current changes with what's in the hotfix worktree"** — Claude diffs across worktrees to prevent duplicate work 


Worktrees are particularly useful when you need to context-switch between a feature branch and an urgent fix without stashing uncommitted work.
### GitHub Actions Integration
Claude Code can help you write, debug, and optimise CI/CD workflows:
  * **"Create a GitHub Actions workflow that runs tests on push and deploys on merge to main"** — Claude generates a `.github/workflows/deploy.yml` with proper job dependencies 
  * **"Why is the CI pipeline failing?"** — Claude reads the workflow file alongside recent error logs to diagnose issues 
  * **"Add a caching step for node_modules to speed up the build"** — Claude modifies the workflow with the correct cache key configuration 


For teams using [DeployHQ](https://www.deployhq.com) alongside GitHub Actions, Claude can help configure webhooks that trigger [automatic deployment from Git](https://www.deployhq.com/features/automatic-deployments) after CI passes.
## Understanding Co-Authored-By Attribution
When Claude Code creates a commit on your behalf, it adds attribution to the commit message by default:

```
fix: resolve authentication bug in login flow

Fixes the issue where users were being logged out unexpectedly
after session timeout.

Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>

```

GitHub recognises the `Co-Authored-By` trailer format and displays Claude in the co-authors list for that commit. This makes it visible when reviewing history or pull requests that AI assistance was used.
### The Case for Keeping Attribution
**Transparency and accountability.** Many organisations value knowing how their code was written. The attribution creates a clear audit trail.
**Quality signals for maintainers.** Open source maintainers find disclosure helpful — knowing AI was involved helps them assess how much scrutiny to give a PR and whether they are coaching a human contributor or reviewing AI-generated output.
**Compliance.** Some regulated industries require disclosure of AI tool usage. The European Union's AI Act includes transparency provisions around AI systems.
### The Case for Disabling Attribution
**Commit message standards.** Strict commit conventions may not accommodate attribution lines, and the extra text can conflict with tooling that parses commit messages.
**Tool vs. collaborator philosophy.** Some developers view AI as a tool (like an IDE or linter), not a co-author. The human who directs, reviews, and approves the code is the true author.
**Clean history.** For some projects, keeping the commit history focused purely on code changes is a priority.
### How to Configure Attribution
The settings file is located at:
  * **macOS/Linux:** `~/.claude/settings.json`
  * **Windows:** `%APPDATA%\claude-code\settings.json`


To **disable** the co-authored-by attribution:

```
{"includeCoAuthoredBy":false,"gitAttribution":false}
```

To **keep** the attribution (which is the default):

```
{"includeCoAuthoredBy":true}
```

**What each setting controls:**
  * **`includeCoAuthoredBy`**: Controls the" Co-Authored-By: Claude" line in commit messages 
  * **`gitAttribution`**: Disables all forms of Git attribution, including the" Generated with Claude Code" line 


### Project-Level Configuration
You can also configure these settings at the project level for team-wide consistency:
  * `.claude/settings.json` — Checked into source control, shared with your team 
  * `.claude/settings.local.json` — Not checked in, useful for personal preferences 


This is particularly useful when different projects have different requirements — perhaps your open source contributions need attribution while your internal projects do not.
### Using CLAUDE.md for Additional Control
Include Git commit instructions in your project's CLAUDE.md file (an [AI coding config file](https://deployhq.com/blog/ai-coding-config-files-guide)) to guide Claude's behaviour:

```
## Git Commit Guidelines

When creating commits:
- Follow conventional commit format
- Keep the first line under 50 characters
- Do not include AI attribution in commit messages

```

## Deploying Git Changes with DeployHQ
Once Claude Code has committed and pushed your changes, the next step is getting that code onto your servers. [DeployHQ](https://www.deployhq.com) connects directly to your Git repository and deploys automatically — creating a seamless workflow from AI-assisted development to production.
The typical flow looks like this:

```

Claude Code commits & pushes
GitHub/GitLab receives push
DeployHQ webhook triggers
Build pipeline runs
Code deployed to server

```

When you [deploy from GitHub](https://www.deployhq.com/deploy-from-github) through [DeployHQ](https://www.deployhq.com), every push to your main branch can trigger an automatic deployment. Combined with [build pipeline integration](https://www.deployhq.com/features/build-pipelines) for asset compilation, testing, and other pre-deployment steps, you get a complete CI/CD workflow without leaving your terminal.
Claude Code handles the Git side (commits, branches, PRs), and [DeployHQ](https://www.deployhq.com) handles the deployment side (builds, transfers, rollbacks). Together, they eliminate manual steps between writing code and shipping it.
## Best Practices for Git Workflows with Claude Code
**Review Claude's commits before pushing.** Always inspect the commit messages and diffs Claude generates. You are ultimately responsible for the code that goes into your repository. A quick `git log --oneline -5` and `git diff HEAD~1` before pushing catches mistakes early.
**Configure CLAUDE.md with your Git conventions.** Specify your branch naming convention, commit message format, protected branches, and any project-specific rules. Claude reads this file on every session and follows the instructions consistently.
**Make smaller, focused commits.** Rather than large multi-purpose commits, smaller ones allow Claude to generate more precise commit messages and make your history easier to bisect when debugging.
**Use descriptive branch names.** Names that indicate the purpose of changes help Claude understand context when creating PRs or analysing branches.
**Specify commit conventions explicitly.** If you use Conventional Commits or another standard, tell Claude to follow it. This improves the readability and structure of your project history.
**Leverage Claude for git archaeology.** Claude excels at searching through history. Use it to answer questions about past changes, understand why decisions were made, or find when bugs were introduced.
**Use /compact for large repositories.** When working in repos with extensive history or many files, the `/compact` command helps Claude manage context efficiently without losing track of your project structure.
## Frequently Asked Questions
### How do I disable the co-authored-by attribution?
Set `"includeCoAuthoredBy": false` and `"gitAttribution": false` in your `~/.claude/settings.json` file. For project-specific control, use `.claude/settings.json` in your repo root. You can also add explicit instructions in your project's CLAUDE.md file as a fallback.
### Can Claude Code resolve merge conflicts?
Yes. Claude reads both sides of a conflict, understands the intent behind each change, and proposes a resolution. You can guide it with preferences like "keep our version of the timeout value" or "combine both implementations". It works for both merge and rebase conflicts.
### Does Claude Code work with GitHub, GitLab, and Bitbucket?
Claude Code works with any Git hosting provider. It interacts with Git directly through the command line. For GitHub-specific features like pull requests, it uses the `gh` CLI. GitLab and Bitbucket equivalents (`glab`, Bitbucket CLI) can be used similarly through natural language prompts.
### How does Claude Code handle large repositories?
Claude Code reads your repository structure and file contents on demand rather than loading everything into memory. For very large repos, use the `/compact` command to help manage context. You can also scope Claude's focus to specific directories or files when working on localised changes.
### Can Claude Code create pull requests?
Yes. Ask Claude to "create a PR for this branch" and it will analyse the commit history, generate a descriptive title and body, and open the PR using the GitHub CLI. It can also update PR descriptions, respond to review comments, and summarise feedback.
### Can I customise what the attribution message says?
The default format is set by Claude Code and cannot be directly customised through settings. However, you can use Git hooks or CLAUDE.md instructions to control how Claude formats commit messages. Some developers configure Claude to set itself as the full commit author rather than co-author using Git environment variables.
### How do other AI coding tools handle attribution?
Different tools take different approaches. Aider adds "(aider)" to the author name and includes the model as a co-author. GitHub Copilot does not add automatic attribution. There is no universal standard, so teams often establish their own conventions for AI disclosure.
* * *
Ready to automate your deployment workflow? [Sign up for DeployHQ](https://www.deployhq.com/signup) and connect your Git repository to deploy code to your servers automatically — every time you push.
For questions or support, reach out at support@deployhq.com or find us on 
Written by
### Facundo F
Facundo | CTO | DeployHQ | Continuous Delivery & Software Engineering Leadership - As CTO at DeployHQ, Facundo leads the software engineering team, driving innovation in continuous delivery. Outside of work, he enjoys cycling and nature, accompanied by Bono 🐶.
