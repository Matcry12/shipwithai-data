---
source_url: "https://make-school-courses.github.io/Git-Team-Workflow/"
source_domain: "make-school-courses.github.io"
topic: "git-first-job"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-25T06:40:17.736977+00:00"
word_count: 809
stage: "raw-extracted"
---

A tutorial to learn how to manage a coherent and organized workflow on collaborative team projects with a shared Git repository.

The goal of this tutorial is to practice branching with Git and how you can use branching to manage a workflow that involves multiple developers.

The team workflow presented here is based on Vincent Driessen’s article “A successful Git branching model” that introduced the “Git flow” pattern, which is now a best practice used by software engineering teams around the world.

In the course of a team project you are likely to apply the steps outlined here several times. You should follow this process on real team projects. Over time, this will make your team more productive while working in parallel.

This image shows the entire process described in the instructions below. The process likely appears complex at first, but you’ll do each step below one at a time. As you practice this process with teams, you will master it!

For this lesson you will work alone, but imagine you are working with a group of other developers. Imagine each commit along the way as being added by a different member of your group.

To start this exercise, set up your repo and code editor:

`Script.md`

file in your code editorthen carefully follow the instructions below step by step.

You are working on the script for a new movie, “The Unicorn King”. You need to fix typos (bugs) in the script, add new characters (features), resolve merge conflicts and publish (push) the script along the way.

While working on a team, you will create branches to manage team workflow:

`master`

branch.`develop`

branch.`feature`

branches.`hot-fix`

or `bug-fix`

branches.At any point you may want to merge one or more of these branches together to incorporate changes from several different lines of Development.

The first step is to create a new branch you can use
to make small changes to the **Development** version.
It’s important that the changes to this branch are
not visible until they are considered ready to be published.

Your goal: Create a new `develop`

branch and rename the character.
This will be the Development version.

`develop`

branch: `git checkout -b develop`

`git add Script.md`

`develop`

: `git commit -m "Rename George to ______"`

Sometimes your team will need to fix the Production version of a movie script
(product) that has already been published to movie executives (users).
Since you don’t want them to see the young boy George’s new name just yet,
it’s important to fix the typos in the Production version (`master`

branch).
This is a **Hot Fix**, so you’ll need to create a new branch off of `master`

.

Check the current version of the project for typos.

`git checkout master`

`typo-fixes`

branch: `git checkout -b typo-fixes`

`git add Script.md && git commit -m "Fix typos"`

`master`

branch: `git checkout master`

`typo-fixes`

branch into `master`

: `git merge typo-fixes`

`git push origin master`

These new changes should be incorporated into the Development version.

`git checkout develop`

`git merge typo-fixes`

Your team will be creating **New Features** frequently. On larger
teams it’s safer to keep this out of the Development version until
the new feature is fully functioning, which may take a long time.

The producers have suggested that adding a zookeeper to the story would be a good idea. They may change their minds in the future. Probably best to keep this in a new feature branch.

Create a new `zookeeper`

branch where you can incorporate the zookeeper.

`develop`

branch: `git status`

`git checkout develop`

`git checkout -b zookeeper`

`git add Script.md && git commit -m "Add Zookeeper"`

The word from the movie execs up top is that the plot’s conclusion is weak and reviews will be critical. You’ll need to improve the story’s ending.

The current ending is already part of the story (product), so your team is
improving something that has already been written (implemented). Therefore,
this work should be done on the Development version (`develop`

branch).

`git checkout develop`

`git add Script.md && git commit -m "Improve story ending"`

The new character ideas were approved! Be sure to proof read them before merging them with main story in the Development version.

`develop`

branch: `git checkout develop`

`zookeeper`

branch into `develop`

: `git merge zookeeper`

When releasing a new version of a product, you’ll merge the latest Development version (`develop`

branch) into the Production version (`master`

branch).

`develop`

branch: `git checkout develop`

`git checkout master`

`git merge develop`

`git push origin master`

Excellent work! Now you know how to manage a coherent and organized workflow on collaborative team projects with a shared Git repository.

In the course of a team project you are likely to apply the steps outlined here several times. You should follow this process on real team projects. Over time, this will make your team more productive while working in parallel.