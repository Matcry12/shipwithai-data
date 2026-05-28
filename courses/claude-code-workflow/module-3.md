# Module 3 — The Daily Loop: When to Delegate, When to Write Yourself

**Objective:** Build the instinct for which tasks belong with the assistant.

---

## Lesson 1: What to Hand Off Without Hesitation

The key question is: is this task *generative* or *decisive*? Generative work — boilerplate, test scaffolding, renaming symbols across files, translating a known pattern into code — costs you nothing to delegate. Decisive work — what the system does when data is missing, an irreversible write, a case where silent failure is worse than loud failure — requires your judgment.

A large fraction of daily coding is generative. "AI copilots accelerate development by generating boilerplate code, suggesting functions, and completing code blocks," including writing API endpoints, generating database queries, producing frontend components, and refactoring legacy code.[^1] These tasks slow you down without teaching you anything. Hand them off.

Multi-file refactors are another strong candidate. Claude Code "excels at agentic, autonomous coding tasks — multi-file edits, complex reasoning, computer use, and parallel sub-agent work. It's stronger when you want to delegate entire tasks, not just get suggestions."[^2] Let the assistant do the traversal; you do the review.

Unfamiliar files are a third category. "Understanding large codebases is a major productivity bottleneck. Claude Code can explain the data flows, identify the location of feature implementation, and highlight the dependencies and side effects."[^3] Before writing anything in a module you've never touched, ask Claude to summarize it. You will write better code faster with that context than without it.

Type definitions, test scaffolding, configuration files, data transfer objects, simple CRUD following established patterns — all of these fall into what one review framework calls "low risk (quick scan)" territory: "Check that conventions are followed and nothing obviously wrong is present. These are unlikely to introduce subtle bugs."[^4] If you are doing that work by hand, you are spending attention on the wrong thing.

**Action:** Audit the last five tickets you completed. Mark every task that was purely generative — boilerplate, scaffolding, renaming, summarizing an unfamiliar file. Those are your delegation candidates next sprint. Write them on a sticky note and keep it by your terminal.

---

## Lesson 2: What You Must Write Yourself

The assistant has no access to your production data. It does not know which migration already ran, or what your on-call history says about the edge case that took down the service last quarter. It will generate confident, fluent code that is completely wrong and not raise its hand to say so. There are tasks where you cannot safely accept that risk.

**Production-data effects.** Any code path that writes, migrates, or deletes production records requires you to understand every line. If you cannot explain what happens when the loop exits early or the foreign key constraint fires, you are not ready to merge it.

**Silent-corruption failure modes.** The most dangerous bugs are not the ones that throw. They are the ones that accept bad input, store it quietly, and surface the corruption three weeks later in a report no one can explain. Authentication flows, payment processing, PII handling — these are what the review framework calls "high risk (adversarial review)": "Review this code as if it were written by someone actively trying to introduce a vulnerability. Check every input validation, every error path, every assumption about trust boundaries."[^4]

**Anything you would be embarrassed to ship without understanding.** If a colleague asked you to walk through the logic and you could not, the code is not yours yet. Participants who relied on AI to debug or verify their code "scored poorly as a result."[^5] The assistant can help you understand; it cannot do the understanding for you.

There is also a category of tasks that are simply faster by hand. "Some tasks take longer to describe in a prompt than to just write. A three-line utility function, a simple config change, a one-line bug fix — just write it. Not everything needs to be delegated. The overhead of prompt → generate → review → verify isn't worth it for trivial changes."[^4]

**Action:** Before starting any task today, ask: "If this code misbehaves in production, can I diagnose it from first principles?" If yes, delegate freely. If no, write it yourself — or spend five minutes understanding the generated output before touching accept.

---

## Lesson 3: Structuring Prompts That Get Reviewable Output

"The bottleneck becomes your ability to clearly specify tasks and critically evaluate results. That's a different skill set, and frankly a more valuable one to develop."[^6] A vague prompt produces output that is hard to review. A structured prompt produces a diff you can evaluate against a clear spec.

Four elements make a prompt reviewable:

**1. Give context — the file, the situation, the existing pattern.**
"Claude can infer intent, but it can't read your mind. Reference specific files, mention constraints, and point to example patterns."[^7] "Add tests for foo.py" is unverifiable. "Write a test for foo.py covering the edge case where the user is logged out, avoid mocks" is not.[^7]

**2. Name the constraint explicitly.**
"Always specify the programming language, framework version, architectural patterns, any performance or security requirements, and parts that shouldn't change."[^3] If a constraint is not in the prompt, do not expect it in the output.

**3. Show one example of acceptable output.**
A function signature, a test name pattern, a comment style — ten seconds of example eliminates three rounds of correction.

**4. Ask for a plan before accepting.**
"Small prompts with iterative context led to a high success rate."[^8] Ask Claude to show what it would change before making edits. "If the AI proposes rewriting a huge amount of code, treat it as a red flag."[^8]

A 200-line generated change reviewed in thirty seconds is not reviewed — it is accepted blind. "AI-generated code must always be reviewed. The major areas to be focused on include the correctness and edge cases, security vulnerabilities, performance implications, and alignment with existing patterns."[^3] "AI coding tools are most useful when engineers treat them as fast typists, not architects. The judgment call still belongs to the person reviewing the diff."[^9] That judgment accrues only through reading diffs, not skimming them. "I've seen Claude: add dependencies I didn't ask for, use patterns that don't match my architecture, write code that works but isn't idiomatic."[^10]

**Action:** Pick one non-trivial task from your backlog. Write a prompt that names the file, states the constraint, shows one example of output format, and asks Claude to show a plan before executing. Compare the quality of that output to your last unstructured prompt.

---

## Module Summary

The daily loop is a skill in task classification. Delegate generative work — boilerplate, scaffolding, multi-file refactors, unfamiliar-file summaries — freely. Write yourself anything that touches production data, carries silent-corruption risk, or that you could not explain in a review. When you delegate, give context, name constraints, show an example, and ask for a plan first. Read every diff as if your name is on it — because it is. Trust builds through verification, never by skipping it.

## Sources

[^1]: teamvoy.com
[^2]: mindstudio.ai
[^3]: thoughtminds.ai
[^4]: frontendmasters.com
[^5]: anthropic.com
[^6]: turbogeek.co.uk
[^7]: code.claude.com
[^8]: docker.com
[^9]: 137foundry.com
[^10]: codewithmukesh.com
