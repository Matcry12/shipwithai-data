---
source_url: "https://githubnext.com/projects/copilot-workspace/"
source_domain: "githubnext.com"
topic: "github-ai-vibe"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-29T13:37:52.213267+00:00"
word_count: 2325
stage: "raw-extracted"
---

# Copilot Workspace

An agentic dev environment, designed for everyday tasks.

The Copilot Workspace technical preview is ending.

The technical preview was sunset on May 30th, 2025. Learn more

### Frequently

asked questions

#### About


#### “Copilot Workspace” or “Copilot Workspaces?”


It’s Copilot Workspace — singular.

That said, you should definitely have a few Copilot Workspace tabs open. For science.

#### Who can access Copilot Workspace?


Anyone with a paid Copilot Individual, Copilot Business, or Copilot Enterprise subscription can use Copilot Workspace.

#### How do I get started?


Check out our getting started guide!

#### Who appears as the author of a PR created with Copilot Workspace?


You do! You're the pilot.

You’re probably tired of hearing it, but it bears repeating: Copilot Workspace is a tool to help you write code, and you should always review and understand the code you’re proposing to others.

#### Can others see the PRs I create with Copilot Workspace?


Yes! PRs created with Copilot Workspace are normal PRs, and are accessible to anyone who would normally have access to PRs in the repository.

#### Can I see Copilot Workspace in action before I get access?


Every PR created with Copilot Workspace will include a comment which links to a read-only version of the Workspace that was used to create the PR. The read-only Workspace is accessible to collaborators with access to the repo, even if they have not been admitted to the technical preview.

#### Can I share a Copilot Workspace session with others?


Currently, you can share a snapshot of a Workspace with others. If they're admitted to the technical preview, they can fork your Workspace and iterate on it.

If you make changes to a Workspace after sharing it, those changes will not be reflected in the shared version — you’ll have to share a new link with them.

#### Some repositories don’t let me use Copilot Workspace. Why?


Copilot Workspace uses OAuth for authentication. Some organizations can have policies which restrict OAuth applications from interacting with their repositories. You will not be able to use Copilot Workspace with those repositories unless the organization admin approves the Copilot Workspace OAuth application.

#### 👋 Developer here! Can I start a Copilot Workspace session from an external tool?


`owner`/

`repo`?task=

`description…`

P.S. we made a Raycast extension.

#### How it works


#### What models power Copilot Workspace?


Right now, Copilot Workspace is powered by GPT-4o. We experimented with many different models from various providers, considering factors like power and latency, and determined GPT-4o is the best model for Copilot Workspace at this time. That said, we’ll continue to evaluate new models as they become available to ensure we’re always using the best model for the experience we want to deliver.

#### What makes Copilot Workspace steerable?


Copilot Workspace offers developers two important moments where they can steer the system via natural language: by altering the specification, and by altering the plan.

When you prompt Copilot Workspace to make a change, it starts by reading your codebase and generating a specification. The spec is comprised of two bullet-point lists: one for the current state of the codebase, and one for the desired state. You can edit both lists, either to correct the system’s understanding of the current codebase, or to refine the requirements for the desired state.

Once you’re happy with the spec, Copilot Workspace will generate a concrete plan for executing the changes. In this step, it will list out every file it intends to create, modify, or delete, as well as a bullet-point list of the actions to be taken in each file. Once again, you can edit any part of this plan — altering the specific instructions, or even changing the list of files that will be affected.

Finally, the generated diff is itself directly editable, so you can tweak the code before creating a pull request or pushing the code to a branch.

If you aren’t satisfied with the proposed changes, you don’t have to start over from scratch. Simply edit the spec or plan at any point, and Copilot Workspace will regenerate all the downstream steps with your new input.

#### Why does steerability matter?


Copilot’s inline suggestions are very easy to evaluate because they’re just a few lines long. When they aren’t correct, you can easily figure that out and ignore them.

When you start to generate more code, that evaluation cost grows. You have to read more code, across more locations, and understand how it all fits together. If the suggestion isn’t quite right, it can feel frustrating — and the more code you try generate at once, the more likely it is that the suggestion will be incorrect in some way.

Copilot Workspace is designed to break through that ceiling on suggestion size by mimicking how developers work through real problems. They start by articulating an understanding of how things work now, and how they would like them to work. Then, they identify where work needs to be done in order to reach the desired state.

When you can steer the system at each of these steps, you are supplying crucial information that helps the model to generate code, and the resulting code is more likely to be correct. At the same time, you also make it easier for yourself to evaluate the correctness of the generated code, because you go into the review process with a clear expectation of which changes should happen where.

#### How is Copilot Workspace different from Copilot and Copilot Chat?


Copilot helps developers to write code by making suggestions as you type. Suggestions from Copilot are a few lines in length, which leads to a great experience for developers in the flow of writing code because those suggestions are easy to evaluate (and adjust where needed.)

Copilot Chat is a great way to talk through potential changes, but it doesn't provide a rigorous, repeatable interaction pattern for applying that discussion to your codebase, especially when it would require changes to multiple files.

Copilot Workspace is a task-oriented development environment. Instead of making suggestions as you type, Copilot Workspace helps you plan and author a coordinated set of changes — even changes that span multiple files in your repository, including changes that add or remove files. This requires an interaction model that is steerable so that developers can guide the system toward the solution they want.

These three different interaction patterns serve different needs that developers have throughout their day, and are complementary to one another.

#### Can I run the code that’s in my Workspace before I create a pull request?


Yes! Each Copilot Workspace makes it easy to launch a Codespace with live sync. You can open a terminal, install your dependencies, and run your code directly from the Workspace. When needed, the Codespace handles port mappings for you.

While the generated diffs are editable in-place, you might want the power of a full IDE. No problem! Just click the “Open in Codespace” button, and you’ll get a full cloud IDE, backed by a server running VS Code.

### About

#### “Copilot Workspace” or “Copilot Workspaces?”


It’s Copilot Workspace — singular.

That said, you should definitely have a few Copilot Workspace tabs open. For science.

#### Who can access Copilot Workspace?


Anyone with a paid Copilot Individual, Copilot Business, or Copilot Enterprise subscription can use Copilot Workspace.

#### How do I get started?


Check out our getting started guide!

#### Who appears as the author of a PR created with Copilot Workspace?


You do! You're the pilot.

You’re probably tired of hearing it, but it bears repeating: Copilot Workspace is a tool to help you write code, and you should always review and understand the code you’re proposing to others.

#### Can others see the PRs I create with Copilot Workspace?


Yes! PRs created with Copilot Workspace are normal PRs, and are accessible to anyone who would normally have access to PRs in the repository.

#### Can I see Copilot Workspace in action before I get access?


Every PR created with Copilot Workspace will include a comment which links to a read-only version of the Workspace that was used to create the PR. The read-only Workspace is accessible to collaborators with access to the repo, even if they have not been admitted to the technical preview.

#### Can I share a Copilot Workspace session with others?


Currently, you can share a snapshot of a Workspace with others. If they're admitted to the technical preview, they can fork your Workspace and iterate on it.

If you make changes to a Workspace after sharing it, those changes will not be reflected in the shared version — you’ll have to share a new link with them.

#### Some repositories don’t let me use Copilot Workspace. Why?


Copilot Workspace uses OAuth for authentication. Some organizations can have policies which restrict OAuth applications from interacting with their repositories. You will not be able to use Copilot Workspace with those repositories unless the organization admin approves the Copilot Workspace OAuth application.

#### 👋 Developer here! Can I start a Copilot Workspace session from an external tool?


`owner`/

`repo`?task=

`description…`

P.S. we made a Raycast extension.

### How it works

#### What models power Copilot Workspace?


Right now, Copilot Workspace is powered by GPT-4o. We experimented with many different models from various providers, considering factors like power and latency, and determined GPT-4o is the best model for Copilot Workspace at this time. That said, we’ll continue to evaluate new models as they become available to ensure we’re always using the best model for the experience we want to deliver.

#### What makes Copilot Workspace steerable?


Copilot Workspace offers developers two important moments where they can steer the system via natural language: by altering the specification, and by altering the plan.

When you prompt Copilot Workspace to make a change, it starts by reading your codebase and generating a specification. The spec is comprised of two bullet-point lists: one for the current state of the codebase, and one for the desired state. You can edit both lists, either to correct the system’s understanding of the current codebase, or to refine the requirements for the desired state.

Once you’re happy with the spec, Copilot Workspace will generate a concrete plan for executing the changes. In this step, it will list out every file it intends to create, modify, or delete, as well as a bullet-point list of the actions to be taken in each file. Once again, you can edit any part of this plan — altering the specific instructions, or even changing the list of files that will be affected.

Finally, the generated diff is itself directly editable, so you can tweak the code before creating a pull request or pushing the code to a branch.

If you aren’t satisfied with the proposed changes, you don’t have to start over from scratch. Simply edit the spec or plan at any point, and Copilot Workspace will regenerate all the downstream steps with your new input.

#### Why does steerability matter?


Copilot’s inline suggestions are very easy to evaluate because they’re just a few lines long. When they aren’t correct, you can easily figure that out and ignore them.

When you start to generate more code, that evaluation cost grows. You have to read more code, across more locations, and understand how it all fits together. If the suggestion isn’t quite right, it can feel frustrating — and the more code you try generate at once, the more likely it is that the suggestion will be incorrect in some way.

Copilot Workspace is designed to break through that ceiling on suggestion size by mimicking how developers work through real problems. They start by articulating an understanding of how things work now, and how they would like them to work. Then, they identify where work needs to be done in order to reach the desired state.

When you can steer the system at each of these steps, you are supplying crucial information that helps the model to generate code, and the resulting code is more likely to be correct. At the same time, you also make it easier for yourself to evaluate the correctness of the generated code, because you go into the review process with a clear expectation of which changes should happen where.

#### How is Copilot Workspace different from Copilot and Copilot Chat?


Copilot helps developers to write code by making suggestions as you type. Suggestions from Copilot are a few lines in length, which leads to a great experience for developers in the flow of writing code because those suggestions are easy to evaluate (and adjust where needed.)

Copilot Chat is a great way to talk through potential changes, but it doesn't provide a rigorous, repeatable interaction pattern for applying that discussion to your codebase, especially when it would require changes to multiple files.

Copilot Workspace is a task-oriented development environment. Instead of making suggestions as you type, Copilot Workspace helps you plan and author a coordinated set of changes — even changes that span multiple files in your repository, including changes that add or remove files. This requires an interaction model that is steerable so that developers can guide the system toward the solution they want.

These three different interaction patterns serve different needs that developers have throughout their day, and are complementary to one another.

#### Can I run the code that’s in my Workspace before I create a pull request?


Yes! Each Copilot Workspace makes it easy to launch a Codespace with live sync. You can open a terminal, install your dependencies, and run your code directly from the Workspace. When needed, the Codespace handles port mappings for you.

While the generated diffs are editable in-place, you might want the power of a full IDE. No problem! Just click the “Open in Codespace” button, and you’ll get a full cloud IDE, backed by a server running VS Code.