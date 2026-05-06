---
title: "Advanced Git Workflow Tips"
topic: "git-first-job"
career_level:
  - executive
source_url: "https://blog.jetbrains.com/dotnet/2021/09/13/advanced-git-workflow-tips"
source_domain: "blog.jetbrains.com"
word_count: 2081
text_to_link_ratio: 0.8504
signal_score: 0.9504
is_curated: false
tags:
  - remote
  - open-source
  - executive
ingested_at: "2026-05-05"
---

[ ![Dotnet logo](https://blog.jetbrains.com/wp-content/uploads/2019/01/Frame-1321314548.svg) ](https://blog.jetbrains.com/dotnet/)
Essential productivity kit for .NET and game developers
  * Follow:


[.NET Tools](https://blog.jetbrains.com/dotnet/category/net-tools/) [How-To's](https://blog.jetbrains.com/dotnet/category/how-tos/)
# Advanced Git Workflow Tips
![Khalid Abuhakmeh](https://blog.jetbrains.com/wp-content/uploads/2023/01/62d2f4d9361a3cab-200x200.gif)
September 13, 2021
For better or worse, mostly better, Git has outclassed its way over version control systems (VCS) like Subversion, Perforce, and ClearCase to become the source control management system of the modern developer. If you didn’t get any of those VCS references, well, consider yourself lucky to live in an age of cheap local branching, convenient staging areas, multiple workflow support, and a wealth of distributed Git-hosting platforms. 
However, while Git is easy to learn, its constant evolution and wide range of capabilities make it challenging to master. As a result, beginners and experienced coding veterans have likely cursed a few choice words searching **_“how do I do this with Git?!”_**
Have no fear! This post will explore a few commands and workflows for some more advanced scenarios when working with a Git repository. You’ll see how to perform the actions with terminal commands or from within Rider’s UI. Let’s get started.
## Cloning and remote URLsCopy heading link
Git has support for Secure Shell (SSH) credentials, a unique cryptographic identifier for clients, with most keys produced using the RSA algorithm. SSH keys act as both the username and password to a remote instance of a code repository. From your perspective, it means having to type your VCS username and password much fewer times in your development workflow. 
When working with remote VCS providers, you may inadvertently clone using the HTTPS URL instead of the SSH URL. While it will still successfully retrieve code, all future pushed commits will require you to type in a username/password. So annoying!
To change the remote HTTP URL to an SSH URL, you can manage remotes repositories using the Git CLI.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
➜ git remote -v
origin https://github.com/khalidabuhakmeh/HelloGit.git (fetch)
origin https://github.com/khalidabuhakmeh/HelloGit.git (push)
➜ git remote -v origin https://github.com/khalidabuhakmeh/HelloGit.git (fetch) origin https://github.com/khalidabuhakmeh/HelloGit.git (push)

```
➜ git remote -v
origin  https://github.com/khalidabuhakmeh/HelloGit.git (fetch)
origin  https://github.com/khalidabuhakmeh/HelloGit.git (push)
```

To change the URL for the `origin` remote, you can use the `set-url` command. The SSH URL should be available from your VCS provider. In the case of GitHub repositories, it usually follows the `git@github.com:<username>/<repository name>.git` pattern.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
➜ git remote set-url origin git@github.com:khalidabuhakmeh/HelloGit.git
➜ git remote set-url origin git@github.com:khalidabuhakmeh/HelloGit.git

```
➜ git remote set-url origin git@github.com:khalidabuhakmeh/HelloGit.git
```

You can run the `git remote -v` command again to see that the URL has been updated.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
➜ git remote -v 
origin git@github.com:khalidabuhakmeh/HelloGit.git(fetch)
origin git@github.com:khalidabuhakmeh/HelloGit.git(push)
➜ git remote -v origin git@github.com:khalidabuhakmeh/HelloGit.git (fetch) origin git@github.com:khalidabuhakmeh/HelloGit.git (push)

```
➜ git remote -v                                                        
origin  git@github.com:khalidabuhakmeh/HelloGit.git (fetch)
origin  git@github.com:khalidabuhakmeh/HelloGit.git (push)
```

Finally, when working within Rider’s UI, you can use the **Git** menu to **Manage Remotes.** Here you’ll see the URL of existing remotes, add new remote repositories, or remove obsolete remotes.
![](https://blog.jetbrains.com/wp-content/uploads/2021/07/1-rider-remote-urls-git.png)Editing Git remote URLs from Rider’s Git Remotes Dialog Window
## Clean repository of all non-tracked artifactsCopy heading link
Project repositories can quickly consume disk space with build artifacts, third-party dependencies, and non-tracked files. Folder bloat can especially be true for long-running projects that have seen many iterations on your machine. A trick you can use to get back to a _“clean”_ state in your repository folder is to use the `git clean` command.
**Warning: Be sure all files you want to retain are committed; this is a destructive command with no recovery.**
You can run the following command in Rider’s terminal window, which should be at the root of your solution.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
➜ git clean -xdf
➜ git clean -xdf

```
➜ git clean -xdf
```

Let’s look at what each of the flags means:
  * **`x`**: Normally, the clean command will ignore files and folders found in the`.gitignore` file of the repository. This flag tells the command to target ** _all_**
  * **`d`**: Inform the command to recurse through all directories, whether they are tracked or untracked.
  * **`f`** : force the clean command to delete files and directories.


If you feel weary of running the `clean` command without knowledge of what it will do to your repository, then add the `**n**`flag along with the others to perform a dry-run.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
➜ git clean -xdfn 
Would remove .idea/.idea.HelloGit/.idea/projectSettingsUpdater.xml
Would remove .idea/.idea.HelloGit/.idea/workspace.xml
Would remove bin/
Would remove obj/
➜ git clean -xdfn Would remove .idea/.idea.HelloGit/.idea/projectSettingsUpdater.xml Would remove .idea/.idea.HelloGit/.idea/workspace.xml Would remove bin/ Would remove obj/

```
➜ git clean -xdfn        
Would remove .idea/.idea.HelloGit/.idea/projectSettingsUpdater.xml
Would remove .idea/.idea.HelloGit/.idea/workspace.xml
Would remove bin/
Would remove obj/
```

You’ll find this command helpful when exploring a new repository and want to get back to a clean state. As mentioned before, long-running projects will also benefit from this command as it may remove years of unused dependencies and outdated files. But, again, be cautious when using this as there’s no undoing this operation.
## Fix spelling errors in commit messagesCopy heading link
I’m sure you’ve worked countless hours to fix a bug, only to make a spelling error in the commit message; those “ _bgus_ ” don’t fix themselves. But, have no fear; you can fix the last commit message by utilizing the `--amend` flag.
After committing the incorrect message, you can use the following command to modify it. Note, this command does rewrite Git history, so you’ll have to force-push your changes if you’ve already pushed the error to a remote repository.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
// Will open the default Git editor
➜ git commit --amend
// Will set the new message immediately
➜ git commit --amend -m "update csproj with dependency"
// Will open the default Git editor ➜ git commit --amend // Will set the new message immediately ➜ git commit --amend -m "update csproj with dependency"

```
// Will open the default Git editor
➜ git commit --amend
// Will set the new message immediately
➜ git commit --amend -m "update csproj with dependency"
```

When using Rider, you can click the **Amend** checkbox in the **Commit** tool window to toggle the amend functionality. 
![](https://blog.jetbrains.com/wp-content/uploads/2021/07/git-commit-amend.jpg)GIF
Updating a previous commit using the **Amend** feature within JetBrains Rider
When using Rider’s Git window, you can choose **Edit Commit Message** by right-clicking any commit in the currently checked out branch and choosing the option from the menu.
![](https://blog.jetbrains.com/wp-content/uploads/2021/07/git-right-click-edit-message.png)Choosing **Edit Commit Message** from Git Window
After choosing to edit a commit message, you can change the text from a newly visible dialog box that will contain your previous message.
![](https://blog.jetbrains.com/wp-content/uploads/2021/07/Screenshot-2021-07-13-at-08.19.08-2x.png)**Edit Commit Message** dialog in Rider
Remember, any amended commit message alters the Git history. If changes have been pushed already, then you will need to perform a force-push.
## Adding files to the previous commitCopy heading link
Like fixing spelling errors in a commit message, you sometimes forget to add a file to a particular commit. Instead of adding a commit to your Git history, you can choose to amend the previous commit with no edits to the message. First, you’ll need to add any files that you wanted to add during the last commit.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
➜ git add .
➜ git commit --amend --no-edit
➜ git add . ➜ git commit --amend --no-edit

```
➜ git add .
➜ git commit --amend --no-edit
```

When using Rider, you can click the **Amend** checkbox and select any files from the **Changes** collection in the Commit window.
![](https://blog.jetbrains.com/wp-content/uploads/2021/07/git-commit-amend-no-edit.png)Add additional files from **Changes** during an Amend operation
Remember, just like in our last amend tip, this changes the Git history and may require a force-push if changes have already been pushed remotely.
## Undo changes to previously committed filesCopy heading link
You may start making changes to a committed file only to realize you no longer want the changes. Luckily, rolling back to a known good state is as simple as checking out the file.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
// previously committed file
➜ git co Program.cs
Updated 1 path from the index
// previously committed file ➜ git co Program.cs Updated 1 path from the index

```
// previously committed file
➜ git co Program.cs
Updated 1 path from the index
```

If you want to roll back changes in Rider, right-click a target file in the **Commit** window, and choose **Rollback** from the command menu. 
![](https://blog.jetbrains.com/wp-content/uploads/2021/07/rider-rollback-git-file.png)Rollback changes in a file using **Rollback** in the commands menu
## Undo last local Git commitCopy heading link
You’ve been working on a significant feature only to realize you just committed all your work to the `main` branch when you meant to commit to a new feature branch. 
To undo your commit locally, run the following command.
Plain text
Copy to clipboard
Open code in new window
EnlighterJS 3 Syntax Highlighter
➜ git reset --soft HEAD~1
➜ git reset --soft HEAD~1

```
➜ git reset --soft HEAD~1
```

The Git command will compare the current **HEAD** commit (your last commit) to the commit before it (before you committed) and stage the files. At this point, you have an opportunity to create a new branch and save your changes correctly. 
When working with Rider’s Git tooling, you can choose the commit in the **Git** window and select **Reset Current Branch To Here.** Generally, you want to choose “**Soft** ” as it will not destroy your work. 
![](https://blog.jetbrains.com/wp-content/uploads/2021/07/rider-undo-local-git-commit.png)git reset dialog in JetBrains Rider showing flags and potential outcomes
Rider has some helpful documentation around what each option means and how it can help you reset our current development environment.
Like some of the previous tips, the **reset** command will rewrite Git history. But unlike the other tips, you’ll use **reset** on protected branches like **main** that you may have inadvertently altered locally but have no intention of pushing changes to a remote repository.
## ConclusionCopy heading link
As you work with Git, you’ll become familiar with the core mechanics of source control, and as the official site says, it’s easy to learn the basics: clone, branch, add, commit and push. We wanted to show you some of the more advanced Git use cases that you’ll likely use in your daily workflow in this post. We hope these tips will help you fix minor annoyances to significant issues in your source control workflow.
If you have any particular **tips you’d like to share** , either from the command line or Rider’s Git tooling, please feel free to share them in the **comments below**.
If you’d like to try JetBrains Rider’s Git tooling first hand, **[download and install the latest Rider version](https://jetbrains.com/rider)**.
[git](https://blog.jetbrains.com/dotnet/tag/git/) [Rider](https://blog.jetbrains.com/dotnet/tag/rider/) [source code management](https://blog.jetbrains.com/dotnet/tag/source-code-management/)
  * Share


[ OSS Power-Ups: CliWrap](https://blog.jetbrains.com/dotnet/2021/09/08/oss-power-ups-cliwrap/)[Webinar: Profiling and Fixing Common Performance Bottlenecks ](https://blog.jetbrains.com/dotnet/2021/09/15/webinar-profiling-and-fixing-common-performance-bottlenecks/)
Thanks, we've got you!
Sort by Recently updatedBest Worst Newest Oldest Recently updated Least recently updated Most controversial Least controversial
Powered by [Remark42](https://remark42.com/)
## Discover more
[ ![](https://blog.jetbrains.com/wp-content/uploads/2026/04/Featured_Blog_1280x720.png) Apr 16 2026 Webinar – OSS Power-Ups: XenoAtom.Terminal.UI Join us Thursday, April 16, 2026, 15:00 – 16:30 UTC (check other timezones) for our free live webinar, OSS PowerUps – XenoAtom.Terminal.UI, with Alexandre Mutel. This is the fifteenth episode of our series of OSS Power-Ups, where we put a spotlight on open-source .NET projects. Register now and g… ![Matthias Koch](https://blog.jetbrains.com/wp-content/uploads/2023/09/headshot-shadow-50x50.png) Matthias Koch April 9, 2026 0 ](https://blog.jetbrains.com/dotnet/2026/04/09/webinar-oss-power-ups-xenoatom-terminal-ui/)
[ ![dotInsights | April 2026](https://blog.jetbrains.com/wp-content/uploads/2026/03/DN-social-BlogFeatured-1280x720-1-1.png) dotInsights | April 2026 Did you know? You can use LINQ to XML to write queries in a readable and strongly-typed way directly against an XML document, making it one of the most intuitive ways to deal with XML in .NET. Welcome to dotInsights by JetBrains! This newsletter is the home for recent .NET and software develo… ![Rachel Appel](https://blog.jetbrains.com/wp-content/uploads/2023/09/rachel-profile-sm-50x50.png) Rachel Appel April 8, 2026 0 ](https://blog.jetbrains.com/dotnet/2026/04/08/dotinsights-april-2026/)
[ ![](https://blog.jetbrains.com/wp-content/uploads/2026/03/RS-social-BlogFeatured-1280x720-1-1.png) Profile .NET Apps Without Restarting: Monitoring Comes to ReSharper Tracking down performance bottlenecks in Visual Studio often means interrupting your workflow, restarting your application in profiling mode, and hoping you can reliably reproduce the exact issue. We think there’s a better way. If you have already used Monitoring in Rider, this experience will fe… ![Alexey Totin](https://blog.jetbrains.com/wp-content/uploads/2021/03/totin-removebg-preview-50x50.png) Alexey Totin March 31, 2026 1 ](https://blog.jetbrains.com/dotnet/2026/03/31/profile-dotnet-apps-without-restarting-monitoring-comes-to-resharper/)
[ ![](https://blog.jetbrains.com/wp-content/uploads/2026/03/RS-releases-BlogFeatured-1280x720-1-2.png) ReSharper 2026.1: Built-in Performance Monitoring, Expansion to VS Code, and Faster Everyday Workflows ReSharper 2026.1 is here, bringing improvements that focus on how you actually work: understanding runtime behavior, writing safer C#, and keeping Visual Studio responsive. This release introduces a new approach to performance monitoring, takes ReSharper beyond Visual Studio, and delivers a range… ![Sasha Ivanova](https://blog.jetbrains.com/wp-content/uploads/2022/07/F34E0F9B-D3F0-4DD4-B7C7-B11AF3FC6D25-50x50.jpeg) Sasha Ivanova March 30, 2026 0 ](https://blog.jetbrains.com/dotnet/2026/03/30/resharper-2026-1-released/)
