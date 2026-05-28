# Module 2 — The Profile README That Sells

**Objective:** Build the one-page pitch at the top of your profile.

---

## Lesson 1: How the Profile README Works (and Why It Matters)

Before you write a single word, understand the mechanism. The profile README lives in a special repository named exactly after your GitHub username. GitHub displays your profile README on your profile page if the repository is public and contains a `README.md` file in its root[^1]. That file renders above your contribution graph and pinned repositories — it is literally the first thing a recruiter sees when they land on your profile.

This placement makes the README unusually powerful. Unlike a resume that a screener opens in a separate tab, the README is inline. It cannot be skipped. Boot.dev puts it plainly: "It's a great opportunity to write a slightly more detailed bio with additional links to things like your resume, LinkedIn profile, top projects, etc."[^2] You have maybe five seconds of attention before a recruiter scrolls. That five seconds is your entire pitch.

The README also functions as a consistency anchor. Whatever role title appears in your resume summary — "Senior Backend Engineer," "ML Engineer," "Full-Stack Developer" — that exact phrase should open your README hook line. Recruiters cross-reference. If your resume says "Senior Backend Engineer" and your GitHub bio says "I build stuff," you look careless. Resume.io frames the README as "a cover letter for your GitHub profile"[^3] — and like a cover letter, it must speak the same language as the document it accompanies.

**Action:** Go to `github.com/new` and create a public repository named exactly your GitHub username. Toggle "Add a README file" to on, then click Create repository. You now have the canvas.

---

## Lesson 2: The Four-Block Structure

A profile README is not a personal essay. It is a structured sales page with four discrete blocks. Each block has one job. Write them in order and resist the urge to merge them.

**Block 1 — The Hook (2–3 lines)**

Open with a role-keyword sentence that mirrors your resume title. Then add one line of differentiation. Example: "Backend engineer focused on distributed systems at scale. I've reduced p99 latency by 40% across two production services." Socialprachar.com advises that the bio should tell people "what you do best" and "what you want next" — and that "a clear bio helps recruiters know who you are, what you can do, and what you want"[^4]. The hook is your bio, expanded by three sentences.

**Block 2 — The Stack (1 short paragraph or a tight list)**

Name the technologies that are relevant to the roles you are targeting. Not everything you have ever touched. Priygop.com's profile README guidance is to include "Tech stack with icons" alongside a "Brief introduction and current focus"[^5]. Icons are optional and can look clean, but the substance is the names themselves. If you are applying for Python backend roles, Python, FastAPI, PostgreSQL, Redis, and Docker belong here. Ruby from a side project three years ago does not.

**Block 3 — Highlights (1–3 projects, one line of value each)**

Link to one to three pinned repositories and describe each in a single sentence that states what problem it solves, not what technology it uses. The sentence "Event-driven order processor built with Kafka and Go" describes a technology. "Replaces a polling loop that caused 12-second checkout delays — handles 10k events/sec" describes value. Resume.io instructs: "Make it clear why each project is one to pay attention to by including detailed descriptions and explanations" that cover the project's purpose and "what problem it solves"[^3]. One line of value per project. No more.

**Block 4 — Contact**

Close with a single line: preferred email, LinkedIn URL, and optionally a portfolio site. Keep it scannable. Socialprachar.com lists this directly in the must-haves: "Show your skills and say how people can get in touch with you"[^4].

**Action:** Draft each of the four blocks as plain text in a scratch document before touching markdown. Check that the hook line contains the exact role keyword from your resume. Then paste the four blocks into your README.md, format with markdown, and commit.

---

## Lesson 3: What to Strip Out

Most profile READMEs fail not because they are missing content, but because they are buried under noise. Here are the four categories of content that actively hurt you.

**Badge spam.** There is an entire ecosystem of automated badges — visitor counters, streak stats, trophy widgets, WakaTime metrics[^6]. A recruiter who opens your profile to assess your backend engineering skills and finds a trophy cabinet is not impressed. They are confused. One or two unobtrusive stats are tolerable. Eight badges stacked in a header is clutter that delays them reaching your projects.

**ASCII art and animated headers.** These signal effort put in the wrong direction. A recruiter evaluating you for a production engineering role does not need to watch a typing animation. The dev.to post on building a profile README notes that the author planned "six sections: a header, a quick introduction, a list of technologies" and deliberately kept the header "simple yet eye-catching"[^7] — and that was a developer writing for their own community. For a recruiter audience, simpler still is better.

**Framework dumps.** Listing every language and framework you have ever installed communicates nothing. Revolentgroup.com points out that you have "160 characters" in the bio to write "an optimized and informative introduction"[^8]. The same discipline applies to the README stack section. If everything is highlighted, nothing is. Cvwizard.com is direct: "If a project doesn't relate to the job description, remove it."[^9] The same editing logic applies to your stack list.

**"Languages I dabble in" lists.** If you are not ready to interview on it tomorrow, it should not be in the stack block. Dabble lists invite questions you cannot answer confidently and create inconsistency with your resume. Priygop.com flags "Technology relevance — Modern frameworks and tools for your target role" as a primary recruiter signal, and lists "abandoned projects" and "copied code" as red flags[^5]. A dabble list is the skills equivalent of an abandoned project.

The test: read your finished README as if you are a recruiter who has thirty seconds and is specifically hiring for the role on your resume. Does every sentence either qualify you or tell them how to reach you? Cut anything that doesn't.

**Action:** After completing your four blocks, do a deletion pass. Remove every badge, widget, or stat that does not directly support the role you are targeting. Remove every technology from your stack that you would not want an interviewer to ask you about. Count the remaining lines. If the README is still longer than 25–30 lines of rendered content, it will push your pinned repos off the visible screen — boot.dev warns explicitly: "keep the Readme fairly short because it will push your pinned repositories down the page, and that's really where you want to keep your reader's attention"[^2].

---

## Module Summary

The profile README is a public, always-on cover letter that loads before anything else on your GitHub profile. It works because of a single mechanic: a public repository named after your username renders its `README.md` inline on your profile page, above the contribution graph. Build it in four blocks — hook, stack, highlights, contact — and make the hook line mirror the role keyword on your resume exactly. Strip badge spam, animated headers, framework dumps, and dabble lists. Keep it short enough that pinned repositories remain visible without scrolling. A recruiter reading your resume and then landing on your GitHub should see the same person described in the same words; that consistency signals intentionality, and intentionality is what separates candidates who look hireable from candidates who look like they just signed up for GitHub.

---

**Citation Index**

| Domain | Query that surfaced it | Quoted sentence used |
|---|---|---|
| docs.github.com | "github username repo readme" | "GitHub will display your profile README on your profile page if all of the following are true... You've created a repository with a name that matches your GitHub username." |
| boot.dev | "github username repo readme" | "It's a great opportunity to write a slightly more detailed bio with additional links to things like your resume, LinkedIn profile, top projects, etc." / "keep the Readme fairly short because it will push your pinned repositories down the page." |
| resume.io | "github profile readme structure" | "You can think of this as a cover letter for your GitHub profile." / "Make it clear why each project is one to pay attention to... A concise explanation of the project's purpose and what problem it solves." |
| socialprachar.com | "github bio recruiters tech" | "A clear bio helps recruiters know who you are, what you can do, and what you want." / "Show your skills and say how people can get in touch with you." |
| priygop.com | "github profile readme structure" | "Tech stack with icons / Featured projects with links / Contact information." / "Technology relevance — Modern frameworks and tools for your target role." |
| revolentgroup.com | "github bio recruiters tech" | "Make the most of the allotted 160 characters to write an optimized and informative introduction." |
| cvwizard.com | "github profile readme structure" | "If a project doesn't relate to the job description, remove it." |
| dev.to | "github profile sections" | "I drafted a plan in my notebook that includes six sections: a header, a quick introduction, a list of technologies I've used..." |
| github.com | "github profile readme" | (awesome-github-profile-readme — cited as the source ecosystem for badge/widget tooling described in the badge spam section) |

## Sources

[^1]: docs.github.com
[^2]: boot.dev
[^3]: resume.io
[^4]: socialprachar.com
[^5]: priygop.com
[^6]: github.com
[^7]: dev.to
[^8]: revolentgroup.com
[^9]: cvwizard.com
