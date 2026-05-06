---
title: "if you didn't specify any tracking information for this branch"
topic: "git-first-job"
career_level:
  - executive
source_url: "https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them"
source_domain: "citizen428.net"
word_count: 1516
text_to_link_ratio: 0.9452
signal_score: 0.9452
is_curated: false
tags:
  - remote
  - open-source
  - executive
ingested_at: "2026-05-05"
---

I originally wrote this article for [Codementor](https://www.codementor.io/citizen428/git-tutorial-10-common-git-problems-and-how-to-fix-them-aajv0katd) in October 2014. It should have something for everyone, from fairly new git users to experienced developers.
##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#1-discard-local-file-modifications)1. Discard local file modifications 
Sometimes the best way to get a feel for a problem is diving in and playing around with the code. Unfortunately, the changes made in the process sometimes turn out to be less than optimal, in which case reverting the file to its original state can be the fastest and easiest solution:

```
git checkout -- Gemfile # reset specified path
git checkout -- lib bin # also works with multiple arguments

```

In case you’re wondering, the double dash (`--`) is a common way for command line utilities to signify the end of command options.
##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#2-undo-local-commits)2. Undo local commits 
Alas, sometimes it takes us a bit longer to realize that we are on the wrong track, and by that time one or more changes may already have been committed locally. This is when `git reset` comes in handy:

```
git reset HEAD~2        # undo last two commits, keep changes
git reset --hard HEAD~2 # undo last two commits, discard changes

```

Be careful with the `--hard` option! It resets your working tree as well as the index, so all your modifications will be lost for good.
##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#3-remove-a-file-from-git-without-removing-it-from-your-file-system)3. Remove a file from git without removing it from your file system 
If you are not careful during a `git add`, you may end up adding files that you didn’t want to commit. However, `git rm` will remove it from both your staging area, as well as your file system, which may not be what you want. In that case make sure you only remove the staged version, and add the file to your `.gitignore` to avoid making the same mistake a second time:

```
git reset filename          # or git remove --cached filename
echo filename >> .gitignore # add it to .gitignore to avoid re-adding it

```

##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#4-edit-a-commit-message)4. Edit a commit message 
Typos happen, but luckily in the case of commit messages, it is very easy to fix them:

```
git commit --amend                  # start $EDITOR to edit the message
git commit --amend -m "New message" # set the new message directly

```

But that’s not all `git-amend` can do for you. Did you forget to add a file? Just add it and amend the previous commit!

```
git add forgotten_file
git commit --amend

```

Please keep in mind that `--amend` actually will create a new commit which replaces the previous one, so don’t use it for modifying commits which already have been pushed to a central repository. An exception to this rule can be made if you are absolutely sure that no other developer has already checked out the previous version and based their own work on it, in which case a forced push (`git push --force`) may still be ok. The `--force` option is necessary here since the tree’s history was locally modified which means the push will be rejected by the remote server since no fast-forward merge is possible.
##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#5-clean-up-local-commits-before-pushing)5. Clean up local commits before pushing 
While `--amend` is very useful, it doesn’t help if the commit you want to reword is not the last one. In that case an interactive rebase comes in handy:

```
git rebase --interactive
# if you didn't specify any tracking information for this branch
# you will have to add upstream and remote branch information:
git rebase --interactive origin branch

```

This will open your configured editor and present you with the following menu:

```
pick 8a20121 Upgrade Ruby version to 2.1.3
pick 22dcc45 Add some fancy library
# Rebase fcb7d7c..22dcc45 onto fcb7d7c
#
# Commands: # p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out

```

On top you’ll see a list of local commits, followed by an explanation of the available commands. Just pick the commit(s) you want to update, change `pick` to `reword` (or `r` for short), and you will be taken to a new view where you can edit the message.
However, as can be seen from the above listing, interactive rebases offer a lot more than simple commit message editing: you can completely remove commits by deleting them from the list, as well as edit, reorder, and squash them. Squashing allows you to merge several commits into one, which is something I like to do on feature branches before pushing them to the remote. No more “Add forgotten file” and “Fix typo” commits recorded for eternity!
##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#6-reverting-pushed-commits)6. Reverting pushed commits 
Despite the fixes demonstrated in the previous tips, faulty commits do occasionally make it into the central repository. Still this is no reason to despair, since `git` offers an easy way to revert single or multiple commits:

```
 git revert c761f5c              # reverts the commit with the specified id
 git revert HEAD^                # reverts the second to last commit
 git revert develop~4..develop~2 # reverts a whole range of commits

```

In case you don’t want to create additional revert commits but only apply the necessary changes to your working tree, you can use the `--no-commit`/`-n` option.

```
# undo the last commit, but don't create a revert commit
git revert -n HEAD

```

The manual page at `man 1 git-revert` list further options and provides some additional examples.
##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#7-avoid-repeated-merge-conflicts)7. Avoid repeated merge conflicts 
As every developer knows, fixing merge conflicts can be tedious, but solving the exact same conflict repeatedly (e.g. in long running feature branches) is outright annoying. If you’ve suffered from this in the past, you’ll be happy to learn about the underused reuse recorded resolution feature. Add it to your global config to enable it for all projects:

```
git config --global rerere.enabled true

```

Alternatively you can enable it on a per-project basis by manually creating the directory `.git/rr-cache`.
This sure isn’t a feature for everyone, but for people who need it, it can be real time saver. Imagine your team is working on various feature branches at the same time. Now you want to merge all of them together into one testable pre-release branch. As expected, there are several merge conflicts, which you resolve. Unfortunately it turns out that one of the branches isn’t quite there yet, so you decide to un-merge it again. Several days (or weeks) later when the branch is finally ready you merge it again, but thanks to the recorded resolutions, you won’t have to resolve the same merge conflicts again.
The man page (`man git-rerere`) has more information on further use cases and commands (`git rerere status`, `git rerere diff`, etc).
##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#8-find-the-commit-that-broke-something-after-a-merge)8. Find the commit that broke something after a merge 
Tracking down the commit that introduced a bug after a big merge can be quite time consuming. Luckily `git` offers a great binary search facility in the form of `git-bisect`. First you have to perform the initial setup:

```
 git bisect start         # starts the bisecting session
 git bisect bad           # marks the current revision as bad
 git bisect good revision # marks the last known good revision

```

After this git will automatically checkout a revision halfway between the known “good” and “bad” versions. You can now run your specs again and mark the commit as “good” or “bad” accordingly.

```
git bisect good # or git bisec bad

```

This process continues until you get to the commit that introduced the bug.
##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#9-avoid-common-mistakes-with-git-hooks)9. Avoid common mistakes with git hooks 
Some mistakes happen repeatedly, but would be easy to avoid by running certain checks or cleanup tasks at a defined stage of the `git` workflow. This is exactly the scenario that hooks were designed for. To create a new hook, add an executable file to `.git/hooks`. The name of the script has to correspond to one of the available hooks, a full list of which is available in the manual page (`man githooks`). You can also define global hooks to use in all your projects by creating a template directory that git will use when initializing a new repository (see man git-init for further information). Here’s how the relevant entry in `~/.gitconfig` and an example template directory look like:

```
[init]
    templatedir = ~/.git_template

  → tree .git_template
  .git_template
  └── hooks
      └── pre-commit

```

When you initialize a new repository, files in the template directory will be copied to the corresponding location in your project’s `.git` directory.
What follows is a slightly contrived example `commit-msg` hook, which will ensure that every commit message references a ticket number like “`#123`“.

```
ruby
  #!/usr/bin/env ruby
  message = File.read(ARGV[0])
  unless message =~ /\s*#\d+/
    puts "[POLICY] Your message did not reference a ticket."
    exit 1
  end

```

##  [#](https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/#10-when-all-else-fails)10. When all else fails 
So far we covered quite a lot of ground on how to fix common errors when working with `git`. Most of them have easy enough solutions, however there are times when one has to get out the big guns and rewrite the history of an entire branch. One common use case for this is removing sensitive data (e.g. login credentials for production systems) that were committed to a public repository:

```
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch secrets.txt' \
  --prune-empty --tag-name-filter cat -- --all

```

This will remove the file `secrets.txt` from every branch and tag. It will also remove any commits that would be empty as a result of the above operation. Keep in mind that this will rewrite your project’s entire history, which can be very disruptive in a distributed workflow. Also while the file in question has now been removed, the credentials it contained should still be considered compromised!
GitHub has a [very good tutorial on removing sensitive data](https://help.github.com/articles/remove-sensitive-data/) and `man git-filter-branch` has all details on the various available filters and their options.
#### Feedback
Discuss on [ Mastodon](https://tootpick.org/#text=https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/%20by%20@citizen428@chaos.social), [Bluesky](https://bsky.app/intent/compose?text=https://citizen428.net/blog/10-common-git-problems-and-how-to-fix-them/%20by%20@citizen428.net) , or  send me an email. 
* * *
