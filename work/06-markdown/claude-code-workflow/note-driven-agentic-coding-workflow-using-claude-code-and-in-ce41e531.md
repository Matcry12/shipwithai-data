---
title: Note-driven agentic coding workflow using Claude Code and Inkdrop
source_url: https://www.devas.life/note-driven-agentic-coding-workflow-using-claude-code-and-inkdrop/
source_domain: devas.life
topic: claude-code-workflow
doc_type: how-to-guide
author: Takuya Matsuyama
published_date: '2026-01-29'
fetched_at: '2026-05-25T06:44:11.155894+00:00'
language: en
word_count: 417
reading_time: 3
signal_score: 0.8475
status: kept
core_question: How can developers use Inkdrop as a backend for Claude Code planning to improve readability
  and tracking?
tldr: Note-driven coding workflow using Claude Code and Inkdrop for storing and tracking AI-generated
  plans with beautiful markdown rendering and revision history.
key_topics:
- Claude Code
- Inkdrop
- workflow
- MCP
- planning
- notes
- AI coding
entities:
  primary: Note-driven AI coding workflow
  aliases:
  - Claude Code Inkdrop integration
  - AI-assisted development
  - plan management system
content_hash: sha256:54da934f071c546f2ac3537ee787fd2ab5d6f6ed6ddf1b60b79dea5730a928c5
---

# Note-driven agentic coding workflow using Claude Code and Inkdrop

Hey, what's up? It's Takuya. I came up with another AI coding workflow that is note-driven, using Claude Code and Inkdrop. When I was using Claude Code's plan mode, I found the generated plans hard to read on the terminal because the CLI is not optimal for viewing Markdown documents. So, I tried using Inkdrop as a backend store through its MCP server for Claude Code to store its plans to solve this issue.

I shared a demo on YouTube, so please check it out:

And here are the config files:

This repository is based on Affaan's one. You can copy and paste the md files into your `.claude`

folder.

## Why Note-Driven?

Of course, it can be done by simply opening local md files on VSCode. But, by storing plans in Inkdrop, you get:

**Beautiful markdown rendering**- Plans are much easier to read with proper formatting, syntax highlighting, Mermaid diagrams, and LaTeX math blocks**Easy to edit**- Modify the plan before confirming, add notes, or adjust steps directly with the robust Markdown editor in Inkdrop**Multi-device review**- With data sync across platforms, review and edit plans from any device, including your phone**Revision history**- Track exactly when work started, what changed, and when it completed, with Inkdrop's revision history**Progress tracking**- Watch checkboxes get ticked off and note status updates appear in real-time

## How It Works

**Request a plan**- Run the`/plan`

command with your task description**Plan is created**- Claude Code analyzes the codebase and generates a detailed implementation plan**Saved to Inkdrop**- The plan is automatically saved as a note with status`none`

**Review and confirm**- Read the plan in Inkdrop's markdown renderer, then confirm to proceed**Execution begins**- Status changes to`active`

, work starts**Progress updates**- Checkboxes are checked off, deviations annotated, blockers noted**Completion**- Status changes to`completed`

, outcome section appended

Check out the repository for more detailed instructions.

## Idea: Creating a CLI tool like Beads?

This workflow makes me think of creating a CLI tool like Beads:

This tool helps AI agents remember context by providing a simple issue tracker designed for them. Beads uses SQLite as a backend store, but I think it is also possible to use Inkdrop as a database, as demonstrated in the above video. It lets you focus on writing concepts, ideas, specifications, designs, and so on. In other words, it means AI agents take notes for *themselves* because they forget things due to the context window size, just like us. What do you think?
