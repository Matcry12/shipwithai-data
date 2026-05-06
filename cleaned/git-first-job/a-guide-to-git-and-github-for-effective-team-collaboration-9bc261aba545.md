---
title: "Ignore node_modules and build files"
topic: "git-first-job"
career_level:
  - executive
source_url: "https://mohamed-elrefaey-77102.medium.com/a-guide-to-git-and-github-for-effective-team-collaboration-9bc261aba545"
source_domain: "mohamed-elrefaey-77102.medium.com"
word_count: 3619
text_to_link_ratio: 0.959
signal_score: 0.959
is_curated: false
tags:
  - remote
  - open-source
  - executive
ingested_at: "2026-05-05"
---

Your project's source code is its most valuable asset. Losing or corrupting the codebase can be a devastating event, impacting not only your project but also your reputation as a developer. This is why it's essential to establish a reliable workflow that every team member follows rigorously when making and promoting changes.

The good news is that creating a robust Git workflow is straightforward, and both Git and GitHub are proven, powerful tools that support teams in managing code, maintaining quality, and collaborating effectively.

This guide covers everything from the basics to advanced Git workflows, providing best practices, real-world scenarios, and actionable tips to help your team set up a structured and efficient development process.

![None](https://miro.medium.com/v2/resize:fit:700/1*VTuGA5y1sN_cEGMl28uzSA.png)

### Part 1: Git and GitHub Basics for Beginners

### What is Git?

**Git** is a version control system that helps track and manage changes in codebases. It allows multiple people to work on the same project without overwriting each other's work and provides a way to roll back to previous versions if needed.

![None](https://miro.medium.com/v2/resize:fit:700/1*aqu1DE8e-hm3iUoUHKaM8A.png)

### What is GitHub?

**GitHub** is a platform for hosting Git repositories. It adds collaboration features, code reviews, and project management tools, allowing teams to work more effectively together.

![None](https://miro.medium.com/v2/resize:fit:700/1*vnsQRRraSudgq5yBPBCgSA.png)

### Key Concepts

* **Repository (Repo)**: A directory where your project's files and history are stored.* **Commit**: A snapshot of your project at a specific time.* **Branch**: A separate line of development, often used for features or bug fixes.* **Merge**: Combining branches to integrate changes.* **Clone**: Copying a remote repository to your local machine.* **Pull**: Bringing changes from a remote repository to your local machine.* **Push**: Sending local commits to a remote repository.

![None](https://miro.medium.com/v2/resize:fit:700/1*1FHhdoFvCj2WPX074-_sIw.png)

### Basic Workflow in Git

* **Clone a Repository**: Download a repository from GitHub to your local machine.

```
git clone <repo-url>
```

* **Create and Switch Branches**: Work on new features or fixes on separate branches. bash Copy code

```
git checkout -b feature-branch
```

* **Add and Commit Changes**: Save a snapshot of your current work.

```
git add .
git commit -m "Your commit message"
```

* **Push Changes**: Upload your branch to the remote repository.

```
git push origin feature-branch
```

* **Create a Pull Request (PR)**: Propose merging your branch into the main branch on GitHub.

### Git Flow Model Variations (Hotfix Branches)

The **Git Flow model** includes not only feature and release branches but also **hotfix branches**. These are critical for production issues that need quick fixes without interrupting other development.

![None](https://miro.medium.com/v2/resize:fit:700/1*R02zl8WXVJm7qo5N_4yz-Q.png)

* **Creating a Hotfix Branch**

```
git checkout -b hotfix-issue-description main
```

* After fixing the bug, merge the hotfix branch back into both `main` and `develop` (or whatever branch represents ongoing development).

**When to Use**: Hotfix branches are ideal for large projects that require maintaining a stable `main` branch while ongoing development occurs in other branches.

### Git Aliases

Git aliases can simplify repetitive commands, saving time and reducing errors.

**Setting Up Aliases**

```
git config --global alias.co checkout
git config --global alias.cm commit
git config --global alias.st status
```

**Common Aliases**:

* `git co`: Shortcut for `git checkout`* `git cm`: Shortcut for `git commit`* `git lg`: Often used for a more compact `git log` view with commits

**When to Use**: Git aliases are helpful for reducing keystrokes and streamlining workflows, especially for frequently used commands.

### Part 2: Intermediate Concepts for Enhanced Collaboration

### Branching Strategy

A structured branching strategy helps manage ongoing work and keeps the codebase stable.

* **Main Branch**: Reflects the latest, stable code.* **Development Branch**: Used to integrate new features and bug fixes before they're production-ready.* **Feature Branches**: Separate branches for each new feature or bug fix.* **Hotfix Branches**: Used to address critical production issues immediately.

![None](https://miro.medium.com/v2/resize:fit:700/1*vPf8o-z4II9TMpcua1Scow.png)

### Fetching vs. Pulling

Understanding `fetch` and `pull` is crucial to keeping your local repository in sync with the remote repository.

* **git fetch**: Downloads updates from the remote repository but doesn't change your working files.* **git pull**: Combines `fetch` and `merge` to bring in changes and apply them to your current branch.

![None](https://miro.medium.com/v2/resize:fit:700/1*1kEgW1zx2IdoEDHl74BEcA.png)

**Scenario**:
If Sarah wants to see if there are any new changes on `main` without affecting her local work, she can use `git fetch`. Later, if she decides to update her branch with those changes, she can use `git pull`.

**Commands:**

```
git fetch origin
git pull origin main
```

### Commit Message Conventions

Consistent commit messages are essential for tracking changes. **Conventional Commits** provide a standardized format that organizes changes.

**Format**:

```
type(scope): description
```

**Types**:

* `feat`: New feature* `fix`: Bug fix* `chore`: Maintenance tasks (e.g., refactoring)* `docs`: Documentation changes

**Example**:

```
feat(auth): add user authentication with JWT
fix(login): resolve login delay issue
```

**Commitlint**: A tool to enforce commit message conventions. You can integrate it with Git hooks:

```
npm install --save-dev @commitlint/config-conventional @commitlint/cli
echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js
```

**Scenario**: Following this convention, the team can easily identify commits related to features, bug fixes, and general maintenance. If they need to revert all bug fixes before a major release, filtering by `fix` commits makes it easy.

### Pull Requests (PRs) and Code Review Process

Pull Requests allow team members to review code before merging it into the main branch.

* **Use a PR Template**: Add a `.github/PULL_REQUEST_TEMPLATE.md` file to prompt contributors to include testing steps and motivation.* **Assign Code Owners**: Use `.github/CODEOWNERS` to designate reviewers responsible for specific parts of the codebase.

**Example PR Checklist**:

* All tests pass* Code is documented* No unnecessary files (e.g., no `console.log`)

### Two People Working Together on a Project: Practical Workflow

Let's go through a practical example of two people, Alex and Jamie, collaborating on a project using Git.

#### Step-by-Step Scenario:

* **Starting with the Main Branch:**

Alex and Jamie start with a common base, the `main` branch, where the latest, stable code lives.

* **Creating Feature Branches:**

Alex is assigned to work on `feature-login`, and Jamie is assigned `feature-signup`.

They each create their own branches:

```
git checkout -b feature-login  # Alex
git checkout -b feature-signup  # Jamie
```

* **Working Independently**

Each person makes commits to their own branch.

They frequently commit their changes:

```
git add .
git commit -m "Add login validation"  # Alex
```

* **Updating Branches with Main (Rebasing)**

While they work, updates are made to `main` by other team members.

Alex wants to bring `feature-login` up-to-date with `main`:

```
git checkout feature-login
git pull origin main --rebase
```

This replays Alex's commits on top of the latest `main` branch commits, keeping the commit history clean.

* **Handling Conflicts**

If a conflict arises during rebase (e.g., both Alex and Jamie modified the same file), Git will prompt them to resolve it.

Alex resolves conflicts, stages the file, and continues the rebase:

```
git add conflicted-file.js
git rebase --continue
```

* **Using Stash to Switch Context**

Jamie is halfway through her work on `feature-signup` when a bug in `main` needs her attention.

She stashes her changes:

```
git stash
git checkout main
```

After fixing the bug on `main`, she switches back to her branch and reapplies her stashed work:

```
git checkout feature-signup
git stash pop
```

* **Creating Pull Requests**

When ready, Alex and Jamie push their branches to GitHub and open Pull Requests (PRs).

They request reviews from each other to ensure code quality and alignment with project goals.

* **Reviewing and Merging**

Alex reviews Jamie's PR, suggests minor changes, and once everything looks good, approves it.

Jamie merges her PR, and Alex then rebases `feature-login` to pull in Jamie's changes cleanly.

* **Final Merge**

After all features are complete and tested, both branches are merged into `main`.

GitHub merges the code while preserving commit history and minimizing conflicts.

**Summary of Key Commands for Team Workflow:**

**Create and switch branches**:

```
git checkout -b branch-name
git checkout main
```

**Rebase to stay up-to-date**:

```
git pull origin main --rebase
```

**Stash changes to switch context**:

```
git stash
git stash pop
```

**Commit changes**:

```
git add .
git commit -m "Your message here"
```

**Push changes to GitHub**:

```
git push origin branch-name
```

### Part 3: Advanced Git Techniques

### Rebasing vs. Merging

**Rebase** and **Merge** both integrate changes but manage commit history differently.

* **Merge**: Combines branches and preserves commit history, adding a merge commit.* **Rebase**: Re-applies commits from your branch on top of the latest commits in another branch, creating a linear history.

**Scenario**:
If Sarah's `feature/wishlist` branch is behind `develop`, she rebases it to integrate the latest changes without adding a merge commit.

**Commands**:

```
git checkout feature/wishlist
git rebase develop
```

**Best Practice**:
Use `rebase` for feature branches before creating a PR to keep the history clean, and `merge` for integrating branches like `develop` into `main`.

### Rebase Onto for Advanced Rebase Operations

The `git rebase --onto` command allows you to rebase a branch onto a different starting point, which is helpful for moving feature branches or splitting them.

* **Example**

```
git rebase --onto new-base old-base branch
```

**When to Use**: This is useful for reorganizing branches when the base branch has changed significantly or when you want to change the base of a feature branch without merging all previous commits.

### Stashing for Temporary Changes

**Stashing** temporarily saves changes that you're not ready to commit.

**Scenario**:
Sarah is working on `feature/wishlist` but needs to switch to a critical bug fix. She stashes her changes, switches branches, makes the fix, and then reapplies her stashed changes.

Commands:

```
git stash
git checkout develop
git stash pop
```

### Cherry-Picking

**Cherry-picking** allows you to select specific commits from one branch and apply them to another.

**Scenario**:
John realizes a bug fix on `develop` is also needed on `feature/wishlist`. Instead of merging, he cherry-picks the specific commit to apply the fix to his branch.

**Commands**:

```
git cherry-pick <commit-hash>
```

### Using Tags for Release Management

Tags mark specific points in the project's history and are often used for releases.

**Example**:

```
git tag -a v1.0.0 -m "First major release"
git push origin v1.0.0
```

**GitHub Releases**:
Combine tags with GitHub Releases to document and publish project versions, making it easy for users to download specific versions.

### Semantic Versioning for Consistent Release Management

**Semantic Versioning** follows a `MAJOR.MINOR.PATCH` format.

**Example**:

* `1.0.0` - Initial release* `1.1.0` - Added feature* `1.1.1` - Bug fix

**Scenario**:
The team uses Semantic Versioning for each release. When they add a major feature, they bump the minor version (e.g., `1.2.0`), and when fixing a bug, they bump the patch version (e.g., `1.2.1`).

### Git Workflows: Git Flow and Trunk-Based Development

Different workflows suit different team sizes and project needs.

* **Git Flow**: A branching model that uses separate branches for features, releases, and hotfixes.* **Trunk-Based Development**: Encourages developers to merge code into `main` frequently, often with short-lived feature branches or no separate branches at all.

**When to Use**:

* **Git Flow** works well for large projects with formal release processes.* **Trunk-Based Development** suits teams that deploy frequently and prioritize continuous integration.

### Git Bisect

**Git Bisect** is a powerful tool for debugging. It helps you find the specific commit that introduced a bug by performing a binary search through your commit history.

* **How to Use Git Bisect**

```
git bisect start
git bisect bad  # Mark the current (buggy) version as bad
git bisect good <commit-hash>  # Mark a known good commit
```

* Git will then checkout a middle commit, and you can test if the bug is present. Keep marking commits as `bad` or `good`, and Git will narrow down to the exact commit where the issue was introduced.

**When to Use**: Git Bisect is invaluable when you need to track down when a bug was introduced, especially in large codebases.

### Commit Hooks

**Commit Hooks** allow you to automate tasks at specific points in your Git workflow, such as pre-commit or post-merge.

* **Setting Up a Pre-Commit Hook**: In the `.git/hooks` directory, you can create a `pre-commit` script. For example, to run tests before every commit

```
#! /bin/sh
npm test || exit 1
```

**When to Use**: Hooks are useful for enforcing standards (e.g., linting, running tests) before allowing commits. This helps maintain code quality across the team.

### Git Submodules

**Git Submodules** allow you to include other Git repositories within your project, which is useful for shared libraries or dependencies.

* **Adding a Submodule**

```
git submodule add <repo-url> path/to/submodule
```

Updating a Submodule

```
git submodule update --remote
```

**When to Use**: Use submodules if your project relies on specific versions of other repositories, and you want to keep them separate but still linked.

### Git .gitignore and .gitattributes

**.gitignore**: Lists files or directories you want Git to ignore. Common examples include build files, dependencies, and sensitive information like credentials.

Example:

```
# Ignore node_modules and build files
node_modules/
build/
```

**.gitattributes**: Controls how certain files are handled by Git, such as line endings or large files.

**Example:**

```
*.jpg binary  # Treat all .jpg files as binary
```

**When to Use**: These files help keep your repository clean and avoid committing unnecessary or sensitive files.

### Branch Protection Rules on GitHub

In a team setting, you can enable **branch protection rules** on GitHub to enforce workflows.

**Example Rules**:

* Require PR reviews before merging* Require passing status checks (like CI tests) before merging* Restrict who can push to certain branches (like `main`)

![None](https://miro.medium.com/v2/resize:fit:700/1*ax5IvjJDnoBQYPqVs_P-jA.png)

**When to Use**: Branch protection rules ensure that code in important branches (e.g., `main`) meets quality standards and avoids accidental overwrites.

### Squash Commits

Squashing commits combines multiple small commits into a single one, which keeps the commit history clean.

* **How to Squash Commits During a Rebase:**

```
git rebase -i HEAD~<number-of-commits>
```

* Use `pick` for the first commit and change `pick` to `squash` (or `s`) for the following commits. This will merge them into one.

![None](https://miro.medium.com/v2/resize:fit:700/1*a9Kgzo6fY4r4hccsySqzcQ.png)

**When to Use**: Squash commits when you have many minor commits in a PR, like "fixed typo" or "small tweak," to present a single, clean commit in the final merge.

### Git Reset vs. Git Revert

Both commands "undo" changes, but in different ways:

* **git reset**: Moves the branch pointer back to a previous commit and changes the history. Use with caution, as this can rewrite history.* **git revert**: Creates a new commit that undoes the changes from a previous commit without changing the history.

![None](https://miro.medium.com/v2/resize:fit:700/1*y9xZsNq7SKRYAJHt8yGvHw.png)

**When to Use**: Use `git revert` to safely undo changes in a team environment, especially on shared branches. Use `git reset` if you need to discard recent commits on a personal branch.

### Part 4: Automation in GitHub and other features

### GitHub Actions for Automation

GitHub Actions lets you automate tasks like testing, building, and deploying your code.

**Example Workflow:**

```
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'
      - run: npm install
      - run: npm test
```

**Scenario**:
Every time a team member pushes code, GitHub Actions automatically runs tests to ensure the changes don't break anything, blocking PRs that don't pass the tests.

### Worktrees for Multi-Branch Work

**Git Worktrees** allow you to work on multiple branches simultaneously in separate directories.

**Commands:**

```
git worktree add ../new-directory branch-name
```

**Remove a Worktree**:

```
git worktree remove ../path-to-new-worktree
```

**Scenario**:
If Sarah is working on a feature but needs to fix a bug in `develop`, she can create a worktree to check out `develop` in a new directory without interrupting her work on the feature.

### Advanced Git Diff Commands

Git's `diff` command is powerful for comparing different branches, commits, or even parts of files.

Compare Current Working Directory to Last Commit:

```
git diff
```

Compare Two Branches:

```
git diff branch1..branch2
```

Compare Specific Files:

```
git diff branch1 branch2 -- path/to/file
```

**When to Use**: Use advanced `git diff` commands to analyze changes between branches or across commits, especially useful for code review and troubleshooting.

### Blame and Annotate for Code Ownership

**Git Blame** shows who last edited each line in a file, which is helpful for understanding the context and purpose behind changes.

* **Using Git Blame**

```
git blame path/to/file
```

* **GitHub's Blame Tool**: On GitHub, you can view blame information directly from the file view by selecting "Blame" to see commit history line-by-line.

![None](https://miro.medium.com/v2/resize:fit:700/1*KFjDv2C7CDzWXSazrb9ZKQ.png)

**When to Use**: Blame is helpful when investigating why certain code exists, who wrote it, and getting context on bugs or regressions.

### Git Hooks for Team-Wide Scripts

**Git Hooks** can be shared across a team to enforce standards and automate tasks like linting, testing, or verifying commit messages.

* **Setting Up Shared Hooks**:* Add custom hooks to a shared directory in the repository.* Configure each user's Git to look for hooks in this directory

```
git config core.hooksPath .githooks
```

**When to Use**: Shared hooks are useful for maintaining consistent practices (e.g., running tests before each commit or ensuring that commit messages follow a format) without relying on every team member to configure their own hooks.

### Reflog for Recovery

**Git Reflog** records every change, including those that aren't part of the current commit history. It's invaluable for recovering lost work.

**Commands**:

```
git reflog
```

**Scenario**:
John accidentally resets his branch, losing a day's work. Using `git reflog`, he finds the lost commit and restores it.

### Dependency Management with GitHub Dependabot

**Dependabot** helps manage and update dependencies by automatically creating pull requests when updates are available.

**Scenario**:
If a vulnerability is found in a dependency, Dependabot alerts the team and creates a PR to update it, reducing security risks.

### Managing Large Files with Git LFS

**Git LFS (Large File Storage)** helps manage large files by storing them outside the main Git repository, keeping the repo size manageable.

**Scenario**:
In a project with large images or video assets, the team uses Git LFS to prevent bloating the repo with large files, improving clone and pull performance. This would be useful for ML projects where the datasets used are big enough to be included in the repo.

### Part 5: Advanced GitHub Features for Team Collaboration

### GitHub Projects (Kanban Boards)

**GitHub Projects** provides a Kanban-style board to manage tasks, track progress, and organize work across the team.

1. **Set Up a Project Board**: Create columns (e.g., "To Do," "In Progress," "Done") and add tasks.- **Assign Tasks**: Add issues or pull requests to the board for easy tracking.

**Scenario**:
The team uses a GitHub Project board for sprint planning. Tasks are assigned to columns, and as work progresses, they're moved from "To Do" to "In Progress" and finally "Done."

![None](https://miro.medium.com/v2/resize:fit:700/1*MejbTyKoiq3FQqZqJoK8-w.png)

### GitHub Discussions for Team Communication

**GitHub Discussions** offers a forum-style space within a repository for team discussions, brainstorming, and Q&A.

1. **Start a Discussion**: Team members can ask questions, share ideas, or discuss upcoming features.- **Categories**: Organize discussions by type (e.g., "General," "Q&A," "Feature Requests").

**Scenario**:
John has an idea for a new feature and starts a discussion in GitHub Discussions to gather feedback from the team. The team can comment, vote, and decide whether to proceed with the feature.

### GitHub Pages for Documentation

**GitHub Pages** allows you to host project documentation as a static website, making it accessible to users or contributors.

1. **Create Documentation**: Add documentation files in a `/docs` folder or other specified directory.- **Enable GitHub Pages**: Go to **Settings > Pages**, select the branch and folder, and publish.

**Example Structure**:

```
.
├── docs
│   ├── index.md
│   └── api-guide.md
```

**Scenario**:
The team publishes API documentation on GitHub Pages, allowing external developers easy access to usage guides and examples.

### Part 5: Repository Structure for Different Project Types

### Monorepo vs. Multirepo

* **Monorepo**: A single repository that contains multiple related projects (e.g., frontend, backend, ML models).* **Multirepo**: Separate repositories for each project, providing more flexibility in access control and lifecycles.

### Recommended Structure for a Monorepo

**Root Directory**:

* **/frontend**: Contains frontend code (React, Angular, etc.).* **/backend**: Contains backend code (Node.js, Django, etc.).* **/ml-models**: Machine learning models and data preprocessing scripts.* **/docs**: Documentation files.* **/.github**: GitHub-specific files like workflows, issue templates, and PR templates.

**Example Directory Structure**:

```
.
├── frontend
│   ├── src
│   ├── public
│   └── package.json
├── backend
│   ├── src
│   └── requirements.txt
├── ml-models
│   ├── data
│   └── model-training.py
├── docs
│   └── README.md
└── .github
    └── workflows
        └── ci.yml
```

**Best Practice**:
Use monorepos when related components (e.g., frontend and backend) need to stay in sync. Use multirepos if components can operate independently or if they have distinct access needs.

**Note**: Please note that this is a very simple structure, based on teh technology stack you are using, this structure might be changing a bit. it is here to illustrate the idea of mono repo.

### Part 6: Best Practices for Team Collaboration in Git and GitHub

1. **Use Pull Requests for All Changes**: PRs provide a record of changes, enable discussion, and facilitate code review.- **Commit Often**: Small, frequent commits help track progress and make collaboration smoother.- **Follow Commit Message Conventions**: Use Conventional Commits for clear, structured commit messages that make history easier to follow.- **Use Descriptive Branch Names**: This helps teammates know the purpose of your branch at a glance.- **Rebase Before Merging**: Keep a clean history by rebasing feature branches before merging.- **Automate Testing with GitHub Actions**: Automate your CI pipeline to ensure every PR is tested and verified.- **Use Worktrees for Complex Workflows**: Worktrees allow you to handle multiple branches without switching contexts.- **Review Code Thoroughly**: Code reviews are essential for maintaining quality, catching errors, and sharing knowledge.- **Document Releases**: Use Git tags and GitHub Releases to provide versioned, downloadable snapshots of the project.

![None](https://miro.medium.com/v2/resize:fit:700/1*u54JDTgN7KkRwxWZeWVFBg.png)

### Cheat Sheet: Common Git and GitHub Commands

Here's a quick reference for frequently used Git and GitHub commands:

### Basic Git Commands

* **Clone a repo**: `git clone <repo-url>`* **Create a branch**: `git checkout -b branch-name`* **Switch branches**: `git checkout branch-name`* **View branches**: `git branch`* **Stage changes**: `git add .`* **Commit changes**: `git commit -m "message"`* **Push changes**: `git push origin branch-name`* **Pull latest changes**: `git pull origin branch-name`

### Branching and Merging

* **Create and switch to a new branch**: `git checkout -b branch-name`* **Merge a branch**: `git merge branch-name`* **Rebase a branch**: `git rebase branch-name`

### Stashing and Recovery

* **Stash changes**: `git stash`* **Apply stashed changes**: `git stash pop`* **View reflog**: `git reflog`

### Advanced Git Commands

* **Cherry-pick a commit**: `git cherry-pick <commit-hash>`* **Tag a commit**: `git tag -a v1.0.0 -m "release message"`* **Push a tag**: `git push origin v1.0.0`* **Create a worktree**: `git worktree add ../path branch-name`

### GitHub CLI

* **Create a PR**: `gh pr create --title "PR title" --body "PR description"`* **List issues**: `gh issue list`

### Conclusion

This comprehensive guide provides everything you need to manage team collaboration using Git and GitHub effectively. By using branching strategies, GitHub's project management tools, structured workflows, and advanced Git techniques, your team will benefit from streamlined development, better organization, and higher code quality.

Leverage GitHub Projects for task tracking, Discussions for team communication, and GitHub Pages for hosting documentation. Use the provided directory structure as a foundation for your projects, and refer to the cheat sheet for daily Git commands. With these tools and practices, your team is well-equipped to handle even the most complex projects efficiently.

### Additional Resources

* **GitHub Documentation**: <https://docs.github.com/>* **GitHub Getting Started**: <https://docs.github.com/en/get-started/getting-started-with-git/set-up-git>* **Semantic Versioning**: <https://semver.org/>* **Conventional Commits**: <https://www.conventionalcommits.org/>* **GitHub Support**: <https://support.github.com/>
