---
title: Four Case Studies in Vibe Coding
source_url: https://itrevolution.com/articles/four-case-studies-in-vibe-coding/
source_domain: itrevolution.com
topic: github-ai-vibe
doc_type: other
author: Gene Kim; Steve Yegge
published_date: '2025-09-04'
fetched_at: '2026-05-29T13:37:56.782898+00:00'
language: en
word_count: 2343
reading_time: 12
signal_score: 1.0
status: kept
core_question: What does four involve in software development?
tldr: 'Four Case Studies in Vibe Coding September 4, 2025 # Four Case Studies in Vibe Coding *The following
  is an excerpt from the forthcoming book Vibe Coding: Building Production-Grade Software With GenAI,
  Chat, Agents, and Beyond* *by Gene Kim and Steve Yegge.* Before we dive into the techniques and frameworks'
key_topics:
- ai
- coding
- development
- agent
- vibe coding
- prompt
- testing
- tool
entities:
  primary: Four
  aliases:
  - Four
  - Case
  - Studies
content_hash: sha256:408c3fdc3d0555aa4e5ae9f54060207d5ce64128542562fc215bf36d7c968fd4
---

September 4, 2025

# Four Case Studies in Vibe Coding

*The following is an excerpt from the forthcoming book Vibe Coding: Building Production-Grade Software With GenAI, Chat, Agents, and Beyond* *by Gene Kim and Steve Yegge.*

Before we dive into the techniques and frameworks that underpin vibe coding, we want to share with you some field reports of real experiences. We'll tell a tale of an experienced developer tackling a side project, share two stories of world-class engineering teams solving important business problems, and regale you about a person who hadn't programmed in nearly twenty years building tools to solve her problem.

These anecdotes are real-world demonstrations of people achieving FAAFO. They give us a taste of the transformative potential that vibe coding will inevitably deliver at scale in technology organizations.

**Building OSS Firmware Uploader** **for CNC Machine**

We mentioned our friend Luke Burton, who spent nearly two decades at Apple managing engineering efforts around some iconic moments. Some of his achievements include being responsible for the technical readiness of the 2014 WWDC introduction of the Swift programming language to millions of developers. Luke has worked in and around the many systems that support iOS and MacOS, including working on improving the security of the iPhone supply chain.

Recently, Luke's hobby has been playing with CNC machines, which are meticulously crafted devices that carve intricate metal parts with knife-edge precision. But as Luke has become interested in modifying the CNC firmware, he's discovered that the firmware development environment is woefully challenging.

Luke is one of those hobbyists who tinkers deeply with their tools. He found that firmware testing is typically done on the CNC machine, instead of locally on the developer's laptop, which would be much faster and safer. Furthermore, uploading the firmware requires cumbersome telnet commands. Unit tests of the firmware seemed almost vestigial, which made modifying the code seem treacherous and unpleasant.

After hearing what we've been working on, he wondered whether vibe coding could help him fix some of these problems. One evening, using Claude Code, he proved to himself he could navigate and start modifying the CNC tooling and code base. Soon afterward, he texted us about how he had created a Python program that automated the upload of firmware to the CNC machine, significantly reducing the friction: "2600 lines of Python with documentation and proper CLI flags. It cost me $50 in Claude Code tokens, but I'm not complaining!" It took him two hours, and he was multitasking the whole time.

Seeing what he built, his collaborator in Germany was amazed, prompting Luke's enthusiastic reply: "You ain't seen nothing yet—give me 15 minutes, and this thing will have an interactive mode with GNU readline support."

He showed this tool to a few people, and they immediately told him, "I NEED THIS." The original controller program is notorious for being unusable because it doesn't allow copying and pasting, there is no "file open" dialog box, the navigation keys don't work, etc.

He didn't complete it in one step. It took patience and iteration. Claude Code struggled to handle strangely compressed files referenced in the original CNC firmware ("I couldn't have done it any better," he said). He eventually switched to Cursor, which used the same Claude Sonnet 3.7 model, and fed it code from another Python program that worked. With AI's help, he got it working in two tries.

This is an example of someone achieving FAAFO. Also, someone who is clever about using multiple tools to push through to a working solution. Furthermore, Luke's contributions will help everyone who is helping improve the CNC firmware better, faster, and safer.

**Christine Hudson Returns to Coding**

As we were working on the book, we got to help someone vibe code for the first time. Our friend Christine Hudson did her master's degree work in machine learning in 2004 but hadn't coded in fifteen to twenty years. She decided to try vibe coding.

For her first project, she chose to export her Google Calendar entries to another Google account. This is something that she would never have considered attempting before AI—the *ambitious* in FAAFO.

One of the first things we had to figure out was which developer environment would be best here. We preferred not to have to configure a local environment. During the session, we tried Google Apps Script, Google Colab notebooks, and terminal apps. All three of us used different approaches to implement the same task, with the goal of having something working in ninety minutes.

Unexpectedly, Christine was not only the first to complete the task but also the only one who succeeded at all. Using Google Apps Script, she successfully exported her calendar to Google Drive as an ICS calendar file. Steve attempted to replicate her approach in real time but did not succeed because of an obscure error with his authentication. Meanwhile, Gene's approach, using Python in a Google Colab notebook, got stuck in a similar spot, trying to create a Google OAuth consent screen.

Steve and Gene were tangled in the barbed wire that all programmers have to overcome: Dealing with everything the program needs to interact with that's out of your control—worse, when it's external services. Every encounter with a third-party API is a chance for a dead-end and retracing your steps.

Christine is now a vibe coder. We're happy that she succeeded, even though we both fell flat on our dumb faces. We had steered Christine toward Google Apps Script because of a crucial benefit: It was already authenticated and had built-in access to Google Calendar APIs. And that was the key that unblocked her.

This insight—knowing which path would avoid authentication complexity—shows the real advantage that experienced developers have. They know the broader technology landscape and have developed some judgment about which approaches are better than others. And then they pick the wrong one, but their student gets it right. But, hey, at least someone succeeded.

We asked Christine about how the experience felt on a scale of 1 (worst experience ever) to 10 (best experience ever). She said there were moments of pure joy ("+10") when she saw the code being written for her, creating an almost magical experience of effortless creation.

And how would she rate her most frustrating part? We were afraid her experience would be a -10, and she'd never want to do this again. After all, we had all struggled in frustration with external obstacles, like Christine's failed Google Cloud sign-ups, the countless error messages, Claude rate limits, switching to ChatGPT, and not being able to upload screenshots. But no. Christine said it had been mildly annoying, but no more so than the computer troubleshooting she has to do every day.

Gene and Steve felt the frustration more than Christine did because they wanted the experience to be seamless, and there were a lot of obstacles. The fun parts of coding had been accelerated, but all the rest of the time we were stuck on miserable troubleshooting. Steve quipped that vibe coding can sometimes be like a hellish trip to Disneyland, where all the rides and fun parts have been compressed to half a second…and all you're left with is waiting in line. But that wasn't Christine's experience at all. She found the process fulfilling and took pride in what she built, despite the setbacks. She, too, was experiencing FAAFO.

Let this be an inspirational case study for anyone who wants to "return to code." You can have as much ambition as you like, and build things you always wanted to build, and it's infinitely easier than it ever was. We welcome you back.

**Adidas 700 Developer Case Study**

After seeing Luke and Christine's hobby projects, you might be thinking that vibe coding is not suitable for "real work in the enterprise." If you believe this, you're not alone. But this is why you need to know about the work of Fernando Cornago, Global VP of Digital and E-Commerce Technology at Adidas, and responsible for nearly a thousand developers.

Adidas generates nine billion euros of revenue annually and is one of the top five e-commerce brands in the world. Formerly responsible for their platform engineering, Fernando is passionate about providing developers with the tools they need to be productive. In 2024 and 2025, he delivered an experience report on their 700-person GenAI developer pilot—an experiment with vibe coding in a large-scale enterprise environment.

This was their second pilot. The first pilot had spectacularly flopped, with 90% of developers hating the coding assistant tool. The reviews included phrases such as a "total waste of time" and nothing but "firefighting and troubleshooting." Such was life on the trail in the pioneering days of AI-based coding (i.e., early 2024) when the tools and models weren't good enough to be useful.

However, with those learnings, they tried again. This second pilot is now entering its second year. As we described earlier, Cornago reported that 70% of developers experienced productivity gains of 20–30%, as measured by increases in commits, pull requests, and overall feature-delivery velocity. Not bad. More importantly, developers reported feeling 20–25% more effective in their daily craft. Also not too shabby, especially as this was all done before coding agents, which are 10x more powerful and addictive.

Among the things that made Fernando most proud is that most of his engineers report a 50% increase in what they call "Happy Time." More precisely, that's the amount of time developers spend on things they want to do, which includes hands-on coding, analysis, and design. That implies they're spending far less "Annoying Time"—unrewarding work such as attending meetings, troubleshooting their environments, dealing with brittle tests, or tedious administrative tasks.

We'll describe the factors that differentiated these two groups, which leaders need to know about, in Part 4. In short, the happier teams worked in loosely coupled architectures. They had clear API boundaries, fast feedback loops, and independence of action. Vibe coding worked well for them.

This tale demonstrates how vibe coding requires creating an environment where developers can do their best work. With the right architecture and fast feedback loops, vibe coding can increase developers' productivity and satisfaction with their jobs. And these happy developers can best achieve organizational goals.

**Elevating Developer Productivity** **at Booking.com**

Booking.com is one of the largest online travel agencies, with a team of more than three thousand developers. Bruno Passos is Group Product Manager, Developer Experience. His mission is to eliminate developer roadblocks so his teams can do their best work. Over the past year, Bruno has been heavily involved in Booking.com's GenAI innovation efforts within engineering—another example of vibe coding at enterprise scale.

Booking.com has a storied history of a culture of experimentation, where almost every feature decision is tested, typically through feature flags—a practice that involves deploying multiple versions of a feature to production and then measuring which one best achieves the desired business goals. One downside is that the code base is full of never-used functionality behind disabled feature flags, legacy code, and old experiments.

The result was developers spending 90% of their time on frustrating toil rather than productive coding. This became one of the focus areas for using Sourcegraph's AI code assistant and search tools. Their developers reported a 30% boost in coding efficiency, with significantly lighter merge requests (70% smaller) and reduced review times.

In Part 4, we'll discuss more of the strategies and tactics Bruno used to achieve these results. Booking.com's creative strategies included educational initiatives that transformed skeptical developers into enthusiastic daily users. They also held days of training with each business unit to help ensure developers knew enough to be successful.

Initially, Booking.com's developer uptake of vibe coding and coding assistant tools was uneven. Some developers embraced their new AI partner; others didn't see the benefits. Bruno's team soon realized the missing ingredient was training. When developers learned how to give their coding assistant more explicit instructions and more effective context, they found up to 30% increases in merge requests and higher job satisfaction.

Bruno's leadership defined short-, medium-, and long-term goals focused on faster merges, higher-quality code, and reduction of technical debt. Sourcegraph and its specialized agents enabled developers to commit 30% more merge requests, with smaller diffs, and reduced review times.

Bruno emphasized that tools alone weren't enough. They supported development teams across the enterprise with targeted, hands-on hackathons and workshops. As a result, initially hesitant developers became enthusiastic daily vibe coders who are finding FAAFO.

**Conclusion**

These four case studies—spanning from hobby projects to enterprise-scale implementations—illustrate the transformative potential of vibe coding across different contexts and skill levels. Luke's CNC firmware project demonstrates how individual developers can achieve ambitious goals with newfound efficiency. Christine's return to coding after a twenty-year hiatus reveals how vibe coding can make programming accessible and enjoyable again for those who had previously stepped away. The Adidas and Booking.com implementations show how large organizations can systematically improve developer productivity, happiness, and business outcomes when the right conditions are present.

As we move forward in this book, we'll explore the techniques and frameworks that can help you and your organization harness this revolutionary approach to software development.

Stay tuned for more exclusive excerpts from the upcoming book *Vibe Coding: Building Production-Grade Software With GenAI, Chat, Agents, and Beyond* *by Gene Kim and Steve Yegge* on this blog or by signing up for the IT Revolution newsletter.

No comments found

## Leave a Comment

## More Like This

### Your Strategy Isn't Failing. Your Feedback Loop Is.

You have a strategy. You have teams. You're tracking metrics. And yet the connection…

#### Melissa Reeve On AI Extinction Events, Unlearning Agile, and What Stage 5 Actually Looks Like

In our continued conversation with Hyperadaptive author Melissa M. Reeve, we talked about the…

##### The Five DevOps Lessons Hyperadaptive Carries Forward

My denial around AI started when ChatGPT showed up and hit the marketing function…

##### Hyperadaptive Author Melissa Reeve on What It Takes to Thrive in the Age of AI

When Melissa M. Reeve began studying how organizations navigate AI transformation, she expected to…
