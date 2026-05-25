---
source_url: "https://www.w3schools.com/git/git_merge_conflicts.asp?remote=github"
source_domain: "w3schools.com"
topic: "git-first-job"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-25T06:47:07.114504+00:00"
word_count: 418
stage: "raw-extracted"
---

# Git Merge Conflicts

## What is a Merge Conflict?

A **merge conflict** happens when two branches change the same part of a file.

Git can't decide which change to keep, so you have to choose.

You must resolve the conflict before you can finish the merge.

## Why Do Merge Conflicts Happen?

Merge conflicts usually happen when you merge branches that changed the same lines in a file.

This is common in collaborative projects or when working on long-lived branches.

## How to See and Resolve Merge Conflicts

When you merge a branch and there are conflicting changes, Git will pause and mark the files with conflicts.

### Example: Merge a Branch

`git merge feature-branch`


If there are conflicts, Git will tell you which files are affected.

## See Which Files Have Conflicts

Use `git status`

to see which files need your attention:

### Example: Check Status

`git status`


## See the Differences

Use `git diff`

to see what changed and help you decide how to resolve the conflict:

### Example: See Differences

`git diff`


## Edit the Conflict Markers

Open the conflicted file. You'll see sections like this:

### Conflict Markers

```
<<<<<<< HEAD
Your changes here
=======
Other branch's changes
>>>>>>> feature-branch
```

Edit the file to keep what you want, then remove the conflict markers (`<<<<<<<`

, `=======`

, `>>>>>>>`

).

## Mark as Resolved

After fixing the file, mark it as resolved:

### Example: Mark Resolved

`git add filename.txt`


## Complete the Merge

Finish the merge with a commit (if Git doesn't do it automatically):

### Example: Finish Merge

`git commit`


## Cancel the Merge

If you want to stop and undo the merge:

### Example: Abort Merge

`git merge --abort`


## Use a Visual Merge Tool

If you prefer, you can use a visual tool to resolve conflicts:

### Example: Use Mergetool

`git mergetool`


## Pick One Side's Changes

If you want to keep only your changes or only the other branch's changes:

### Example: Keep Our Changes

`git checkout --ours filename.txt`


### Example: Keep Their Changes

`git checkout --theirs filename.txt`


## Troubleshooting & Best Practices

- If you're stuck, you can always use
`git merge --abort`

to start over. - Make sure you remove all conflict markers before marking as resolved.
- If you use
`git mergetool`

and don't like the result, you can still edit the files by hand.

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

`git checkout filename.txt`