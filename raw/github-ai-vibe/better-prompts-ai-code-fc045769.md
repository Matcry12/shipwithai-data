---
source_url: "https://graphite.com/guides/better-prompts-ai-code"
source_domain: "graphite.com"
topic: "github-ai-vibe"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-29T13:37:53.511776+00:00"
word_count: 1425
stage: "raw-extracted"
---

# Table of contents

- Be specific with language and requirements
- Include examples and constraints
- Break down complex tasks and iterate
- Avoid common prompting pitfalls
- [Graphite Agent: AI code review for quality and consistency](#graphites-Graphite Agent-ai-code-review-for-quality-and-consistency)

Large language models (LLMs) can generate code in many programming languages, but the quality of their output depends heavily on how you prompt them. Crafting a precise prompt can be the difference between hours of debugging and a seamless implementation. The key is to clearly communicate your intent and requirements, because an AI doesn't inherently know your goals – it only follows the patterns described in your prompt. This guide introduces language-agnostic prompt engineering techniques to help both beginners and experienced developers get more accurate and useful code from AI. We'll illustrate each technique with examples of weak vs. improved prompts to show how small changes can yield better results. For a deeper dive into how AI code review works, see our guide on AI code review.

### Be specific with language and requirements

The first rule of prompt engineering for code is to be specific about what you want. Vague prompts yield vague (often incorrect) results. Always mention the programming language, the task or algorithm, and any requirements or constraints. For example, consider asking an AI to generate a sorting algorithm:

**Weak prompt:**"Write a sorting algorithm."**Improved prompt:**"Write a**Python**implementation of**merge sort**optimized for**memory efficiency**, including**time complexity analysis**and**error handling**for edge cases (e.g. empty arrays)."

The improved prompt is much clearer. It specifies:

- The programming language (Python) and specific algorithm (merge sort).
- The optimization goal (memory efficiency) and required output details (time complexity analysis).
- Error handling expectations and an edge case to consider (empty arrays).

By spelling out these details, you greatly reduce ambiguity. Microsoft's Developer Tools research group observed that prompts with explicit specifications reduced the need for back-and-forth refinements by 68%. In practice, this means the AI is more likely to produce correct, ready-to-use code on the first try.

Being specific also means providing technical context when relevant. If certain constraints matter – such as the target environment, API version, performance or security requirements – include them in the prompt. For instance, specify "Node.js 18 server environment" or "Python 3.10+" if it matters. Otherwise, the model might generate code that is technically correct but not suitable for your situation.


Tip:AI code review tools like Graphite Agent can help enforce technical requirements and catch missing context.

### Include examples and constraints

Another powerful technique is to provide examples or test cases in your prompt. Examples act as implicit constraints, guiding the model toward the format or behavior you expect. For instance, if you want a function with a specific signature or output format, show a snippet of that.

Imagine you need an email validation function. A weak prompt might just say, "Validate an email address." An improved prompt would describe requirements and give a usage example, e.g.:


Prompt:"Create a TypeScript function`validateEmail(email: string): {isValid: boolean; message: string}`

that checks if an email is RFC-5322 compliant and rejects disposable domains. For example, if the input is`"test@tempmail.com"`

, it should return an object like`{ isValid: false, message: 'Disposable domain not allowed' }`

."

In this improved version, the prompt lists specific rules (RFC compliance and no disposable domains) and provides a clear function signature and an example of expected output. This gives the AI a template to follow and boundaries to respect. As Dr. Rachel Thomas of fast.ai notes, *"examples in prompts serve as implicit constraints that guide the model toward the desired output format."* By including a small example or an outline of the output, you help the model understand exactly what you want.

### Break down complex tasks and iterate

If your desired output is complex, avoid requesting everything in one huge prompt. It's often better to break down a complex task into smaller steps or use an iterative approach. Large models can handle reasonably detailed prompts, but asking for a full application in one go is likely to produce a convoluted or partial answer. Instead, tackle complex tasks in stages and possibly across multiple prompts:

**Decompose the problem:**Outline sub-tasks in separate prompts (e.g. first define the data model, then the API endpoints, then the UI components). This ensures each part is handled with focus.**Use step-by-step reasoning:**You can actually instruct the model to "think step by step." For example: "I need a JavaScript function to find the longest increasing subsequence in an array. Let's solve this step by step: first explain the concept, then choose an algorithm (greedy vs DP), then write the code, then analyze complexity." By embedding this reasoning process in the prompt, you encourage the AI to work through the problem methodically.**Iterate with the AI:**Treat the AI's first output as a draft. Review it, then issue follow-up prompts to refine the code.

By breaking prompts into smaller pieces or sequential turns, you make it easier for the model to comply at each step. You also get opportunities to catch mistakes early and steer the output in the right direction. Remember that you can carry context between prompts (in a chat-based LLM) – use that to your advantage for iterative improvement.

For more information on integrating AI into your code review workflow and how to review code written by AI, these guides offer practical advice for iterative, AI-assisted development.

### Avoid common prompting pitfalls

While applying the above techniques, watch out for a few common mistakes that can undermine your results:

**Under-specifying the task:**Don't assume the AI "knows" what you intended. If a prompt is too minimal, the model might solve the wrong problem or omit important features. Always double-check that your prompt fully describes the problem.**Ignoring context or constraints:**Failing to mention the operating environment, framework, or performance/security constraints can result in code that doesn't fit your project needs. Also make sure to include any version requirements or security considerations. Without this, you might get code that technically works but is impractical or unsafe for your use case. The more context you give, the more relevant the output.**Over-reliance on AI without verification:**Even with good prompts, AI-generated code isn't guaranteed to be perfect. The model might produce subtle logic bugs, use deprecated APIs, or just take an unconventional approach. Never merge AI-written code into production without reviewing it. Treat the AI as a coding assistant, not an infallible coder. Write prompts that encourage best practices (like asking for safe, idiomatic code), and always test and review the output thoroughly. Using linters or static analysis on AI code is also a smart safeguard.


To compare approaches:This guide, Automated vs. manual code reviews: Finding the right balance, explores the strengths and limitations of both, and how to combine them for best results.

By avoiding these pitfalls, you ensure that prompt engineering remains a helpful aid rather than a source of technical debt. Prompting is an iterative learning process – over time, you'll learn which clarifications or extra details yield better code from your preferred LLM.

### Graphite Agent: AI code review for quality and consistency

Writing a good prompt is the first step, but ensuring the quality and consistency of AI-generated code is the next challenge. This is where tools like Graphite Agent come in. Graphite Agent is an AI-powered code review assistant that provides immediate, context-aware feedback on code changes – including those written by an AI. It hooks into your development workflow (e.g. reviewing pull requests) and flags issues ranging from logic bugs and security vulnerabilities to style violations and missing documentation. Graphite Agent uses your repository's context and even custom rules you define to give relevant suggestions. For example, you can configure Graphite Agent with your project's style guide or common AI mistakes to watch for, and it will catch those patterns in AI-generated code before a human reviewer even sees them.

![screenshot of Graphite Agent comment](/images/content/guides/better-prompts-ai-code/sample-Graphite Agent-comment.png)

By incorporating a tool like Graphite Agent in your workflow, you add an extra layer of scrutiny for AI-produced code. It helps ensure the code meets your team's quality standards and is consistent with the rest of your codebase. In practice, Graphite Agent can automatically identify edge cases the AI missed, point out performance issues, and even suggest fixes – all of which saves human reviewers time and instills confidence in using AI-generated code. Remember, prompt engineering and AI coding tools are most effective when paired with robust review practices. Graphite Agent bridges that gap by reviewing AI code for you, so you can safely harness AI code generation while maintaining high code quality and consistency.