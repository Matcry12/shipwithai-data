---
source_url: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github
title: "Resolving a merge conflict on GitHub"
crawl_depth: 1
crawled_at: 2026-05-05T14:26:54Z
word_count: 729
---

# Resolving a merge conflict on GitHub
You can resolve simple merge conflicts that involve competing line changes on GitHub, using the conflict editor.
You can only resolve merge conflicts on GitHub that are caused by competing line changes, such as when people make different changes to the same line of the same file on different branches in your Git repository. For all other types of merge conflicts, you must resolve the conflict locally on the command line. For more information, see [Resolving a merge conflict using the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line).
If you have access to Copilot cloud agent and it is enabled for the repository, you can click **Fix with Copilot** in the merge box to have Copilot resolve the merge conflicts automatically. Copilot will analyze the conflicting changes, resolve the conflicts, and verify that the build, tests, and linter still pass. For more information, see [Review output from Copilot](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/make-changes-to-an-existing-pr#resolving-merge-conflicts).
When you resolve a merge conflict on GitHub, the entire [base branch](https://docs.github.com/en/get-started/learning-about-github/github-glossary#base-branch) of your pull request is merged into the [head branch](https://docs.github.com/en/get-started/learning-about-github/github-glossary#head-branch). Make sure you really want to commit to this branch. If the head branch is the default branch of your repository, you'll be given the option of creating a new branch to serve as the head branch for your pull request. If the head branch is protected you won't be able to merge your conflict resolution into it, so you'll be prompted to create a new head branch. For more information, see [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
  1. Under your repository name, click 
![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Pull requests," is outlined in dark orange.](https://docs.github.com/assets/cb-51156/images/help/repository/repo-tabs-pull-requests-global-nav-update.png)
  2. In the "Pull Requests" list, click the pull request with a merge conflict that you'd like to resolve.
  3. Near the bottom of your pull request, click **Resolve conflicts**.
![Screenshot of a warning that a pull request has a merge conflict. The "Resolve merge conflicts" button is outlined in dark orange.](https://docs.github.com/assets/cb-69649/images/help/pull_requests/resolve-merge-conflicts-button.png)
If the **Resolve conflicts** button is deactivated, your pull request's merge conflict is too complex to resolve on GitHub. You must resolve the merge conflict using an alternative Git client, or by using Git on the command line. For more information see [Resolving a merge conflict using the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line).
  4. Decide if you want to keep only your branch's changes, keep only the other branch's changes, or make a brand new change, which may incorporate changes from both branches. Delete the conflict markers `<<<<<<<`, `=======`, `>>>>>>>` and make the changes you want in the final merge.
  5. If you have more than one merge conflict in your file, scroll down to the next set of conflict markers and repeat steps four and five to resolve your merge conflict.
  6. Once you've resolved all the conflicts in the file, click **Mark as resolved**.
![Screenshot of the editor to resolve a merge conflict in a pull request. The "Mark as resolved" button is outlined in dark orange.](https://docs.github.com/assets/cb-148198/images/help/pull_requests/mark-as-resolved-button.png)
  7. If you have more than one file with a conflict, select the next file you want to edit on the left side of the page under "conflicting files" and repeat steps four through seven until you've resolved all of your pull request's merge conflicts.
  8. Once you've resolved all your merge conflicts, click **Commit merge**. This merges the entire base branch into your head branch.
![Screenshot of the editor to resolve a merge conflict in a pull request. The "Commit merge" button is outlined in dark orange.](https://docs.github.com/assets/cb-198808/images/help/pull_requests/merge-conflict-commit-changes.png)
  9. If prompted, review the branch that you are committing to.
If the head branch is the default branch of the repository, you can choose either to update this branch with the changes you made to resolve the conflict, or to create a new branch and use this as the head branch of the pull request.
If you choose to create a new branch, enter a name for the branch.
If the head branch of your pull request is protected you must create a new branch. You won't get the option to update the protected branch.
Click **Create branch and update my pull request** or **I understand, continue updating BRANCH**. The button text corresponds to the action you are performing.
  10. To merge your pull request, click **Merge pull request**. For more information about other pull request merge options, see [Merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request).


## [Further reading](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github#further-reading)
