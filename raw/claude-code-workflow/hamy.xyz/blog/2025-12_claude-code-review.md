---
source_url: https://hamy.xyz/blog/2025-12_claude-code-review
title: "How To Run In-Terminal Code Reviews with Claude Code"
crawl_depth: 0
crawled_at: 2026-05-05T14:36:11Z
word_count: 534
---

* [![](https://hamy.xyz/static/images/hamy-logo-terminal-garden_horizontal_1k_0.png)](https://hamy.xyz/)


# How To Run In-Terminal Code Reviews with Claude Code
Essay - Published: 2025.12.03 | 1 min read (493 words)  
[claude-code](https://hamy.xyz/tags/claude-code) | [create](https://hamy.xyz/tags/create) | [software-engineering](https://hamy.xyz/tags/software-engineering)
DISCLOSURE: If you buy through affiliate links, I may earn a small commission. [(disclosures)](https://hamy.xyz/blog/disclosures)
I previously shared [how I review code with AI](https://hamy.xyz/blog/2025-10_ai-code-review) and have since iterated on my approach.
Here's how I've been doing AI code reviews in my terminal using Claude Code.
## Simple Code Review
Most of the time I just need a simple code review to get feedback on my direction and sanity check if anything has gone off the rails.
My current prompt for this is:

```
Review the code in this PR - Provide feedback and list the top 5 things we could do to improve it ranked by criticality and level of effort.

```

Some changes from my previous prompt:
  * **Provide feedback** - to get a summary of where the code is good and could use improvement
  * **Increase ideas from 3 to 5** - At least half of the ideas are usually bad so more ideas means more hits
  * **Rank by criticality** - to highlight the ones you should focus on
  * **Rank by level of effort** - to help determine if this should be in this PR or better served as a fast follow / separate workstream


In general this prompt typically gives ~2 ideas that are worth implementing and can be run in ~30s which is pretty good ROI.
## Code Review with Tooling
This next code review is basically the same as above but we ask Claude Code to run tools and parse outputs to help provide data for the code review. It uses sub agents to protect the main agent's context and parallelize the tasks.
  * Runs tests
  * Runs lints
  * Performs code review


This provides a more comprehensive check of where the code's at and what needs to be changed.

```
Run the following steps in parallel with a generic subagent for each one.
				
1. Run tests on the files in my current commit. Summarize the broken tests in an easy to read format so I can go and debug.
2. Run lint on the files in my current commit. Summarize the failed lints in an easy to read format so I can go and debug.
3. Review the code in the commit - List the top 5 things we could do to improve it ranked by criticality and level of effort.

```

## Next
That's how I've been getting fast, "local" (it still talks to central servers) code reviews with Claude Code.
I've also been playing around a bit with cloud-first code reviews with tools like Claude Code Cloud and Codex but we'll leave that for another time.
If you liked this post you might also like:


## Want more like this?
The best way to support my work is to like / comment / share this post on your favorite socials.


#### Inbound Links


#### Outbound Links


### Connect with Me
[YouTube (HAMY LABS)](https://youtube.com/@HAMYLABS)[Blue Sky (sirhamy.bsky.social)](https://bsky.app/profile/sirhamy.bsky.social)
### Subscribe for Updates
[RSS Feed](https://hamy.xyz/blog/rss)[Email List](https://hamniverse.substack.com/)[Podcast](https://hamy.xyz/blog/hamy-labs-pod)
### Support this blog
[Become a HAMINIONs Member](https://hamy.xyz/blog/haminions)[Shop HAMY Merch](https://shop.hamy.xyz/)[Sponsor HAMY LABS](https://hamy.xyz/blog/sponsors)
Built with [CloudSeed Rust](https://cloudseedrust.com)
