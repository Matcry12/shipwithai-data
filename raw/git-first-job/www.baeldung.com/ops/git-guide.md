---
source_url: https://www.baeldung.com/ops/git-guide
crawl_depth: 0
crawled_at: 2026-05-05T14:26:31Z
word_count: 3442
---

## 1. Overview[](https://www.baeldung.com/ops/git-guide#overview)
In this tutorial, we’ll discuss the commands that we most frequently use when working with Git.
We’ll start with installation and configuration and then create our first local repository. Next, we’ll learn how to commit changes and synchronize them with a remote repository.
Additionally, we’ll discuss branching and also learn some advanced techniques like amending commits and manipulating the commit history.
## 2. What Is Git?[](https://www.baeldung.com/ops/git-guide#what-is-git)
**Git i****s a version control system (VCS) that allows saving and tracking changes to files over time** without overwriting previous snapshots. It helps developers collaborate on projects together.
Unlike its main competitor – [_SVN_](https://www.baeldung.com/cs/git-vs-svn), Git also implements a distributed workflow system. It means that every developer working with Git has a local copy of the entire repository. Git also allows working asynchronously without a constant connection to the central repository.
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_leaderboard_mid_1)
**3. Git Installation**
We can [install Git](https://git-scm.com/downloads) on the most common operating systems like Windows, Mac, and Linux. In fact, on most Mac and Linux machines, Git comes installed by default.
To see if we already have Git installed, let’s open up a terminal and execute:

```
$ git version
git version 2.24.3 (Apple Git-128)Copy
```

Moreover, Git comes with built-in GUI tools for committing ([_git-gui_](https://git-scm.com/docs/git-gui)) and browsing ([_gitk_](https://git-scm.com/docs/gitk)). There are also plenty of [third-party tools](https://git-scm.com/downloads/guis) or IDE plugins that enhance the experience.
**4._git help_ – A Handy Manual**
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_leaderboard_mid_2)
Before we create our first repository, let’s run the [_git_  _help_](https://git-scm.com/docs/git-help) command. **It displays useful information about Git itself** :

```
$ git help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
...Copy
```

We can also check the manual for a specific command in multiple ways:

```
$ git --help init
$ git help init
$ git init --helpCopy
```

All the three variants above return identical output.
With the _-g_ option _,_ we can also access the list of internal guides to develop our skills:

```
$ git help -g
The common Git guides are:
   attributes          Defining attributes per path
   cli                 Git command-line interface and conventions
   core-tutorial       A Git core tutorial for developers
...
$ git help core-tutorialCopy
```

To print the tutorial, we need to provide its name as a parameter.
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_leaderboard_mid_3)
**5._git_  _config_ – Configuring Git**
Once we have Git installed, we can easily configure it with the [_git_ _config_](https://git-scm.com/docs/git-config) command, which**allows managing options**.
Git supports options at different levels like _system_ , _global_ , _local_ , _worktree_ , or _file_.
While the _system_ settings are system-wide and are applied to every user and all of their repositories on the system, the _global_ level refers to user-specific settings.
The _local_ configuration is specific to the single repository, and it is the default level that Git uses when we don’t pass any option to the _git config_ command.
The  _worktree_ and  _file_ levels are more advanced configuration levels, which can be applied to a single branch or file in the repository.
Further, **Git resolves the effective value of an option by checking the _local_ level first and then goes until the _system_ level if the option isn’t set**.
As an example, let’s configure our username used in the commit history:
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_incontent_1)

```
$ git config --global user.name "Baeldung User"Copy
```

We’ve just set our name globally.
To override an option for a single repository, we can use the _–local_ flag in its directory.
To print the list of effective options, we use:

```
$ git config -l
user.name=Baeldung UserCopy
```

We can execute the _git –help config_ command to get details about all the available options.
## 6. Creating a Repository[](https://www.baeldung.com/ops/git-guide#creating-a-repository)
Next, we need to create a repository. For this, we have two alternatives – **a new repository can be either created locally from scratch, or an existing one can be cloned**.
### 6.1. _git init_ – Initialize a New Repository[](https://www.baeldung.com/ops/git-guide#1-git-init---initialize-a-new-repository)
If we decide to initialize a new repository, we need to use the [_git init_](https://git-scm.com/docs/git-init) command. **It turns the current directory into a Git repository** and starts tracking its content:

```
$ mkdir simple-repo; cd simple-repo; git init
Initialized empty Git repository in /simple-repo/.git/Copy
```

Git also creates a hidden directory called  _.git_ in it. This directory stores all the objects and [refs](https://git-scm.com/book/en/v2/Git-Internals-Git-References) that Git creates and uses as part of our project’s history. Those files are created during commits and point to specific revisions of our files.
After that, in most cases, we want to connect our already created repository with a remote one. We use **the[ _git remote_](https://git-scm.com/docs/git-remote) command to manage remote links for the current repository**:
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_incontent_2)

```
$ git remote add origin https://github.com/eugenp/tutorials.gitCopy
```

We’ve just added a new remote called _origin_ and connected it to the official Baeldung GitHub repository.
### 6.2. _git clone_ – Clone an External Repository[](https://www.baeldung.com/ops/git-guide#2-git-clone---clone-an-external-repository)
Sometimes we want to contribute to an existing repository. First, we need to download the existing repository locally.
**The[ _git clone_](https://git-scm.com/docs/git-clone) command clones the repository into a new directory**:

```
$ git clone https://github.com/eugenp/tutorials.git
Cloning into 'repo'...Copy
```

When it finishes, the new directory created contains all the project’s files, branches, and history.
Additionally, the cloned repository is already configured and connected with the external source:

```
$ cd tutorials
$ git remote -v
origin	https://github.com/eugenp/tutorials.git (fetch)
origin	https://github.com/eugenp/tutorials.git (push)Copy
```

Git will use those origin links to manage any further changes.
## 7. Git Workflow[](https://www.baeldung.com/ops/git-guide#git-workflow)
After we have configured our local repository, we are ready to apply the first changes. But before we do that, let’s check how Git tracks those changes.
Our local repository consists of three different trees maintained by Git.
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_incontent_3)
The first one is the **_Working Directory,_ which holds the actual version of files.**
After making our changes to the files, we can move the files into _Index,_ which acts as a staging area. We do this using the _git add_ command. **Files in _Index_ begin to be tracked by Git.**
Finally, **we can apply and save our changes into the _Local Repository_ using the _git commit_ command.** Committing the changes updates the repository’s HEAD, which always points to the last commit we’ve made.
Those three steps are used to maintain the local changes. But as we know, the repository may also contain an external source. The last step is to synchronize both repositories and publish our changes.
##  [![git workflow](https://www.baeldung.com/wp-content/uploads/sites/6/2024/02/git_workflow.webp)](https://www.baeldung.com/wp-content/uploads/2021/11/git_workflow.png)8. Making Changes[](https://www.baeldung.com/ops/git-guide#making-changes)
Now that we know how Git’s tracking system works, we’re ready to apply our first changes to our repository.
### 8.1. _git status_ – Show Current Changes[](https://www.baeldung.com/ops/git-guide#1-git-status---show-current-changes)
Let’s create a simple file and add it to our repository. Afterward, we execute the [_git status_](https://git-scm.com/docs/git-status) command and analyze its output:

```
$ "Hello World" >> myfile.txt
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	myfile.txt

nothing added to commit but untracked files present (use "git add" to track)Copy
```

**The command prints the current detailed status of our changes**. The first part shows if the local and remote branches are synchronized.
Next, the output shows the status of the _working tree_ – the list of currently modified files with their maintenance status. As we see, the _myfile.txt_ file is currently in the _Working Directory_ area and not tracked by Git.
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_incontent_4)
### 8.2. _git add_ – Track the Changes[](https://www.baeldung.com/ops/git-guide#2-git-add---track-the-changes)
To start tracking the changes, **we need to move them to the _Index_ by using the [ _git add_](https://git-scm.com/docs/git-add)** command:

```
$ git add myfile.txt
$ git stage *Copy
```

We can specify multiple files at once by separating them with a space. We can also specify all files using the asterisk sign.
Alternatively, we can also use the [_git stage_](https://git-scm.com/docs/git-stage) command, which is a synonym for the _git add_ command _._
Let’s now verify the status:

```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   myfile.txtCopy
```

As we can see, Git has started tracking our files.
### 8.3. _git restore_ _&__gitignore_ – Untrack the Changes[](https://www.baeldung.com/ops/git-guide#3-git-restore-amp-gitignore--untrack-the-changes)
Git allows removing files from the _Index_. If we moved our changes into it by mistake and **want to temporarily disable tracking them, we use _[git restore](https://git-scm.com/docs/git-restore):_**

```
$ git restore -S myfile.txt
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	myfile.txtCopy
```

We’ve just moved our file once again to the _Working Area_ and excluded it from further commits until we stage it again. The _-S_ (_–staged_) flag tells Git to restore only the repository’s _Index_.
We can also permanently exclude files and disable tracking them. To do this, we need to create a [_.gitignore_](https://git-scm.com/docs/gitignore) file. This file contains filename patterns and is applied to all the files in the current directory and its child directories. Any further _add_ actions will ignore files matching those patterns.
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_incontent_5)
### 8.4. _git commit_ – Save the Changes[](https://www.baeldung.com/ops/git-guide#4-git-commit--save-the-changes)
Let’s revert the last changes and move our file once again to the _Staging Area_ :

```
$ git add myfile.txtCopy
```

Now, it’s time to save our work, so we need to do a commit.
**The commit is a Git object, which is like a snapshot of our repository at a specific time.**
To commit changes, let’s use the [_git commit_](https://git-scm.com/docs/git-commit) command:

```
$ git commit -m "My first commit"
[master 8451901] My first commit
 1 file changed, 1 insertion(+)
 create mode 100644 myfile.txtCopy
```

We’ve just created our first commit locally.
The _git commit_ command contains many additional options to perform more complex operations, which we can inspect with the _git commit –help_ command.
The most useful is the _-m_ flag, which specifies a commit message describing changes done in the current snapshot.
Finally, let’s check the status:
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_incontent_6)

```
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree cleanCopy
```

Now, our working tree doesn’t contain any additional changes, but the local repository contains more commits than its external source. Therefore, to publish our changes, we should synchronize local changes with the origin.
### 8.5. _git log_ & _git show_ – Inspect Commits[](https://www.baeldung.com/ops/git-guide#5-git-log-amp-git-show---inspect-commits)
Once we’ve created the commit, we can check its details. Commits include lots of additional metadata, like the author, timestamp, and more.
To**print the list of commits of the current branch, we use the[ _git log_](https://git-scm.com/docs/git-log)** command:

```
$ git log
commit 845190154ed7a491a6143669c4ce88058fb93f8a (HEAD -> master)
Author: ...
Date: ...

    My first commit

commit 9a1e11ec981b41e4b4b9c245a7a96cd6707f4705 (origin/master, origin/HEAD)
...Copy
```

The list shows the commit history of the current branch in reverse chronological order by default.
Each entry contains the general metadata like the commit’s id (a unique SHA-1 checksum), author, date, and given message.
When we want to go deeper into a single commit, we print its details using the [ _git show_](https://git-scm.com/docs/git-show) command followed by the requested commit id:

```
$ git show 845190154ed7a491a6143669c4ce88058fb93f8a
commit 845190154ed7a491a6143669c4ce88058fb93f8a (HEAD -> master)
Author: ...
Date:...

    My first commit

diff --git a/myfile.txt b/myfile.txt
new file mode 100644
index 0000000..557db03
--- /dev/null
+++ b/myfile.txt
@@ -0,0 +1 @@
+Hello WorldCopy
```

This time, the output also**displays the differences done by the commit versus the previous snapshot using the[ _git diff_](https://git-scm.com/docs/git-diff)** command.
### 8.6. _git stash_[](https://www.baeldung.com/ops/git-guide#6-git-stash--shelve-the-changes)
**The[ _git stash_](https://git-scm.com/docs/git-stash) command temporarily shelves changes we’ve made**, reverting the _Working Directory_ to match the _HEAD_ commit. This allows us to quickly switch context and start working on something else.
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_incontent_7)
Let’s create another file and add it to the _Staging Area_. After that, let’s execute the _git stash_ :

```
$ touch myfile-2.txt; git add *
$ git stash push
Saved working directory and index state WIP on master: 8451901 My first commitCopy
```

Now, let’s try to list the file:

```
$ ls myfile-2.txt
ls: myfile-2.txt: No such file or directoryCopy
```

We can see that now the file isn’t present. This is because all pending changes have been removed from the _Working Directory_ and saved in the stash.
We can print all the stashed away modifications using the _list_ option:

```
$ git stash list
stash@{0}: WIP on master: 8451901 My first commitCopy
```

Since we didn’t provide its description, the stash is by default listed as _WIP on… ._ We can change the default value into a more descriptive message using the _-m_ flag on the command line.
To inspect its details, we use the _show_ option:

```
$ git stash show
 myfile-2.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)Copy
```

The output prints information about changes stored in the latest stash.
Finally, if we want to restore the changes, we use the _pop_ option:
[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_incontent_8)

```
$ git stash pop
...
$ ls myfile-2.txt 
myfile-2.txt
Copy
```

We’ve just removed a single stashed state from the stash list and applied it on top of the current state.
## 9. Manipulating the Commit History[](https://www.baeldung.com/ops/git-guide#manipulating-the-commit-history)
Now that we’ve learned how to save changes in the repository, let’s modify previously saved commits. In the following sections, we’ll cover the most common use cases.
### 9.1. _git commit –amend_ – Add Additional Changes to the Commit[](https://www.baeldung.com/ops/git-guide#1-git-commit---amend---add-additional-changes-to-the-commit)
Suppose we forgot to include a file when committing a change. Of course, we can create another commit on top of the last one, but it might make the changes history messy.
In such cases, **we may want Git to rewrite our last commit and include the file we forgot using the _amend_ option**.
Let’s review the last commit:

```
$ git show --summary
commit 845190154ed7a491a6143669c4ce88058fb93f8a (HEAD -> master)
Author: ...
Date: ...

    My first commit

 create mode 100644 myfile.txt
Copy
```

Having our _my-file2.txt_ popped from the stash, let’s commit it using the _amend_ option:

```
$ git commit --amend
[master 0ed9f03] My first commit
 2 files changed, 1 insertion(+)
 create mode 100644 myfile-2.txt
 create mode 100644 myfile.txtCopy
```

We can notice that Git added the file to our last commit combining the changes.
### 9.2. _git rebase_ – Reapply Commits[](https://www.baeldung.com/ops/git-guide#2-git-rebase---reapply-commits)
A more advanced technique for modifying commits is through the [git](https://git-scm.com/docs/git-rebase) _[rebase](https://git-scm.com/docs/git-rebase) _command _._**It reapplies commits from the history on top of another base** , allowing us to change them on the fly.
Let’s create another commit in our repository:

```
$ touch myfile-3.txt
$ git add *
$ git commit -m "My second commit"Copy
```

Now, we should have two single commits – _My first commit_ and  _My second commit_.
Let’s start to rebase both commits in an interactive mode:

```
git rebase -i HEAD~2Copy
```

This opens an editor, where we can manipulate the history using commands:

```
pick 82d8635 My first commit
pick 6d58108 My second commit

# Rebase 9a1e11e..82d8635 onto 9a1e11e (2 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# d, drop <commit> = remove commit 
...Copy
```

On the top, we have the list of rebasing commits followed by the manual. We have plenty of options here. We can change the order by swapping the lines, or _reword_ the commit message, or _squash_ them into one, _edit,_ or even  _drop_ a single commit. The instruction lines will be applied from top to bottom.
### 9.3. _git reset_ – Rollback to the Specific State[](https://www.baeldung.com/ops/git-guide#3-git-reset---rollback-to-the-specific-state)
Sometimes, we might want to drop the current state and revert to a historical snapshot. To do this, we use the [_git reset_](https://git-scm.com/docs/git-reset) option _:_

```
$ git reset 82d8635Copy
```

**It undoes all commits after the specified commit** , preserving changes locally and moving them to the _Staging Area_. But, if we want to drop all working changes, we can use _–hard_ flag.
## 10. Synchronizing the Repository[](https://www.baeldung.com/ops/git-guide#10-synchronizing-the-repository)
After working locally on the repository till now, it’s finally time to publish our changes.
**Before uploading them, we should always synchronize our local copy with the remote** to avoid conflicts during publishing**.**
### 10.1. _git fetch_ – Update References[](https://www.baeldung.com/ops/git-guide#101-git-fetch---update-references)
While we’re implementing our changes, others may have published changes to the same branch. So we should check and sync them with our local repository.
The [_git fetch_](https://git-scm.com/docs/git-fetch) command helps us to do so:

```
$ git fetchCopy
```

**This downloads objects and refs from the origin repository**.
We should note that **this action never modifies the current working tree**. This is because we can only inspect the updated commit history for our repository. If we find any pending changes, we must go further.
### 10.2. _git merge_ – Apply Incoming Changes[](https://www.baeldung.com/ops/git-guide#102-git-merge---apply-incoming-changes)
We must merge any incoming changes on the same branch before we publish our code. If we don’t do this, the publishing process could fail.
Let’s update our branch:

```
$ git merge origin/masterCopy
```

The [ _git merge_](https://git-scm.com/docs/git-merge) command is a very powerful tool. **It downloads all new changes from the given reference and combines them with the current working tree** choosing the right merge strategy. Many changes will be applied automatically, even if modifications exist on the same files.
But sometimes, there is no easy way to merge changes. In that case, we have a _merge conflict_ , and we have to resolve it manually before moving on. We need to edit the failed file, prepare a final version, and commit the changes.
### 10.3. _git pull_ – Update and Apply at Once[](https://www.baeldung.com/ops/git-guide#103-git-pull--update-and-apply-at-once)
The [ _git pull_](https://git-scm.com/docs/git-pull) command is nothing more than _git fetch_ and  _git merge_ combined into one:

```
$ git pull origin/masterCopy
```

**It checks a given branch for the latest changes and merges them with the current branch** , in the same way as _git fetch_ and _git merge_ do. It’s the most common way to update the current branch.
Furthermore, pulling changes might also require an additional manual action to resolve _merge conflicts_.
### 10.4. _git push_ – Publishing Local Commits[](https://www.baeldung.com/ops/git-guide#104-git-push---publishing-local-commits)
Once we synchronize our local repository and fix pending _merge conflicts_ , we are finally ready to publish our commits. We need to choose the remote target and the local branch.
Let’s execute the [_git push_](https://git-scm.com/docs/git-push) command:

```
$ git push origin masterCopy
```

**This updates the _master_ branch of the remote repository with all commits made locally**.
Finally, we check the history:

```
$ git log
commit 6d5810884c3ce63ca08084959e3a21405a1187df (HEAD -> master, origin/master, origin/HEAD)
Author: ...
Date: ...
    My second commitCopy
```

We’re done! We’ve just sent our changes to the remote repository.
## 11. Git Branching[](https://www.baeldung.com/ops/git-guide#11-git-branching)
Now, let’s talk about branches. Previously, we intentionally skipped any branch operations. All changes were done on **the _master_ branch, which is the default one for each Git repository**.
**Branches are used to develop features isolated** from each other. We use other branches for development and merge them back to the _master_ branch upon completion.
### 11.1. _git branch_ – Manage Branches[](https://www.baeldung.com/ops/git-guide#111-git-branch--manage-branches)
**The[ _git branch_](https://git-scm.com/docs/git-branch)helps us manage branches**. To create a new one, we simply specify its name:

```
$ git branch new-branchCopy
```

A local branch is not available to others until we push it to the remote repository.
We can now see the newly created branch by listing all of them:

```
$ git branch --list --all
* master
  new-branch
  remotes/origin/HEAD -> origin/master
  remotes/origin/masterCopy
```

If we want to delete a local branch, we execute:

```
$ git branch -d new-branchCopy
```

### 11.2. _git checkout_ – Change Current Branch[](https://www.baeldung.com/ops/git-guide#112-git-checkout---change-current-branch)
If **we want to switch current branch, we use the[ _git checkout_](https://git-scm.com/docs/git-checkout) or **[_**git switch**_](https://git-scm.com/docs/git-switch) functions:

```
$ git switch new-branch
Switched to branch 'new-branch'
$ git checkout master
Switched to branch 'master'Copy
```

We’ve just changed from the _master_ to the _new-branch_ and then back to _master_ again using both the commands.
Although both work similarly, the _git_ _switch_ command simply allows switching branches. In contrast, the _git checkout_ is a more complex command enabling us to additionally manage working tree files, resetting branches, or reverting files to specific versions.
## 12. Conclusion[](https://www.baeldung.com/ops/git-guide#12-conclusion)
In this article, we covered all the Git basics and discussed most of the common operations which every developer should know while working with Git. Through practical examples, we learned how to work with this Version Control System.
We started by installing and configuring Git and then created the first repository. After that, we made some changes and learned how to modify the commit history. Finally, we published the changes by synchronizing both repositories and learned how to work with Git branches.


[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=display&utm_source=baeldung.com&utm_content=baeldung_leaderboard_btf_2)
