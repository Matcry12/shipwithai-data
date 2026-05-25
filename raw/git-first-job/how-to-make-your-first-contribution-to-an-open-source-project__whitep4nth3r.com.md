---
source_url: "https://whitep4nth3r.com/blog/how-to-make-your-first-open-source-contribution/"
source_domain: "whitep4nth3r.com"
topic: "git-first-job"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-25T06:43:02.104479+00:00"
word_count: 2198
stage: "raw-extracted"
---

# How to make your first contribution to an open source project

I recently (and accidentally) became a maintainer of a new open source project, npmx.dev. The project’s vision is to provide a new way to browse the npm package registry, with some exciting bonus features.

I’ve always been on the fringes of open source; I’ve contributed to a few projects here and there, such as the Astro docs, Google Lighthouse, and some others, and most of my code on GitHub is open source for the wider community. But, contributing to open source projects can be scary: big codebases, unfamiliar tech, lots of new people, and a sea of open issues can make it hard to know where to start.

However, open source isn’t really all about **code**, it’s about **community.** Since my involvement in npmx, I’ve experienced first-hand what a welcoming and inclusive approach to open source can do to empower anyone to make a variety of contributions to help make The Web ecosystem a great place to be and work.

And so, with that experience and some great examples of what good looks like in open source, and because npmx just announced their alpha release, I thought I’d put together a guide on how to get involved in open source to help you get started.

Throughout this guide, I’ll be using some specific open source terms. Here's what they mean:

**Open source**: a software development model that encourages open collaboration, with source code, documentation, and discussion around the development of the project freely available to the public.**Issue**: A ticket used to track bugs, features, questions, or tasks.**Pull Request (PR)**: a request to merge any changes into the main project, and to review and discuss those changes.**Maintainer**: a key contributor to the project who leads, manages, and steers the direction of the project. Maintainers are responsible for reviewing and merging pull requests, managing issues, and taking care of the community, usually acting as the final decision-makers. Some maintainers may also be called**stewards**.**Contributor**: anyone who has contributed anything to an open source project, whether it is code, documentation, testing and reviewing pull requests, design, finding issues, community management, or anything else related to the project.

Where this guide provides specific examples on things such as pull requests and issues, the examples will be specific to GitHub, as that's where all the action is happening for npmx.

## 1. Find a cool project

The first step is to find a project that you are excited about. Maybe it’s a library or tool you already use that you want to help improve, or perhaps its a project that you really want to see succeed, or it could be that some of your friends are working on something fun.

Your interests matter more than the popularity of the project, and your time is valuable. If you care about the problems that the project is solving, you’ll be more motivated to contribute and invest more of your time in the project.

Making ten contributions to a single project is much more valuable for

youthan making ten contributions to ten different projects.

And don’t worry if you don’t feel like you’re unqualified to contribute: you are.

## 2. Read the community guidelines

Before making your first contribution, look for the project’s community guidelines or code of conduct. You can usually find this type of document in the root of a project repository, named `CODE_OF_CONDUCT.md`

or similar.

A code of conduct should help you understand what you can expect from the community: how people treat each other, how conflict is handled, and what behaviour is encouraged or discouraged. A great example is the npmx code of conduct, outlining the community’s standards and the responsibilities of the project maintainers.

If your chosen project doesn’t have a code of conduct or community standards, you might consider skipping it. That being said, your first contribution **could** be to create these community standards from one of the many templates available. If you’re comfortable agreeing to the code of conduct for your chosen project, move on to the next step!

## 3. Browse closed pull requests

Take a look at some closed pull requests to help you understand more about the project culture and direction, and how maintainers and contributors work together. It will also give you an idea of how the community standards are being upheld. Some questions you can ask yourself:

What kind of work is being contributed?

Are reviews kind and constructive?

How are mistakes or incomplete work handled?

If the project is busy, how are multiple pull requests addressing the same issue handled?

What’s missing from contributions?


If you’re browsing a project on GitHub, you can find the closed PRs by navigating to the pull requests page, and filtering by closed.

## 4. Check the contributors list

Next, take a look at the contributors list. A healthy and active project often has:

Many contributors (not just one or two people doing everything)

Recent activity

A visible breadth of contributors


While you can’t conclude everything from avatars and usernames, immediate visual diversity can be a strong signal that the project is welcoming to all kinds of people. This, in my opinion, always makes for a more exciting project to get involved with. It's been really wholesome to see how many contributors have been working on npmx so far.

## 5. Explore open issues

Exploring open issues will help you get an idea of what needs to be worked on. Issues may be bugs, tasks, larger feature requests, or discussions about ideas that are not yet set in stone. Project maintainers will often use helpful issue labels to categorise issues based on skills or areas of the project. When you’re just starting out, it’s a good idea to look for issues with the label `good first issue`

, or you could filter issues by your area of expertise.

For example, when joining a new project, I often use the issue filter to surface good first issues, or issues labelled `front`

or `front end`

, `a11y`

or `accessibility`

, or `docs`

, as those are my areas of expertise. Another good label to look for is `help wanted`

, as this type of issue is usually more of a discussion around planning an approach to solving a problem.

For your first contribution, I recommend choosing a small, low-lift issue. A lot of the time investment when making your first contribution is taking time to understand the code or the documentation, learning the process of contributing, and ultimately, building relationships with other contributors and maintainers as you move through the process. Choosing a smaller issue means less cognitive overheads for you, and more opportunity to make a meaningful impact. For example, my first contribution to npmx was a pull request to fix the alignment of the logo in the header. This pull request fixed a very small issue that was reported by another contributor that allowed me to open my first pull request with minimal effort.

In a very active open source project, there may be multiple open pull requests that address the same issue. This could feel a little daunting at first (and it’s sometimes tricky for maintainers to manage), but it’s usually not a big deal and can be managed effectively. If you’re worried about this and don’t want to attempt something that is already in progress, GitHub helpfully identifies which issues have open PRs on the issues list with an icon, which I’ve highlighted on the image below.

## 6. Read the contributing guide

When you’ve found an issue you’d like to make a contribution for, it’s time to understand how the process works. Well-maintained open source projects will have a contribution guide in the project, which you can usually find in the root of a project repository, named `CONTRIBUTING.md`

. A contributing guide is usually geared towards contributing to code or documentation, and will include instructions on how to set up the project, maintaining a consistent code style, testing, and how to format your pull requests.

If you get stuck or notice something confusing or outdated whilst you’re trying to set up the project, you may have found your first opportunity for a contribution! In fact, when setting up the npmx project, I wasn’t sure how the code formatting worked because it wasn’t clear in the contributing guide. And so, after discussing with other maintainers, I opened a pull request to clarify how code is formatted.

## 7. Chat with the community

Many projects have a Discord, Slack, or other space for chatting with the community, which will usually be linked somewhere in the project repository or in the project itself. If you want help or just want to chat about the project and what issues would be good to tackle, it’s a great idea to join one of those spaces. It’s also a good opportunity to check that the community standards are being upheld and that you feel welcomed by the maintainers and contributors when you join.

Also, don’t feel like you need to jump in and get involved straight away. It can be daunting to jump into an active chat stream of people who are actively working on a project. Take your time, and do a little lurking until you feel comfortable enough to take part.

## 8. Open a pull request

If you’ve found an open issue and you know how to tackle it, you can usually do the work and open a pull request without asking for it to be assigned to you. That being said, in a very active project it is always helpful to leave a comment on an issue stating that you intend to work on it.

Communication in open source is key, especially with many people working asynchronously on a project across multiple time zones, day and night. But on the other hand, a very active project can feel very noisy and overwhelming, and more often than not, maintainers will appreciate your initiative when it comes to direct contributions, rather than the extra admin of assigning people to issues, and the extra time it takes for contributors to wait for permission.

To open a code-based pull request, fork the repository to your own GitHub account using the fork button on the main page of the repository, and clone your fork of the repository to your local machine.

When you've cloned the repository to your local machine, create a new branch off of main to make your changes. When you push those changes to your own GitHub fork, you'll see a banner at the top of your repository page with a "Compare & pull request" button.

Click this button to write a title and description for your PR, making sure to follow the contributing guidelines. Then, click "Create pull request". In an active project, you probably won't need to message the maintainers to notify them that you've submitted a PR, as they'll be watching for pull requests coming in. I know you're probably really excited to make your first contribution, but be patient in waiting for a review and approval!

## 9. Not every PR needs an issue

If you spot a typo, a small refactor, or an improvement worth making, you can propose it directly with a PR rather than creating an issue. Make sure to include a clear description of the change and why it’s useful, especially if it’s your first contribution. Even if your pull request is not accepted, you’ve practised the contribution workflow, so you’re ready for the next issue.

Even if someone else submits a similar PR before you, your work won’t be wasted. Maintainers may still merge your pull request, borrow ideas from it, or use it to improve the final solution. This happened to me on an early PR for npmx, where I made a small change to the Open Graph images for the package pages, which will eventually be superseded by a full redesign of the Open Graph images across the project.

## 10. Not every contribution has to be code

**In open source, all contributions are valuable,** whether or not they make it into the project codebase or documentation. Finding and reporting issues, requesting or suggesting features, reviewing and testing pull requests, opening PRs that don’t get merged, updating documentation, and welcoming people into the community are all valuable ways to get involved. Participating in open source projects gives you a wealth of opportunities to use your existing strengths, or learn new skills to add to your experience.

## Get involved

In my experience, open source really is about humans, rather than code. Open source projects have huge potential to bring people together and solve problems for the people that work on The Web, making the ecosystem (and, optimistically, the world) better for everyone to benefit.

If you’re looking for a great open source experience to get involved in, I would highly recommend the npmx project, who welcomed me with open arms from the outset. Find an open issue, give it a try, and join us in the npmx Discord to experience a truly wholesome community approach to building great tools for The Web. Start small, and have fun!