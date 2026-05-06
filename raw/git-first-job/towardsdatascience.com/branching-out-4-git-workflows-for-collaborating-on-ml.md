---
source_url: https://towardsdatascience.com/branching-out-4-git-workflows-for-collaborating-on-ml/
title: "Branching Out: 4 Git Workflows for Collaborating on ML"
crawl_depth: 0
crawled_at: 2026-05-05T14:26:31Z
word_count: 2762
---

Customise Consent Preferences ![](https://cdn-cookieyes.com/assets/images/close.svg)
The cookies that are categorised as "Necessary" are stored on your browser as they are essential for enabling the basic functionalities of the site. ... Show more
NecessaryAlways Active
Necessary cookies are required to enable the basic features of this site, such as providing secure log-in or adjusting your consent preferences. These cookies do not store any personally identifiable data.
Functional
Functional cookies help perform certain functionalities like sharing the content of the website on social media platforms, collecting feedback, and other third-party features.
Analytics
Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics such as the number of visitors, bounce rate, traffic source, etc.
Performance
Performance cookies are used to understand and analyse the key performance indexes of the website which helps in delivering a better user experience for the visitors.
Advertisement
Advertisement cookies are used to provide visitors with customised advertisements based on the pages you visited previously and to analyse the effectiveness of the ad campaigns.
Uncategorised
Other uncategorised cookies are those that are being analysed and have not been classified into a category as yet.
Reject All Save My Preferences Accept All
# Branching Out: 4 Git Workflows for Collaborating on ML
My unversioned code left me swimming through a sea of scripts. Then I found Git. 
Feb 12, 2025
11 min read
![](https://towardsdatascience.com/wp-content/uploads/2025/02/1_lhl78yndn7W2EH1TI0DvrQ.png)Swimming in a deep ocean of untracked scripts (image by the author with ideogram.ai) 
It’s been more than 15 years since I finished my master’s degree, but I’m still haunted by the hair-pulling frustration of managing my of  _R_ scripts. As a (recovering) perfectionist, I named each script very systematically by date (think: `ancova_DDMMYYYY.r`). A system I just *knew* was better than `_v1`, `_v2`, `_final` and its frenemies. Right?
Trouble was, every time I wanted to tweak my model inputs or review a previous model version, I had to swim through a sea of scripts.
Fast forward a few years, a few programming languages, and a career slalom later, I can clearly see how my solo struggles with code versioning were a lucky wake-up call.
While I managed to navigate those early challenges (with a few cringey moments!), I now recognise that most development, especially with Agile ways of working, thrives on robust version control systems. The ability to track changes, revert to previous versions, and ensure reproducibility within a collaborative codebase can’t be an afterthought. It’s actually a necessity.
When we use version control workflows, often in Git, we lay the groundwork for developing and deploying more reliable and higher quality data and AI solutions.
## **Before we begin**
If you already use version control and you’re thinking about different workflows for your team, welcome! You’ve come to the right place.
If you’re new to Git or have only used it on solo projects, I recommend reviewing some introductory Git principles. You’ll want more background before jumping into team workflows. GitHub provides links to several Git and GitHub tutorials [here](https://docs.github.com/en/get-started/start-your-journey/git-and-github-learning-resources). And [this](https://towardsdatascience.com/a-simple-git-workflow-for-github-beginners-and-everyone-else-87e39b50ee08) getting started post introduces basics like how to create a repo and add a file.
## **Development teams work in different ways**
### But a ubiquitous feature is reliance on version control.
Git is incredibly flexible as a version control system, and it allows developers a lot of freedom in how they manage their code. If you’re not careful, though, flexibility leaves room for chaos if not managed effectively. Establishing Git workflows can guide your team’s development so you’re using Git more consistently and efficiently. Think of it as the team’s shared roadmap for navigating Git’s highways and byways.
By defining when we create branches, how we merge changes, and why we review code, we create a common understanding and foster more reliable ways of developing as a team. Which means that every team has the opportunity to create their own Git workflows that work for their specific organisational structure, use-cases, tech stack, and requirements. It’s possible to have as many ways of using Git as a team as there are development teams. Ultimate flexibility.
You may find that idea liberating. You and your team have the freedom to design a Git workflow that works for you!
But if that sounds intimidating, not to worry. There are several established protocols to use as a starting point for agreeing on team workflows.
## **Make Git your friend**
Version control is useful in so many ways, but the benefits I see over and over on my teams cluster into a few essential categories. We’re here to focus on workflows so I won’t go into great depth, but the central premise and advantages of Git and GitHub are worth highlighting.
**(Almost) anything is reversible.** Which means that version control systems free you up to get creative and make mistakes. Rolling back any regrettable code changes is as simple as `git revert`. Like a good neighbour, Git commands are there.
**Simplifies code collaboration.** Once you get into the flow of using it, Git really facilitates seamless collaboration across the team. Work can happen concurrently without interfering with anyone else’s code, and code changes are all documented in commit snapshots. This means anyone on the team can take a peek at what the others have been working on and how they went about it, because the changes are captured in the Git history. Collaboration made easy.
**Isolating exploratory work in feature branches.** How will you know which model gives the best performance for your specific business problem? In a recent revenues use case, it could’ve been time series models, maybe tree-based methods, or convolutional neural networks. Possibly even Bayesian approaches. Without the parallel branching ability Git provided my team, trialling the different methods would’ve resulted in a codebase of pure chaos.
**In-built review process (massively improves code quality).** By putting code through peer review using GitHub’s pull request system, I’ve seen team after team grow in their abilities to leverage their collective knowledge to write cleaner, faster, more modular code. As code review helps team members identify and address bugs, design flaws, and maintainability, it ultimately leads to higher quality code.
**Reproducibility.** As in, every change made to the codebase is recorded in the Git history. Which makes it incredibly easy to track changes, revert to previous versions, and reproduce past experiments. I can’t understate its importance for debugging, code maintenance, and ensuring the reliability of any experimental findings.
## **Different flavours of workflows for different types of work**
### **Feature-branching workflow: The Standard Bearer**
This is the most common Git workflow used in dev teams. It’d be difficult to unseat it in terms of its popularity, and for good reason. In a feature branching workflow, each new functionality or improvement to the code is developed in its own dedicated branch, separate from the main codebase.
A branching workflow provides each developer with an isolated workspace (a branch) — their own complete copy of the project. This lets every person on the team do focused work, independent of what’s happening elsewhere in the project. They can make code changes and forget about upstream development, working independently until they’re ready to share their code.
At that point, they can take advantage of GitHub’s pull request (PR) functionality to facilitate code review and collaborate with the team to ensure the changes are evaluated and approved before being merged into the codebase.
This approach is especially beneficial to Agile development teams and teams working on complex projects that call for frequent code changes.
A feature branching workflow might look like this:

```
# In your terminal:

$ git switch <new_branch_name> # Creates and switches onto a new branch
$ git push -u origin <new_branch_name> # For first push only. Creates new working branch on the remote repository

# Create and activate your virtual environment. Pip install any required packages.

$ python3 -m venv <new_venv_name>
$ source new_venv_name/bin/activate
$ pip install requirements.txt (or <packages>)

# Make changes to your code in feature branch
# Regularly stage and commit your code changes, and push to remote. For example:

$ git add <file> # Stages the file to prepare repo snapshot for commit
$ git commit -m "<Your descriptive message>" # Records file snapshots into your version history
$ git push # Sends local commits to the remote repository; to your working branch

# Raise Pull Request (PR) on repo's webpage. Request reviewer(s) in PR.
# After PR is approved and merged to `main`, delete working branch.
```

### **Centralised workflow: Git Primer**
This approach is what I think of as an introductory workflow. What I mean is that the `main` trunk is the only point where changes enter the repository. A single `main` branch is used for all development and all changes are committed to this branch, ignoring the existence of branching (we ignore software features all the time, right?).
This isn’t an approach you’ll find being used by high-velocity dev teams or continuous delivery teams. So you might be wondering — is there ever good reason for a centralised Git workflow?
Two use-cases come to mind.
First, centralised Git workflows can streamline the initial explorations of a very small team. When the focus is on rapid prototyping and the risk of conflicts is minimal — as in a project’s early days — a centralised workflow can be convenient.
And second, using a centralised Git workflow can be a good way to migrate a team onto version control because it doesn’t require any branches other than `main`. Just use with caution as things can quickly go pear shaped. As the codebase grows or as more people contribute there’s an greater risk of code conflicts and accidental overwrites.
Otherwise, centralised Git workflows are generally not recommended for sustained development, especially in a team setting.
A centralised workflow might look like this:

```
# In your terminal:

$ git checkout <main> # Switches onto `main` branch

# Create and activate your virtual environment. Pip install any required packages.

$ python3 -m venv <new_venv_name>
$ source new_venv_name/bin/activate
$ pip install requirements.txt (or <packages>)

# Make changes to code
# Regularly stage and commit your code changes, and push to remote. For example:

$ git add <file> # Stages the file to prepare repo snapshot for commit
$ git commit -m "<Your descriptive message>" # Records file snapshots into your version history
$ git push # Sends local commits to the remote repository; to whichever branch you're working on. In this case, the `main` branch
```

## **ML workflows: Branching Experiments**
Data scientists and MLOps teams have a somewhat unique use-case compared to traditional software development teams. The development of machine learning and AI projects is inherently experimental. So from a Git workflow perspective, protocols need to flex to accommodate frequent iteration and complex branching strategies. You may also need the ability to track more than code, like experiment results, data, or model artifacts.
Feature branching augmented with experiment branches is probably the most popular approach.
This approach starts with the familiar feature branching workflow. Then within a feature branch, you create sub-branches for specific experiments. Think: “experiment_hyperparam_tuning”, or “experiment_xgboost”. This workflow affords enough granularity and flexibility to track individual experiments. And as with standard feature branches, this isolates development allowing experimental approaches to be explored without affecting the main codebase or other developers’ work.
But  _caveat emptor_ : I said it was popular, but that doesn’t mean the branching experiments workflow is simple to manage. It can all turn to a tangled mess of spaghetti-branches if things are allowed to grow overly complex. This workflow involves frequent branching and merging, which can feel like unnecessary overhead in the face of rapid experimentation.
A branching experiments workflow might look like this:

```
# In your terminal:

$ git checkout <feature_branch> # Move onto a feature branch ready for ML experiments
$ git switch <experiment_branch> # Creates and switches onto a new branch for experiments

# Create and activate your virtual environment. Pip install any required packages.
# Make changes to your code in feature branch.
# Continue as in Feature Branching workflow.
```

## **Reproducible ML workflow**
Integrating tools like [MLflow](https://mlflow.org/docs/latest/getting-started/index.html) into a feature branching workflow or branching experiments workflow offers additional possibilities. Reproducibility is a key concern for ML projects, which is why tools like MLflow exist. To help manage the full machine learning lifecycle.
For our workflows, MLflow enhances our capabilities by enabling experiment tracking, logging model runs in the registry, and comparing the performance of various model specifications.
For a branching experiments workflow, the MLflow integration might look like this:

```
# In your terminal:

$ git checkout <feature_branch> # Move onto a feature branch ready for ML experiments
$ git switch <experiment_branch> # Creates and switches onto a new branch for experiments

# Create and activate your virtual environment. Pip install any required packages.
# Initialise MLflow within your Python script.
# Make changes to branch. As you experiment with different hyperparameters or model architectures, create new experiment branches and log the results with MLflow.
# Regularly stage and commit your code changes and MLflow experiment logs. For example:

$ git add <file> <file> <file> # Stages the file to prepare repo snapshot for commit
$ git commit -m "<Your descriptive message>" # Records file snapshots into your version history
$ git push # Sends local commits to the remote repository; to your working branch

# Use the MLflow UI or API to compare the performance of different experiments within your feature branch. You may want to select the best-performing model based on the logged metrics.
# Merge experimental branch(es) into the parent feature branch. For example:

$ git checkout <feature_branch> # Switch back onto the parent feature branch
$ git merge <experiment_branch> # Merge experiment branch into the parent feature branch

# Raise Pull Request (PR) to merge it into `main` once the feature branch work is completed. Request reviewers. Delete merged branches.
# Deploy if applicable. If the model is ready for deployment, use the logged model artifact from MLflow to deploy it to a production environment.
```

# **Takeaways**
The Git workflows I’ve shared above should provide a good starting point for your team to streamline collaborative development and help them to build high-quality data and AI solutions. They’re not rigid templates, but rather adaptable frameworks. Try experimenting with different workflows. Then adjust them to craft the an approach that’s most effective for your needs.
  * **Git Workflows Simplify:** The alternative is too frightening, too messy, too slow to be sustainable. It’s holding you back.
  * **Your Team Matters:** The ideal workflow will vary depending on your team’s size, structure, and project complexity.
  * **Project Requirements:** The specific needs of the project, such as the frequency of releases and the level of ML experimentation, will also influence your choice of workflow.


Ultimately, the best Git workflow for any data or MLOps dev team is the one that suits the specific requirements and development process of that team.
* * *
Written By
Julie Ripplinger
[Collaboration](https://towardsdatascience.com/tag/collaboration/), [Git](https://towardsdatascience.com/tag/git/), [ML Engineering](https://towardsdatascience.com/tag/ml-engineering/), [Mlops](https://towardsdatascience.com/tag/mlops/), [Programming](https://towardsdatascience.com/tag/programming/)
Share This Article
Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.
## Related Articles
  * ![Photo by Evie S. on Unsplash](https://towardsdatascience.com/wp-content/uploads/2023/12/014GNfNJ1eNRiXaZ8-scaled.jpg)
## [Understanding Predictive Maintenance - Wave Data: Feature Engineering (Part 2 Spectral)](https://towardsdatascience.com/understanding-predictive-maintenance-wave-data-feature-engineering-part-2-spectral-3eced3bdbb3e/)
Feature Engineering of spectral data 
December 1, 2023
13 min read
  * ![Photo by June Wong on Unsplash](https://towardsdatascience.com/wp-content/uploads/2021/03/0Rfhdl5B9e7FStJ4J-scaled.jpg)
## [Gauss, Imposters, and Making Room for Creativity](https://towardsdatascience.com/gauss-imposters-and-making-room-for-creativity-ad01daabacae/)
Our weekly selection of must-read Editors’ Picks and original features 
March 18, 2021
4 min read
  * ## [Foundational RL: Dynamic Programming](https://towardsdatascience.com/foundational-rl-dynamic-programming-28f96f6fb40e/)
Road to Reinforcement Learning 
December 19, 2022
5 min read
  * ![Photo by Isabella and Zsa Fischer on Unsplash](https://towardsdatascience.com/wp-content/uploads/2022/09/0l_zkiC2s8kWQdSj0-scaled.jpg)
## [5 Passive Income-Generating Products You Can Develop in Your Spare Time as a Data Analyst](https://towardsdatascience.com/5-passive-income-generating-products-you-can-develop-in-your-spare-time-as-a-data-analyst-c3639800dcbd/)
Finding your niche in these products will help you generate extra income on the side. 
September 15, 2022
8 min read
  * ![Photo by Yannis Papanastasopoulos on Unsplash](https://towardsdatascience.com/wp-content/uploads/2021/09/0yhu45_ZQ3MIRUAgn-scaled.jpg)
## [How Data Can Make a Difference in the Real World](https://towardsdatascience.com/how-data-can-make-a-difference-in-the-real-world-dda77eda5de7/)
Our weekly selection of must-read Editors’ Picks and original features 
September 23, 2021
4 min read
  * ![Photo by Camille Vandoorsselaere on Unsplash](https://towardsdatascience.com/wp-content/uploads/2021/03/0LMzRG6hlpIq8zLAX-scaled.jpg)
## [Careers in Machine Learning, Python Music, and AI’s Brain Connection](https://towardsdatascience.com/careers-in-machine-learning-python-music-and-ais-brain-connection-a40a3fd7fab1/)
Our weekly selection of must-read Editors’ Picks and original features 
March 25, 2021
3 min read
  * ![Photo by Nathan Anderson @unsplash.com](https://towardsdatascience.com/wp-content/uploads/2023/06/00EQ1vH_CYS43q0Uh.jpg)
## [Unsupervised Learning Series - Exploring Hierarchical Clustering](https://towardsdatascience.com/unsupervised-learning-series-exploring-hierarchical-clustering-15d992467aa8/)
Let’s explore how hierarchical clustering works and how it builds clusters based on pairwise distances. 
June 20, 2023
12 min read
