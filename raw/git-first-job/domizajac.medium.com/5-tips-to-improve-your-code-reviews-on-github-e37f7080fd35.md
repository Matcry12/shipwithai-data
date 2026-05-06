*Code review is one of the simplest but at the same time the most powerful mechanisms for programmers. Unfortunately, very often it is also the most underestimated one. In my previous work, I went with my teammates through a journey from zero to quite a good organized and well-working process. Was it worth our time and effort? Definitely, yes! Below you can find some thoughts and tips based on our experiences.*

#### Let's start from the beginning — what is Code Review?

If you are a programmer you probably heard that phrase before. But for tech newbies let's start with a short definition. Code Review (CR in short) is a practice when the second engineer audits your changes before merging them to the main codebase. That super easy behavior improves code quality and accelerates knowledge sharing among the team. Moreover, it helps to avoid mistakes (especially complex ones like architecture problems). All the most popular version controlling platforms like GitHub or GitLab prepared special tools to support CR in their environments. And the majority of companies and teams have special standards defining how the CR should look like and how many approvals you need before merging the code to the main branch. Below you can find 5 tips that in my opinion are super useful when defining your standards.

#### 1. Protected branches

First of all — protect your main branch against unexpected changes. It doesn't matter if someone will call `git push` locally on a wrong branch or someone from another team who doesn't know your standards is trying to add something to your codebase. **Pushing something directly to the main branch should not be possible**. Fortunately, GitHub is offering a great mechanism for that called **protected branches**. You can create special rules for a branch or set of branches (e.g. based on name pattern) defining that e.g. pull request and approval from at least one reviewer are required to merge your code to the main branch.

![Screenshot of branch protection rule section in github. There is an input field for branch name or name pattern and checklist of rules for given branches.](https://miro.medium.com/v2/resize:fit:700/1*4i9ak4BA1qxHM_zamRA4HQ.png)

Screenshot of the section responsible for defining branch protection rules.

How to configure that?

1. Go to `github.com` and navigate to your repository- Click `Settings` tab- In the left-side menu click `Branches` option- Click `Add branch protection rule` button- Put branch name or regex for name patter in `Branch name pattern input`- Choose one of the items available in the checklist below- Save your changes

#### 2. Labels

It's a super small but extremely useful feature for me. Especially in big, open-source repositories. Labels are nothing else but additional, easy-to-see and filter pieces of information visible on pull request lists. You can use them to e.g. differentiate internal and external changes. MRs connected with particular features of your app, type of changes, or size. Using labels makes managing merge requests much easier for me! How to create a label?

![Form to create a new label containing fields “name”, “description” and “color” and buttons “cancel” and “save”](https://miro.medium.com/v2/resize:fit:700/1*EOCnRgIXLFsAthocDOFnmg.png)

Creating a new label is really easy!

1. Go to github.com and navigate to your repository- Go to the `Pull request` section- Click `Labels` close to the filtering input- Click the green `New label` button- Fulfill all fields in the form and click `Create labels` button

Now you can assign this label to any of your new or existing merge requests in the pull request creation form or menu in the pull requests section.

#### 3. Automated Checks

Not everything can be tested automatically. But many things like syntax or running tests can be. Don't waste your and your colleagues' time checking things that can be tested by the computer. You can use Jenkins/Github Actions/CircleCI or any other tool of your choice to start automated tests on each merge request creation. Add a rule to disable merge until all required checks pass. It may save your production someday! Small tip: add also a way to easily re-trigger those tests manually — e.g. sending a special message in a comment on GitHub. It's very useful in debugging problems.

![Plush Android sitting in front of 2 computers — one of them is completely covered in stickers, the second one has no sticker on it.](https://miro.medium.com/v2/resize:fit:700/1*eknEDlH4ORGfzqpzA9BUVg.jpeg)

One of the biggest benefits of using a code review mechanism is that everyone has a different view, background, and priorities. E.g. one person loves may love stickers on the laptop and the second hates them. But our software should work for everyone! So the second person can see things you accidentally missed in your code.

#### 4. Template Pull Request message with a checklist

Each merge request should have a good, short, and self-explaining title and some description. In big teams, it's also useful to add additional information like links to tasks/issues from your task-tracking system like Jira or Trello. Some things cannot be tested manually — like accessibility (if you don't know yet why accessibility is so important check my article [here](https://domizajac.medium.com/how-to-make-the-internet-available-for-everyone-accessibility-in-the-web-development-73d7e73deec4)) or fulfilling business requirements. Unfortunately, when your team and projects are growing it's more and more difficult to remember all of those things to put in the merge request message as an author and things to check as a reviewer. You can easily address those problems using templates for merge requests. Thanks to that you'll see a predefined draft of a message with a checklist of things to manually check when you create a merge request and it's enough to fulfill the form with needed information and mark all items in the checklist as done.

![Screenshot of merge request template from Github — there is a place to put JIRA link of the issue and checklist of things to manually check during review like accessibility check or sending strings to translations.](https://miro.medium.com/v2/resize:fit:700/1*BUnEsqIsGmj6o7VSPpac3g.png)

Example of merge request template (yes, the screenshot was taken before IE depreciation).

How to do so?

1. Open your repository in your favorite code editor- Add file pull\_request\_template.md in the root of your repository or the docs folder placed in the root.- Put your template inside of the file (You can use markdown syntax there to create headings, checklists, etc).- Merge the change to the main branch.

Note: If you want to have more than 1 template of the message create the `PULL_REQUEST_TEMPLATE` directory (also in the root or in the docs folder) and keep your markdown files there. In this setup, a user can choose one of the templates using the dropdown menu during creating the MR.

#### 5. Always be open-minded and empathic

My last tip is not technical but extremely important (inspired by the tweet above presenting 4 people beating the 5th people with the description "4 of 5 developers enjoy code review"). When you do a code review always keep an open mind and be emphatic. Code review is not about roasting someone of their skills. It's not a place to show your superiority or greater experience. It's a mechanism to let us all grow, learn and keep high quality. So, don't only criticize. If someone is doing a great job — let them know about it! If someone is solving something differently than you, try to understand their approach before pushing them to code your way. If someone made a mistake — let them know but in a supportive, not hating way. Each of us has learned once, and we all make mistakes sometimes. Write only the messages you would like to get — to help you develop your skills but not to be depressing. **Despite stereotypes empathy is a crucial skill in software engineering** — don't forget that! All in all, programming is a team sport nowadays.
> Despite stereotypes empathy is a crucial skill in software engineering

#### Summary

The tips described below do not exhaust all possibilities of improving your code review but are in my opinion a good start to creating a good code review process and defining some standards. I hope, you found this article useful. If so, clap the button below or share it with your friends. Thanks in advance and happy coding!
