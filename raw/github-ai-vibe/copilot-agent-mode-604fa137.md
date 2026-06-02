---
source_url: "https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-mode?view=visualstudio"
source_domain: "learn.microsoft.com"
topic: "github-ai-vibe"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-29T13:37:59.312143+00:00"
word_count: 1929
stage: "raw-extracted"
---

With the GitHub Copilot agent mode in Visual Studio, you can use natural language to specify a high-level task. AI creates a plan, makes code edits, runs terminal commands, invokes tools, and applies changes across your codebase. It monitors outcomes, such as build results, unit-test failures, or tool outputs, and iterates as needed.

Unlike ask mode, agent mode doesn't stop after a single response. It continues running and refining steps until you reach the goal in your prompt or more input is required.

In agent mode, Copilot operates autonomously and determines the relevant context for your prompt.

Follow these steps to get started:

Open the Copilot Chat window, select Ask to expand the mode dropdown, and then select Agent.

Enter your prompt, and then select Send or select the Enter key to submit it. You can specify a high-level requirement, and you don't have to specify which files to work on.

Agent mode might invoke multiple tools to accomplish different tasks. Optionally, select the Tools icon to configure which additional tools the agent can use for responding to your request.

Copilot requests confirmation before running a terminal command or using a tool that isn't built in.

Copilot automatically detects issues in code edits or terminal commands, and then takes action. The process repeats until the issues are resolved.

As Copilot processes your request, it streams the suggested code edits directly in the editor. Review the suggested edits and either:

Keep or discard the suggested edits as a whole in Total changes in the chat window.

Review individual file diffs and apply them selectively.

If you want to review individual code changes that the agent made, you can review the specific change at each step.

If you want to review individual code changes that the agent made, you can either:

Review the specific change at each step.

Review the cumulative changes from the last time that changes were kept or undone.

Continue to iterate on the code changes to refine the edits or implement more features.

Understand agent mode tools

Agent mode can use the following tools for responding to a request:

Agent skills that provide task-specific instructions

Tip

Visual Studio also includes built-in agents like @debug, @profiler, @test, and @vs that integrate with specific IDE features. In agent mode, @debug can guide bug reproduction, instrumentation and telemetry collection, and fix validation. You can also create custom agents for your team workflows. For more information, see Use custom agents in GitHub Copilot.

To view and manage the tools that are available in agent mode, select the Tools icon in the chat window.

Based on the outcome of a tool, Copilot might invoke other tools to accomplish the overall request. For example, if a code edit results in syntax errors in the file, Copilot might explore another approach and suggest different code changes.

Additional tools that you add by running MCP servers aren't automatically enabled. Their checkboxes are cleared by default, and you must select them to activate the tools.

find_symbol tool

The find_symbol tool brings language-aware symbol navigation directly to agent mode. When enabled, Copilot automatically uses find_symbol to:

Find all references to symbols across your project

Access metadata like type information, declarations, and scope

Once you enable the tool, Copilot uses it automatically when answering your questions or suggesting code changes.

Supported languages include C++, C#, Razor, and TypeScript, plus any other language for which you have a supported Language Server Protocol (LSP) extension installed.

For C++ projects, agent mode can also use C++ tools to navigate call and class hierarchies. For more information, see C++ code editing tools.

For best results, write clear prompts and use AI models that support tool-calling. For more information about model capabilities, see AI model comparison (GitHub Docs).

C++ code editing tools

When C++ code editing tools are enabled in the Tools list in Copilot Chat, agent mode can use these Visual Studio-specific tools:

get_symbol_call_hierarchy to traverse call hierarchies

get_symbol_class_hierarchy to navigate class and type hierarchies

These tools help the agent reason over C++ relationships so it can make more precise navigation and editing decisions. To use these tools, install the Desktop development with C++ workload. After these tools are available and enabled, agent mode uses them automatically when applicable.

Manage tool approvals

When Copilot invokes a tool, it requests confirmation to run the tool. The reason is that tools might run locally on your machine and perform actions that modify files or data.

In the chat window, after a tool invocation, use the Allow dropdown options to automatically confirm the specific tool for the current session or solution, or all future invocations.

You can reset tool confirmation selections in the Tools > Options pane. Expand the All Settings > GitHub > Copilot > Tools section.

You can reset tool confirmation selections in the Tools > Options dialog. Expand the GitHub > Copilot > Tools section.

Accept or discard edits

Copilot lists the edited files in the Total changes list in the chat window.

Select each file to review changes individually. You can keep or undo edits made to each chunk of code.

Alternatively, in the Total changes list, select Keep or Undo for all edits made since the last time that you selected Keep or Undo.

Tip

Starting in Visual Studio 2026 version 18.6, you can use the multi-file summary diff view to see all Copilot changes across multiple files in a single tab with granular accept and undo controls.

Revert edits

As you request code edits, you might want to revert some changes. To revert, select Restore next to the checkpoint before the prompt that includes changes you don't want.

Currently, the Visual Studio Copilot agent doesn't support stepwise undo or redo.

Interrupt an agent mode request

To interrupt an ongoing request, you can cancel it. Canceling a request stops all running tools and terminal commands.

To stop a build, select Build on the top toolbar, and then select Cancel. Or use the Ctrl+Break keyboard shortcut.

Planning in agent mode (Preview)

Note

Planning is available in public preview with Visual Studio 2022 version 17.14. This feature is under active development and might evolve based on user feedback.

Planning in agent mode allows Copilot to break down complex or multistep requests into structured, trackable tasks before execution.

When Planning is active, Copilot:

Creates a user-facing markdown plan that outlines goals and progress.

Maintains an internal JSON plan (plan-{sessionId}.json) that serves as an LLM-readable scratchpad for step tracking, reasoning, and coordination.

This structure helps Copilot stay consistent, update its plan dynamically, and provide developers with visibility into what it’s doing.

How it works

Request analysis

When a task requires multiple steps, Copilot enters planning mode.

Plan creation

Markdown plan: Describes the task, steps, and progress in a readable format.

JSON plan: A structured, LLM-readable format that captures the same plan in machine parsable form. This JSON file allows Copilot to update and interpret the plan consistently across turns.

Execution and iteration

Copilot executes each step in the plan, updating both files as it proceeds.

The markdown plan updates visibly in the editor.

The JSON plan evolves behind the scenes as Copilot refines, reorders, or adapts steps.

Storage

Both files are stored in C:\Users\username\AppData\Local\Temp\VisualStudio\copilot-vs.

Tools used in Planning

When you enable Planning, a dedicated set of internal tools becomes active. These tools coordinate how Copilot creates, updates, and finalizes plans during execution.

Tool

Description

plan

Generates the initial structured plan from the user request.

adapt_plan

Refines or adjusts the plan based on new context or feedback.

update_plan_progress

Updates step completion status and synchronizes plan state.

record_observation

Captures runtime results or insights that influence next actions.

finish_plan

Finalizes the plan once all steps are complete.

These tools allow Copilot to manage multi-step workflows incrementally, maintain execution state, and stay aligned with user intent.

Enabling and managing Planning tools

To enable Planning:

Open the Tools > Options pane, and expand the All Settings > GitHub > Copilot > Copilot Chat section.

Select the Enable Planning checkbox.

To enable Planning in Visual Studio 2022 version 17.14 or later:

Open the Tools > Options dialog and expand the GitHub > Copilot section.

Select the Enable Planning checkbox, and then select OK.

After you enable planning, the Planning tools appear in the Tools list in the chat window:

You can selectively disable the planning tool set directly in the Tools list in the chat window. If you need to disable planning tools, we recommend disabling all, not just one. Changes apply immediately to your current chat session.

Tip

Disabling individual tools allows you to experiment with different planning behaviors or debug specific steps during development.

Limitations

Plans are stored temporarily and deleted when the session ends unless saved manually.

Slight latency overhead exists due to structured state tracking.

Some specialized agents might not yet support planning.

What visibility does agent mode have into my files?

Agent mode can manipulate only:

Local files that are part of the solution.

Local files that are in the open solution directory or its subdirectories.

Agent mode can't access files and directories excluded through file exclusion.

For terminal commands, agent mode has the same permissions as the running Visual Studio process and isn't limited to the preceding restrictions. Carefully review proposed terminal commands before you run them.

I don't see ask mode and agent mode in the Copilot Chat window

Take the following troubleshooting steps in the specified order:

Make sure you're using Visual Studio 17.14 or later.

Check the version at Help > About Visual Studio.

If you're not using version 17.14 or later, open the Visual Studio Installer and update your build.

Confirm the Enable Agent mode in the chat pane option is selected.

In the Tools > Options pane, expand the All Settings > GitHub > Copilot > Copilot Chat section, and verify the option is selected.

In the Tools > Options dialog, expand the GitHub > Copilot section, and verify the option is selected under Copilot Chat.

Try restarting Visual Studio.

When should I use ask mode vs. agent mode?

Ask mode is excellent when you want 100% confidence that no code edits are made unless you explicitly select Apply or copy and paste the code yourself.

Agent mode can handle the same conceptual questions and generate code examples without applying them, along with its agent capabilities of editing code.

If you want to use MCP capabilities, you must have agent mode selected.

What happened to Copilot Edits in Visual Studio?

Agent mode is an evolution of Copilot Edits, with a greater ability to iterate on errors, use tools, and automatically apply code changes.

For the initial release of Visual Studio 2022 version 17.14, Copilot Edits is still available if the Enable Agent mode in the chat pane option isn't selected. Check the option setting in the Tools > Options dialog, under the GitHub > Copilot > Copilot Chat section.

As an administrator, how do I control the use of agent mode for Visual Studio users?

Agent mode in Visual Studio is governed by the Editor preview features flag on the GitHub Copilot dashboard for administrators. If the administrator turns off this setting, users under that subscription can't use agent mode in Visual Studio.

GitHub Copilot Agent Mode is an AI-powered coding assistant that works on its own to analyze your entire project, handle tricky coding tasks, improve solutions over time, and help make your software development process faster and more collaborative.

The GitHub Copilot certification exam evaluates your skill in using the AI-driven code completion tool in various programming languages, certifying your capability to optimize software development workflows efficiently.