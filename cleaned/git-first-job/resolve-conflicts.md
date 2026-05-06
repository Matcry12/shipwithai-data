---
title: "Resolve Git conflicts﻿"
topic: "git-first-job"
career_level: []
source_url: "https://www.jetbrains.com/help/pycharm/resolve-conflicts"
source_domain: "www.jetbrains.com"
word_count: 1171
text_to_link_ratio: 0.7013
signal_score: 0.8013
is_curated: false
tags:
  - remote
  - open-source
ingested_at: "2026-05-05"
---

#  Resolve Git conflicts﻿
Last modified: 05 June 2025
When you work in a team, you may come across a situation when somebody pushes changes to a file you are currently working on. If these changes do not overlap (that is, changes were made to different lines of code), the conflicting files are merged automatically. However, if the same lines were affected, Git cannot randomly pick one side over the other, and asks you to resolve the conflict.
In Git, conflicts may arise when you attempt to perform one of the following operations: [pull](https://www.jetbrains.com/help/pycharm/sync-with-a-remote-repository.html#pull), [merge](https://www.jetbrains.com/help/pycharm/apply-changes-from-one-branch-to-another.html#merge), [rebase](https://www.jetbrains.com/help/pycharm/apply-changes-from-one-branch-to-another.html#rebase-branch), [cherry-pick](https://www.jetbrains.com/help/pycharm/apply-changes-from-one-branch-to-another.html#cherry-pick), [unstash changes](https://www.jetbrains.com/help/pycharm/shelving-and-unshelving-changes.html#unstash) or [apply a patch](https://www.jetbrains.com/help/pycharm/using-patches.html#apply-patch). If there are conflicts, these operations will fail, and you will be prompted to accept the upstream version, prefer your version, or merge the changes:
![File merged with conflicts](https://resources.jetbrains.com/help/img/idea/2026.1/py_merge_conflicts_dialog.png)
The Conflicts dialog is triggered automatically when a conflict is detected on the Git level.
If you click Close in this dialog or call a Git operation that leads to a merge conflict from the command line, a Merge Conflicts node will appear in the Changes view of the Commit tool window with a link to resolve them:
![The Merge Conflicts node in the Local Changes view](https://resources.jetbrains.com/help/img/idea/2026.1/git_merge_conflicts_node.png)
PyCharm provides a tool for resolving conflicts locally. This tool consists of three panes:
  * The left pane shows the read-only local copy
  * The right pane shows the read-only version checked in to the repository.
  * The central pane is a fully-functional editor where the results of resolving conflicts are displayed. Initially, the contents of this pane are the same as the base revision of the file, that is, the revision from which both conflicting versions are derived.

![color coding in the conflict resolution tool](https://resources.jetbrains.com/help/img/idea/2026.1/conflict_resolution_tool_legend.png)
  1. Modified line
  2. Deleted lines
  3. Newly added lines
  4. Conflicting lines


###  Resolve conflicts﻿[](https://www.jetbrains.com/help/pycharm/resolve-conflicts.html#vcs-resolve-conflicts)
  1. Click Merge in the Conflicts dialog, the Resolve link in the Local Changes view, or select the conflicting file in the editor and choose VCS | Git | Resolve Conflicts from the main menu.
  2. To automatically merge all non-conflicting changes, click ![the Apply Non-Conflicting Changes button](https://resources.jetbrains.com/help/img/idea/2026.1/app.diff.applyNotConflicts.svg) (Apply All Non-Conflicting Changes) on the toolbar. You can also use the ![the Apply Non-Conflicting Changes from the Left button](https://resources.jetbrains.com/help/img/idea/2026.1/app.diff.applyNotConflictsLeft.svg) (Apply Non-Conflicting Changes from the Left Side) and ![the Apply Non-Conflicting Changes from the Right button](https://resources.jetbrains.com/help/img/idea/2026.1/app.diff.applyNotConflictsRight.svg) (Apply Non-Conflicting Changes from the Right Side) to merge non-conflicting changes from the left/right parts of the dialog, respectively.
  3. To resolve a conflict, you need to select which action to apply (accept ![the Accept button](https://resources.jetbrains.com/help/img/idea/2026.1/app.diff.arrow.svg) or ignore ![the Ignore button](https://resources.jetbrains.com/help/img/idea/2026.1/app.diff.remove.svg)) to the left (local) and the right (repository) versions and check the resulting code in the central pane:
![Resolving conflicts](https://resources.jetbrains.com/help/img/idea/2026.1/py_resolveConflict.png)
You can also right-click a highlighted conflict in the central pane and use the commands from the context menu. The Resolve using Left and Resolve using Right commands provide a shortcut to accepting changes from one side and ignoring them from the other side, respectively:
![the context menu of a conflicting change](https://resources.jetbrains.com/help/img/idea/2026.1/resolve_using_left_right.png)
For simple conflicts (for example, if the beginning and the end of the same line have been modified in different file revisions), the Resolve simple conflicts ![the Resolve simple conflicts button](https://resources.jetbrains.com/help/img/idea/2026.1/app.diff.magicResolve.svg) button that allows merging the changes in one click becomes available.
![the Resolve Simple Conflicts button](https://resources.jetbrains.com/help/img/idea/2026.1/simple_conflict_resolve.png)
Such conflicts are not resolved with the Apply All Non-Conflicting Changes action since you must make sure that they are resolved properly.
> ### note
> Note that the central pane is a fully-functional editor, so you can make changes to the resulting code directly in this dialog.
  4. It may also be useful to compare different versions to resolve a conflict. Use the ![the Compare contents button](https://resources.jetbrains.com/help/img/idea/2026.1/app-client.expui.vcs.diff.svg) toolbar button to invoke the list of options. Note that Base refers to the file version that the local and the repository versions originated from (initially displayed in the middle pane), while Middle refers to the resulting version. 
  5. Review merge results in the central pane and click Apply.


##  Productivity tips﻿[](https://www.jetbrains.com/help/pycharm/resolve-conflicts.html#resolve-conflicts-productivity-tips) Apply non-conflicting changes automatically[](https://www.jetbrains.com/help/pycharm/resolve-conflicts.html#wp5r4z_75) 
    
You can configure PyCharm to always apply non-conflicting changes automatically instead of telling it to do so from the Merge dialog. To do this, select the Automatically apply non-conflicting changes option on the Tools | Diff Merge settings page `Ctrl``Alt``0`. Manage changes in the central pane[](https://www.jetbrains.com/help/pycharm/resolve-conflicts.html#wp5r4z_76) 
    
You can manage changes in the central pane using the toolbar that appears when you hover over a change marker in the gutter and then click it. The toolbar is displayed together with a frame showing the previous contents of the modified line:
![the change toolbar](https://resources.jetbrains.com/help/img/idea/2026.1/conflicts_change_toolbar.png)
For example, when there are multiple non-conflicting changes, and you only need to skip one or two of them, it's easier to apply all of them simultaneously using the Apply all non-conflicting changes action and then undo the unwanted ones using the Revert action from this toolbar.
##  Handle conflicts related to LF and CRLF line endings﻿[](https://www.jetbrains.com/help/pycharm/resolve-conflicts.html#CRLF_warning)
Quite often, people working in a team and contributing to the same repository use different operating systems. This may result in problems with line ending, because Unix, Linux and macOS use `LF`, and Windows uses `CRLF` to mark the end of a line.
PyCharm displays the discrepancies in line endings in the Diff Viewer, so you can fix them manually. If you want Git to solve such conflicts automatically, you need to set the `core.autocrlf` attribute to `true` on Windows and to `input` on Linux and macOS (for more details, refer to [Dealing with line endings](https://help.github.com/articles/dealing-with-line-endings/)). You can change the configuration manually by running `git config --global core.autocrlf true` on Windows or `git config --global core.autocrlf input` on Linux and macOS.
However, PyCharm can automatically analyze your configuration, warn you if you are about to commit `CRLF` into a remote repository, and suggest setting the `core.autocrlf` setting to `true` or `input` depending on your operating system.
To enable smart handling of `LF` and `CRLF` line separators, open the Settings dialog `Ctrl``Alt``0`, and select the Version Control | Git node on the left. Enable the Warn if CRLF line separators are about to be committed option.
After you have enabled this option, PyCharm will display the Line Separators Warning Dialog each time you are about to commit a file with `CRLF` separators, unless you have set any related [Git attributes](https://www.kernel.org/pub/software/scm/git/docs/gitattributes.html) in the affected file (in this case, PyCharm supposes that you clearly understand what you are doing and excludes this file from analysis).
In the Line Separators Warning Dialog, click one of the following:
  * Commit As Is to ignore the warning and commit a file with `CRLF` separators.
  * Fix and Commit to have the `core.autocrlf` attribute set to `true` or `input` depending on your operating system. As a result, `CRLF` line separators will be replaced with `LF` before the commit.


If, at a later time, you need to review how exactly conflicts were resolved during a merge, you can locate the required merge commit in the Log tab of the Git tool window `Alt``0`, select a file with conflicts in the Commit Details pane in the right, and click ![the Show diff icon](https://resources.jetbrains.com/help/img/idea/2026.1/app-client.expui.vcs.diff.svg) or press `Ctrl``0`. For more information, refer to [Review how changes were merged](https://www.jetbrains.com/help/pycharm/investigate-changes.html#review_merge_commit).
### See also
#### Procedures


#### Reference
