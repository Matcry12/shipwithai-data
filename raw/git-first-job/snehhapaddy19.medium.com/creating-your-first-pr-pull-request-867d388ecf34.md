I hope you enjoyed the previous 2 parts. Now let us get working. As a prerequisite, you need to have Git installed in your system. It is also preferable to have a good code editor, such as VSCode in your system(this is my favorite one). And yeah, you should also have a GitHub account. So I have created a repository, for you to practice (<https://github.com/SnehhaPadmanabhan/Github_Beginner_Helper>). There are 3 places that we are keeping track of: the main repo(whose link is provided above), the copy forked in your GitHub account and the copy in your local machine. Awesome, so let us get started.

![None](https://miro.medium.com/v2/resize:fit:700/1*yuHFfviLv50w-y4NqTPYMw.png)

Source: Google

#### Step 0

If this is your first experience with open source, you can follow this step. Head over to the Git command line and execute the following lines(by doing this, you are hooking your local machine to your GitHub account. So any changes you make here in your local machine will be inflicted in your GitHub). PS: It is a double hiphen.

*git config — global user.name "YOUR NAME"*

*git config — global user.email "YOUR EMAIL ID"*

If you want to attach the local machine to a single repo instead of all repos, then omit the "global" keyword.

#### Step 1: Fork

Fork my repo(using the fork button that can be seen in the top right corner). This will create a copy of the entire repo in your account.

![None](https://miro.medium.com/v2/resize:fit:700/1*44KJHq1VbcsEPOMnGde77w.png)

Source: Snip of my personal machine

#### Step 2: Clone

Now you can modify the code in your local machine. For that, you have to download the code in your system. So open VSCode and head to the terminal tab, or go to the Git CLI to download the code into your local system, and type the following line. (For this, you need the link to the code that is needed to be downloaded. You can obtain that by clicking on the green "Code" button either in the original or in the forked repository. This will be our <link>.)

![None](https://miro.medium.com/v2/resize:fit:700/1*Euo2CXffxM145w_eUCyhfQ.png)

Source: Snip of my personal machine

*git clone <link>*

And that should be something like:

*git clone* *<https://github.com/SnehhaPadmanabhan/Github_Beginner_Helper>*

#### Step 3: Make changes

Now start making changes to the code in your local machine.

***IMPORTANT NOTE: I will only be accepting PRs that contain quality code(examples will be adding codes for competitive programming problems, or adding your own projects). Please bear in mind that you should never raise a PR only for the sake of it working in open source. Your PR should be of value to the project that you are contributing. You should also not raise a PR on an issue someone has already solved. Respect other developers efforts, it is the open source "community" after all. The owner of the project would have spent hours getting it to where it is, and you should not be raising a PR for an insignificant change(something like adding a white space, or changing variable names or any other trivial case for that matter). Imagine how difficult it will be for the maintainer to take the time to go through the PR and then realizing it was a spam all the way. So remember, no spamming, never! Be true to yourself and the project you are working for. Be mindful of your contribution and be respectful of others there.***

For the sake of this task, open VS code and open the folder that was downloaded. Create a text file inside the folder named "tests" and add anything you want to it(this will be open source and will be visible to other developers in my repo). Important: Do a Ctrl+S to save the changes locally. Only then will it be reflected in the repo.

![None](https://miro.medium.com/v2/resize:fit:700/1*Muw2v7nKcWIsBqyrSnx_fw.png)

Source: Snip of my personal machine

Now you have made the changes and it is ready for the next step.

#### Step 4: Add the changes

The git add command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit(Hey add this change). You can do that by executing:

*git add .*

You can also view all the changes made after the previous commit by executing

*git status*

#### Step 5: Confirm the changes

Now you have to confirm that you have verified the changes that were added. That is done by "committing" the changes(Hey I am sure that these changes have to be made). You can also describe the changes made by including a message when committing (the -m part)

*git commit -m "Added some content to the folder or any other message"*

#### Step 6: Push

Now you have to push the code from your local machine to your account(Hey this code can be pushed from my local machine to the internet). How does this happen? Well that is why you set the global variables in step 0.

*git push*

#### Step 7:Pull request

After this, you should be able to see your file in the repo in your GitHub account. Now the next step is to add this code to the main repo. This can be done by creating a pull request(request the owner to pull your code into their repo). Head over to the folder that contains the file you wrote. You should be able to see a "Pull request" button in your folder. Click on that, and then create a pull request. If I merge it with my repo, it means you have made your first open source contribution. Congratulations!!!

### Conclusion

This is just the tip of the ice berg. Open source has a lot more to it, and we can learn all that through practice. By now, you should have faced your fear of open source, if you had one. Moving on, if you want to contribute to bigger projects, you can follow the same steps, after great understanding of the code. If you enjoyed learning with me, do give this series a clap and follow me on medium. See you sometime soon!!
