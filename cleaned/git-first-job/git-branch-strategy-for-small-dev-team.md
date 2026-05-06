---
title: "[Git branch strategy for small dev team [closed]](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team)"
topic: "git-first-job"
career_level:
  - executive
source_url: "https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team"
source_domain: "stackoverflow.com"
word_count: 2762
text_to_link_ratio: 0.6509
signal_score: 0.7509
is_curated: false
tags:
  - remote
  - open-source
  - executive
ingested_at: "2026-05-05"
---

# [Git branch strategy for small dev team [closed]](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team)
Asked 16 years, 1 month ago
Modified [9 years, 5 months ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team?lastactivity "2016-11-22 00:36:19Z")
Viewed 101k times 
This question shows research effort; it is useful and clear
195 
This question does not show any research effort; it is unclear or not useful
Save this question.
Show activity on this post.
We have a web app that we update and release almost daily. We use git as our VCS, and our current branching strategy is very simple and broken: we have a master branch and we check changes that we 'feel good about' into it. This works, but only until we check in a breaking change.
Does anyone have a favorite git branch strategy for **small teams** which meets the following requirements:
  1. Works well for teams of 2 to 3 developers
  2. Lightweight, and not too much process
  3. Allows devs to isolate work on bug fixes and larger features with ease
  4. Allows us to keep a stable branch (for those 'oh crap' moments when we have to get our production servers working)


Ideally, I'd love to see your step-by-step process for a dev working on a new bug


Share a link to this question
Copy link[CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/ "The current license for this post: CC BY-SA 2.5")
Short permalink to this question
Follow 
Follow this question to receive notifications
asked Mar 11, 2010 at 21:13
[![Bilal and Olga's user avatar](https://i.sstatic.net/d2PRz.png?s=64)](https://stackoverflow.com/users/253511/bilal-and-olga)
3,26163335
[ Add a comment ](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team "Use comments to ask for more information or suggest improvements. Avoid answering questions in comments.") |  [ ](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team "Expand to show all comments on this post")
##  6 Answers 6
Sorted by:  [ Reset to default ](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team?answertab=scoredesc#tab-top)
Highest score (default)  Trending (recent votes count more)  Date modified (newest first)  Date created (oldest first) 
This answer is useful
255 
This answer is not useful
Save this answer.
Loading when this answer was accepted…
Show activity on this post.
You might benefit from the workflow Scott Chacon describes in [Pro Git](http://git-scm.com/book). In this workflow, you have two branches that always exist, _master_ and _develop_.
_master_ represents the most stable version of your project and you only ever deploy to production from this branch.
_develop_ contains changes that are in progress and may not necessarily be ready for production.
From the _develop_ branch, you create topic branches to work on individual features and fixes. Once your feature/fix is ready to go, you merge it into _develop_ , at which point you can test how it interacts with other topic branches that your coworkers have merged in. Once _develop_ is in a stable state, merge it into _master_. It should always be safe to deploy to production from _master_.
Scott describes these long-running branches as "silos" of code, where code in a less stable branch will eventually "graduate" to one considered more stable after testing and general approval by your team.
Step by step, your workflow under this model might look like this:
  1. You need to fix a bug.
  2. Create a branch called _myfix_ that is based on the _develop_ branch.
  3. Work on the bug in this topic branch until it is fixed.
  4. Merge _myfix_ into _develop_. Run tests.
  5. You discover your fix conflicts with another topic branch _hisfix_ that your coworker merged into _develop_ while you were working on your fix.
  6. Make more changes in the _myfix_ branch to deal with these conflicts.
  7. Merge _myfix_ into _develop_ and run tests again.
  8. Everything works fine. Merge _develop_ into _master_.
  9. Deploy to production from _master_ any time, because you know it's stable.


For more details on this workflow, check out the [Branching Workflows](http://git-scm.com/book/en/Git-Branching-Branching-Workflows) chapter in Pro Git.
Share a link to this answer
Copy link[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/ "The current license for this post: CC BY-SA 3.0")
Short permalink to this answer
Follow 
Follow this answer to receive notifications
[![Qantas 94 Heavy's user avatar](https://i.sstatic.net/WzNwl.png?s=64)](https://stackoverflow.com/users/2074608/qantas-94-heavy)
16.1k317489
answered Mar 11, 2010 at 22:01
[![Jimmy's user avatar](https://www.gravatar.com/avatar/8893e2e206c0377ff776d2535887d23f?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/242493/jimmy)
37.6k1386100
## 11 Comments
Add a comment
[![](https://i.sstatic.net/U8esd4ED.png?s=64)](https://stackoverflow.com/users/5716/program247365)
program247365
[program247365](https://stackoverflow.com/users/5716/program247365) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment10782010_2429011)
Also Scott Chacon has an excellent article on his site on how Github's workflow with Git works - [scottchacon.com/2011/08/31/github-flow.html](http://scottchacon.com/2011/08/31/github-flow.html)
2011-12-29T21:51:52.023Z+00:00
8
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/f413eba6a4985222aeb8328e92ae89c6?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/270901/richard)
Richard
[Richard](https://stackoverflow.com/users/270901/richard) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment16381825_2429011)
I think this is great, except if you create bug fix branches from the develop branch, you are forcing you can't merge it into master and deploy it without also merging in everything else "new" that you've not released yet, which might be a real pain if there is something in that branch that needs documenting / database changes or something else hard to do. I think for urgent "hotfixes", you should make your branch from master. 
2012-09-01T07:45:16.47Z+00:00
77
Reply
  * Copy link


[![](https://i.sstatic.net/AdeT5.jpg?s=64)](https://stackoverflow.com/users/396216/murat-derya-%c3%96zen)
Murat Derya Özen
[Murat Derya Özen](https://stackoverflow.com/users/396216/murat-derya-%c3%96zen) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment28352956_2429011)
What if we are developing 2 separate features, F1 and F2, where F1 is to be released in a week but F2 is to be released in 2 weeks, assuming that the development of F1 and F2 coincide? Any suggestions on that? 
2013-10-03T18:06:09.187Z+00:00
6
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/a2909c1103b9ceba6c8933c85dc4f803?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/10245/tim-abell)
Tim Abell
[Tim Abell](https://stackoverflow.com/users/10245/tim-abell) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment67876134_2429011)
The `develop` is an unecessary 'solution' to a problem that git doesn't have. As far as I can tell the success is due to a well written if misguided article with no comments allowed. Here's a counter-article [barro.github.io/2016/02/…](https://barro.github.io/2016/02/a-succesful-git-branching-model-considered-harmful/)
2016-10-28T16:36:39.97Z+00:00
6
Reply
  * Copy link


[![](https://i.sstatic.net/VvF8J.png?s=64)](https://stackoverflow.com/users/384724/todd)
Todd
[Todd](https://stackoverflow.com/users/384724/todd) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment72172190_2429011)
At step 8, merging the develop branch into master sounds like a bad idea given that some of the code in develop might not be ready to go into production. Wouldn't we be better off merging the feature branch into master? 
2017-02-28T19:58:51.127Z+00:00
7
Reply
  * Copy link


Add a comment | Show 6 more comments
This answer is useful
47 
This answer is not useful
Save this answer.
Loading when this answer was accepted…
Show activity on this post.
After coming in as a novice trying to find a straight-forward strategy to teach to other devs who have never used source control. This is the one that fit <http://nvie.com/posts/a-successful-git-branching-model/> I tried using the standard GIT workflow thats in the man pages but it confused me slightly and my audience completely. 
Over the past 6 months I have only had to fix conflicts twice. I have added steps to always test after a merge and to 'fetch and merge" or 'pull --rebase" a lot (once in the morning and in the afternoon) while developing features. We also used github.com as the central place to pull the latest code.
Share a link to this answer
Copy link[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/ "The current license for this post: CC BY-SA 3.0")
Short permalink to this answer
Follow 
Follow this answer to receive notifications
answered Jun 6, 2011 at 16:39
[![Clutch's user avatar](https://www.gravatar.com/avatar/9de93007dfb196017c4256f9a0f9ae32?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/25143/clutch)
7,750115058
## 5 Comments
Add a comment
[![](https://www.gravatar.com/avatar/e36253e3da734a26b7373a2ded71825f?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/1415352/keithxm23)
keithxm23
[keithxm23](https://stackoverflow.com/users/1415352/keithxm23) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment17021076_6255217)
That is an excellent link! That workflow works superbly well for our small team who always work remotely and parallelly on multiple release versions at a time. Very well documented. Thanks Clutch! 
2012-09-27T14:50:24.307Z+00:00
0
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/852c5968aa2f0b4379d94304cfac4f3f?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/2430505/boise)
Boise
[Boise](https://stackoverflow.com/users/2430505/boise) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment25912157_6255217)
Ah, so this is where I found that link :-) I looked at several Git strategies before setting up my first Git project (I have moved from SCCS to CVS to SVN over the years and now I wanted to try Git for a new project) and this was the one that made the most sense to me. I recognize your post so I'm pretty sure this is where I found it. So Thanks - it works wonderfully well! 
2013-07-20T22:42:21.153Z+00:00
0
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/a2909c1103b9ceba6c8933c85dc4f803?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/10245/tim-abell)
Tim Abell
[Tim Abell](https://stackoverflow.com/users/10245/tim-abell) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment67875952_6255217)
I die a little inside everytime I see someone pick up that blog post. Here's a rebuttal: [barro.github.io/2016/02/…](https://barro.github.io/2016/02/a-succesful-git-branching-model-considered-harmful/)
2016-10-28T16:30:58.053Z+00:00
7
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/c0813ef73a1a468d754775e4cb276abe?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/248616/nam-g-vu)
Nam G VU
[Nam G VU](https://stackoverflow.com/users/248616/nam-g-vu) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment68659903_6255217)
I share the same feeling with you @TimAbell; I strongly feel it not right when the `default master branch` is NOT used the most often be developer in this `A successful Git branching model`
2016-11-21T09:07:38.977Z+00:00
0
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/26cab2ab8ca66a06c5036a81e4acb521?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/456456/r-schreurs)
R. Schreurs
[R. Schreurs](https://stackoverflow.com/users/456456/r-schreurs) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment136990187_6255217)
Your having to fix conflicts twice might be circumvented by using [git rerere](https://git-scm.com/docs/git-rerere). Some background can be found in [Fix conflicts only once with git rerere](https://medium.com/@porteneuve/fix-conflicts-only-once-with-git-rerere-7d116b2cec67). 
2023-12-22T14:58:59.01Z+00:00
0
Reply
  * Copy link


Add a comment
This answer is useful
35 
This answer is not useful
Save this answer.
Loading when this answer was accepted…
Show activity on this post.
(Made my [comment](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team/2429011#comment10782010_2429011) above it's own answer, as I should have initially.)
From Scott Chacon of Github:
> How We Do It So, what is GitHub Flow?
>   * Anything in the master branch is deployable 
>   * To work on something new, create a descriptively named branch off of master (ie: new-oauth2-scopes) 
>   * Commit to that branch locally and regularly push your work to the same named branch on the server 
>   * When you need feedback or help, or you think the branch is ready for merging, open a **pull request**
>   * After someone else has reviewed and signed off on the feature, you can merge it into master
>   * Once it is merged and pushed to ‘master’, you can and should deploy immediately
> 

See the entire article for more details: <http://scottchacon.com/2011/08/31/github-flow.html>
Note that "pull requests" are a Github invention, and it's something that's baked into their website, not Git itself: <https://help.github.com/articles/using-pull-requests/>
Share a link to this answer
Copy link[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/ "The current license for this post: CC BY-SA 3.0")
Short permalink to this answer
Follow 
Follow this answer to receive notifications
[![Community's user avatar](https://www.gravatar.com/avatar/a007be5a61f6aa8f3e85ae2fc18dd66e?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/-1/community)
[Community](https://stackoverflow.com/users/-1/community)Bot
11
answered Aug 16, 2012 at 19:34
[![program247365's user avatar](https://i.sstatic.net/U8esd4ED.png?s=64)](https://stackoverflow.com/users/5716/program247365)
4,02973646
## 3 Comments
Add a comment
[![](https://www.gravatar.com/avatar/c6b8a179e282f28068efe790273e78cc?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/849055/squadrons)
Squadrons
[Squadrons](https://stackoverflow.com/users/849055/squadrons) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment46148874_11994209)
With a smaller team and devs less experienced with git, this workflow's simplicity wins out. The only thing we do differently is having a 'staging' branch between the feature branch and master that acts as a live QA site for non devs to okay the feature in a production like environment. 
2015-03-09T16:50:12.523Z+00:00
4
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/a2909c1103b9ceba6c8933c85dc4f803?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/10245/tim-abell)
Tim Abell
[Tim Abell](https://stackoverflow.com/users/10245/tim-abell) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment67875991_11994209)
@Squadrons sounds like you need [octopus deploy](https://octopus.com/) for that, that has gates built in to ok/deny builds getting onto different environments and doesn't pollute your source control with such things. 
2016-10-28T16:32:29.883Z+00:00
0
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/7a1054e17f3c41c66b1b28d4d6b09379?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/17211/razor)
Razor
[Razor](https://stackoverflow.com/users/17211/razor) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment70634427_11994209)
Creating feature branches off of master and then merging them back in for deployment is OK, so long as you have a tag so there's a safe rollback point. Deployments don't always go according to plan. Whether you believe in "roll forward only" doesn't matter much when you're haemorrhaging money. 
2017-01-18T12:52:36.603Z+00:00
0
Reply
  * Copy link


Add a comment
This answer is useful
16 
This answer is not useful
Save this answer.
Loading when this answer was accepted…
Show activity on this post.
Use the `master` branch as your development branch and create release branches for performing bug fixes.
Any new features will go on `master` during the development window (either committed directly or as topic branches with pull-requests, up to you -- not shown in graphic). Once all your planned features are implemented, enter feature freeze, and perform testing. When you're happy, tag the release on `master` as `v1.0`.
Over time your users will find bugs in `v1.0` so you'll want to create a branch from that tag (e.g. name it after the release `1.0`) and fix those bugs in the branch. When you've got enough bugs fixed that you think it warrants a new release then tag it as `v1.0.1` and merge it back into `master`.
Meanwhile a new development window can be happening on the `master` branch which will eventually be tagged as `v1.1`.
Rinse & repeat.
This follows [Semantic Versioning](http://semver.org) numbering logic.

```
 ---------(v1.0)--------------------------------(v1.1)-----------------------------> master
             \                                     \  
              ---(v1.0.1)---(v1.0.2)---> 1.0        ---(v1.1.1)---(v1.1.2)---> 1.1

```

Share a link to this answer
Copy link[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/ "The current license for this post: CC BY-SA 3.0")
Short permalink to this answer
Follow 
Follow this answer to receive notifications
answered Aug 26, 2011 at 20:15
[![leif.gruenwoldt's user avatar](https://www.gravatar.com/avatar/2d128be9e2e492517499a7dc00af1a42?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/52176/leif-gruenwoldt)
14.1k56467
## 5 Comments
Add a comment
[![](https://www.gravatar.com/avatar/75b0d3755139a330ecfc894a225d2ad1?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/505093/kwahn)
kwahn
[kwahn](https://stackoverflow.com/users/505093/kwahn) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment54412543_7210106)
Don't forget to merge your `1.0.1` changes back into `master`
2015-10-23T16:08:37.913Z+00:00
5
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/c0813ef73a1a468d754775e4cb276abe?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/248616/nam-g-vu)
Nam G VU
[Nam G VU](https://stackoverflow.com/users/248616/nam-g-vu) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment68659665_7210106)
And always keep in mind to rebase `1.1` on master after merging `1.0.1` - this helps minimize confiction. 
2016-11-21T09:00:09.993Z+00:00
1
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/2d128be9e2e492517499a7dc00af1a42?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/52176/leif-gruenwoldt)
leif.gruenwoldt
[leif.gruenwoldt](https://stackoverflow.com/users/52176/leif-gruenwoldt) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment68690553_7210106)
@NamGVU I wouldn't recommend that. `1.1` is a release branch and has tags representing the exact state of one or more releases. Rebasing that branch would cause you to lose that representation. I'd strongly recommend setting your release branches to deny force pushes to prevent this. 
2016-11-22T00:23:51.593Z+00:00
0
Reply
  * Copy link


[![](https://www.gravatar.com/avatar/3328abe19153c39b04338b2a323ceb36?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/5778708/m-bitsnbites)
m-bitsnbites
[m-bitsnbites](https://stackoverflow.com/users/5778708/m-bitsnbites) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment69953768_7210106)
No. Don't merge release branches back into master! It can give you all sorts of headaches that you do not need (merging in release-only stuff, merge conflicts with newer releases, breaking builds, non-linear history, etc. Believe me, I've seen it happen more than once). Instead, treat releases as forks. See [bitsnbites.eu/a-stable-mainline-branching-model-for-git](http://www.bitsnbites.eu/a-stable-mainline-branching-model-for-git/)
2016-12-29T08:47:05.217Z+00:00
1
Reply
  * Copy link


[![](https://i.sstatic.net/AIjBF.jpg?s=64)](https://stackoverflow.com/users/2642204/bartoszkp)
BartoszKP
[BartoszKP](https://stackoverflow.com/users/2642204/bartoszkp) [Over a year ago](https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team#comment70471492_7210106)
cherry-pick is a better option for retrieving release changes into master 
2017-01-13T13:41:47.417Z+00:00
5
Reply
  * Copy link


Add a comment
This answer is useful
4 
This answer is not useful
Save this answer.
Loading when this answer was accepted…
Show activity on this post.
In a VCS, having just a "master" branch shows quickly its limits because you cannot pursue all the development effort at the same time on one branch.  
That means you need to know **[when to branch](https://stackoverflow.com/questions/2100829#2107672)**.
But in a DVCS (as in "Decentralized" VCS), you also have a **[publication issue](https://stackoverflow.com/questions/1039817/git-commit-frequency/1040502#1040502)** , with branches you keep local to your repositories, and branches you are pushing to or pulling from.
In this context, start by identifying your concurrent development effort, and decide on a publication (push/pull) process. For instance (and this is not the only way):
  * prod is a read-only public branch with the code in production. Everyone could pull from it in order to: 
    * rebase its current development on top of it (for local testing, or for integrating on the local dev repo a hotfix done in the prod repo on the prod branch)
    * branch to do new features (from a known stable code)
    * branch to start the next release branch (the one which is to be in production)  
no one should push directly to prod (hence the read-only)
  * release is a read-write consolidation branch, where the relevant commits are cherry-picked to be part of the next release.  
Everyone can push to release to update the next release.  
Everyone can pull from said release in order to update his/her local consolidation process.
  * featureX is a private read-write branch (in that it does not need to be push to the central prod repo), and can be pushed/pulled between dev repos. It represents middle to long term effort, different from the daily dev
  * master represents the current dev, and is pushed/pulled between the dev repos.


Other release management processes exist, as this [SO question attests](https://stackoverflow.com/questions/1042400/git-releases-management/1042463#1042463).
Share a link to this answer
Copy link[CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/ "The current license for this post: CC BY-SA 2.5")
Short permalink to this answer
Follow 
Follow this answer to receive notifications
[![Community's user avatar](https://www.gravatar.com/avatar/a007be5a61f6aa8f3e85ae2fc18dd66e?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/-1/community)
[Community](https://stackoverflow.com/users/-1/community)Bot
11
answered Mar 11, 2010 at 21:58
[![VonC's user avatar](https://i.sstatic.net/I4fiW.jpg?s=64)](https://stackoverflow.com/users/6309/vonc)
1.4m5694.8k5.8k
## Comments
Add a comment
This answer is useful
3 
This answer is not useful
Save this answer.
Loading when this answer was accepted…
Show activity on this post.
Read through ReinH's Git Workflow for Agile teams here: <http://reinh.com/blog/2009/03/02/a-git-workflow-for-agile-teams.html>
This works very well for small teams. The goal here is to make sure everything that might be potentially unstable goes in to a branch of some kind. Only merge back to master when you are ready for everyone working outside of the feature branch to use it.
Note: this strategy is hardly git specific, but git makes implementing this strategy pretty easy.
Share a link to this answer
Copy link[CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/ "The current license for this post: CC BY-SA 2.5")
Short permalink to this answer
Follow 
Follow this answer to receive notifications
answered Mar 12, 2010 at 14:53
[![whaley's user avatar](https://www.gravatar.com/avatar/14d6944fb1469c80688a27155ae2c967?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/46375/whaley)
16.3k106168
## Comments
Add a comment
Start asking to get answers
Find the answer to your question by asking.
Explore related questions


See similar questions with these tags.
