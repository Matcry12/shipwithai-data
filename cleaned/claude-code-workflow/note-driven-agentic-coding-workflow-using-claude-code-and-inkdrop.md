---
title: "Start the conversation"
topic: "claude-code-workflow"
career_level:
  - senior
  - executive
source_url: "https://www.devas.life/note-driven-agentic-coding-workflow-using-claude-code-and-inkdrop"
source_domain: "www.devas.life"
word_count: 539
text_to_link_ratio: 0.6435
signal_score: 0.6435
is_curated: false
tags:
  - open-source
  - executive
ingested_at: "2026-05-05"
---

Hey, what's up? It's Takuya. I came up with another AI coding workflow that is note-driven, using Claude Code and [Inkdrop](https://www.inkdrop.app/?utm_source=devas.life&utm_medium=web&utm_campaign=blog&utm_content=note-driven-agentic-coding-workflow-using-claude-code-and-inkdrop). When I was using Claude Code's plan mode, I found the generated plans hard to read on the terminal because the CLI is not optimal for viewing Markdown documents. So, I tried using Inkdrop as a backend store through its [MCP server](https://github.com/inkdropapp/mcp-server?ref=devas.life) for Claude Code to store its plans to solve this issue.
I shared a demo on YouTube, so please check it out:
And here are the config files:
[ GitHub - inkdropapp/note-driven-agentic-coding-workflow: Complete Claude Code configuration collection - agents, skills, hooks, commands, rules, MCPs. Battle-tested configs from an Anthropic hackathon winner. Complete Claude Code configuration collection - agents, skills, hooks, commands, rules, MCPs. Battle-tested configs from an Anthropic hackathon winner. - inkdropapp/note-driven-agentic-coding-workflow ![](https://storage.ghost.io/c/d0/bc/d0bc0a46-ecd4-4f66-8377-998e00d2e3f7/content/images/icon/pinned-octocat-093da3e6fa40-9.svg)GitHubinkdropapp ](https://github.com/inkdropapp/note-driven-agentic-coding-workflow?ref=devas.life)
This repository is based on [Affaan's one](https://github.com/affaan-m/everything-claude-code?ref=devas.life). You can copy and paste the md files into your `.claude` folder.
## Why Note-Driven?
Of course, it can be done by simply opening local md files on VSCode. But, by storing plans in Inkdrop, you get:
  * **Beautiful markdown rendering** - Plans are much easier to read with proper formatting, syntax highlighting, Mermaid diagrams, and LaTeX math blocks
  * **Easy to edit** - Modify the plan before confirming, add notes, or adjust steps directly with the robust Markdown editor in Inkdrop
  * **Multi-device review** - With data sync across platforms, review and edit plans from any device, including your phone
  * **Revision history** - Track exactly when work started, what changed, and when it completed, with [Inkdrop's revision history](https://docs.inkdrop.app/reference/revision-history?ref=devas.life)
  * **Progress tracking** - Watch checkboxes get ticked off and note status updates appear in real-time

![](https://storage.ghost.io/c/d0/bc/d0bc0a46-ecd4-4f66-8377-998e00d2e3f7/content/images/2026/01/2026-01-23-Note-driven-agentic-coding-3.jpg)Generated plan that include a Mermaid diagram
## How It Works
  1. **Request a plan** - Run the `/plan` command with your task description
  2. **Plan is created** - Claude Code analyzes the codebase and generates a detailed implementation plan
  3. **Saved to Inkdrop** - The plan is automatically saved as a note with status `none`
  4. **Review and confirm** - Read the plan in Inkdrop's markdown renderer, then confirm to proceed
  5. **Execution begins** - Status changes to `active`, work starts
  6. **Progress updates** - Checkboxes are checked off, deviations annotated, blockers noted
  7. **Completion** - Status changes to `completed`, outcome section appended

![](https://storage.ghost.io/c/d0/bc/d0bc0a46-ecd4-4f66-8377-998e00d2e3f7/content/images/2026/01/2026-01-23-Note-driven-agentic-coding-4.jpg)Check the work progress on revision history
Check out the repository for more detailed instructions.
## Idea: Creating a CLI tool like Beads?
This workflow makes me think of creating a CLI tool like Beads:
[ GitHub - steveyegge/beads: Beads - A memory upgrade for your coding agent Beads - A memory upgrade for your coding agent. Contribute to steveyegge/beads development by creating an account on GitHub. ![](https://storage.ghost.io/c/d0/bc/d0bc0a46-ecd4-4f66-8377-998e00d2e3f7/content/images/icon/pinned-octocat-093da3e6fa40-10.svg)GitHubsteveyegge ](https://github.com/steveyegge/beads?ref=devas.life)
This tool helps AI agents remember context by providing a simple issue tracker designed for them. Beads uses SQLite as a backend store, but I think it is also possible to use Inkdrop as a database, as demonstrated in the above video. It lets you focus on writing concepts, ideas, specifications, designs, and so on. In other words, it means AI agents take notes for _themselves_ because they forget things due to the context window size, just like us. What do you think?
##  DiscussionMember discussion
0 comments
# Start the conversation
Become a member of Takuya Matsuyama to start commenting.
Sign up now
Already a member?Sign in
## Read more
### [10 years of indie dev: How I went global from Japan (talk w/ Hiroshi) - Part 1/2 I joined Hiroshi's podcast episode a few weeks ago. We shared our experience and knowledge on indie dev. I'd like to cross-post our talk in English here. I also tried to create an English dub using AI. The voice cloning quality is quite impressive, so I ](https://www.devas.life/10-years-of-indie-dev-how-i-went-global-from-japan-talk-w-hiroshi-part-1-2/) ### [What a Japanese cooking principle taught me about overcoming AI fatigue Hey, what's up? It's Takuya. I've been thinking about how to live well in this AI era as a developer, content creator, and artist. By “living well,” I mean enjoying the act of creating while maintaining good mental health. I imagine many of my ](https://www.devas.life/what-a-japanese-cooking-principle-taught-me-about-overcoming-ai-fatigue/) ### [How to run Claude Code in a Tmux popup window with persistent sessions Hey, what's up? It's Takuya. I've been using Claude Code in my terminal workflow. At first, I was running it at the right side of my terminal using tmux, but I found it not useful because it was too narrow to display messages and ](https://www.devas.life/how-to-run-claude-code-in-a-tmux-popup-window-with-persistent-sessions/) ### [I made my Keychron K2 HE stealthy Hey guys, I've got a new keyboard: Keychron K2 HE and customized it with blank black and wooden keycaps. So, I'd like to share how I did it. Here is a video: Unboxing The above keyboard is Keychron Q1, which I've been using for ](https://www.devas.life/i-made-my-keychron-k2-he-stealthy/)
