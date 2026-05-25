---
title: Use AI to Boost Developer Productivity
source_url: https://www.docker.com/blog/ai-developer-productivity-workflow/
source_domain: docker.com
topic: claude-code-workflow
doc_type: how-to-guide
author: Cameron Pavey
published_date: '2025-11-21'
fetched_at: '2026-05-25T06:44:17.390181+00:00'
language: en
word_count: 3320
reading_time: 17
signal_score: 0.9795
status: kept
core_question: What workflow pattern maximizes productivity when using AI coding tools?
tldr: Framework for effective AI-assisted development through prompting, planning, producing, and refining
  cycles with context management and prompt crafting strategies.
key_topics:
- workflow cycle
- context management
- prompt crafting
- AI productivity
- planning phase
entities:
  primary: AI developer productivity workflow
  aliases:
  - AI coding workflow
  - developer productivity cycle
  - agentic AI patterns
content_hash: sha256:20c18496332d51195f7204ccb38d390adbf65d07d7b5ecacfd6dcc4d94fe2f50
---

When I started incorporating AI tools into my workflow, I was first frustrated. I didn't get the 5x or 10x gains others raved about on social. In fact, it slowed me down.

But I persisted. Partly because I see it as my professional duty as a software engineer to be as productive as possible, partly because I'd volunteered to be a guinea pig in my organization.

After wrestling with it for some time, I finally got my breakthrough discovery—the way to use AI tools well involves the same disciplines we've applied in software development for decades:

- Break work down into reasonable chunks
- Understand the problem before trying to solve it
- Identify what worked well and what didn't
- Tweak variables for the next iteration

In this article, I share the patterns of AI use that have led me to higher productivity.

These aren't definitive best practices. AI tools and capabilities are changing too quickly, and codebases differ too much. And then we're not even taking the probabilistic nature of AI into account.

But I do know that incorporating these patterns into your workflow can help you become one of the developers who benefit from AI instead of being frustrated or left behind.

# A Cycle for Effective AI Coding

Too many people treat AI like a magic wand that will write their code _and_ do their thinking. It won't. These tools are just that: tools. Like every developer tool before them, their impact depends on how well you use them.

To get the most from AI tools, you need to constantly tweak and refine your approach.

The exact process you follow will also differ depending on the capabilities of the tools you use.

For this article, I'll assume you're using an agentic AI tool like Claude Code, or something similar: a well-rounded coding agent with levers you can tweak and a dedicated planning mode, something that more tools are adopting. I've found this type of tool to be the most impactful.

With such a tool, an effective AI coding cycle should look something like this:

The cycle consists of four phases:

**Prompting**: Giving instructions to the AI**Planning**: Working with the AI to construct a change plan**Producing**: Guiding the AI as it makes changes to the code**Refining**: Using learnings from this iteration to update your approach for the next cycle

You might think this is overly complicated. Surely you could simply go between prompting and producing repeatedly? Yes, you could do that, and it might work well enough for small changes.

But you'll soon find that it doesn't help you write *sustainable* code quickly.

Without each step in this loop, you risk that the AI tool will lose its place or context, and the quality of its output will plummet. One of the major limitations of these tools is that they will not stop and warn you when this happens; they'll just keep on trying their best. As the operator of the tool and ultimately the owner of the code, it's your responsibility to set the AI up for success.

Let's look at what this workflow looks like in practice.

## 1. Prompting

AI tools are not truly autonomous: the quality of the output reflects the input you provide. That's why prompting is arguably the most important phase in the loop: how well you do it will determine the quality of output you get, and by extension, how productive your use of AI will be.

This phase has two main considerations: context management and prompt crafting.

### Context Management

A common characteristic of current-gen AI tools is that the quality of their output tends to decrease as the amount of context they hold increases. This happens for several reasons:

**Poisoning**: errors or hallucinations linger in context**Distractions**: the model reuses mediocre context instead of searching for better info**Confusion**: irrelevant details lower output quality**Clashes**: outdated or conflicting info leads to errors

As long as AI tools have this limitation, you get better results by strictly managing the context.

In practice, this means rather than having one long-running conversation with your agent, you should "wipe" its context in between tasks. Start from a fresh slate each time, and re-prompt it with the information it needs for the next task so that you don't implicitly rely on accumulated context. With Claude Code, you do this with the `/clear`

slash command.

If you don't clear context, tools like Claude will "auto-compact" it, a lossy process that can carry forward errors and reduce quality over time.

If you need any knowledge to persist between sessions, you can have the AI dump it into a markdown file. You can then either reference these markdown files in your tool's agent file (CLAUDE.md for Claude Code) or mention the relevant files when working on specific tasks and have the agent load them in.

# Structure varies, but it might look something like this…

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | `.` `├── CLAUDE.MD` `└── docs` `└── agents` ` ` `└── backend` ` ` `├── api.md` ` ` `├── architecture.md` ` ` `└── testing.md` ````` |

## Prompt Crafting

After ensuring you're working with a clean context window, the next most important thing is the input you provide. Here are the different approaches you can take depending on the task you are dealing with.

### Decomposition

Generally, you want to break work down into discrete, actionable chunks. Avoid ambiguous high-level instructions like "implement an authentication system", as this has too much variability. Instead, think about how you would actually do the work if you were going to do it manually, and try to guide the AI along the same path.

Here's an example from a document management system task I gave Claude. You can view the whole interaction summary in this GitHub repo.

- Prompt: "Look at DocumentProcessor and tell me which document types reference customers, projects, or contracts."
- Output: AI identified all references

- Prompt: "Update the mapping functions at {location} to use those relationships and create tests."
- Output: Implemented mappings + tests

- Prompt: "Update documentIncludes to ensure each type has the right relations. Check backend transformers to see what exists."
- Output: Filled in missing relationships

Notice how the task is tackled in steps. A single mega-prompt would have likely failed at some point due to multiple touchpoints and compounding complexity. Instead, small prompts with iterative context led to a high success rate.

Once the task is done, wipe the context again before moving on to avoid confusing the AI.

#### Chaining

Sometimes you *do* need a more detailed prompt, such as when tasking the AI with a larger investigation task. In this case, you can improve your chances of success greatly by chaining prompts together.

The most common way of doing this is by providing your initial prompt to a separate LLM, such as ChatGPT or Claude chat, and asking it to draft a prompt for you for a specific purpose. Once you're satisfied with the parameters of the detailed prompt, feed it into your coding agent.

Here's an example:

Prompt (ChatGPT): "Draft me a prompt for a coding agent to investigate frontend testing patterns in this codebase, and produce comprehensive documentation that I can provide to an AI to write new tests that follow codebase conventions."

This prompt produces a fairly detailed second-stage prompt that you can review, refine, and feed to your agent:

You can see the full output here.

This approach obviously works best when you ensure the output aligns with the reality of your code. For example, this prompt talks about `jest.config.js`, but if you don't use jest, you should change this to whatever you do use.

##### Reuse

Sometimes, you'll find a pattern that works really well for your codebase or way of working. Often, this will happen after Step 4: Refining, but it can happen at any time.

When you find something that works well, you should set it aside for reuse. Claude Code has a few ways you can do this, with the most idiomatic one being custom slash commands. The idea here is that if you have a really solid prompt, you can encode it as a custom command for reuse.

For example, one great time saver I found was using an agent to examine a Laravel API and produce a Postman collection. This was something I used to do manually when creating new modules, which can be quite time-consuming.

Using the chaining approach, I produced a prompt that would:

- Generate a new Postman collection for a given backend module
- Use the Controller/API test suite to inform the request body values
- Use the Controller and route definitions to determine the available endpoints

Running the prompt through an agent consistently produced a working Postman collection almost instantly. You can see the prompt here.

When you find a valuable pattern or prompt like this, you should consider sharing it with your team, too. Increasing productivity across your team is where the real compounding benefits can happen.

### 2. Planning

Tools like Claude Code have a planning mode that allows you to run prompts to build context without making any changes. While you don't always need this functionality, it's invaluable if you're dealing with a change with any appreciable amount of complexity.

Typically, the tool will perform an investigation to find all the information it needs to determine what it *would* do if it weren't in planning mode. It will then present you with a summary of the intended changes. The key inflection point here is that it allows you to review what the AI is planning to do.

In the screenshot below, I used planning mode to ask Claude what's needed to add "Login with Google" to an existing app that already supports "Login with Discord":

I could see everything the AI planned to change to decide whether it makes sense for my use case.

Important: read the plan carefully! Make sure you understand what the AI is saying, and make sure it makes sense. If you don't understand or if it seems inaccurate, ask it to clarify or investigate more.

You should not move on from the planning phase until the plan looks exactly like what you would expect.

If the AI proposes rewriting a huge amount of code, treat it as a red flag. Most development should be evolutionary and iterative. If you break work into small chunks, the AI should propose and make small changes, which in turn will be easier to review. If the plan includes far more changes than you expected, review your input to see if the AI is missing important context.

Once you've iterated on the plan, you can give the AI the go-ahead to execute the plan.

### 3. Producing

During the third phase, the AI will begin to make changes to your codebase. Although the AI will produce most of the output here, you're not off the hook. You still own any code it produces at your behest, for better or worse. It's therefore better to see the producing phase as a collaboration between you and the AI: the AI produces code and you're guiding it in real-time.

To get the most out of your AI tool and spend the least amount of time doing rework, you need to guide it. Remember, your goal is maximum productivity—**real** productivity, not just lines of code. That requires that you need to actively engage with the tool and work with it as it builds things, rather than just leaving it to its own devices.

If you take sufficient care with creating your prompt and doing planning, there shouldn't be too many surprises during the actual coding phase. However, AI can still make mistakes, and it will certainly overlook things, especially in larger systems. (This is one of the major reasons why fully "vibe coded" projects break down quickly as they increase in scope. Even when the entire system has been built by AI, it will not remember or know everything that exists in the codebase.)

A day must still pass where I've not caught AI making a mistake. They might be small mistakes, like using string literals in place of pre-existing constants, or inconsistent naming conventions. These things might not even stop the code from working.

However, if you let these changes through unchecked, it will be the start of a slippery slope that is hard to recover from. Be diligent, and treat any AI-generated code as you would code from another team member. Better still, understand that this code has your name attached to it, and don't accept anything that you aren't willing to "own" in perpetuity.

So if you notice a mistake has been made, point it out and suggest how it can be fixed. If the tool deviates from the plan or forgets something, try to catch it early and course-correct. Because your prompts are now small and focused, the features the AI builds should also be smaller. This makes reviewing them easier.

### 4. Refining

Luckily, rather than constantly fighting the machine and going back and forth on minor issues, the final phase of the loop—refining—offers a more sustainable way to calibrate your AI tool over time.

You might not make a change to your setup after every loop, but every loop will yield insight into what is working well and what needs to change.

The most common way to tweak the behavior of AI tools is to use their specific steering documents. For instance, Claude has CLAUDE.md, and Cursor has Rules.

These steering documents are typically a markdown file that gets loaded into the agent's context automatically. In it, you can define project-specific rules, style guides, architectures, and more. If you find, for example, that the AI constantly struggles with how to set up mocks in your tests, you can add a section to your doc that explains what it needs to know, with examples it can use for reference, or links to known-good files in the codebase it can look at.

This file shouldn't get too big, as it does take up space in the LLM's context. Treat it like an index, where you include information that is always needed directly in the file, and link out to more specialized information that AI can pull in when needed.

Here's an excerpt from one of my CLAUDE.md files that work well:

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 | ````md` `...` `## Frontend` `...` `### Development Guidelines` `For detailed frontend development patterns, architecture, and conventions, see:` `**[Frontend Module Specification](./docs/agents/frontend/frontend-architecture.md)**` `This specification covers:` `- Complete module structure and file organization` `- Component patterns and best practices` `- Type system conventions` `- Testing approaches` `- Validation patterns` `- State management` `- Performance considerations` `...` ````` |

The AI understands the hierarchy of markdown files, so it will see that there's a section about frontend development guidelines, and it will see a link to a module specification. The tool will then decide internally whether it needs this information. For instance, if it's working on a backend feature, it will skip it, but if it's working on a frontend module, it will pull in this extra file.

This feature allows you to conditionally expand and refine the agent's behavior, tweaking it each time it has trouble in a specific area, until it can work in your codebase effectively more often than not.

### Exceptions to the Cycle

There are some cases where it makes sense to deviate from this flow.

For quick fixes or trivial changes, you might only need **Prompting** → **Producing**. For anything beyond that, skipping planning and refinement usually backfires, so I don't recommend it.

Refinement will likely need to be done quite often when first starting or when moving to a new codebase. As your prompts, workflows, and setup mature, the need to refine drops. Once things are dialed in, you likely won't need to tweak much at all.

Finally, while AI can be a real accelerator for feature work and bug fixes, there are situations where it will slow you down. This varies by team and codebase, but as a rule of thumb: if you're deep in performance tuning, refactoring critical logic, or working in a highly regulated domain, AI is more likely to be a hindrance than a help.

## Other Considerations

Beyond optimizing your workflow with AI tools, a few other factors strongly affect output quality and are worth keeping in mind.

### Well-Known Libraries and Frameworks

One thing you'll notice quickly is that AI tools perform much better with well-known libraries. These are usually well-documented and likely included in the model's training data. In contrast, newer libraries, poorly documented ones, or internal company libraries tend to cause problems. Internal libraries are often the hardest, since many have little to no documentation. This makes them difficult not only for AI tools but also for human developers. It's one of the biggest reasons AI productivity can lag on existing codebases.

In these situations, your refinement phase often means creating guiding documentation for the AI so it can work with your libraries effectively. Consider investing time up front to have the AI generate comprehensive tests and documentation for them. Without it, the AI will have to reanalyze the library from scratch every time it works on your code. By producing documentation and tests once, you pay that cost up front and make future use much smoother.

#### Project Discoverability

The way your project is organized has a huge impact on how effectively AI can work with it. A clean, consistent directory structure makes it easier for both humans and AI to navigate, understand, and extend your code. Conversely, a messy or inconsistent structure increases confusion and lowers the quality of output you get.

For instance, a clean, consistent structure might look like this:

1 2 3 4 5 6 7 8 9 10 11 12 | ````` `.` `├── src` `│ ├── components` `│ ├── services` `│ └── utils` `├── tests` `│ ├── unit` `│ └── integration` `└── README.md` ````` |

Compare that with this confusing structure:

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | ````` `.` `├── components` `│ └── Button.js` `├── src` `│ └── utils` `├── shared` `│ └── Modal.jsx` `├── pages` `│ ├── HomePage.js` `│ └── components` `│ └── Card.jsx` `├── old` `│ └── helpers` `│ └── api.js` `└── misc` ` ` `└── Toast.jsx` ````` |

In the clear structure, everything lives in predictable places. In the confusing one, components are scattered across multiple folders (`components`, `pages/components`, `shared`, `misc`), utilities are duplicated, and old code lingers in `old/`.

An AI, like any developer, will struggle to build a clear mental model of the project, which increases the chance of duplication and errors.

If your codebase has a confusing structure and restructuring it is not an option, map out common patterns—even if there are multiple patterns for similar things—and add these to your steering document to reduce the amount of discovery and exploration the AI tool needs to do.

## Wrapping Up

Adding AI tools to your workflow won't make you a 10x developer overnight. You might even find that they slow you down a bit initially, as all new tools do. But if you invest the time to learn them and adapt your workflow, the payoff can come surprisingly quickly.

The AI tooling space is evolving fast, and the tools you use today will likely feel primitive a year from now. However, the habits you build and the workflow you develop—the way you prompt, plan, act, and refine—will carry forward in one form or another. Get those fundamentals right, and you'll not only keep up with the curve, you'll stay ahead of it.
