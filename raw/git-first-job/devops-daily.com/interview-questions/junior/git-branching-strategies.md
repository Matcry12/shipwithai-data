---
source_url: https://devops-daily.com/interview-questions/junior/git-branching-strategies
title: "Git Branching Strategies"
crawl_depth: 0
crawled_at: 2026-05-05T14:26:31Z
word_count: 188
---

# Git Branching Strategies
What are common Git branching strategies? Describe GitFlow or trunk-based development.
junior
beginner
Git
Question
What are common Git branching strategies? Describe GitFlow or trunk-based development.
Answer
Common strategies include GitFlow (feature branches, develop, release, and main branches with structured releases), GitHub Flow (simple feature branches merged to main with continuous deployment), and trunk-based development (short-lived branches or direct commits to main with feature flags). Trunk-based development is preferred for CI/CD as it reduces merge conflicts and enables faster delivery.
Branching strategies directly impact deployment frequency and team collaboration. DevOps engineers help teams choose and implement strategies that support their CI/CD goals. Understanding trade-offs helps optimize the development workflow.
Code Examples
Common branch operations

```

```

  * Long-lived feature branches causing merge conflicts
  * Not keeping branches up-to-date with main
  * Using complex branching when simple approaches would work


Interviewers often ask these as follow-up questions
  * What are the pros and cons of GitFlow vs trunk-based development?
  * How do feature flags enable trunk-based development?
  * When would you use a release branch?


git
branching
gitflow
trunk-based
cicd
## More Git interview questions
