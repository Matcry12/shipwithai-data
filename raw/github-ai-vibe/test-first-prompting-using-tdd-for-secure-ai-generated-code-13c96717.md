---
source_url: "https://www.endorlabs.com/learn/test-first-prompting-using-tdd-for-secure-ai-generated-code"
source_domain: "endorlabs.com"
topic: "github-ai-vibe"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-29T13:38:33.781949+00:00"
word_count: 871
stage: "raw-extracted"
---

*This article is part of a 5-part series on secure code prompt patterns:*

*Design-Spec Prompt Pattern**Secure vs Insecure Diff Prompt Pattern**Anti-Pattern Avoidance Prompt Pattern**Toolchain-Aligned Prompt Pattern (coming soon)**Test-First Prompt Pattern (this blog)*

Context engineering techniques provide security teams a way to move from being enforcers who catch bugs late in the process to architects who embed security directly into the AI’s generative process.

Test-Driven Development (TDD) is an engineering best practice that can be a powerful prompting pattern to ensure code-level correctness and secure behavior before the AI even presents a solution to the developer.

## What is TDD (and why should security care)?

**Test-Driven Development (TDD)** is a process where the developer writes tests *before* writing any implementation code. While traditionally viewed as a tedious engineering task, TDD is experiencing a revival because AI removes the burden of writing the actual test code.

TDD is essential for secure prompting because it:

**Forces Upfront Threat Modeling:**You must define exactly what secure behavior looks like (such as specific encryption protocols) before the AI writes a single line of feature code.**Catches Hallucinations:**AI operates on token associations, not semantic logic; it can easily hallucinate a negation (e.g., using != instead of ==) that breaks a security check. A solid test layer catches these logic errors immediately.**Empowers the Human-in-the-Loop:**The developer shifts from a "coder" to a specification checker and validator.

## Implementing TDD with “Red, Green, Refactor”

In GitHub for Beginners: Test-driven development (TDD) with GitHub Copilot, Kedasha Kerr details the "Red, Green, Refactor" cycle, a concept originally championed by software researcher Kent Beck. It serves as the foundation for this prompt pattern:

**Red Stage:**Define the criteria for the function and ask the AI to generate the tests first. These tests will initially fail (or not even build) because the code doesn't exist yet.**Green Stage:**Ask the AI to create the implementation specifically to pass those tests.**Refactor Stage:**Refine the code for cleanliness and performance while running the tests to ensure the security logic remains intact.

## How to use the "Test-First" prompt pattern

This pattern is most effective when you use refinement-based prompting, which is iterating on an idea over multiple turns to inject security context.

### Step 1: Prompt for the tests (“red”)

Provide the AI with specific criteria, including security requirements like CWE (Common Weakness Enumeration) mitigations, and ask it to generate only the test functions.

**Example prompt:** *“I'm adding a new validator function called for usernames. Usernames must be 3-16 characters and start with a letter. Generate unit tests that check these criteria and specifically test for CWE-20 (Improper Input Validation). Just create the test functions.”*

### Step 2: Prompt for implementation (“green”)

Once the tests are established, ask the AI to generate the implementation code that satisfies them.

**Example prompt:** *“Review the tests you just generated. Now, create the implementation code that passes these tests and save it in a file called < insert name >. Ensure it uses secure libraries for any data processing.”*

### Step 3: Prompt for refinement (“refactor”)

After the code is functional (“green”), you must ensure it meets professional standards for maintainability and security hardening. This is where you optimize the logic and remove any hallucinated clutter while keeping your tests running to ensure the happy path remains secure.

**Example prompt:** *“The code now passes the tests. Now, refactor the implementation to follow the RORO (Receive an Object, Return an Object) pattern, add guard clauses at the top of the function for early returns on invalid inputs, and ensure all error messages are logged with structured context. I want you to mimic the style of this code: < insert sample code from the same project/directory >.”*

## The human-in-the-loop

As models improve, the role of the developer is evolving from a coder to a specification checker and validator. By using a Test-First approach, you are validating that the AI's "machine-driven intent" aligns with your "secure-by-design" requirements. Even a single line of hallucinated code can break a security protocol; TDD ensures that your test layer is solid enough to catch those hallucinations before they reach production.

## From prompts to policies: Rules and skills

To make your test-first workflow more reliable at scale, you can transition from individual prompts to a structured framework of rules (e.g., in .cursorrules or .mdc) and Skills (e.g. skill.md).

Rules act as your "always-on" foundational guardrails, enforcing mandatory security policies - such as the requirement that a failing test must precede any code - across every interaction in your repository.

While rules establish the policy, Skills provide the on-demand "active workflow knowledge" needed to perform specific security tasks, such as generating complex threat models or running deterministic validation scripts. Because skills utilize progressive disclosure, they load detailed instructions and resources only when the agent decides they are relevant to your current task, preventing context bloat while ensuring your TDD process is grounded in specialized expertise.

By combining these, you empower the human-in-the-loop to act as a specification architect, using rules to mandate the TDD process and skills to ensure every AI-generated feature is verified against professional security standards.

### What's next?

When you're ready to take the next step in securing your software supply chain, here are 3 ways Endor Labs can help: