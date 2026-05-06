---
title: "Agentic Coding: Making Developers More Productive with AI"
topic: "claude-code-workflow"
career_level:
  - senior
source_url: "https://ed-wentworth.medium.com/how-im-using-agentic-coding-with-claude-and-cursor-in-real-world-projects-b4b6694c132d"
source_domain: "ed-wentworth.medium.com"
word_count: 890
text_to_link_ratio: 0.8532
signal_score: 0.8532
is_curated: false
tags:
  - remote
  - open-source
  - senior
ingested_at: "2026-05-05"
---


I've been developing software professionally since 1992, and started coding as a kid back in 1982. Over the decades, I've seen countless productivity boosts — from new languages to powerful tools — but I've always dreamed of something bigger: the ability to code in natural language.

That dream now feels real.

### Will AI Agents Replace Me?

Talking turkey, I mused that this was the end of my job. If the agent is doing all the coding then do they need me anymore? But at this point I don't see how I am out of the loop. My experience and knowledge is in full use to guide the agent in the right direction. It is just making me more productive.

### My Setup

I'm using [Cursor](https://cursor.com) with large language models like **[Claude 4 Sonnet](https://www.theverge.com/news/672705/anthropic-claude-4-ai-ous-sonnet-availability?utm_source=chatgpt.com)**, and experimenting with a workflow that minimizes traditional coding. Instead of writing code line-by-line, I use prompts. My goal is to adopt an [A](https://agentic-coding.github.io/?utm_source=chatgpt.com)**[gentic Coding](https://agentic-coding.github.io/?utm_source=chatgpt.com)** approach on real production projects — not toy apps or labs, but genuine business code.

### Real Projects, Real Challenges

I began with a relatively safe, isolated UI project: a small React frontend built on top of an existing API. It was a greenfield project — easy for the agent to understand and build.

Now, I'm applying the same workflow to backend services built in **Java with Spring Boot**. Here, the challenges are more complex and there is plenty of existing code. It seems like the Agent performs better with React (perhaps due to better training data and less legacy complexity), but it can handle this backend code if given enough structure and clarity.

### Lessons Learned (so far)

#### 1. Don't be vague. Be specific.

Early on, I made the mistake of saying things like:
> *"Create an API that returns usage statistics."*

The results were hit-or-miss. What worked better was defining the exact **request and response payloads**, ideally as **example JSON** or **schemas**. [More on prompt design](https://www.ranthebuilder.cloud/post/agentic-ai-prompting-best-practices-for-smarter-vibe-coding).

However if i have a commit to revert to, I can run the agent in 'creative mode' where I just let it invent, but stop or revert if it is not heading in the right direction.

#### 2. Ask for a plan before action.

If I don't explicitly ask for a breakdown of the work, the agent will charge ahead — sometimes making sweeping and incorrect changes. I now instruct it to:

* Analyze first* Propose a plan* Wait for my approval before coding

[Cursor's Agent Mode](https://docs.cursor.com/chat/agent) makes this workflow smooth, especially when combined with "[Cursor Rules](https://docs.cursor.com/context/rules)" to enforce it.

#### 3. Keep plans outside the chat.

Chats can get long and lose context. Instead, I ask the agent to generate a **story with tasks in Markdown**. This lets me:

* Review and edit the plan* Check it into version control* Collaborate with team members asynchronously

I created a user story template (with the agent's help!) for it to follow that covers **functional** and **non-functional requirements** like performance and scalability.

For larger efforts, I can collaborate with other humans accross multiple roles (product, quality, platform, leadership, etc.) to create PRD (Product Requirements Document) with the Agent's help. These may include UX designs. This can then be further broken down into stories, and then stories into implementable and specific tasks.

#### 4. Control the tech stack.

If I don't define constraints, the agent might introduce unfamiliar libraries or patterns. To avoid that, I provide a document detailing:

* Preferred libraries* Architectural patterns* Tech stack decisions

This file becomes part of the prompt context. It can just be part of a docs or the **README.md** of your project but you may need to supply it as context.

Some of this the Agent can deduce from the code base you expose to it but I have seen it make more assumptions than I would expect. Architects or leads, or the engineering community should pool together to create these well documented standards to be supplied as context.

#### 5. Give the agent broad, contextual awareness.

Our systems use **domain-specific terms** that aren't obvious from code alone. I make sure to:

* Provide a **Product Requirements Document (PRD)*** Include a **domain glossary*** Annotate our APIs and domain models thoroughly

Without this context, the agent is forced to guess — especially when our codebase is inconsistent.

This is a great time for collaborating with humans: product, managers, tech leaders, UX, QE etc. to review and enhance these documents. The Agent can be used to help craft these documents and keep it up to date.

#### 6. Make documentation first-class.

Our architecture is more or less microservice-based. The agent can read local code for the service I cloned, but when services interact via REST with other services, I ensure:

* External service APIs are documented with **OpenAPI/Swagger*** Repos contain well-written README.md files* Dependencies are explained clearly in Markdown

The question is how much can the Agent see to get context. It may not be able to read the entire multitude of repositories in the organization at once, or you may not want to expose it all, but it can read README and json files defining these service apis it needs to collaborate with. These requirements can be added to PRD or stories you are working on to help keep it focused.

### More reading

* See [these recommendations](https://agentic-coding.github.io/) for more guidance.* More [in depth on Claude sonnet](https://codersera.com/blog/how-to-use-claude-4-and-sonnet-with-cursor-and-windsurf?utm_source=chatgpt.com)* [Better prompting with claude and cursor or windsurf](https://www.ranthebuilder.cloud/post/agentic-ai-prompting-best-practices-for-smarter-vibe-coding?utm_source=chatgpt.com)

### Final Thoughts (for now)

Agentic coding doesn't eliminate the need for engineers — it *elevates* the role. My job is less about syntax and more about **architecture**, **design**, and **communication**.

When properly guided, agents like Claude become powerful collaborators. But they need context, clarity, and constraints.

*(Written with assistance from ChatGPT)*
