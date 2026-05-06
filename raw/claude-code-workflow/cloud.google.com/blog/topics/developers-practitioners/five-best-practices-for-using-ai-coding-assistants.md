---
source_url: https://cloud.google.com/blog/topics/developers-practitioners/five-best-practices-for-using-ai-coding-assistants
crawl_depth: 0
crawled_at: 2026-05-05T14:36:11Z
word_count: 1126
---

Developers & Practitioners
October 7, 2025
![https://storage.googleapis.com/gweb-cloudblog-publish/images/5_Best_Practices_for_Using_AI_Coding_Assis.max-2500x2500.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/5_Best_Practices_for_Using_AI_Coding_Assis.max-2500x2500.png)
##### Kari Loftesness
Business Lead, Cloud Developer Experience
##### Jason Davenport
Developer Advocate
Does owning a kitchen knife mean you know how to effectively dice onions or julienne carrots? Of course not. Access to a tool doesn't guarantee profenciency. To get the results you're looking for, you need to learn the right techniques.
AI coding assistants are no different. These are new and powerful additions to your developer toolbox that you can [access today](https://github.com/google-gemini/gemini-cli). But like any tool, you need to know when and how to use them effectively. 
So, how can you get the most out of AI coding assistants? To find out, we asked several engineers from our Google Cloud Developer Experiences team to actively use [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Gemini Code Assist](https://codeassist.google/), and [Jules](https://jules.google/) while they completed complex app development and migration projects. Based on those engineering sprints, we found **five best practices** that led to better outcomes, and we're sharing these best practices so you can turn access to tooling into AI expertise as well.
## Consider your use case when choosing a tool
Getting the most out of AI requires deliberate planning. Before you begin coding, think about the requirements for your project and associated tasks you’ll need to complete. This up-front thought exercise will clarify which AI tool you should start with and which might be helpful later. Each [Google developer tool](https://cloud.google.com/blog/products/ai-machine-learning/choose-the-right-google-ai-developer-tool-for-your-workflow) has different strengths, so you want to choose the right one for the job.
Depending on the complexity of your work, you might not use agentic frameworks to accomplish your task. Writing a new function? Use inline generation. Taking an app from v1 to v2? Use an agent to help plan out all the file changes needed. Throughout our engineering sprints, we used tools like [Gemini CLI](https://github.com/google-gemini/gemini-cli) to help on larger migrations where multiple files were involved. When we were writing specific functions, inline generation through [Gemini Code Assist](https://codeassist.google/) fit our developer flow better. Once you choose the right tool, you can start to train that tool toward your goals.
## Train the tool with foundational work
Most generative models act based on natural language. In many examples, AI performs better on generation once you’ve leveraged it to also document the code base. “Shift left” in your AI assistance workflow by documenting early to produce higher-quality output later. This includes things like generating READMEs where needed and even generating unit tests based on the existing code. 
As you check this work, you can also find idiosyncrasies in your code where AI may struggle with comprehension, and as a result, potentially future generation. Do this training before you get to the next best practice we recommend: using AI to help you plan your code.
## Make a plan
A large part of a developer's job is planning, and AI models are no different. Spending extra time with AI tools to build and revise an execution plan generally gives you better code output on complex tasks. You can create a strong plan in several ways:
  * Iterate on a requirements document to fully understand the problem you will solve.
  * Use source code analysis to understand the current code structure, including package dependencies and other runtime details.
  * Create a set of tests that will determine if the generated code works based on your requirements.
  * Create the execution plan, detailing which files and folders need to be modified based on the AI's understanding of the problem.


You should also ask the AI to build and save a step-by-step plan (like in a `plan.md` file). This encourages both you and the AI to pause and think through the upcoming steps before execution. AI tools work best when you manage them. Break down a complex, high-level assignment into several manageable components. For example, during a large migration, we recommend migrating one service at a time instead of several at once. Finally, instruct the AI to ask for your approval before executing on new plan milestones. This crucial step keeps you, [the developer, in control of your project](https://cloud.google.com/discover/human-in-the-loop?hl=en).
## Prioritize prompt engineering
Take time to make your prompts as relevant as possible, just as you would when helping a new teammate scope a task. Consider what details you need to share for a person to succeed, and provide all those details to your AI tool. You can even ask Gemini or other chatbot tools to help improve your prompt before you send it to the AI assistant.
Even when you're in the agentic coding flow, prompting is still essential. Understanding the specific models you use helps you get better iterative results. Be specific about your requests and desired outcomes. Models are token predictors, so grouping your thoughts and clearly stating what you want to happen next are good practices, whether you are prompting a model or reviewing a task for a teammate.
## Connect the dots between sessions 
We've all encountered that one piece of code you can't touch without breaking the whole application—that is context. The most effective way to get better performance day after day is to create a context file at the end of each working session, for example [GEMINI.md](https://github.com/davenportjw/online-boutique/blob/gemini/work/GEMINI.md). This file can include high-level instructions, specific details around dependency versions, architecture diagrams, and more. This `GEMINI.md` file gives the tool a "cheat sheet" it can use to kick off your next AI-assisted session.
Documenting context significantly improves the planning and execution accuracy of the AI coding tools. It also ensures the tool understands your project and your specific working style. During our sprints, we saved all key learnings into a file at the end of every working day and instructed the AI to access it the next morning. This allowed us to pick up exactly where we left off, and now we're even exploring the idea of storing more layered context files based on repository and general user preferences. The key to creating usable code is giving models the right context.
* * *
We’re just scratching the surface of what’s possible with AI coding assistants, and we’re excited to keep learning with you. [Join an upcoming AgentVerse event](https://cloud.google.com/blog/topics/developers-practitioners/your-epic-quest-awaits-conquer-the-agentverse) to learn more about how to take an AI idea from concept to reality.
Posted in


##### Related articles
[ ![https://storage.googleapis.com/gweb-cloudblog-publish/images/corrected_updated_final_codelabs_image.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/corrected_updated_final_codelabs_image.max-700x700.png) Developers & Practitioners Next '26 Hands-On: 10 Codelabs to Build Featured Tech By Mandy Grover • 3-minute read ](https://cloud.google.com/blog/topics/developers-practitioners/next-26-hands-on-10-codelabs-to-build-featured-tech)
[ ![https://storage.googleapis.com/gweb-cloudblog-publish/images/Agent_Skills_Blog_-_Hero.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Agent_Skills_Blog_-_Hero.max-700x700.png) Developers & Practitioners Level Up Your Agents: Announcing Google's Official Skills Repository By Megan O'Keefe • 2-minute read ](https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository)
[ ![https://storage.googleapis.com/gweb-cloudblog-publish/images/GCN26_102_BlogHeader_2436x1200_Opt_5_Dark.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/GCN26_102_BlogHeader_2436x1200_Opt_5_Dark.max-700x700.jpg) Networking What’s new with the Cross-Cloud Network at Next ‘26 By Rob Enns • 13-minute read ](https://cloud.google.com/blog/products/networking/whats-new-in-cloud-networking-at-next26)
[ ![https://storage.googleapis.com/gweb-cloudblog-publish/images/0_gemini_enterprise_agent_platform.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/0_gemini_enterprise_agent_platform.max-700x700.jpg) AI & Machine Learning Introducing Gemini Enterprise Agent Platform, powering the next wave of agents By Michael Gerstenhaber • 12-minute read ](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)
