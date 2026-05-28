# Module 4 — Code Review with AI: Self-Review and PR Review

Code review is where bugs get caught, standards get enforced, and engineering judgment gets exercised. AI assistants don't replace that judgment — but they absorb the mechanical first pass so you arrive at judgment calls faster and with sharper context. This module covers self-review before push, incoming PR triage, and where AI review cannot substitute for human expertise.

---

## Lesson 4.1 — Self-Review Before You Push

Before you open a pull request, ask the assistant to read your diff and act as a first reviewer. Run the review in parallel sub-tasks so each concern stays isolated. Here is a prompt structure adapted from terminal review practice[^1]:

```
Run the following steps in parallel with a generic subagent for each one.
1. Run tests on the files in my current commit. Summarize the broken tests
   in an easy to read format so I can go and debug.
2. Run lint on the files in my current commit. Summarize the failed lints
   in an easy to read format so I can go and debug.
3. Review the code in the commit - List the top 5 things we could do to
   improve it ranked by criticality and level of effort.
```

Parallelising keeps context clean and gives you three focused outputs instead of one overloaded summary. The third sub-task surfaces type mismatches, unhandled error paths, and missed edge cases — exactly what slips past an author's eyes after hours on the same code.

"AI catches issues before they integrate deeper into the system, reducing costly fixes later."[^2] Catching a null-check problem in self-review takes thirty seconds; catching it in a production incident takes an afternoon.

Keep the ask concrete: ask for the top five issues ranked by criticality, not an exhaustive list. Ask targeted questions — "Is the error handling solid on the payment path?" "What edge cases am I missing for empty input?" — and treat every flagged item as a question, not a verdict. Push only when you have resolved or consciously deferred each one.

**Action:** Before your next push, run a parallel three-sub-task review (tests, lint, code review). Resolve every critical or high-effort item before opening the PR.

---

## Lesson 4.2 — Reviewing Incoming PRs

Much of PR review time goes to orientation: reading changed files, tracing call paths, understanding why a change was structured a particular way. AI compresses that dramatically.

When you run `/pr <url>` and ask a focused question, "Claude Code fetches the diff, review comments, and CI status, then reads the changed files in their full repository context."[^3] That full-context read means the assistant understands what changed functions do elsewhere in the codebase, not just inside the diff.

Start with a summary request: "Summarize this PR: what changed, why it changed, and what could go wrong." That loads a mental model before you read a line of code. Then ask targeted risk questions:

- "List the branches in the new code that have no test coverage."
- "Does the error handling here match the patterns used in the rest of this module?"
- "Are there inputs that could cause this to fail silently?"
- "Is there anything in this diff that changes public API surface without updating callers?"

The value is in focused questions, not a comprehensive verdict. "By handling trivial, repetitive tasks automatically, these tools enable reviewers to focus their efforts on providing meaningful, actionable feedback to improve overall code quality."[^4] Let the assistant handle summarization and pattern-matching; you handle questions that require knowing your system and your product's constraints.

The same capability applies to your outgoing work. "Claude Code analyzes staged changes, understands the intent across multiple files, and produces a structured PR description."[^5] A well-structured description — summary, list of changes, testing notes — makes your reviewer's job easier before they ever open the diff.

**Action:** Take the next PR in your queue. Before reading the diff, run `> /pr <url>` and ask for a summary and a list of untested branches. Note how your reading of the diff changes when you arrive with that context.

---

## Lesson 4.3 — What AI Review Misses (And Why You Still Own Approval)

Understanding what AI review does well makes it easy to over-trust it. The failure modes are specific and consequential.

**Domain invariants.** Your system has rules that live nowhere in the code — constraints established in incident retrospectives, unwritten agreements about data contracts, business rules that exist only in institutional memory. "Code review for AI-assisted work carries a higher bar — not because the tools are unreliable, but because they lack your team's tacit knowledge. They don't know about the edge case that caused last quarter's incident. They don't know about the performance constraint buried in a comment six files away."[^6] The assistant cannot flag a violation of a rule it has never seen written down.

**Performance regressions tied to production data shape.** A function that runs in 2ms on test fixtures may run in 8 seconds on production data with a different cardinality. An N+1 query is invisible to static analysis if the loop is short in tests. AI review looks at code structure; it does not simulate your production data distribution.

**Business-logic security.** Authorization logic and access-control boundaries can be syntactically clean, pass all tests, and still be wrong in ways that only someone who understands the business model can catch. An AI tool will check that you called the auth function — not whether you called the *right* one for this user role in this context.

**Stale training data.** "The code won't raise its hand and say 'by the way, I'm using a deprecated endpoint.' It'll look perfectly confident and be perfectly wrong."[^7] Models trained before a major API overhaul validate code against the old API with complete confidence.

The right mental model: "AI coding tools are most useful when engineers treat them as fast typists, not architects. The judgment call still belongs to the person reviewing the diff."[^6]

Structure your review in two passes. First pass: AI flags mechanical issues — null checks, untested branches, style violations. Second pass: human review on what AI cannot see — business invariants, real-load performance, security correctness in context.

"Human reviewers should focus their unique cognitive abilities on complex logic, architectural soundness, and potential edge cases."[^8] AI review is the first pass. It is never the final approval.

**Action:** Write down three invariants for a system you own that exist nowhere in the code — rules from past incidents, unwritten data contracts, business constraints. Keep that list as a manual checklist alongside your review workflow.

---

## Module Summary

AI-assisted code review accelerates orientation and pattern-matching: reading diffs, tracing call paths, identifying untested branches, flagging missing error handling. Use it as a disciplined first pass — parallel sub-tasks before you push; focused risk questions on incoming PRs. The speed gain is real. The ceiling is equally real: domain invariants, production-data performance, business-logic security, and post-training API changes remain invisible to the tool. The approval is always yours.

## Sources

[^1]: hamy.xyz
[^2]: codemag.com
[^3]: support.claude.com
[^4]: daily.dev
[^5]: sitepoint.com
[^6]: 137foundry.com
[^7]: frontendmasters.com
[^8]: group107.com
