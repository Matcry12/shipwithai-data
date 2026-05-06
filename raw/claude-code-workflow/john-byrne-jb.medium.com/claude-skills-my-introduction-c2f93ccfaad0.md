I have been steadily resisting the onslaught of AI, refraining from using it daily in my work life! Why? I felt I was still learning and it felt like my impostor syndrome would massively be exaggerated if I started using it!

One of the team made the leap and started using Claude Code and when I saw how they were doing I thought I had better start learning and seeing how I can use this new tool that everyone is talking about!

One of the things that upset me was the concept of "Prompt Engineering"! It felt like one of those terms where it simply contradicts itself! How can it be engineering if it is potentially different everytime for example:

```
Prompt 1:
Run a Trivy scan on this project and fix any vulnerabilities you find.

Prompt 2:
Run a Trivy scan on this project and fix any vulnerabilities you find, but only if a confirmed fixed version exists.
```

What are the differences I hear you cry! Well the first prompt gives Claude discretion, it may choose to fix transitive dependencies that might not have a fix simply by bumping to the latest version ie making an educated guess thereby acting and tell you after.

The second prompt constrains Claude to only act on what Trivy explicitly reports as a safe version. Anything without a fix may be logged and skipped so nothing is guessed and you have a more engineered solution.

It was at this point as I shared my frustration that I was told about Skills or as I am going to coin the phrase "Prompt Architecture". In my mind if prompt engineering is the craft of writing effective instructions then Skills are prompt architecture; ie creating a repeatable process, reusable by anyone on the team, can be version controlled and iterates from knowledge and experience.

A useful way is to think about the hierarchy:

![None](https://miro.medium.com/v2/resize:fit:700/1*e0MBeoihg5gaOXHk7D5Ucg.png)

#### Prompt Architecture

A prompt is a one-time idea. A Skill is a decision you've already made — encoded so you never have to make it again.

Think about what that actually means at scale. A prompt lives in someone's head, or buried in a Slack message, or copy-pasted into a notes app. It works once, for one person, in one context. The next time a similar problem surfaces — different team member, different repo, different sprint — someone starts from scratch. That's not engineering. That's your business memory leaking out of your organisation one conversation at a time.

A Skill changes that contract. When you build one properly, you're not just writing instructions for Claude — you're **capturing a decision about how your team solves a type of problem**. The guardrails encode the hard-earned experience. The Skill or Skills encode your agreed process. The argument handling makes it accessible to anyone, not just the person who wrote it.

That's the architectural shift: from *"here's what I told Claude"* to *"here's how we do this"*.

### What this gives you that prompts never can

**Reliability.** The same Skill, run by different people against different repositories, follows the same logic, applies the same constraints, and makes the same category of decisions. The outcome won't be identical — the input varies — but the *behaviour* is consistent.

**Predictability.** With a raw prompt, you're at the mercy of how Claude interprets your intent on any given run. A well-structured Skill removes that surface area. The steps are ordered. The guardrails are explicit. The edge cases are handled. You can reason about what it will do before you run it.

**Institutional knowledge.** This is the one most teams underestimate. The Trivy Skill I'll show you in a moment wasn't written in one sitting — it was written, run, broken, fixed, and tightened over multiple iterations. That iteration *is* the value. Every guardrail in that Skill exists because something went wrong without it. That knowledge now lives in the Skill, not in my head. New team member? Same Skill. Six months later? Same Skill. You're not starting from scratch — you're standing on what you learned.

**Version control.** A Skill is a file. It lives in your repository. It has a commit history. You can review it, roll it back, raise a PR against it. You can track *why* a guardrail was added three months ago. Try doing that with a prompt you typed into a chat window.

#### Skills compound; prompts don't

The most important thing to understand is that Skills aren't static; they get better. Every time a Skill hits an edge case you hadn't considered, you update it — and that improvement is immediately available to everyone who uses it. The Skill your team runs in six months will be sharper than the one you write today, and it will carry the scar tissue of every failure along the way.

Prompts reset to zero. Architecture accumulates.

That's why I think of this as Prompt Architecture rather than Prompt Engineering. Engineering implies craft applied once. Architecture implies something you build, inhabit, extend, and hand down.

#### The Anatomy of a Skill

A Skill is a structured, reusable prompt packaged for repeatable execution — think of it as a function, not a one-liner.

Skills can be broken down into 4 key elements:

* YAML Formatter — This is the metadata that describes and configures the Skill. Unlike the other anatomy parts it is optional, leaving it out doesn't impact how the Skill runs. In this section you can simply define the following **description** — shown in Skill pickers and previews,
  **argument-hint** — hints the expected input format to the user,
  **allowed-tools** — restricts which tools Claude may invoke.

```
Example:
---
description: Runs a Trivy CVE scan,
  fixes Maven and NPM deps, and
  raises a PR with results logged
  to CHANGELOG.md
argument-hint: [github-repo-url]
allowed-tools: Bash
---
```

* Environment Setup — Argument handling and working context. The first thing the Skill does — establish *where* it's operating. The special variable `$ARGUMENTS` captures anything the user passed when invoking the Skill. This block handles both cases: argument provided or not. Every subsequent step operates on the resolved context, so getting this right is critical. Common patterns: clone a repo URL, load a file path, set a target environment, or default to the current directory.

```
Example:

## Setup
- If $ARGUMENTS is provided,
  treat it as a GitHub repo URL:
  - git clone $ARGUMENTS
  - cd into cloned directory
- If no argument provided,
  use current working directory
```

* Main Task Body — Ordered steps that define what the Skill will actually do. The core of the Skill. Written as numbered steps so Claude executes them sequentially and in order. Each step should have a clear single responsibility. Good steps include: what to run, what to do with the output, when to skip, and when to stop and ask the user. Steps can reference each other's outputs — e.g. "parse the file from Step 1" — giving the Skill memory across its own execution.

```
Example:

## Step 1 - Run Trivy scan
Run command, output to JSON.
If tool missing: stop + instruct.

## Step 2 - Triage results
Parse output. If none: stop.
Log findings to CHANGELOG.md.
Split by ecosystem.

## Step 3 - Fix Maven CVEs
...

## Step N - Create PR
Push branch, raise PR.
```

* Rules/Guardrails — This is how the developer constrains the behaviour across all steps. A flat list of constraints that apply globally — not tied to any single step. They act as a safety layer, catching edge cases the step logic might not explicitly cover. Good guardrails are: things Claude might otherwise infer or guess at incorrectly, destructive actions that need an explicit block, and confirmations required before high-impact operations. Without guardrails, an otherwise well-written Skill can still produce unexpected behaviour at the edges.

```
Example:

## Important rules
- Never delete dependencies,
  only version bumps
- Never guess a fixed version,
  only use Trivy output
- Warn user before --force
  and show diff
- Confirm with user before
  pushing if 5+ deps changed
- Never push if Step 5
  was aborted
```

So let me walk you through an example that frustrates me and I daresay a lot of developers — CVE management!

Identify a repeatable issue, in this case what I want to achieve is:

* A repeatable task to run against a github repo to identify CVEs* Use Trivy to identify the CVEs* Fix the CVEs, create and push a pr for review by the team

#### The Final Skill:

```
Here's how those four elements come together in practice.
```

This Skill didn't come out right first time. It was run, broken, and tightened across several iterations — and every guardrail in it marks a mistake that won't happen twice. That's the model. Find a repeatable problem, build the Skill, and let failure make it better. The prompt you wrote today gets forgotten. The Skill you committed today gets inherited.
