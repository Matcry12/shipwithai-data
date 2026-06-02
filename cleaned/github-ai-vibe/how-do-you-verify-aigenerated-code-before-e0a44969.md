---
title: How do you verify AI-generated code before deploying? Do you even bother?
source_url: https://www.reddit.com/r/GithubCopilot/comments/1qz3on6/how_do_you_verify_aigenerated_code_before/
source_domain: reddit.com
topic: github-ai-vibe
doc_type: other
published_date: '2026-02-08'
fetched_at: '2026-05-29T13:38:50.356555+00:00'
language: en
word_count: 1039
reading_time: 6
signal_score: 1.0
status: kept
core_question: How do you verify AI-generated code before deploying?
tldr: 'How do you verify AI-generated code before deploying? Do you even bother? # How do you verify AI-generated
  code before deploying? Do you even bother? How do you verify AI-generated code before deploying? Do
  you even bother? I''ve been relying on Cursor and Claude to write most of my code'
key_topics:
- ai
- coding
- development
- agent
- agentic
- testing
- workflow
- tool
entities:
  primary: How
  aliases:
  - How
  - you
  - verify
content_hash: sha256:e758218557fe2e6a49b909d20f0b2d71276d90a349c422104fdc89d0c81cd588
---

# How do you verify AI-generated code before deploying? Do you even bother?

How do you verify AI-generated code before deploying? Do you even bother?

I've been relying on Cursor and Claude to write most of my code recently. It works, but I honestly have no idea if what I'm shipping has security issues or bad practices I'm not catching.

I tried ESLint and Semgrep but the output is a wall of jargon that doesn't mean much to me.

Curious how others handle this:

- Do you review AI-generated code before deploying, or just trust it?

- If you do review, what's your process?

- Has anyone actually been burned by a security issue in AI-generated code?

You're likely going to find eves possible opinion on this. My own: AI code needs to be heavily reviewed, ideally 95% of that being automated so that you don't have to spend too much time reviewing. Blindly accepting code is something I only do for private projects with low stakes.

Thanks for your reply. How did you implement the automation? And would you mind sharing any best practices?

Have other AIs review it, I usually have two different models review them.

Did it actually uncover a lot of issues?

Yes, I use opus , gemini 3 pro high , gpt5.2 to review others. But sometimes it can lead to overthinking. You have be very conscious of what you are doing. I only do this for core functions because it burns tokens and needs a lot of time

3-4 passes of reviewing by another LLM or the same one with a clean context. Followed by continuous manual review and nudging in different directions during review and code creation.

How do you conduct security checks? Do you use any dedicated tools, or just rely on static code analysis?

Yes, in my workflow there should be three stages of review: review with other models- eg implementation done with opus, review with chatgpt codex then validate the review with sonnet and implement it, your review and a peer dev review before actual QA testing.

What are the main areas of review? Code quality and security?

I might not be so strict about code style but the performance capacity, limitations and security need to be checked. I've seen even good coding models forget about things like multi tenancy, the volume of the data they are processing etc. their primary goal as a developer persona is to deliver the code in a similar fashion how it sees other is your examples unless otherwise instructed.

It heavily depends on the tech stack and what you are actually building….

Yes, I usually use JavaScript or TypeScript to develop web applications.

You should likely tell more about what you are building :)

The same way you do your own code. Unless it's a toy project you should be confident in your code before you deploy.

It's AI-generated, so I'm worried something might go wrong – I honestly don't have much confidence in it.

Yep, so at the least you'll want to read the code to understand what each section is doing. Sometimes the exact details don't matter too much, if it works, it works, but other times you'll want to confirm it covers the edge cases you care about.

For any change, you'll want to test it too and make sure it works. Unit/acceptance tests are great and help more the larger the scale of the project is, but just testing it manually after each change helps a lot.

If you don't do these, you're really rolling the dice on whether the AI guessed what you wanted correctly. The AI will also perform worse as time goes on and the code gets messier and unorganised if you don't review/refactor as you go.

I review all of it and make it modify it until it looks handcrafted. It's still saving me a lot of time.

I find less so with Opus 4.5 and now Opus 4.6. I can do fairly large refactors or add features.

In the past with other models, there would have been a lot more back and forth, correcting mistakes or clarifying misunderstandings, reviewing the code and testing to make sure it did what it said it would.

But now I make sure everything is planned out well in markdown files, then Opus does its thing. At first I'd review/test. But recently I've been finding that Opus just gets things right, and usually can figure out on its own if something is going to cause an issue. It's quite amazing really. Comparing agentic development now to a few months ago, progress has been crazy.

But I do get other models like Gemini to do occasional audits and reviews too.

On my current project, every time a new model comes out, I get it to audit and optimise as much as it can. Has worked very well.

Tell it you like TDD. It'll write tests and then make the code pass the tests. Make sure you tell it not to allow any workarounds or edits to tests without your review. Have agents review your PRs. Establish very precise GitFlow/Workflow. It all helps but nothing is perfect.

The models are getting so much better it won't be long before there are no more human PR reviewers. There will be (or already are) humans directing teams of agent reviewers.

Hello u/That-Row1408. Looks like you have posted a query. Once your query is resolved, please reply the solution comment with "!solved" to help everyone else know the solution and mark the post as solved.

*I am a bot, and this action was performed automatically. Please **contact the moderators of this subreddit** if you have any questions or concerns.*

Write your own tests €^ not the ones it creates and edits to pass (edits the test, not the code). lol

I use an azure-security reviewer skill created with skill-creator that I use to evaluate all code and applications I create. It includes domain knowledge specific for my needs. It always catches things I need to fix before releasing. You can do this for your stack as well. Vercel labs has some good ones for react and supabase.

Never deploy non-reviewed code, AI-generated or not.
