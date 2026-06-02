---
title: Shipping Faster Doesn’t Mean You Understand What You’ve Shipped
source_url: https://scalac.io/blog/shipping-faster-vs-understanding/
source_domain: scalac.io
topic: github-ai-vibe
doc_type: opinion
author: Piotr Borkowicz
published_date: '2026-05-28'
fetched_at: '2026-05-29T13:38:13.443469+00:00'
language: en
word_count: 1232
reading_time: 7
signal_score: 1.0
status: kept
core_question: Does faster shipping with AI tools mean developers actually understand what they've built?
tldr: Critical examination of how AI increases developer confidence without understanding, arguing that
  shipping speed doesn't equal code comprehension and questioning the viability of AI-only development.
key_topics:
- AI coding assistants
- code comprehension
- security risks
- developer expertise
- production systems
- code review
entities:
  primary: AI-assisted development risks
  aliases:
  - vibe coding pitfalls
  - code comprehension gaps
content_hash: sha256:9d4f236f42841cb7ef9d64b5922def857b1cd654454eedc10c435b01967c8a9e
---

# Shipping Faster Doesn't Mean You Understand What You've Shipped

*By Łukasz Marchewka, Software & solution architect, CTO at Scalac*

Developers are shipping more than ever. Managers are seeing faster output than ever. The metrics look good. The pipeline is green.

At some point, the question of whether anyone actually understands what's being built stopped feeling urgent. That's what I want to talk about.

**The illusion that it works**

AI adds one particularly dangerous ingredient: confidence.

A Stanford study on AI-assisted development found that participants using an AI coding assistant wrote significantly less secure code than those who did not, while also being more confident that their code was secure.

That is the specific thing AI adds. Not the underlying problem itself, but the feeling that there is no problem.

The distance between "it seems to work" and "it works correctly when it actually matters" has always existed. AI does not create that gap. It just makes people feel more comfortable standing in it.

A weaker developer with a strong AI assistant can produce things they would not have been able to produce before. That can be useful. It can also be risky.

Because if they cannot inspect, verify, and reason about what was generated, they are not using a tool. They are depending on one.

And the system gives them confidence before it gives them evidence.

**Code the author can't explain**

I keep a simple rule: no pull request over 300 lines. Not because large PRs are always bad. But a thousand-line review bounces between reviewer and developer until someone gets tired, and eventually something ships not because it is ready, but because the team ran out of energy to push back.

That rule matters more now than it ever did. Today I regularly see PRs well over a thousand lines, and they are easy to produce. An afternoon with an AI assistant and you have more code than a team used to write in a week.

The problem is not the size itself. It is what the size hides. Ask the author why it works and they go quiet. Ask what happens under load, or in an edge case, and they are guessing. They generated the shape of a solution, but not the understanding behind it.

Developers have always copied from Stack Overflow, adapted snippets from blog posts, and hoped the context was close enough. AI is the same instinct, only faster and better formatted. The output looks polished: clean names, consistent structure, sensible-looking abstractions. That makes it harder to challenge in review than messy human-written code. At least messy code admits something is unfinished.

Breaking that output into reviewable pieces requires understanding it first. That is often exactly what is missing. The cognitive load did not disappear. Writing got cheaper. Reading got more important.

You can use AI to help with review. I do, sometimes. But the judgment still has to be yours. The moment you outsource that, you are not reviewing anymore. You are approving.

**"Anyone can build production systems now"**

Two claims keep coming up that I don't believe.

The first: real projects can now be built in hours or days. You can build a proof of concept in hours. You can ship an impressive demo in a day. But I've been waiting for someone to show me a genuinely valuable production system built that way. Not a toy. Not a demo. Not a landing page wrapped around generated code. A real system people would pay for and trust. So far, I haven't seen it.

Take Clockify. It works not because someone generated screens and endpoints quickly, but because teams spent years understanding what users actually need, then built around reliability, permissions, billing, data integrity, security, reporting, and all the edge cases that only appear in production. Would you run your company's billing on a clone built in three hours? Would you put your revenue and reputation on it?

The second claim: we no longer need traditional developers, just vibe coders. People who prompt instead of program.

Think about surgical robots. They exist, they're precise, they're already in operating rooms. Nobody looked at that and said we no longer need surgeons. You wouldn't let a patient describe their symptoms to a robot and call it healthcare.

Software is the same. How do you evaluate what AI produced if you don't understand the consequences of what you asked for?

Teams will get smaller. That's probably unavoidable. But there's a difference between reducing headcount responsibly and betting the company on the assumption that AI replaces the people who actually understand the system.

The spreadsheet shows salaries. It doesn't show who knows why the billing logic works the way it does, who gets called at 2am when something breaks, who can tell the difference between a generated fix and a correct one. Cut those people and you don't have a leaner team. You have a team that can ship until something breaks.

**Generation is the easy part**

I work mostly at the level of architecture, design, trade-offs, direction. AI helps with execution — generating boilerplate, drafting configuration, speeding up repetitive and creative work. I won't pretend otherwise.

But executing faster and understanding what you've built are not the same thing.

We were building complex GitHub workflows. AI generated around twenty separate inputs to control the pipeline. Technically it covered every case. On paper it was complete.

When I reviewed it, something was off. Most teams don't think about pipelines by controlling every individual job. They think in stages, groups of jobs, operational intent. The inputs were correct in isolation. They just didn't match how anyone would actually use the pipeline.

Generating the original inputs took almost no time. Getting to a version that matched how the pipeline would actually be used took a longer back-and-forth with the model — longer than expected, but worth it. That process surfaced two edge cases I hadn't considered at first.

That back-and-forth is the work.

The first output gives you something to react to. The value comes from pushing against it, questioning it, reshaping it until it matches the real problem. That is where understanding develops. If you skip that conversation, you may still get code that passes every check. But you also skip the part where you learn why it works, where it breaks, and what trade-offs you accepted along the way.

The first output gives you something to react to. The value comes from pushing against it, questioning it, reshaping it until it matches the real problem.

**Understanding is still the job**

AI made the first version cheaper. That is useful. Sometimes very useful. A workflow appears faster, a draft is ready sooner, and a tedious piece of configuration takes minutes instead of hours.

But the first version is not where software usually gets expensive.

It gets expensive later, when that workflow has to support a real release process. When the billing logic has to change without breaking old invoices. When an incident happens and the person on call has to understand not only what the system does, but why it was built that way.

That is the part I would not outsource too quickly.

Sure, use AI to move faster. Use it to get to the first version sooner. But do not confuse producing code with owning a system.

Those are different jobs. And production only cares about the second one.
