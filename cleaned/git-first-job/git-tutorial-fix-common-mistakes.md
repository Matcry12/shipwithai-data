---
title: ""
topic: "git-first-job"
career_level:
  - executive
source_url: "https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes"
source_domain: "www.creative-tim.com"
word_count: 2577
text_to_link_ratio: 0.7841
signal_score: 0.8841
is_curated: false
tags:
  - remote
  - open-source
  - executive
ingested_at: "2026-05-05"
---

This article is a collection of the 18 most frequently asked questions and their answers when it comes to using Git in a team. Some Git questions are more intimidating and may seem difficult to answer, even for experienced Git users. For example, did you forget to include a certain change or make a mistake in your commit message? Don’t worry. In these situations, it’s common to want to roll back or undo a change made by you or your team. You can do this with almost all activities in Git, such as commits, merges, local or remote changes, and even uncommitted changes. It can all be “undone”.
**Here’s the table of content for this article:**
  1. [How to create a Git branch?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#1-how-to-create-a-git-branch)
  2. [How to rename a Git branch?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#2-how-to-rename-a-git-branch)
  3. [How to delete a local Git branch?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#3-how-to-delete-a-local-git-branch)
  4. [How to delete a remote Git branch?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#4-how-to-delete-a-remote-git-branch)
  5. [How to Git checkout remote branch?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#5-how-to-git-checkout-remote-branch)
  6. [How to edit (amend) a Git commit message?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#6-how-to-edit-amend-a-git-commit-message)
  7. [How to undo the last commit?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#7-how-to-undo-the-last-commit)
  8. [How to Git revert to the previous commit?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#8-how-to-git-revert-to-the-previous-commit)
  9. [How to revert a commit that has been pushed to the remote?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#9-how-to-revert-a-commit-that-has-been-pushed-to-the-remote)
  10. [How to Git revert a single file?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#10-how-to-git-revert-single-file)
  11. [How to undo Git add?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#11-how-to-undo-git-add)
  12. [How to remove a file from gGit without removing it from your file system?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#12-how-to-remove-a-file-from-git-without-removing-it-from-your-file-system)
  13. [Git Pull vs. Git Fetch](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#13-git-pull-vs-git-fetch)
  14. [How to force “Git pull” to overwrite local files?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#14-how-to-force-git-pull-to-overwrite-local-files)
  15. [How to push to GitHub when receiving the “need merge” error?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#15-how-to-push-to-github-when-receiving-the-need-merge-error)
  16. [How to create a tag in the GitHub repository?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#16-how-to-create-tag-in-github-repository)
  17. [How to clone all remote branches in Git?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#17-how-to-clone-all-remote-branches-in-git)
  18. [How to update or sync a forked repository?](https://www.creative-tim.com/blog/educational-tech/git-tutorial-fix-common-mistakes/#18-how-to-update-or-sync-a-forked-repository)

![github](https://www.creative-tim.com/blog/content/images/2021/09/github.jpg)
### 1. How to create a Git branch?
Before starting to create a new branch, make sure that your master/main is updated with the latest changes:

```
 $ git pull

```

After the above step, you can create your new branch and switch directly to it:

```
 $ git checkout -b <new-branch-name>

```

Or, you can just create the new branch without switching to it:

```
 $ git branch <new-branch-name>

```

If you want to switch to your new branch after you created it, just use:

```
 $ git checkout <new-branch-name>

```

Now that the branch is created, you can push it on GitHub:

```
 $ git push origin <new-branch-name>

```

### 2. How to rename a Git branch?
In order to rename a Git branch, one option would be to first switch to it and follow the below step:

```
 $ git checkout <old-branch-name>

```

Afterwards, you should see a message that confirms that the switch was successful:
Switched to branch 
Now you can rename the branch by:

```
 $ git branch -m <new-branch-name>

```

Another way to rename your Git branch is by using only one line, specifying both the old name and the new name:

```
 $ git branch -m <old-branch-name> <new-branch-name>

```

Once you have renamed your Git branch, it’s recommended to check its status:

```
 $ git branch -a

```

### 3. How to delete a local Git branch?
When developers work on different features, they often create other branches, separated from the main one with the main code.
Once the work on a feature is completed, it is often recommended to delete the branch.
As Git doesn’t allow you to delete the branch that you are currently on, you must first switch to a branch that you are NOT deleting, and after that, you can delete the branch that you want to:

```
 $ git checkout main // or master
 $ git branch -d <branch-name>

```

If the branch hasn’t been pushed or merged, you can force the deletion of the branch by using -D instead of -d.
### 4. How to delete a remote Git branch?
In order to delete a branch remotely, you should use the next command:

```
 $ git push <remote-name> --delete <branch-name>

```

### 5. How to Git checkout remote branch?
When working in a team, you might use remote repositories that can be hosted or on a colleague's local copy. Each of the remote repositories contains its own branches. For switching to a remote branch, you will have first to fetch the content of the branch and switch to it after that:

```
 $ git fetch --all
 $ git checkout <remote-branch-name>

```

### 6. How to edit (amend) a Git commit message?
For some reason, in certain cases, you would want to change your commit message. First, you need to know that editing your commit message translates in creating a new commit and replacing the old one.
If you haven’t pushed your commit yet to GitHub, and this exists only in your local repository, here is an easy way to change your last commit’s message. Go to the repository that contains your last commit in the command line and type:

```
 $ git commit --amend

```

Next, you need to edit the commit message and save your new commit. The next time you push, you should be able to see your new commit and message on GitHub.
As you might have been in the situation that you have already pushed the commit to GitHub, don’t worry, there is still a way to change your most recent commit message. In order to do this, you will have to force push a commit with an amended message. Be advised; this is not recommended as it changes the history of your repository, so use this option only when it is absolutely needed.
First, follow the steps from above and then type:

```
 $ git push --force-with-lease <branch-name>

```

### 7. How to undo the last commit?
You accidentally committed the wrong files to Git, but didn't push the commit to your Git repository yet. Because you did not push to a remote repository yet, your changes are not public. At this point, you can undo your changes. The easiest way to undo the last Git commit is to execute the $ git reset command with the “–soft” option that will preserve changes done to your files. You have to specify the commit to undo which is “HEAD~1” in this case.

```
 $ git reset --soft HEAD-1

```

If you want to delete the last commit, you can execute the `$ git reset` command with “-hard” option. The changes will be removed from the working directory and from the index, so _you will lose all modifications_.

```
 $ git reset --hard HEAD-1

```

Note: If you are not familiar with this notation, “HEAD~1” means that you want to reset the HEAD (the last commit) to one commit before in the log history.

```
 $ git log --oneline

```

### 8. How to git revert to the previous commit?
First of all, get commits list in order to have the commit id, using the git log command:

```
 $ git log --online

```

If you want to temporarily go back to the previous commit and then come back to where you were, all you have to do is check out the desired commit:

```
 $ git checkout <0c2a9da42>

```

Or, if you want to make commits while you're there, go ahead and make a new branch while you're at it:

```
 $ git checkout -b old-state <0c2a9da42>

```

On the other hand, if you want to really get rid of everything you've done since then, but you didn't push any of these commits, there is a possibility. All you have to do is simply reset:

```
 $ git reset --hard <0c2a9da42>

```

If you have pushed the commits, there is still a way to get rid of them. Check the next topic to see how.
### 9. How to revert a commit that has been pushed to the remote?
If you have already pushed your chain of commits to the remote repository, a _revert_ is a nicer way to cancel out changes. The revert command adds a new commit at the end of the chain.

```
 $ git revert <0c2a9da42>

```

### 10. How to Git revert single file?
You have made multiple changes on a file and committed them. Now you want to return to a previous file version. You can do the following to revert a single file to its previous status.
If the file isn’t committed, you can use:

```
 $ git checkout <filename>

```

If the file is already committed, you should find the hash of the commit and the path to your file and run this command in terminal:

```
 $ git checkout <commit-hash> -- <path/to/file>

 // e.g.
 $ git checkout <0c2a9da42> -- assets/main.css

```

You can see the commits which have made modifications to the given file(s) very easily, and you can get the correct commit hash by running the following command

```
 $ git log path/to/file

```

### 11. How to undo Git add?
You moved multiple files into the staging area with $ git add command, but no longer want to be part of a commit, then a simple reset will do the job:

```
 // for all files
 $ git reset  // OR
 $ git reset HEAD // OR
 $ git reset 

```

If you want to unstage a single file, you can use:

```
 // for single file
 $ git reset <filename> // OR
 $ git reset HEAD <filename> // OR
 $ git reset @ <filename> 

```

The changes you made will still be in the file/files. The above set of commands just remove that file/files from your staging area. The `$ git reset` command allows you to _reset_ your current head to a specific state. You can reset the state of specific files as well as an entire branch.
Note: _HEAD_ is a reference to the current commit. _@_ alone is a shortcut for head since Git v1.8.5
### 12. How to remove a file from Git without removing it from your file system?
You committed the wrong file on Git, or you forgot to add a file to .gitignore and committed it. Now you want to remove the file from git but you don't want to remove it from your local development environment.
Removing a single file with Git without deleting it:

```
 $ git rm --cached <filename>

```

Removing multiple files with Git without deleting them

```
 $ git rm --cached <filename1 filename2 filename3> 

```

Removing a single directory with Git without deleting it:

```
 $ git rm --cached <directory-name>

```

`--cached` will remove from just the index but not allow you to delete the file on the local system. The files will be removed in the remote repository when you run `$ git push`.
### 13. Git Pull vs. Git Fetch
Git pull and fetch are two commands that are commonly used, so knowing the difference between them will come in handy.
Suppose you're working on a clone repository, which is basically a duplicate of another repository. In that case, it's important to keep it updated with the latest changes that might have been applied to the original. In order to do that and bring those changes locally, you are going to use the above commands.

```
 $ git fetch

```

This is the command that allows you to download an object from another repository but it will not do any file transferring, meaning that will not make any changes locally. Basically, it is just checking if any changes are available.

```
 $ git pull

```

This is the command that will bring those changes from the remote repository and that will integrate them with your local branch. In other words, git pull does the same as git fetch, only that it is followed by an additional action(s):

```
 // e.g.  
 $ git merge

```

### 14. How to force “git pull” to overwrite local files?
If you want to overwrite everything with a copy from the remote branch, note that you will discard all your local changes.  
If you have local commits that you haven’t pushed yet, those will be lost as well.  
To overwrite/reset your local files, follow the below steps:

```
 $ git fetch --all
 $ git reset --hard origin/<branch-name>

```

### 15. How to push to GitHub when receiving the “need merge” error?
If you didn’t run a $ git pull before you tried to push your changes to the branch, you’d be getting a merge error. When you get this error, it usually means that someone else pushed a commit to the same branch you are trying to push to, but you don’t have it locally yet.  
To fix the issue, run the below code:

```
 $ git pull origin <branch-name>
 $ git push origin <branch-name>

```

If you want to do a force push, meaning that you don’t want to merge your local branch with the remote one, you can use the below syntax:

```
 $ git push -f origin <branch-name>

```

### 16. How to create a tag in the GitHub repository?
Git supports two types of tags: _lightweight_ and _annotated_.  
A _lightweight_ tag is very much like a branch that doesn’t change — it’s just a pointer to a specific commit.  
_Annotated_ tags, however, are stored as full objects in the Git database. They’re checksummed; contain the tagger name, email, and date; have a tagging message. It’s generally recommended that you create annotated tags.
Create a lightweight tag:

```
 $ git tag <tagname> // e.g $ git tag v1.0.0

```

Created Annotated tag (_recommened_):

```
 $ git tag -a <tagname> // e.g $ git tag -a v1.0.0
 // or create tag with message
 $ git tag -a <tagname> -m "tag description" // e.g $ git tag -a v1.0.0 -m "First release"

```

When pushing to your remote repo, tags are NOT included by default. You will need to explicitly say that you want to push your tags to your remote repo.
Push all locally tags:

```
 $ git push origin --tags

```

Push a single tag:

```
 $ git push origin <tagname>

```

To list all tags, use the following command:

```
 $ git tag

```

### 17. How to clone all remote branches in Git?
You can use the **git clone command** to your local Git. It will clone the whole repo to your system, then change your current working directory to the cloned repository folder.

```
 $ git clone git://account_name/reponame
 $ cd reponame

```

If you have many remote branches that you want to fetch at once, do:

```
 $ git pull --all

```

Next, look at the local branches in your repository:

```
 $ git branch 
 * main

```

But there are other branches hiding in your repository! You can see these using the -a flag:

```
 $ git branch -a
 * main
   remotes/origin/HEAD
   remotes/origin/main
   remotes/origin/another-branch

```

If you just want to take a quick peek at an upstream branch, you can check it out directly:

```
 $ git checkout origin/another-branch

```

But if you want to work on that branch, you'll need to create a local tracking branch which is done automatically by:

```
 $ git checkout another-branch

```

### 18. How to update or sync a forked repository?
You have successfully forked your interested repository. You need to keep it up to date with the original repository. The original repository is commonly referred to upstream .
Open your terminal and navigate to your cloned repository on local computer. Your local repository is not directly linked to the original repository. You must configure a remote that points to the upstream repository in Git.

```
 $ git remote -v // list all remote 
 $ git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
 $ git remote -v // verify the new upstream repository

```

There are two steps required to sync your repository with the upstream: first, you must fetch from the remote, then you must merge the desired branch into your local branch.

```
 $ git fetch upstream
 $ git checkout main
 $ git merge upstream/main

```

Past the initial upstream setup and main checkout, all you need to do is run the following command to sync your main with upstream:

```
 $ git pull upstream main

```
![github how to](https://www.creative-tim.com/blog/content/images/2021/09/github-how-to.jpg)
### **Final Thoughts**
Thanks for reading! These are the 18 repetitive questions that developers who use Git ask. We hope you found the answer you are looking for. If you encounter a problem in Git that is not on our list, we are waiting for you into our special 
**Extra Resources**  
Check out our latest repos:


[Educational Tech](https://www.creative-tim.com/blog/educational-tech/ "Educational Tech") [github](https://www.creative-tim.com/blog/github/ "github") [tutorial](https://www.creative-tim.com/blog/tutorial/ "tutorial") [Web Development](https://www.creative-tim.com/blog/web-development/ "Web Development") [open-source](https://www.creative-tim.com/blog/open-source/ "open-source")
### You might also like...
