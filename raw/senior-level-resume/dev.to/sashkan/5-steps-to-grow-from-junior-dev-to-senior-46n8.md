---
source_url: https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8
crawl_depth: 0
crawled_at: 2026-05-05T08:33:18Z
word_count: 2344
---

I've been writing code for eleven years now, and slowly moved from intern, to junior, to senior, to lead developer, with the occasional job as a CTO.
Over the past two years, I've spent roughly 250 hours reviewing applications and technical tests, both on site and online, and helped wonderful teams build great products.
Here are the 5 key differences between a junior and a senior developer. And to illustrate each concept, I'll give examples based on real-life events, that lead either to great success, or tremendous failures.
##  [ ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#1-ask-challenge-believe) 1 - Ask, Challenge, Believe 
[![Image description](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9j42pd3ys3esycxcilr7.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9j42pd3ys3esycxcilr7.png)
Whatever you're working on, it is way easier to build a great product if you actually believe in it. And the only way to build conviction is to ask around. Why am I adding this feature ? Why are we making these changes ? Does my team know about this pattern ? 
The key idea here is, you have to believe in the product you are building. You have to build conviction before laying down your first line of code. You cannot nurture any doubt as of why you are shipping this feature, who's going to use it, or how.
In 2020, I was working at a major company in video games. We were hosting an e-sport tournament, and our marketing team thought about developing a scoreboards client app, and plugging it into an eternal API to fetch scores in real time. I was in charge of the technical part, managing a team of 5 developers. 
Unfortunately, the same marketing team did its own research for available APIs, and decided to sign a contract with a company before including any tech member in the process.
Which lead to a very goofy meeting, when I finally met my tech counterpart in said company. For 90 minutes, we listened to my manager, knowing that their API was not the one we needed. In fact, I knew half a dozen of APIs that could have done the job, for a fraction of the price.
I went back to my team, and we took a moment to decide how to tackle this issue. To which they answered the ONE question you have to fear when working on any product: "Why do we need this ?". They did not believe in this new scoreboard app. Neither did I: there was no conviction whatsoever.
So, I calmly asked for a quick talk with my manager, and asked him what we needed exactly. He gave my a short list of features, and I told him that it would take roughly 3 weeks to ship them all, and that I knew of an API that could get the job done for 12.99 a month. To which he responded that he already paid the API company in full, for the use of their API and the services of a consultant, for the next 4 months. We're talking 115k euros.
So, I did the only sensible thing to do. I went to my manager's manager, took the blame for the miscommunication, and asked him what to do next. We thanked the API company, we thanked the consultant, and based simply on the small list of feature my manager had given me, we managed to ship the whole project in three weeks. Suddenly, our tech team believed in the project, because we know WHY we were doing it, and HOW we could do it properly.
The key idea here is: a senior developer spends a lot of time building conviction, questioning patterns, and proactively bringing solutions through his knowledge and past experiences. Once your whole team believes in an app, or a feature, you'll know exactly how to code it.
##  [ ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#2-know-your-tools) 2 - Know your tools 
[![Image description](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fm2skjjvtb9qfkdfykeyr.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fm2skjjvtb9qfkdfykeyr.png)
There are thousands of way to add authentication to your app. Or real-time. Or to build an endpoint that fetches data. Which means that there are thousands of way to do it poorly.
A senior dev knows the main patterns to add a feature, and therefore, he can code it quickly, shipping a code that is both clean, reliable, and well documented.
A great way to assess your "seniority" is to take a look at a few numbers:
  * How many threads do I have on my merge requests ?
  * How long does it take for my MR to be merged ?
  * How often am I asked for advices/review ?


No matter how complex your app might be, there are not that many tools that we use on a daily basis. My current stack includes Nest.js, Next.js, tailwind and GraphQL, which can be overwhelming for a junior dev.
So, instead of simply reading the documentation, every time I start working on a new topic, or using a new tool, I document it for myself, using the [micro-thesis system](https://www.youtube.com/watch?v=XE_CGBlQ17o). I'm using Obsidian as my Documentation system, but there are a lot of viable tools out there.
Here is my process:
  * I use my daily note to list my tasks for the day. 
  * If this task requires learning a new skill, I turn it into a link using the [[]] syntax.
  * As I learn how to use this new tool, I write the best documentation I can. It has to be simple, include pieces of code, be reusable, and include links toward useful documentations.


This way, the next time I'll have to use said tool, and I have to do is search for this page in my Obsidian vault. not only will I have a head start on how to use it, it will also include links toward all of my notes that mention this page, making it easier to decide whether or not this is the right tool for the task at hand. 
This also means that, whenever a tool is updated, I must update my documentation accordingly. This is pretty much how I keep myself updated on the latest versions of my stack. 
Another important thing to keep in mind is the ratio between the time needed to ship a feature, and the price invested in using a third part application. 
Let's say you are building an app that required both authentication and authorization. Maybe you have an repository you can fork, maybe you don't. If you don't, it will take you some time to add these features. In the mean time, libraries and freemium SAAS might help you setup your authentication in no time.
If I'm building a small app, I'll always go for free solutions for everything I don't feel like coding myself. Let's keep it simple: a freelance software engineer charges 1000 dollars a day. Adding a proper authentication might take 2/3 working days. in the mean time, adding and configuring Clerk/Kinde/Lucia takes roughly an hour, and these solutions are free.
The key idea here is: your tools are not limited to your coding skills. Just like in the old RTS games I used to play, consider both your time, money and skills as resources, and pick wisely which one to use, and how much you want to spend.
##  [ ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#3-code-small) 3 - Code Small. 
[![Solidity of Simplicity](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwercxhfncmty1dlinm0s.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwercxhfncmty1dlinm0s.png)
Being a software engineer is awesome. It feels like having a bottomless box of Lego bricks at your disposal. You can use them to build whatever you want, from the smallest car to the biggest city.
But when it comes to professional projects, you have to understand that every line of code is a liability. Which means, the less you code, the more reliable your codebase is.
So, here are the 3 golden rules I try to live by:
  * A merge request solves ONE issue.
  * If I need to use a bullet list to explain the changes I made, and said bullet list includes more than 3 or 4 elements, I probably messed up.
  * The ability to properly split up your code requires experience, and is as important as the actual performance of your code. Both on front end (think composition in React) and back-end (think modules/services/whatever architecture you are using to split your code into small manageable chinks)


if you do so, you'll manage to ship faster, build confidence within your team, and quickly setup a flow that'll allow you to deliver value on a daily basis. 
On the other hand, you know that a pull request that affects countless files, is not properly documented, and includes loads of code smells will either be a nightmare to review, and will either stay open for a very long time, or will simply be closed. I usually go for the second option, by asking to split its content into smaller parts.
##  [ ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#4-reviews-are-gold) 4 - Reviews are gold 
[![Image description](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fofvnp1281svbps84u1xx.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fofvnp1281svbps84u1xx.png)
Consider this: as a software engineer, 90% of your knowledge comes from experience. Actual work experience. And said experience comes from mistakes and failures, both yours and your teammates'
The lesson here is, your main goal as a senior developer is to provide and receive feedback. As we said, there are thousands of ways to add a feature, some are better than others, and you don't have enough of a lifetime to try them all. So, ask around and collaborate.
Here is the usual process I follow when reviewing a MR:
  * Understand the underlying goal. "What are we trying to achieve here ?"
  * "How would I code it ?"


From there, I'm more of a multi-commits kind of guy, so I simply review one commit at a time. If, at any point, I don't understand something (why do you use this lib ? Why did you name it that way ?), I add a comment. 
Nowadays, I'm working as a lead developer, and my team has a wide range of seniority. Which means some MRs will receive a couple of comments (usually questions or interesting debates), and some others will receive 54 comments, from naming to logic to performances. In which case, I switch from review to peer programming. 
If you are managing a team, note that the amount of comments on any given review is an actual metric for the quality of code.
5 - Own it
[![Ownership](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqne5waq4eh7tb72xevks.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqne5waq4eh7tb72xevks.png)
It usually takes me about two months to decide whether or not I'm confident on the level of expertise of a coworker. If my standards are met, I don't have a problem with telling them that they are responsible for 99% of the development process, from the tools they use to the patterns they pick. The last percent is the review, and the consequences. I want them to be owners of the code, but I'll be the custodian of their wellbeing. 
At the end of they day, you have to embrace ownership on your decisions, both personal and professionals, which brings me to the following personal statements:
  * I'm way more efficient at work when I do the things that matter to me first thing in the morning. And not a single one of them is work-related
  * This includes drinking water, moisturising, flossing, workout, meditate.
  * Keep track of everything that matters. The good thing is, there are not a lot of things that matter.
  * Communicate to find your love/delegate balance, using the following chart:


[![Image description](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7cqkb4opovnzn5raoe4l.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7cqkb4opovnzn5raoe4l.png)
As a senior developer, you are responsible of both the quality of the code you ship, AND the quality of the code you review. As a manager, you are responsible of any given failure that comes from either your code, or the code your team ships. Which means that the BEST way to ensure code quality is not only to make thoughtful review, but to create the best possible environnement so that everyone can perform well
##  [ ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#tldr) TL;DR 
A senior dev would read the article.
[ ![profile](https://media2.dev.to/dynamic/image/width=64,height=64,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F1%2Fd908a186-5651-4a5a-9f76-15200bc6801f.jpg) The DEV Team ](https://dev.to/devteam) Promoted
Dropdown menu
* * *


[![Midnight Hackathon image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FpGxGqI1.jpeg)](https://mlh.link/midnight-hackathon-may-2026?bb=263328)
##  [ ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#build-the-future-of-data-privacy-on-midnight) [Build the Future of Data Privacy on Midnight](https://mlh.link/midnight-hackathon-may-2026?bb=263328)
This is your opportunity to build on a fully launched network designed to solve the internet's biggest privacy challenges. You’ll get hands-on experience with cutting-edge data protection tech to create applications that give users true control over their digital lives.
Read More 
[ ![nimrodkra profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F248246%2F71399f0b-c340-4094-8c18-a5a74b479c74.png) ](https://dev.to/nimrodkra)
Nimrod Kramer 
[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F248246%2F71399f0b-c340-4094-8c18-a5a74b479c74.png) Nimrod Kramer  ](https://dev.to/nimrodkra)
Follow
Just a guy sharing ideas. Building daily.dev to help busy developers stay updated with the latest tech news. I love 🍣, 🏓, ☕️ and 🦄 . 
  * Location 
Tel Aviv, Israel 
  * Work 
Co-Founder, CEO at daily.dev 
  * Joined 
Aug 2, 2018


• [ Mar 30 ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#comment-367aj)
Dropdown menu
  * Hide 


great advice, especially the part about building conviction and staying current. one thing i'd add to the "know your tools" section is daily.dev. millions of developers use it to stay up to date with the latest patterns, libraries, and industry discussions without having to manually check dozens of dev blogs. the personalized feed helps you discover new approaches to problems you're working on. honestly, staying current is one of the biggest separators between junior and senior devs, and having a good discovery system makes all the difference.
For further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)
[ ![profile](https://media2.dev.to/dynamic/image/width=64,height=64,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Forganization%2Fprofile_image%2F6839%2F3d85988f-d18e-4522-b261-f86613cd9b50.png) Sonar ](https://dev.to/sonar) Promoted
Dropdown menu
* * *


[![State of Code Developer Survey report](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fucarecdn.com%2F2f2ce9b0-68e0-48a1-bf3e-46c08831a9be%2F)](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259978)
##  [ ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#state-of-code-developer-survey-report) [State of Code Developer Survey report](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259978)
Did you know 96% of developers don't fully trust that AI-generated code is functionally correct, yet only 48% always check it before committing? Check out Sonar's new report on the real-world impact of AI on development teams.
[Read the results](https://www.sonarsource.com/sem/the-state-of-code/developer-survey-report/?utm_medium=paid&utm_source=dev&utm_campaign=ss-state-of-code-developer-survey26&utm_content=report-devsurvey-banner-x-2&utm_term=ww-all-x&s_category=Paid&s_source=Paid+Social&s_origin=dev&bb=259978)
👋 Kindness is contagious
Dropdown menu
* * *


Dive into this insightful article, celebrated by the caring DEV Community. **Programmers from all walks of life** are invited to share and expand our collective wisdom.
A simple thank-you can make someone’s day—drop your kudos in the comments!
On DEV, **spreading knowledge paves the way** and strengthens our community ties. If this piece helped you, a brief note of appreciation to the author truly counts.
###  [ ](https://dev.to/sashkan/5-steps-to-grow-from-junior-dev-to-senior-46n8#-cta-httpsdevtoenterstatenewuser-) [Let’s Go!](https://dev.to/enter?state=new-user&bb=239336)
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
