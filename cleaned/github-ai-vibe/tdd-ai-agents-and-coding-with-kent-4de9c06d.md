---
title: Kent Beck
source_url: https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent
source_domain: newsletter.pragmaticengineer.com
topic: github-ai-vibe
doc_type: case-study
author: Gergely Orosz
published_date: '2025-06-11'
fetched_at: '2026-05-29T13:38:10.258797+00:00'
language: en
word_count: 1186
reading_time: 6
signal_score: 1.0
status: kept
core_question: How does Kent Beck approach using AI coding agents and why is TDD still essential?
tldr: Interview with Kent Beck covering his 52-year programming career, extreme programming origins, and
  how test-driven development remains a superpower when using AI coding agents.
key_topics:
- test-driven development
- TDD
- AI agents
- extreme programming
- Kent Beck
- unit tests
- feature flags
entities:
  primary: Kent Beck and AI coding
  aliases:
  - test-driven development with AI
  - extreme programming evolution
content_hash: sha256:75d2133878511acb5167e959ee1d52b1ea7386488caa84f0eb03576f868d57c7
---

# Kent Beck

## Stream the Latest Episode

**Listen and watch now on YouTube, Spotify and Apple.** See the episode transcript at the top of this page, and timestamps for the episode at the bottom.

**Brought to You By**

• **Sonar** — Code quality and code security for ALL code.

• **Statsig** — The unified platform for flags, analytics, experiments, and more.

• **Augment Code** — AI coding assistant that pro engineering teams love

—

**In This Episode**

Kent Beck is one of the most influential figures in modern software development. Creator of **Extreme Programming (XP**), co-author of The Agile Manifesto, and a pioneer of **Test-Driven Development (TDD**), he's shaped how teams write, test, and think about code.

Now, with over five decades of programming experience, Kent is still pushing boundaries—this time with AI coding tools. In this episode of Pragmatic Engineer, I sit down with him to talk about what's changed, what hasn't, and why he's more excited than ever to code.

In our conversation, we cover:

Why Kent calls AI tools an "unpredictable genie"—and how he's using them

Why Kent no longer has an emotional attachment to any specific programming language

The backstory of The Agile Manifesto—and why Kent resisted the word "agile"

An overview of XP (Extreme Programming) and how Grady Booch played a role in the name

Tape-to-tape experiments in Kent's childhood that laid the groundwork for TDD

Kent's time at Facebook and how he adapted to its culture and use of feature flags

And much more!

## Takeaways

Some of the most interesting topics discussed were these:

**1. Kent is re-energized thanks to using AI agents to build stuff. **Kent has been coding for 52 years, and the last decade, he's gotten a lot more tired of all of it: learning *yet another* new language or framework, or debugging the issues when using the latest framework.

What he loves about these AI agents (and AI coding tools) is how he doesn't need to know *exactly* all the details: he can now be a lot more ambitious in his projects.

Currently, Kent is building a server in Smalltalk (that he's been wanting to do for many years) and a Language Server Protocol (LSP) for Smalltalk

**2. Test driven development (TDD) is a "superpower" when working with AI agents. **AI agents can (and do!) introduce regressions. An easy way to ensure this does not happen is to have unit tests for the codebase.

Kent Beck is one of the biggest proponents of TDD, so it's no surprise he is using this approach when coding with these agents as well. What *is* surprising is how he's having trouble stopping AI agents from deleting tests in order to make them "pass!"

**3. Facebook wrote no unit tests in 2011, and this stunned Kent, back in the day. **Kent joined Facebook in 2011, and was taken aback by the lack of testing and how everyone pushed code to production without automated testing.

What he came to realize – and appreciate! – was how Facebook had several things balancing this out:

Devs took responsibility for their code very seriously

Nothing at Facebook was "someone else's problem:" devs would fix bugs when they saw them, regardless of whose commit caused it

Feature flags were heavily used for risky code

Facebook did staged rollouts to smaller markets like New Zealand

To this date, Facebook ships code to production in a unique way. We covered more in the deepdive Shipping to Production.

**4. The "Extreme" in "Extreme Programming" was a marketing hack (kind of!) **Kent shared the hilarious story of how he came up with the name "Extreme Programming." He came up with a methodology that worked really well for one of his clients (which would become Extreme Programming) and wanted to name it. This is how:

"

I wanted to pick a word that Grady Booch would never say that he was doing.Because that was the competition! I didn't have a marketing budget. I didn't have any money. I didn't have that kind of notoriety [that Grady Booch already had]. I didn't have that corporate backing.So if I was going to make any kind of impact, I had to be a little bit outrageous. Extreme sports were coming up back then. And I picked that metaphor.

It's actually a good metaphor because extreme athletes are the best prepared, or they're dead. People so desperately wanted something kind of like that then it just exploded from there."

*We previously did an episode on Software architecture with Grady Booch.*

### Interesting quote: devs should experiment with GenAI

From 53:30:

Gergely: "I wonder if we're going back to discovering things that we you were popularizing in the 2000s."

Kent: "People should be experimenting. Try all the things, because we just don't know.

The whole landscape of what's 'cheap' and what's 'expensive' has all just shifted.Things that we didn't do because we assumed they were going to be expensive or hard just got ridiculously cheap. Like, what would you do today if cars were suddenly free? Okay, things are going to be different, but what are the second and third-order effects? Nobody can predict that! So we just have to be trying stuff."

**The Pragmatic Engineer deepdives relevant for this episode**

**Timestamps**

(00:00) Intro

(02:27) What Kent has been up to since writing Tidy First

(06:05) Why AI tools are making coding more fun for Kent and why he compares it to a genie

(13:41) Why Kent says languages don't matter anymore

(16:56) Kent's current project building a small talk server

(17:51) How Kent got involved with The Agile Manifesto

(23:46) Gergely's time at JP Morgan, and why Kent didn't like the word 'agile'

(26:25) An overview of "extreme programming" (XP)

(35:41) Kent's childhood tape-to-tape experiments that inspired TDD

(42:11) Kent's response to Ousterhout's criticism of TDD

(50:05) Why Kent still uses TDD with his AI stack

(54:26) How Facebook operated in 2011

(1:04:10) Facebook in 2011 vs. 2017

(1:12:24) Rapid fire round

**References**

**Where to find Kent Beck:**

• LinkedIn: https://www.linkedin.com/in/kentbeck/

• Website: https://kentbeck.com/

• Newsletter:

**Mentions during the episode:**

• *Extreme Programming Explained: Embrace Change*: https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658

• The Agile Manifesto: https://agilealliance.org/agile101/the-agile-manifesto/

• *Tidy First?: A Personal Exercise in Empirical Software Design*: https://www.amazon.com/Tidy-First-Personal-Exercise-Empirical/dp/1098151240

• Measuring developer productivity? A response to McKinsey: https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity

• Dead Code, Getting Untangled, and Coupling versus Decoupling: https://newsletter.pragmaticengineer.com/p/dead-code-getting-untangled-and-coupling

• Augment: https://www.augmentcode.com/

• Smalltalk: https://en.wikipedia.org/wiki/Smalltalk

• Swift: https://www.swift.org/

• Go: https://go.dev/

• Rust: https://www.rust-lang.org/

• Haskell: https://www.haskell.org/

• C++: https://isocpp.org/

• JavaScript: https://www.javascript.com/

• Managing the Development of Large Software Systems: https://www.praxisframework.org/files/royce1970.pdf

• Martin Fowler's website: https://martinfowler.com/

• DSDM: https://en.wikipedia.org/wiki/Dynamic_systems_development_method#

• *Crossing the Chasm, 3rd Edition: Marketing and Selling Disruptive Products to Mainstream Customers*: https://www.amazon.com/Crossing-Chasm-3rd-Disruptive-Mainstream/dp/0062292986

• Tottenham Hotspur: https://www.tottenhamhotspur.com/

• J.P. Morgan: https://www.jpmorgan.com/

• Software architecture with Grady Booch: https://newsletter.pragmaticengineer.com/p/software-architecture-with-grady-booch

• Grady Booch on LinkedIn: https://www.linkedin.com/in/gradybooch/

• The Philosophy of Software Design – with John Ousterhout: https://newsletter.pragmaticengineer.com/p/the-philosophy-of-software-design

• A Philosophy of Software Design: My Take (and a Book Review): https://blog.pragmaticengineer.com/a-philosophy-of-software-design-review/

• Cursor: https://www.cursor.com/

• Facebook Engineering Process with Kent Beck: https://softwareengineeringdaily.com/2019/08/28/facebook-engineering-process-with-kent-beck/

• Claude Code: https://www.anthropic.com/claude-code

• The Timeless Way of Building: https://www.amazon.com/Timeless-Way-Building-Christopher-Alexander/dp/0195024028

—

Production and marketing by Pen Name.
