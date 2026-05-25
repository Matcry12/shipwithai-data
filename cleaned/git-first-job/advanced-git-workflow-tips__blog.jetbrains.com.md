---
title: "Advanced Git Workflow Tips"
topic: "git-first-job"
career_level:
  - entry
source_url: "https://blog.jetbrains.com/dotnet/2021/09/13/advanced-git-workflow-tips/"
source_domain: "blog.jetbrains.com"
word_count: 1382
text_to_link_ratio: 1.0
signal_score: 1.0
is_curated: false
tags:
  - Git remotes
  - SSH keys
  - git clean
  - commit amendments
  - workflow optimization
ingested_at: "2026-05-25"
doc_type: "how-to-guide"
core_question: "What practical Git techniques help developers work more efficiently with remote repositories and maintain clean commit history?"
tldr: "Advanced Git workflow tips covering remote URL management, SSH setup, repository cleanup with git clean, commit message amendments, and adding files to previous commits."
---

# Advanced Git Workflow Tips

For better or worse, mostly better, Git has outclassed its way over version control systems (VCS) like Subversion, Perforce, and ClearCase to become the source control management system of the modern developer. If you didn't get any of those VCS references, well, consider yourself lucky to live in an age of cheap local branching, convenient staging areas, multiple workflow support, and a wealth of distributed Git-hosting platforms.

However, while Git is easy to learn, its constant evolution and wide range of capabilities make it challenging to master. As a result, beginners and experienced coding veterans have likely cursed a few choice words searching *"how do I do this with Git?!"*

Have no fear! This post will explore a few commands and workflows for some more advanced scenarios when working with a Git repository. You'll see how to perform the actions with terminal commands or from within Rider's UI. Let's get started.

## Cloning and remote URLs

Git has support for Secure Shell (SSH) credentials, a unique cryptographic identifier for clients, with most keys produced using the RSA algorithm. SSH keys act as both the username and password to a remote instance of a code repository. From your perspective, it means having to type your VCS username and password much fewer times in your development workflow.

When working with remote VCS providers, you may inadvertently clone using the HTTPS URL instead of the SSH URL. While it will still successfully retrieve code, all future pushed commits will require you to type in a username/password. So annoying!

To change the remote HTTP URL to an SSH URL, you can manage remotes repositories using the Git CLI.

➜ git remote -v origin https://github.com/khalidabuhakmeh/HelloGit.git (fetch) origin https://github.com/khalidabuhakmeh/HelloGit.git (push)

To change the URL for the `origin`

remote, you can use the `set-url`

command. The SSH URL should be available from your VCS provider. In the case of GitHub repositories, it usually follows the `git@github.com:<username>/<repository name>.git`

pattern.

➜ git remote set-url origin git@github.com:khalidabuhakmeh/HelloGit.git

You can run the `git remote -v`

command again to see that the URL has been updated.

➜ git remote -v origin git@github.com:khalidabuhakmeh/HelloGit.git (fetch) origin git@github.com:khalidabuhakmeh/HelloGit.git (push)

Finally, when working within Rider's UI, you can use the **Git** menu to **Manage Remotes.** Here you'll see the URL of existing remotes, add new remote repositories, or remove obsolete remotes.

## Clean repository of all non-tracked artifacts

Project repositories can quickly consume disk space with build artifacts, third-party dependencies, and non-tracked files. Folder bloat can especially be true for long-running projects that have seen many iterations on your machine. A trick you can use to get back to a *"clean"* state in your repository folder is to use the `git clean`

command.

**Warning: Be sure all files you want to retain are committed; this is a destructive command with no recovery.**

You can run the following command in Rider's terminal window, which should be at the root of your solution.

➜ git clean -xdf

Let's look at what each of the flags means:

: Normally, the clean command will ignore files and folders found in the`x`

`.gitignore`

file of the repository. This flag tells the command to target*all*untracked files, even if they happen to be ignored.: Inform the command to recurse through all directories, whether they are tracked or untracked.`d`

: force the clean command to delete files and directories.`f`

If you feel weary of running the `clean`

command without knowledge of what it will do to your repository, then add the

flag along with the others to perform a dry-run.**n**

➜ git clean -xdfn Would remove .idea/.idea.HelloGit/.idea/projectSettingsUpdater.xml Would remove .idea/.idea.HelloGit/.idea/workspace.xml Would remove bin/ Would remove obj/

You'll find this command helpful when exploring a new repository and want to get back to a clean state. As mentioned before, long-running projects will also benefit from this command as it may remove years of unused dependencies and outdated files. But, again, be cautious when using this as there's no undoing this operation.

## Fix spelling errors in commit messages

I'm sure you've worked countless hours to fix a bug, only to make a spelling error in the commit message; those "*bgus*" don't fix themselves. But, have no fear; you can fix the last commit message by utilizing the `--amend`

flag.

After committing the incorrect message, you can use the following command to modify it. Note, this command does rewrite Git history, so you'll have to force-push your changes if you've already pushed the error to a remote repository.

// Will open the default Git editor ➜ git commit --amend // Will set the new message immediately ➜ git commit --amend -m "update csproj with dependency"

When using Rider, you can click the **Amend** checkbox in the **Commit** tool window to toggle the amend functionality.

When using Rider's Git window, you can choose **Edit Commit Message** by right-clicking any commit in the currently checked out branch and choosing the option from the menu.

After choosing to edit a commit message, you can change the text from a newly visible dialog box that will contain your previous message.

Remember, any amended commit message alters the Git history. If changes have been pushed already, then you will need to perform a force-push.

## Adding files to the previous commit

Like fixing spelling errors in a commit message, you sometimes forget to add a file to a particular commit. Instead of adding a commit to your Git history, you can choose to amend the previous commit with no edits to the message. First, you'll need to add any files that you wanted to add during the last commit.

➜ git add . ➜ git commit --amend --no-edit

When using Rider, you can click the **Amend** checkbox and select any files from the **Changes **collection in the Commit window.

Remember, just like in our last amend tip, this changes the Git history and may require a force-push if changes have already been pushed remotely.

## Undo changes to previously committed files

You may start making changes to a committed file only to realize you no longer want the changes. Luckily, rolling back to a known good state is as simple as checking out the file.

// previously committed file ➜ git co Program.cs Updated 1 path from the index

If you want to roll back changes in Rider, right-click a target file in the **Commit** window, and choose **Rollback **from the command menu.

## Undo last local Git commit

You've been working on a significant feature only to realize you just committed all your work to the `main`

branch when you meant to commit to a new feature branch.

To undo your commit locally, run the following command.

➜ git reset --soft HEAD~1

The Git command will compare the current **HEAD** commit (your last commit) to the commit before it (before you committed) and stage the files. At this point, you have an opportunity to create a new branch and save your changes correctly.

When working with Rider's Git tooling, you can choose the commit in the **Git **window and select **Reset Current Branch To Here.** Generally, you want to choose "**Soft**" as it will not destroy your work.

Rider has some helpful documentation around what each option means and how it can help you reset our current development environment.

Like some of the previous tips, the **reset **command will rewrite Git history. But unlike the other tips, you'll use **reset **on protected branches like **main** that you may have inadvertently altered locally but have no intention of pushing changes to a remote repository.

## Conclusion

As you work with Git, you'll become familiar with the core mechanics of source control, and as the official site says, it's easy to learn the basics: clone, branch, add, commit and push. We wanted to show you some of the more advanced Git use cases that you'll likely use in your daily workflow in this post. We hope these tips will help you fix minor annoyances to significant issues in your source control workflow.

If you have any particular **tips you'd like to share**, either from the command line or Rider's Git tooling, please feel free to share them in the **comments below**.

If you'd like to try JetBrains Rider's Git tooling first hand, **download and install the latest Rider version**.
