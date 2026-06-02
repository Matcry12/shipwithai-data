---
source_url: "https://www.makingdatamistakes.com/ai-first-development/"
source_domain: "makingdatamistakes.com"
topic: "github-ai-vibe"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-29T13:38:42.625764+00:00"
word_count: 5709
stage: "raw-extracted"
---

# A field guide to AI-first development

Detailed techniques and prompts for AI-first coding, for experienced developers to build medium-sized production-ready codebases, providing lots of architecture-level product guidance but without writing a line of code by hand.

Want to know how to build a well-architected 60,000-line project from scratch in 6 weeks, without writing a single line of code by hand? This was my second AI-first project, and it went smoothly, using techniques and prompts from the first one. (See Postscript below if you're curious about how things turned out.)

This approach relies heavily on human software engineering expertise & judgment, and has been optimised for: greenfield, solo __experienced developer__, ideal architecture for AI-first coding, and speedy progress, in June 2025 (Claude 4, o3, Gemini 2.5).

Of course, if you're developing as part of a team, on a larger legacy codebase, with users in production, and place a premium on reliability, then you have a completely different set of constraints. If so, then __human-first, AI- assisted programming__ makes more sense for now (i.e. treating AI like a junior pair programmer).

But as models improve, AI-*first* will eventually become the dominant mode of development. The AI will write pretty much all the code, with the human as engineering & product manager.

# Let go emotionally of the idea that you are there to write code.

Your job (as developer) is to be a manager of an AI team of developers.

*There's an old joke: "*__in the future__*, all factories will have two employees - a person and a dog. The person is there to feed the dog, and the dog is there to bite the person if they try to touch the machines.”*

I found it very hard to resist the temptation to obsess over every line of code, especially for the bits I like building. To break that habit, it helped enormously at first to be using TypeScript & React for this project, because I don't know either of them very well! It forced me to apply generalised best practices and solve meta-problems (how to instruct the AI to make good decisions itself). But there have been lots of moments where it would have helped a lot if I knew React better.

Take joy in the pace at which your vision becomes real, in product and architectural decisions, in meta-building (building the __factory__ that in turn builds the product), and in the value people get from what you've built.

# AI-first development is a skill

AI-first coding is a skill that can be learned. It is also a toolset that you can build or adopt. It's immature, and changing fast. It's a bazooka strapped to a chainsaw, and the default is that you cut off your arm rather than build a house with it. Steve Yegge puts this well.

- Be willing to read, learn, and experiment.
- Start off in a sandbox, e.g. a hackathon, or building for fun, or a low-stakes project. This way, you can take risks. We learn faster when we can make bold mistakes.
- Your expertise is a multiplier. You will be much more effective if you deeply understand the architecture and tools that you're building with.
- Using AI as a Socratic tutor (rather than an oracle) works well in unfamiliar territory.
- AI still does stupid stuff routinely. The techniques below will make it happen less often, and will help you notice and fix it quickly. But it will still happen a lot, for now. You probably should check every line of production code yourself, unless you have great tests.

# Work as though AI is free, instantaneous, and smarter than you.

This will be true in the not-so-distant future, and we can live in that future today by working around the ways in which we're not there yet.

- It's zero marginal cost if you pay for the Anthropic $200/month
__all-you-can-eat plan__plus Cursor $20/month. - If you set up your workflow so that you can work in parallel, you won't notice the delays as much.
- In order to live in the future where AI is even smarter, use planning docs and the "multiple model" techniques from below.

*"If I have six hours to chop down a tree, I will spend the first four sharpening my axe"*.

A lot of the software engineering best practices that we've known about for a long time are quite effortful. With AI, the effort/cost has dropped enormously, because you're not one that actually has to write the tests or update the docs. And if anything, the benefits are even greater, because a good doc makes it much more likely that the AI will follow the right coding style, reuse existing machinery, avoid gotchas, and generally make good decisions. So **the cost-benefit ratio of good practices is suddenly much higher for AI-first coding**.

- Take the time to have conversations and get aligned about requirements, and then agree on a good plan (for bigger pieces of work), before setting the AI loose on the code.
- Invest in your development setup, documentation, CLAUDE.md file, pick AI-friendly simple architecture, linting, tests, browser automation, infrastructure for ensembling multiple models, handy scripts, safety nets, etc.
- Be profligate in asking for web research, e.g. for debugging, best practices, 3rd-party libraries, etc - and ask it to write up the best stuff as docs that you can refer to later.
- Make time for regular housekeeping, e.g. update documentation and CLAUDE.md, fix linter/type-checker issues, make automated tests work/relevant/high-coverage, etc.
- Address root causes. When you spot a patch of quicksand that keeps being a source of friction and bugs, take the time to fix/refactor/improve it. See below re "fix inputs, not outputs".
- Build your own foundational skills and understanding. Get to know your IDE really well. Use
__evidence-based____prompting__techniques. And it might be helpful to build intuitions about how modern LLMs work (__Simon Willison for the application level__,__Anthropic for interpretability__,__Raschka for algorithms__,__3blue1brown for mathematics__,__Karpathy for implementation intuitions__).

# For big features, use the following __workflow__

- Prefer Claude, because it's nicer to talk to, listens, raises concerns, and can use subagents (if Claude Code) to search the web.
- Use voice recognition (not whatever's built into your OS - something like Wispr Flow for speed, or Voice Ink for privacy).
- If it's a big, open topic where you're trying to think through the requirements for the first time, tell it to interview you like a journalist, asking one question at a time (to avoid cognitive overload), and answer out loud while folding the laundry.

Write a __planning doc__.

- This is invaluable for so many reasons, including: being sure that you & the AI are aligned; giving you fine-grained visibility & control over the plan; an ongoing progress update; a historical record; something to feed into prompts later as a reference; externalises context to carry into new conversations; a concrete proposal for other AIs to critique; something to hang on your wall above your mantlepiece, etc.
- That prompt will break things down strategically into stages, and make sure that good habits are built-in to the process at the right moments.
- Ask another AI to
__critique the planning doc__, especially if it's tricky/meaty, and then decide what to take on board. o3 is good for this, because it's smart and it really delights in telling you all the ways that this was written by cowboys and listing all the ways to improve things.


__Execute the planning doc__, stage-by-stage.

- This gives you a chance to review/test/
__debrief__before__committing__, and then run__/compact__on the conversation before proceeding. - Prefer o3 in Cursor for
__debugging__and reviewing the code that has been written.

# Invest in your __evergreen documentation__

(Obviously don't write the docs *yourself*.)

- Lots of cross-references to other docs and relevant code. Then in your prompts you can just reference one or two of those docs and that's usually enough to help the agent figure out what references to follow and find the relevant bits of code.
*"Add a delete icon, as per DESIGN_ICONS.md”* - Create
__research docs__. For example, if you're making use of a new library, ask Claude to write itself documentation on how to use it. - Regular
__documentation housekeeping__, i.e. make sure it's up-to-date, covers everything, nothing's obsolete, not too much overlap, well-referenced, up-to-date documentation-index etc. - If you have to
__rename a file__, make sure to update all the references to it. For big renames, it helps to set up__SD for find-replace__(nice syntax, and a dry-run mode) along with an__explanatory doc__.

# Pick AI-friendly architecture

What makes for an AI-friendly choice?

- Pick languages/libraries/frameworks with
*lots*of pretraining data (i.e. they've been around for a while, and lots of people use & discuss them), with good documentation, with few gotchas. I suspect it helps too if there hasn't been too much API-version churn, especially recently (otherwise a lot of the pretraining might use older examples). You can provide up-to-date docs, but the AI will always be tugged towards its pretraining. - Simple (after all, anything that causes human developers friction will be tricky for AI too). Standard.
__Monorepo__. No__microservices__. Try to avoid multiple languages. Try to avoid separate frontend and backend. Try to avoid ultraprocessed foods.- In a previous project, I wanted to use an unusual setup with Python/Flask, with
__Svelte.js__embedded within Jinja templates. It took a long time to get it to work, and it kept breaking whenever the AI made changes. Eventually__Glenn Smith__pointed out that my bad architecture choices were holding me back. After I reworked everything with a more conventional setup (giving Svelte.js a full frontend), things immediately went much more smoothly. - For my next project, I went a step further in the same direction:
__Next.js__plus Shadcn for CSS (thanks for the__recommendation, Peter Nixey__. Same setup used by Replit, Lovable and v0, probably the most popular approach around, one language, shared code & types across front and backend, libraries to do standard stuff. Things looked better out of the box, and development has gone much faster and more smoothly. - Pick AI-friendly hosting, i.e. where everything can be orchestrated by CLI or config without needing to point and click at all. For example,
__Supabase__is Postgres under the hood, and offers a bunch of other nice features. For simple setups,__Vercel__has been the best so far, except that it doesn't provide programmatic access to production logs. Alternatively,__Josh Wohle recommends Replit__to avoid devops altogether.

- In a previous project, I wanted to use an unusual setup with Python/Flask, with

# Optimise for correctness, __throughput__, and minimal human-intervention/blocking-time, rather than latency, wall-clock time, or AI-effort

- It doesn't matter how long the AI churns for, as long as it gets it right eventually.
- Work in parallel.
- Try to have some stuff going on that the AI can power through on its own with little supervision (e.g. a well-defined planning doc stage, or some housekeeping), alongside one or two things that are much more interactive (e.g. a sounding-board conversation about requirements, or iteratively tweaking the UI).
- Try to work on features that touch different areas of the codebase in different worktrees, so that you're less likely to experience merge conflicts.
- See multiple Git worktrees.
- Make it easier to context-switch by using separate desktops for each worktree, with a sticky note on each reminding you what's going on.

- Try and catch errors at compile-time or test-time, rather than human-review-time. I'm still trying to figure this out, but it might involve running the linter/type-checker/tests at the end of each planning doc stage, or even as a custom hook before each Git commit (see hooks below), or automatically asking for a code review from another AI.
- Run housekeeping tasks to keep things ship-shape regularly (although I think this will work even better if we can keep things clean as we go along), e.g.:
- Update out-of-date docs, add missing docs, amalgamate duplicate docs, refactor overlapping docs, etc. see "Invest in your evergreen documentation".
- Cull/consolidate broken tests - see "Testing"
- Make sure linting and type-checking are clean (see below).

- Don't look at the code by eye. Find other ways to understand the system, e.g. ask Claude to explain the code, read the docs, or ask it to
__generate a diagram__. (thanks for this tip,__David H__!).

# Multiple models

- Use the right model for the job.
- Claude for conversation, writing, editing, tool use, long to-do lists, following instructions, and especially sub-tasks that can be delegated to subagents. Prefer Opus for anything complex, because Sonnet's intelligence seems to fluctuate.
- o3 for debugging, critiquing, and for tricky code. It is very good at suggesting root cause solutions, and its code works first-time more often. (Feed it the same
__CLAUDE.md__that Claude receives). - o3-pro is smarter than o3, but
__10x cost__and hopeless at editing in Cursor (late June 2025). - I've heard Gemini is great too, especially where a large context would help, but I have tried it less. Gemini editing in Cursor is currently broken in late June 2025, and the Gemini CLI is way behind Claude Code.

- Probably different models do have different strengths and weaknesses. But the much larger effect is just that on any given task, one model may succeed where another one fails. If one model is stuck and doesn't fix something within a couple of tries, immediately switch to a different one and see what happens.
- The simplest way to make models smarter is to ensemble them. Even using the same model called multiple times with different prompts can apparently help quite a lot. Better still, call a couple of different models to critique/suggest and then combine their output. At a minimum, asking o3 to critique a planning document written by Claude works incredibly well. Here's a
__prompt__.

# Invest in your rules file

I usually create a `AGENTS.md`

(which Cursor will read), and then symlink it to `CLAUDE.md`

, `GEMINI.md`

, etc, because these get fed in automatically in every conversation. *This is the file I pay the most attention to in the whole codebase.*

- Lead with a brief description of your company/project/product/vision. Provide some context about stage, e.g. "we have zero users and it's all about fast prototyping" vs "we're NASA and keen that our spaceships don't explode". Include a reference to longer docs, e.g. PRODUCT_VISION.md.
- Lay out your
__principles__in detail, e.g.*"Fix the root cause rather than putting on a bandaid"*,*"Make minimal changes focused on the task at hand"*,*"NEVER make major, destructive, or irreversible changes without explicit authorisation from the user"*, etc. These tend to be pretty constant across projects for me. - Briefly cover important guidelines, coding style, best practices, preferred libraries, automated testing, linter, setting up development environment, debugging, common commands, plus references to longer docs, e.g. CODING_GUIDELINES.md, SETUP_OVERVIEW.md, etc. (For comparison, here's a different, interesting approach from someone else whose CLAUDE.md
__really doubles down on coding guidelines__, but I think may be more relevant for human-first AI-assisted coding.) These coding guidelines tend to be a bit more project-specific than the principles. - Include a list of key documentation files with 1-sentence description for each.
- Include a brief description of your codebase and site organisation, architecture, overview of UI components & interface, plus references to longer docs, e.g. SITE_ORGANISATION.md, ARCHITECTURE_OVERVIEW.md, UI_COMPONENTS.md, DESIGN_OVERVIEW.md, etc.
- For jumping between Cursor, Claude, and Gemini CLI, create a symlink from
`AGENTS.md`

(which Cursor will read) to`GEMINI.md`

and`CLAUDE.md`

(thanks for__the suggestion__). I do not trust`.cursor/rules`

. - Currently, my
`AGENTS.md`

is 250 lines long, but I keep playing with this to figure out the right balance between being comprehensive vs overwhelming.

# Give it access to the same information that a human developer has/depends on to succeed at their job

For example:

__Playwright MCP__(see below) for screenshots, browser console logs, etc. (But always tell it to run within a subagent, because Playwright is very verbose, and will quickly fill up your context window)- Local dev webserver logs (ideally both a compact errors-only log file, and the full output).
- Local database.
- etc

# Prefer __Claude Code__ if you can put up with the UI

Mainly because a) of subagents; b) `/compact`

; and c) I trust them to get the best out of their models with fewer weird gotchas and misaligned incentives.

*"*__Use subagents__*where appropriate, with careful instructions and references to relevant code & docs"*. Dunno if this extra mantra helps, but I worry a lot about it calling subagents with insufficient context which then make half-assed/ill-judged edits.- For extra points, tell it to run the subagents in parallel (if you're confident that the changes wouldn't benefit from shared context). It's enormously satisfying to watch it working on multiple pieces of independent work at the same time! Note that this causes the terminal display to go haywire, but it'll settle back down when it all finishes.
- Claude Code is pretty good about using its
__todolist__to track multi-step progress, but it doesn't do any harm to remind it! - Run Claude Code
__within Cursor IDE__- if you do this, it will then (apparently) have__direct access to Cursor's linter output__. - Even though most modern IDEs are based on Microsoft's VS Code, and even though Microsoft owns GitHub and half of OpenAI and invented AI-assisted programming with GitHub Copilot… their AI tools (e.g. original VS Code, Copilot for anything) were weirdly terrible whenever I've tried them. Avoid.

That said, o3 is phenomenal for writing and debugging code, the Claude Code CLI interface for editing is painful, it doesn't stream the output, it's hard to see the changes that have been made, it's a bit buggy too, and it's hard to scan through a long conversation 🙁 So you'll also need Cursor (or perhaps Windsurf) for editing by hand, and for non-Claude models.

# Context management is key

The models need all and only the relevant context.

- Many of the other tips (e.g. re rules files and documentation) help the models to agentically sniff out relevant stuff from the codebase by providing lots of signposts, well-named files, etc.
- The other half of context management is about minimising the context window, by trimming it down and making sure the models have
*only*what they need. The models all get markedly dumber as you get to 100k tokens, or if the__context includes unhelpful/misleading stuff__. Run /compact long before Claude Code starts to warn about auto-compacting, and long before Cursor suggests you start a new chat.__Planning docs__are the key here, so that you can just tell it to re-read the planning doc and related code & docs after each /compact, and you're back up and running.- Right now, probably 50% of my messages are telling Claude to
__commit, compact, then continue__on the next stage of a planning doc.

- Make heavy use of subagents (because they have their own context window). But note that they are only allowed <40k tokens, and there's a risk that they in turn haven't been provided with enough context.
- Other minor ideas I've been experimenting with to help the AI get the context it needs:
- Filenames help an AI that's seeing the codebase for the first time every conversation. Make them longer and more descriptive. For example, I had an auto-generated file called `database.ts` that the agents kept editing. To avoid this, I made multiple changes, including renaming it to `database_autogenerated.ts`. (I also added a comment at the top of the file, and a mention in docs. But I bet the filename alone would tip them off.)
- Maybe make variable names longer and more descriptive. It'll make their meaning more obvious to the AI, and it makes grepping and renaming easier. Yes, it takes more tokens to type them, but see “Don't optimise for wall clock time.”


# Be as lax with permissions as you can, but no more

For models I trust, allow it to run most commands, *except* Git commits and anything destructive and hard to reverse. Provide guidance, especially in your rules file. But for this to work, you also need to plan for the worst, and have good safety nets. Here's a more detailed set of recommendations:

- Allow most Bash commands, web searches, etc. For obviously destructive, hard-to-reverse commands, i.e. add them to the denylist, or at least exclude them from the allowlist.
*Guidance*: provide lots of`CRITICAL`

messages in your rules file (e.g.`CLAUDE.md`

) and relevant documentation that warns against destructive or unwelcome operations. Deny all commands that will write to production without explicit user authorisation. Even in dev, you'd probably prefer that it doesn't drop tables, run migrations, reset, etc. Think about what other guidance to provide for your specific project.- One of the reasons I favour Claude is that it's a pretty safe and sensible pair of hands, and usually listens to instructions (e.g. "don't make changes yet"). That is, unless its context window is >100k tokens, in which case all bets are off.
- If you can, use deterministic, tested scripts with careful, well-named checks & constraints, rather than prompts/instructions for dangerous/risky stuff.
- Accept that guidance will only protect you somewhat. So you also need
*safety nets*just in case the model*does*do something dumb. Store everything important in version control, occasionally back up the whole dev folder, treat your dev setup (including the dev database) as ephemeral and make sure it's easy to reconstruct, back up your laptop to an external hard disk every so often, etc. If the stakes are higher, build more elaborate safety nets (virtual machines, no access to production credentials, etc). - Why no Git commits? Partly because (unless you amend them immediately) they're hard to reverse. Mostly so you can use them as a natural pause, for summarising & reviewing progress, and compacting context.

*"Don't say you're sorry - just don't do it again"*

Your job is to build a factory that in turn builds the product. "__Fix inputs, not outputs" (thanks to John Rush for this framing!).__ In other words, when your 'factory' produces the wrong output, improve the inputs (i.e. the setup/automatic scripts/instructions/prompts) rather than fixing the code by hand yourself.

- If we see the same error or problem more than a couple of times, it's a sign that we need to address an underlying cause. That could be documenting some
__web research about best practices/snippets/gotchas__, tweaking__CLAUDE.md__, improving compile-time checking with stronger type definitions, improving error messages & logging, writing better tests, switching to a 3rd-party library, a refactor, etc. - Solve problems in a stack. For example, let's say I see the AI struggling with a 3rd-party library. Open up a new Claude Code (i.e. add to the stack) to first address the underlying problem (e.g. write a doc with web research of best practices for using that library). Then pop the stack by closing that terminal, and go up a few messages in the conversation to ask the agent to retry, referencing the new doc, etc.
- I hit a wall at about 40k lines, and then at about 80k lines. In both cases, we had just added a lot of new features and infrastructure very quickly, but found that improving on them often felt like one-step-forward-one-step-back.
- It had been so exhilarating to see new features emerge that perhaps I had kept pressing ahead without enough review, rapidly building new skyscrapers of sand. So there's a lesson there. And this was before my habit of first asking o3 for a critique of the planning document, and then again later of the output.
- Follow the practice of
__addressing technical debt as part of an associated feature improvement__- when I found that progress was slow on a particular feature, I stopped to first invest in the underlying machinery that was holding the project back (i.e. add to the stack). If something fails silently, perhaps invest in better error-handling and messages to propagate explicit, debuggable, user-visible messages. If you keep finding stuff in a manual review that you think is obvious, perhaps invest in better end-to-end Playwright testing. If the type-checker isn't catching obvious bugs, perhaps invest in stronger type-checking or enable more warnings. Etc.


# Get used to a different cadence

Progress will feel very bursty. There will be troughs, and things will sometimes feel out of control. Your bicycle has been upgraded to a broomstick, your lightsaber has become a bazooka. On a good day, you’ll co-produce literally dozens of features and many thousands of production-ready lines of code. But there will be days when __nothing works__, and you don't feel you understand your own codebase. If you get stuck in a broken state:

- Resist the urge to try and fix the problem by hand yourself - remember the dog in the factory. Behave as though you're the engineering manager, mentor, or product manager. What moves can you make if you're not the one actually wielding the spanner? Have fortitude, especially if this is the first time you're making the transition from individual contributor to manager. Invest in building your skills as a Manager of AI Colleagues, because that will ultimately be much, much higher-leverage.
- Switch to another model - that unsticks things astonishingly often.
- Ask it to be in
__detective-scientist mode__. Ask it to explain or draw a__diagram__of what's going on, and feed that back in as input. Ask for opinions from multiple models. Ask it to look through the Git history and describe the changes that have been made recently. Ask it to build a test that replicates the problem, and then leave it to work in a loop for a while. Make sure it has access to all the information it needs to be able to debug things effectively, and improve your logging and error messages. Do some housekeeping, in case better docs or errant type-checking unclog the solution. Take a breath, take a break, get some sleep, this too shall pass.

# Quality control and automated testing

Overall, blended productivity is driven by the number of times we get stuck in quicksand, rather than how fast we can go in bursts at top speed.

And the AI still drives into quicksand pretty regularly, getting into a broken state that takes a little while of both AI and human time to unwind. And it still does dumb things and papers over the cracks with bandaids. Even taking all this into account, the rate of progress is worth it. But it's painful sometimes, and I'm sure we can do better here.

Automated testing is part of the answer, though I'm still experimenting with the right approach.

- For human-first AI-assisted coding, then test-driven development works well. Provide very close guidance about how the tests should work (or even write them directly yourself), and then you can rely more on the code that the AI writes to pass them.
- For AI-first coding, I've tried to farm out the test-writing to the AI too, based on the planning document. But I'm not sure how well this is working. Many of the tests break over time, or somehow miss obvious bugs that crop up immediately during a manual review. I'm reluctant to write the tests manually, because that would dramatically slow things down.

Here's my current approach:

- Define actions at early stages of the planning doc to write detailed unit tests first (i.e. test-driven development). It might even help to have a different AI write those tests.
- Then once the code has been written and is passing the tests, then add actions to cull & consolidate most of the low-level tests into fewer, high-coverage integration or browser-automated-E2E tests, where the main goal is for these to catch regressions in future.
- Mocks are a big part of the brittleness and rot over time. So I'm moving away from mocks. I'm following
__Supabase's advice__for testing to write to the main dev database and use random IDs for isolation. I'm even moving towards using real LLM calls in tests, perhaps even with the actual production model. It's slower, and more expensive, but remember that we're working as though AI is free and instantaneous - so the wallclock time for the tests matters less, and in practice I think the cost of the LLM during tests will be rounding error. - I'm making much heavier use of browser-automated end-to-end (E2E) tests with Playwright (see below). This requires investment in setting up
__Playwright__:- Setup
__Playwright MCP__. - Add a note to the rules file to always run Playwright in
*headless*mode (so that the browser window doesn't pop up and interrupt you) and in*isolated*mode (so it can run in parallel). - Provide instructions for authentication, e.g. a hardcoded dev username + password so that Playwright can log in to your dev server.
- Always run Playwright with a subagent, so that its verbose output doesn't fill up the context window.

- Setup
- And I'm trying to update my rules file and planning docs to ensure that the tests get run & addressed more regularly. Maybe Git-commit hooks or Claude Code hooks could help here.

In practice, I find that I'm still doing a lot of manual review & testing at the end of each planning doc stage. This is a nuisance, but as the AIs are getting better, they can do larger and larger chunks of work correctly, and fix bugs quickly. So my main goal for automated testing is to notice regressions, i.e. so that the AI will notice new bugs that it accidentally introduced as its changing code.

# Invest in __handy scripts__

MCP is great. But it's complicated, often verbose about context, non-deterministic, and often overkill. So if you find yourself wanting to do the same thing often, you're much better off asking the AI to write a script (referring to your code guidelines doc for command-line libraries and patterns), with nice documentation, optional arguments, examples in your rules file, etc. Then you can just tell it to call that script later.

e.g. to __sync across your Git worktrees__, generate date/time prefixes for your file names, restart the dev webserver in the background, etc.

# Run multiple Git __worktrees__

Each worktree should have its own port, dev server, desktop, etc - but share the same dev database.

- Currently, I'm not using any kind of pull requests or feature-specific branches (except occasionally for big, risky refactors). Each Git worktree is already its own branch, but regularly sync them all into main and back. So, in effect, all of the agents are working out of main except they're blind to each other's uncommitted changes. (Part of the reason this works is that the
__planning doc__stages are supposed to end with working code.) - This aims to avoid/minimise merge conflicts, because they are a source of complexity and screw-ups that could require tiring human intervention. This way I can rely on AI to
__resolve merge conflicts itself__. - To sync:
__run this command__from the main folder, and it will automatically pull in changes from the other worktree branches into main as the hub, and then back out to each of them.

# Misc tips

- Make the AI write the Git commits. Instruct them to include lots of detail in the Git message, so that if you need to know something about the Git history, it'll be easier for the AI to inspect it and report back.
- If you have a good conversation but you don't quite feel ready to turn it into a plan yet, then capture the conversation for future reference.
- Allow yourself to occasionally have fun with
__playful features__that might have taken a human hours to do, but take <5 mins of human-time. It's pretty easy to do things that would've otherwise taken hours in less than an hour. - Learn about prompt engineering, from the Anthropic docs and tutorial. For experts, Sander Schulhoff on Lenny's podcast has useful tips, e.g. it's often better to go back and edit the original message rather than adding in the information piecemeal through multi-step conversation.

## These look promising but I haven't properly tried them yet

__Claude Code custom hooks__, e.g. to run linter, type-checker, and tests before Git commit. These look useful. So far, I've relied on my__meta-instructions for writing planning documents__to add these as actions at the appropriate point.- Writing custom MCPs. Instead, I've invested in rich instruction & reference docs, scripts, and subagents. If I was working in Cursor more (which doesn't have subagents), I would definitely have written/adopted an MCP-subagent (or a variety of them) by now to externalise context-verbose work.
__Custom subagents__and__commands__. These look interesting, but I've stuck with Markdown prompts for now, because they're portable across Claude Code, Cursor, etc.- Other IDEs beyond Claude Code and Cursor. I like the philosophy behind Cline and Aider, the ideas in Kiro look congenial, and
__Peter Nixey__and__Alex Appelbe__swear by__Windsurf__. (I would love an IDE with tighter browser integration, because Playwright MCP continues to feel brittle and verbose, but I didn't initially find that Windsurf helped with that.) __Replit__,__Lovable__,__Bolt__,__v0__, etc.__Joshua Wohle__is especially bullish about Replit, because it handles all the devops for you (hosting, database, etc), and you can combine it with Claude Code/Cursor for frontier model magic. But I'm a little wary about potential barriers to exit, I want control over architecture decisions, and I bet that frontier models will continue to improve so fast that I'd rather rely on their magic directly. (For I wasn't a developer, I certainy would give them a try.)

# Postscript

I'm about to launch __Spideryarn__ in alpha (a tool for researchers to get more from what they read), where every line of code was written by AI. And before that, AI did the late-stage work on Hello Zenno.

If you found this useful, subscribe for monthly posts on software, AI, and management.

Or drop me a line at consulting@gregdetre.com if you'd like help training your software engineering team on AI techniques or building products with AI.

# Acknowledgements

Thank you to __Marc Zao-Sanders__, __Johnnie Ball__, __Joshua Wohle__, __Ed Dowding__, Ian Broom, __David Hathiramani__, __Peter Nixey__, __Glenn Smith__, __Ian Strang__, __Martijn Verburg__, for ideas and comments.

# Useful references

On the importance of managing context

Other field guides:

- https://newsletter.pragmaticengineer.com/p/amazon-google-and-vibe-coding-with (from 45:16)
__https://allenpike.com/2025/coding-agents____https://blog.nilenso.com/blog/2025/05/29/ai-assisted-coding/__- https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/