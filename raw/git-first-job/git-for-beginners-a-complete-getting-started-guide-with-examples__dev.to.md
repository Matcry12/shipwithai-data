---
source_url: "https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda"
source_domain: "dev.to"
topic: "git-first-job"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-25T06:38:03.570337+00:00"
word_count: 699
stage: "raw-extracted"
---

Whether you're a student, a new developer, or just curious about coding, **Git** is something you’ll hear about often. This guide is written for **absolute beginners**. We’ll walk you through the **basics of Git**, how to install it, set it up, and use it with simple commands and real examples.

### 1. What is Git and Why Use It?

**Git** is a version control system (VCS). It helps developers keep track of changes in their code. If something goes wrong, Git allows you to go back to a previous version.

**Why use Git?**

- Track every change in your project
- Work with teams easily
- Prevent accidental data loss
- Collaborate using platforms like GitHub

### 2. Version Control Basics

There are two main types of version control:

-
**Local VCS**: Tracks changes on your computer only -
**Distributed VCS (like Git)**: Every developer has a full copy of the project history

With Git, every change is recorded. You can see what was changed, when, and by whom.

### 3. Installing Git on Windows, macOS, and Linux

**Windows**:

- Download Git from https://git-scm.com/download/win
- Run the installer and follow the default steps

**macOS**:


```
brew install git
```


(You need to have Homebrew installed)

**Linux (Ubuntu/Debian)**:


```
sudo apt update
sudo apt install git
```


After installation, check if Git is working:


```
git --version
```


### 4. Setting Up Git (username, email)

Before using Git, set your name and email:


```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```


You can verify:


```
git config --list
```


### 5. Creating a Repository (git init)

A **repository** is like a folder that Git tracks.


```
mkdir my-project
cd my-project
git init
```


You now have a Git repository in the `my-project`

folder.

### 6. Cloning a Repository (git clone)

Cloning means downloading a remote Git project to your computer.


```
git clone https://github.com/username/repo-name.git
```


### 7. Git File Lifecycle: Untracked → Staged → Committed

Git tracks file changes in 3 steps:

-
**Untracked**: New files Git doesn’t know about yet -
**Staged**: Files marked to be saved -
**Committed**: Files are saved in Git history

**Example flow:**


```
touch index.html # untracked
git add index.html # staged
git commit -m "Add index file" # committed
```


### 8. Staging Changes (git add)

Use `git add`

to tell Git which files you want to track.


```
git add file1.html
# To Add all files.
git add .
```


### 9. Committing Changes (git commit)

Once staged, commit your changes with a message:


```
git commit -m "Added homepage layout"
```


### 10. Checking Status and History (git status, git log)

To check current changes:


```
git status
# To see commit history:
git log
```


You’ll see details like author, date, and message.

### 11. Basic File Operations (git rm, git mv)

To delete a file from Git and your folder:


```
git rm unwanted.txt
git commit -m "Remove unwanted file"
```


To rename or move a file:


```
git mv oldname.txt newname.txt
git commit -m "Renamed file"
```


### 12. Creating Your First .gitignore File

The `.gitignore`

file tells Git which files or folders to skip.

Example `.gitignore`

:


```
node_modules/
.env
*.log
```


Create the file in your root directory:


```
touch .gitignore
```


### 13. 🌐 Using Git with GitHub (Basics)

GitHub is a website that stores Git repositories online. Here’s how to push your local code to GitHub:

**Step 1**: Create a new repository on GitHub

**Step 2**: Connect local project with GitHub:


```
git remote add origin https://github.com/yourusername/my-project.git
git branch -M main
git push -u origin main
```


## Conclusion

Now you know the basics of Git, how it works, and how to use it daily. You’ve learned how to:

- Set up Git on any system
- Create and clone repositories
- Track changes using
`git add`

and`git commit`

- Work with GitHub

This is just the beginning. In the next blog, we’ll go deeper into **branches, merging, and resolving conflicts**.

##
**Want more Laravel tips?**

Visit LaravelDailyTips for practical guides, interview questions, and tricks.

Subscribe now and get battle-tested Laravel insights delivered to your inbox before anyone else!