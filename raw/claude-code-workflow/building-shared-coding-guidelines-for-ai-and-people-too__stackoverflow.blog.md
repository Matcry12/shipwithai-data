---
source_url: "https://stackoverflow.blog/2026/03/26/coding-guidelines-for-ai-agents-and-people-too/"
source_domain: "stackoverflow.blog"
topic: "claude-code-workflow"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-25T06:42:26.480727+00:00"
word_count: 1907
stage: "raw-extracted"
---

As engineering organizations grow, getting everyone to work on the same software starts to get unwieldy. Everybody has their own quirks and styles, which can lead to a Tower of Babel implemented as a service-oriented architecture. So leadership folks came up with ticketing systems, scrum, and deployment pipelines to bring some consistency to the process. For the code itself, they wrote coding standards and guidelines.

In 2026, software engineers are writing less and less code by hand. Instead, they use coding agents to write code based on their designs. But if those agents contribute to an enterprise code base, then they need to follow the standards and guidelines. Fortunately, most of the code generators have implemented ways to add standards and guidelines to your agents.

The catch is that it’s not the same as onboarding a new junior developer. You can’t just throw a few documents at them and let them explore. Agents are fast but lack the context of your code. And a lot of the context for human coders comes as tacit learnings as they see particular forms, styles, and patterns. We call red flags in code “smells,” which speaks to the vibe-based nature of a lot of code understanding. Despite popular discourse, coding agents don’t run on vibes, at least not in professional situations.

As coding agents create more and more code, the cognitive burden of software engineering is shifting to design and architecture as well as code review. Code review will be most engineers’ first look at the code since they didn’t write it themselves. They just know what they wanted the code to do. Coding guidelines for agents can inject a bit of determinism into a non-deterministic process.

Coding guidelines and standards (which I’ll just call “guidelines”) for agents need to be a little different—more explicit, demonstrative of patterns, and obvious. But not super different, as good documentation is for all coding entities.

Here’s how to best create coding standards for agents *and *humans.

## Ground rules

The code that agents produce needs to work with a bunch of code that’s already in production (unless you live a blessed life building a purely greenfield project). It needs to use the same languages and libraries, hook into any build and deployment systems, and fit with the platform engineering systems and paradigms you use. If your front end uses Express, your agent shouldn’t code with React.

Beyond the tech stack, your engineering team has a set of methodologies and best practices they use to write code for a shared codebase. Some of these may be universal best practices, some may be team culture, and some may be the ways that your team deviates from or ignores best practices. While this may be assumed common knowledge with your human teammates, take nothing for granted with agents. “What are the prompts that you need to give it, like DRY?” said Vish Abrams, chief architect at Heroku. “There's classic programming principles that to seasoned engineers are common knowledge. The same thing is true about deployment. You want to build your application where configuration and code are separate. You can tell the LLM to build your application that way, or you can just say, build me a snake game and it'll do whatever it wants to. Maybe it’s not maintainable at all.”

This might be the time to revisit your coding guidelines altogether. Many of the best practices were created when code was artisanal and hand-written. If you’re only engaging with the code during review, maybe some guidelines change. Maybe having multiple copies of functionality is better for code review, so you see the functionality with the PR. Maybe not. But many of the best practices serve to make code readable and maintainable for humans.

## How to code the code

Coding, like writing, has a lot of little decisions that can vary across organizations. For outsiders, they may seem small and arbitrary, but they can have downstream impacts and slow down reviews for colleagues used to certain conventions. We use the serial comma here on the Stack Overflow blog, but others don’t and are wrong.

Like a style guide, your agentic coding guidelines should indicate the decisions your team has made about which language constructs to use and *why*. Here are a few decisions to consider including:

**Variable and method naming**: Naming things is one of the hard problems of software engineering. Do you want your agents running wild and creating `FactoryBuilderBuilderFactory` or mixing camelCase and underscore_style? If you have differences in styles within a codebase, say between C++ and SQL code, then indicate them separately. Indicate how to identify and resolve duplicate names.**Tabs vs. spaces**: If your team has an opinion on the tabs vs. spaces debate, let the agent know. Some IDEs and languages may make this debate moot; make sure your agent knows the score regardless.**Layout**: Some programming languages like Python require specific indentation and formatting, while others (particularly the curly brace kinds) allow freer placement. You might have particular feelings about layout for these things, and research suggests that layout can affect the speed of comprehension.**Exceptions and logging**: Your code needs to fail well, and agents need to know how you expect failures and collect data on software in production. It would be great if all this could happen automatically, but most of the time, it requires code within the software to do the job right. Might as well have the agent write that for you as well.**Comments**: Agents can write comments, but should they do it before or after a method? Do they follow indent rules? Are you using an API documentation generator? How much detail do you want? This is something that human coders could probably guess at, but the agents need guidance.

This is not a comprehensive list of guidelines for coding agents, and you’ll likely find more annoying quirks your agent uses along the way. See below for dealing with that.

## Good documentation is good documentation

I know this is meant to be a guide for agentic coding guidelines, but ultimately good documentation is the same whether it’s for people or agents. In fact, many of the qualities below are more important for agents because they are much more unpredictable.

**The guidelines should be clear and consistent.** It should be dead obvious how to follow any guidelines that you write. Test your guidelines by approaching them in the most bad faith manner as possible; if you can find a way to misinterpret it, rewrite it. Write in a simple, repeated style throughout the document—you don’t have to be perfect, just predictable. AI loves patterns.

**Don’t confuse the AI.** When I wrote documentation, I assumed the reader could have a wide range of English skills. They could be a non-native speaker. That means not using idiomatic language or other constructs that require interpretation. Be simple, explicit, and boring. The same goes for code examples. Cover all edge cases so there are no decisions for the AI to make.

**Make your decisions obvious**. Engineers build conventions tacitly. “We take for granted as engineers that when you're writing code and you spend a whole evening and you're writing a bunch of new functions, you're also implicitly absorbing the context of the code base,” said Greg Foster, CTO of Graphite. Any guideline needs to take this tacit knowledge and make it explicit. Provide objective reasons for each guideline. Some guidelines might be inherited from standard conventions (“We use tabs because we’re primarily a Python shop and this makes indentation more consistent”).

## Examples show patterns

I resisted examples in documentation at first. But once I had to use documentation to solve a problem, boy did I get it. Screenshots, sample code, API playgrounds, all these showed me how to use tools better than a numbered list of steps alone. There’s a reason that we jokingly offered a CTRL+C+V keyboard (and then not so jokingly): that sample code gives you a template you can use to customize your own code. And AIs love a good template.

Provide explicit examples of both correct and incorrect implementations of the code guidelines. AIs can use these as patterns to determine what the correct code looks like in most given situations. Multiple examples for each won’t hurt, but again, ensure that your examples are consistent.

Consider also giving the agents an overall example of what code looks like when it follows all guidelines—a “gold standard” file. Individual examples are like unit tests: your gold standard is the end-to-end test. There’s some discussion on whether you only need the gold standard file, or whether it can work in concert with individual examples. We suggest testing to see which gets the best results.

## Errors are feedback

If you’ve worked with agents enough, you probably know already that you’re not gonna get this in one. Your first version of the coding guidelines isn’t going to deliver perfectly formed agentic code. That’s okay; those failures are feedback that you can use to make your guidelines better.

On this blog, Charity Majors talked about using CI/CD processes to speed up the SDLC feedback loop; agents are no different. While you don’t need to implement a Ralph Wiggum loop, you can and should take mistakes in the code as an opportunity to update your standards files. Those errors might even be helpful to reveal the tacit parts of your coding conventions, those secret requirements that you may not have been explicitly aware of.

Using failure as a feedback loop is how you’ll have better agentic processes in general. “There's a big difference between people that just chicken-type a prompt,” said Quinn Slack, CEO and co-founder of Sourcegraph. “They don't really want the AI to win. Then there's people that put in a ton of time defining their rules, their `agents.md` file, and they write out what it should do. If it makes a mistake, then they'll go and update that and try to get it to be a flywheel.”

The other feedback loop to pay attention to is human. Keep the standards file open as a dialogue with your engineering team. Put it in Stack Internal or another documentation repository and get everyone to edit, comment, and update. This is the code that everyone will be building and reviewing; they should have a say in the guidelines.

## Onboarding for AI

The last step, of course, is to make sure that these guidelines live with your code and your agent context. Explicitly put all these rules in your `agents.md` and check them into a standard repo or build a Claude skill for them. Document the standard package for a coding setup like you do for the deployment pipeline.

That said, this shouldn’t be your call to give up all those other deterministic code standard enforcers. Linters, formatters, and static analysis tools still have a place in your build pipeline. They catch the basics that your agents botch.

Big companies who have tried to wrangle the coding styles of hundreds or thousands of engineers have a leg up on folks just thinking about this now. “Big companies have well-articulated style guides and best practices and processes to build code and deploy software,” said Logan Kilpatrick, Senior Product Manager at DeepMind/Google. “All of that is perfect ripe context to give to the model to make it helpful for you. Without a lot of that context, you are just taking a shot in the dark.”