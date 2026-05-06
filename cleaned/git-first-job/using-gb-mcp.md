---
title: "Using the GitButler MCP Server to Build Better AI-Driven Git Workflows"
topic: "git-first-job"
career_level:
  - executive
source_url: "https://blog.gitbutler.com/using-gb-mcp"
source_domain: "blog.gitbutler.com"
word_count: 1270
text_to_link_ratio: 0.8909
signal_score: 0.8909
is_curated: false
tags:
  - remote
  - executive
ingested_at: "2026-05-05"
---

3 months ago by [Estib Vega](https://blog.gitbutler.com/author/estib)
5 min read
[git](https://blog.gitbutler.com/tag/git)[mcp](https://blog.gitbutler.com/tag/mcp)[gitbutler](https://blog.gitbutler.com/tag/gitbutler)[model context protocol](https://blog.gitbutler.com/tag/model%20context%20protocol)[artificial intelligence](https://blog.gitbutler.com/tag/artificial%20intelligence)[ai coding](https://blog.gitbutler.com/tag/ai%20coding)
# Using the GitButler MCP Server to Build Better AI-Driven Git Workflows
By exposing GitButler functionality through the Model Context Protocol, the MCP server allows AI tools to interact directly with your Git workflow.
As AI coding becomes more common, one problem keeps coming up. The code gets generated quickly, but version control still feels bolted on after the fact. You write or modify files with an AI assistant, then manually stage, commit, and clean things up once the task is done.
The GitButler MCP server closes that gap.
By exposing GitButler functionality through the Model Context Protocol, the MCP server allows AI tools to interact directly with your Git workflow. Instead of treating Git as a separate manual step, your assistant can record changes, create commits, and manage branches as part of the same workflow that generated the code.
This post walks through how the GitButler MCP server works, how to set it up, and how to use it effectively in real development workflows.
## What the GitButler MCP Server Actually Does
The GitButler MCP server is a small service that runs locally and exposes GitButler actions to AI tools that support MCP. When an AI assistant connects to it, it can call specific features like updating branches or recording changes.
From a practical standpoint, this means your AI assistant can:
  * Capture file changes without you running Git commands
  * Create structured commits with useful context
  * Keep branches up to date automatically
  * Coordinate changes across multiple edits or prompts


The server is started with a simple command:
BASH

```
but mcp

```

This launches the MCP server over standard input and output so editors and AI tools can communicate with it.
There is also an internal mode:
BASH

```
but mcp --internal

```

This exposes additional tools that GitButler uses internally. Most users should stick with the default mode unless they know they need the extra surface area.
* * *
## Why This Matters for AI-Assisted Development
Without MCP integration, AI assisted workflows usually look like this:
  1. Prompt the assistant to generate or modify code
  2. Review the changes
  3. Manually decide what to stage
  4. Write a commit message
  5. Commit and manage branches yourself


With the GitButler MCP server in place, that flow can be reduced to:
  1. Prompt the assistant
  2. Let the assistant record and commit changes through GitButler


The key improvement is not just automation. It is context. The MCP server allows the assistant to pass along information about why a change was made, not just what files were modified. GitButler can then use that context to create better commits than a generic auto commit ever could.
* * *
## Setting Up the MCP Server
Before connecting anything, make sure the GitButler CLI is installed. You can install it from GitButler settings if it is not already available on your system.
Once installed, you can connect the MCP server to any MCP client.
### Cursor
Cursor uses a JSON configuration file to define MCP servers.
  1. Open Cursor settings and navigate to MCP servers
  2. Create or edit `~/.cursor/mcp.json`
  3. Add the GitButler configuration:


JSON

```
{"mcpServers":{"gitbutler":{"command":"but","args":["mcp"]}}}
```

After restarting Cursor, GitButler will be available to the assistant. You should see abilities like updating branches appear when the assistant lists available actions.
* * *
### VS Code
VS Code supports MCP through its command palette.
  1. Open the command palette
  2. Run “MCP: List Servers”
  3. Choose Add Server and select stdio
  4. Set the command to `but`
  5. Set the arguments to `["mcp"]`


VS Code will store this configuration in its MCP settings and automatically start the server when needed.
### Claude Code
Claude Code provides a simple CLI based setup.
Run the following command:
BASH

```
claude mcp add gitbutler but mcp

```

Then verify that it is registered:
BASH

```
claude mcp list

```

Once registered, Claude Code can call GitButler tools directly.
## Using the MCP Server Day to Day
Once the MCP server is connected, the most important tool you will interact with is the one that updates GitButler branches. This is the action that records changes and turns them into commits.
There are two main ways to use it.
### Manual Invocation
You can explicitly ask your AI assistant to update GitButler branches after a task is complete. This works well when you want full control.
For example:
“Update GitButler branches with these changes.”
This approach is predictable and easy to reason about.
### Rule Based Automation
Most tools allow you to define rules that automatically trigger MCP clients. This is where things get powerful.
A common rule looks like this:
If files were modified, run the GitButler update branches tool.
With this in place, every time the assistant edits code, GitButler records the change. You no longer need to remember to commit.
It is usually best to start conservative. Trigger commits only after meaningful changes rather than every single file edit. You can refine rules over time as you gain confidence.
## How GitButler Processes MCP Requests
When an MCP tool is called, GitButler does not blindly commit everything.
The process looks like this:
  1. The assistant sends file changes and contextual information to GitButler
  2. GitButler records the state of the working directory
  3. Commit metadata is generated using the context provided
  4. The commit is created and attached to the appropriate branch


You can inspect all of this in the GitButler UI. Every automated action appears in the Actions view, which makes it easy to understand what happened and when.
This visibility is important. Automation should never feel opaque, especially when it touches your Git history.
## Best Practices for Using the MCP Server Effectively
### Keep Commits Meaningful
Avoid committing on every single token of output from the assistant. Group related changes into logical units. This keeps your history readable and useful.
### Review Early and Often
Even with automation, take time to review commits in GitButler. This builds trust in the workflow and helps catch mistakes before they reach your remote repository.
### Use It with Branching Strategies
The MCP server works well alongside feature branches. You can let the assistant manage changes on a branch without touching main until you are ready.
### Do Not Remove Manual Escape Hatches
Automation should assist you, not trap you. Always be comfortable falling back to manual commits or direct GitButler actions when needed.
## Final Thoughts
The GitButler MCP server is not just about saving keystrokes. It changes how AI tools fit into real development workflows.
By letting assistants interact directly with GitButler, version control becomes part of the same feedback loop as code generation. Changes are recorded with context, commits stay readable, and developers stay in control.
If you are already using AI tools to write code, the MCP server is one of the cleanest ways to make sure your Git history keeps up with the speed of your ideas.
[![Estib Vega](https://blog.gitbutler.com/_next/image?url=%2Fprofiles%2Festib.jpg&w=256&q=75)](https://blog.gitbutler.com/author/estib)
Written by [Estib Vega](https://blog.gitbutler.com/author/estib)
Full-Stack Engineer. Using TypeScript and Rust @ GitButler
## More to _Read_
[![We’ve raised $17M to build what comes after Git](https://gitbutler-docs-images-public.s3.us-east-1.amazonaws.com/17-series-a.webp) We’ve raised $17M to build what comes after Git This monthby Scott Chacon4 min read GitButler has raised a Series A round to accelerate developing the infrastructure for how software gets built next. ](https://blog.gitbutler.com/series-a)[![The Great CSS Expansion](https://gitbutler-docs-images-public.s3.us-east-1.amazonaws.com/the-great-css-expansion.webp) The Great CSS Expansion 1 month agoby Pavel Laptev17 min read CSS now does what Floating UI, GSAP ScrollTrigger, Framer Motion, and react-select used to require JavaScript for. Here is exactly how much that saves, why these libraries were painful beyond their size, and what the platform still hasn't figured out. ](https://blog.gitbutler.com/the-great-css-expansion)[![Simplifying Git by Using GitButler](https://gitbutler-docs-images-public.s3.us-east-1.amazonaws.com/simplify-git.webp) Simplifying Git by Using GitButler 2 months agoby PJ Hagerty7 min read Git is great - and has been for twenty years. But in that time, how many of us have advanced our git skills? Most of us know about five or six commands: clone, status, push/pull, add, commit, branch, and checkout. ](https://blog.gitbutler.com/simplifying-git)
## Stay in the _Loop_
Subscribe to get fresh updates, insights, and  
exclusive content delivered straight to your inbox.  
No spam, just great reads. 🚀
