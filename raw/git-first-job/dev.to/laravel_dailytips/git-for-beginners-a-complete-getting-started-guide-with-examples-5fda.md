---
source_url: https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda
crawl_depth: 0
crawled_at: 2026-05-05T14:26:40Z
word_count: 1020
---

Whether you're a student, a new developer, or just curious about coding, **Git** is something you’ll hear about often. This guide is written for **absolute beginners**. We’ll walk you through the **basics of Git** , how to install it, set it up, and use it with simple commands and real examples.
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#1-what-is-git-and-why-use-it) 1. What is Git and Why Use It? 
**Git** is a version control system (VCS). It helps developers keep track of changes in their code. If something goes wrong, Git allows you to go back to a previous version.
**Why use Git?**
  * Track every change in your project
  * Work with teams easily
  * Prevent accidental data loss
  * Collaborate using platforms like GitHub


###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#2-version-control-basics) 2. Version Control Basics 
There are two main types of version control:
  * **Local VCS** : Tracks changes on your computer only
  * **Distributed VCS (like Git)** : Every developer has a full copy of the project history


With Git, every change is recorded. You can see what was changed, when, and by whom.
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#3-installing-git-on-windows-macos-and-linux) 3. Installing Git on Windows, macOS, and Linux 
**Windows** :
  1. Download Git from <https://git-scm.com/download/win>
  2. Run the installer and follow the default steps


**macOS** :  


```
brew install git

```

Enter fullscreen mode Exit fullscreen mode
(You need to have Homebrew installed)
**Linux (Ubuntu/Debian)** :  


```
sudo apt update
sudo apt install git

```

Enter fullscreen mode Exit fullscreen mode
After installation, check if Git is working:  


```
git --version

```

Enter fullscreen mode Exit fullscreen mode
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#4-setting-up-git-username-email) 4. Setting Up Git (username, email) 
Before using Git, set your name and email:  


```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

```

Enter fullscreen mode Exit fullscreen mode
You can verify:  


```
git config --list

```

Enter fullscreen mode Exit fullscreen mode
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#5-creating-a-repository-git-init) 5. Creating a Repository (git init) 
A **repository** is like a folder that Git tracks.  


```
mkdir my-project
cd my-project
git init

```

Enter fullscreen mode Exit fullscreen mode
You now have a Git repository in the `my-project` folder.
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#6-cloning-a-repository-git-clone) 6. Cloning a Repository (git clone) 
Cloning means downloading a remote Git project to your computer.  


```
git clone https://github.com/username/repo-name.git

```

Enter fullscreen mode Exit fullscreen mode
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#7-git-file-lifecycle-untracked-%E2%86%92-staged-%E2%86%92-committed) 7. Git File Lifecycle: Untracked → Staged → Committed 
Git tracks file changes in 3 steps:
  * **Untracked** : New files Git doesn’t know about yet
  * **Staged** : Files marked to be saved
  * **Committed** : Files are saved in Git history


**Example flow:**  


```
touch index.html                     # untracked
git add index.html                   # staged
git commit -m "Add index file"       # committed

```

Enter fullscreen mode Exit fullscreen mode
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#8-staging-changes-git-add) 8. Staging Changes (git add) 
Use `git add` to tell Git which files you want to track.  


```
git add file1.html

# To Add all files.
git add .

```

Enter fullscreen mode Exit fullscreen mode
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#9-committing-changes-git-commit) 9. Committing Changes (git commit) 
Once staged, commit your changes with a message:  


```
git commit -m "Added homepage layout"

```

Enter fullscreen mode Exit fullscreen mode
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#10-checking-status-and-history-git-status-git-log) 10. Checking Status and History (git status, git log) 
To check current changes:  


```
git status

# To see commit history:

git log

```

Enter fullscreen mode Exit fullscreen mode
You’ll see details like author, date, and message.
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#11-basic-file-operations-git-rm-git-mv) 11. Basic File Operations (git rm, git mv) 
To delete a file from Git and your folder:  


```
git rm unwanted.txt
git commit -m "Remove unwanted file"

```

Enter fullscreen mode Exit fullscreen mode
To rename or move a file:  


```
git mv oldname.txt newname.txt
git commit -m "Renamed file"

```

Enter fullscreen mode Exit fullscreen mode
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#12-creating-your-first-gitignore-file) 12. Creating Your First .gitignore File 
The `.gitignore` file tells Git which files or folders to skip.
Example `.gitignore`:  


```
node_modules/
.env
*.log

```

Enter fullscreen mode Exit fullscreen mode
Create the file in your root directory:  


```
touch .gitignore

```

Enter fullscreen mode Exit fullscreen mode
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#13-using-git-with-github-basics) 13. 🌐 Using Git with GitHub (Basics) 
GitHub is a website that stores Git repositories online. Here’s how to push your local code to GitHub:
**Step 1** : Create a new repository on [GitHub](https://github.com)
**Step 2** : Connect local project with GitHub:  


```
git remote add origin https://github.com/yourusername/my-project.git
git branch -M main
git push -u origin main

```

Enter fullscreen mode Exit fullscreen mode
##  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#conclusion) Conclusion 
Now you know the basics of Git, how it works, and how to use it daily. You’ve learned how to:
  * Set up Git on any system
  * Create and clone repositories
  * Track changes using `git add` and `git commit`
  * Work with GitHub


This is just the beginning. In the next blog, we’ll go deeper into **branches, merging, and resolving conflicts**.
##  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#want-more-laravel-tips) **Want more Laravel tips?**
Visit [LaravelDailyTips](https://laraveldailytips.com/) for practical guides, interview questions, and tricks.
Subscribe now and get battle-tested Laravel insights delivered to your inbox before anyone else!
[ ![profile](https://media2.dev.to/dynamic/image/width=64,height=64,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F1%2Fd908a186-5651-4a5a-9f76-15200bc6801f.jpg) The DEV Team ](https://dev.to/devteam) Promoted
Dropdown menu
* * *


[![Google article image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FtbKnECG.png)](https://dev.to/googleai/build-a-talking-robot-with-gemini-live-and-reachy-mini-20e2?bb=263066)
##  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#build-a-talking-robot-with-gemini-live-and-reachy-mini) [Build a Talking Robot with Gemini Live and Reachy Mini](https://dev.to/googleai/build-a-talking-robot-with-gemini-live-and-reachy-mini-20e2?bb=263066)
In this tutorial you'll learn:
  * How the architecture works — from microphone to motor.
  * How to set it up on your own machine.
  * How to give the robot a custom personality without touching a single line of Python.Let's dive in.


Read More 
For further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)
[ ![profile](https://media2.dev.to/dynamic/image/width=64,height=64,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F6839%2F3d85988f-d18e-4522-b261-f86613cd9b50.png) Sonar ](https://dev.to/sonar) Promoted
Dropdown menu
* * *


[![State of Code Developer Survey report](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fucarecdn.com%2F2f2ce9b0-68e0-48a1-bf3e-46c08831a9be%2F)](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259978)
##  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#state-of-code-developer-survey-report) [State of Code Developer Survey report](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259978)
Did you know 96% of developers don't fully trust that AI-generated code is functionally correct, yet only 48% always check it before committing? Check out Sonar's new report on the real-world impact of AI on development teams.
[Read the results](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259978)
👋 Kindness is contagious
Dropdown menu
* * *


**Sign in** to DEV to enjoy its full potential.
Unlock a **customized** interface with dark mode, personal reading preferences, and more.
###  [ ](https://dev.to/laravel_dailytips/git-for-beginners-a-complete-getting-started-guide-with-examples-5fda#-cta-httpsdevtoenterstatenewuser-) [Okay](https://dev.to/enter?state=new-user&bb=239375)
