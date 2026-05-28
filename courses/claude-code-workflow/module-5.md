# Module 5 — Putting Claude Code on Your Resume

AI-assisted development is now table stakes in tech hiring. But knowing how to represent that skill is not obvious. Most developers either undersell it ("familiar with AI tools") or oversell it in ways that make hiring managers uncomfortable ("built entire platform with AI"). This module is about the narrow corridor between those two mistakes.

---

## Lesson 1 — From Generic to Specific: Writing Resume Bullets That Signal Judgment

The phrase "familiar with AI coding assistants" appears on thousands of resumes. It communicates nothing about what you can do, the scale you operated at, or what decisions you made. It is not a hiring signal — it is noise.

What reads as a hiring signal is specificity. Consider the difference between these two lines:

- *Familiar with AI coding tools to accelerate development.*
- *Refactored 4,000-line Python service to async using Claude Code, reduced p95 latency 35%.*

The second line does three things the first cannot: it names a concrete task, it quantifies the outcome, and it positions you as the engineer making the call — with the tool as the instrument.

This matches what strong technical resume writing actually requires. The formula that works is: **[Action] + [Technology] + [Scale/Scope] + [Result]**. As one resume guide puts it, "technical resume bullets must quantify engineering impact using a precise action-technology-result formula" and "effective bullets combine specific technologies, concrete actions, and numeric improvements that immediately capture a recruiter's attention"[^1]. The same pattern applies when Claude Code is the technology in your stack: the action is yours, the scale is real, and the result is measured.

The AI assistant is the multiplier, not the headline. You led the migration. You caught the edge case. You reviewed the output and pushed back when it was wrong. The bullet should make that clear.

**How to build your bullet:**

1. Identify a task where Claude Code materially changed how you worked — not just that you used it, but that it changed the scope or speed of what you shipped.
2. Anchor the bullet to your decision-making: what did you delegate, what did you verify, what did you change before merging?
3. Attach a number. Latency, test coverage, deployment frequency, hours saved, lines of legacy code removed. If you cannot find a number, the task may not be specific enough.

**Action:** Write two resume bullets for work you have done in the last six months where Claude Code played a role. Use the formula above. If you cannot get to a measurable result, work backward — what would you have had to measure to know it worked? That is the number you need.

---

## Lesson 2 — Interview Prep: What Hiring Managers Actually Want to Hear

A resume gets you the interview. What happens in that conversation determines the offer.

Hiring managers at engineering-forward companies are not impressed by AI use on its own. They care about your judgment. The implicit question behind every AI-related interview question is: *do you understand what the tool can and cannot do, and do you know when to override it?*

Research on how developers actually use AI coding assistants is revealing here. Studies found that "participants in our study voiced concerns that over-reliance on AI could erode debugging proficiency among junior engineers or weaken collective ownership of code"[^2]. Experienced interviewers know this dynamic. They want to see that you are not in the over-reliance category.

Separately, Anthropic's own research found that "the largest gap in scores between the two groups was on debugging questions, suggesting that the ability to understand when code is incorrect and why it fails may be a particular area of concern if AI impedes coding development"[^3]. Interviewers who have read anything like this will probe your debugging ability — not to trick you, but to verify that your AI use has not become a crutch.

What to prepare:

**The delegation story.** Pick one instance where you handed a task to Claude Code. Be ready to describe: what you asked for, what it produced, what you checked, and what you changed before it shipped. Specifics matter — "I reviewed the generated migration script and caught an index that would have locked the users table during peak traffic" is a very different answer than "I checked the output."

**The catch story.** Pick one instance where the output was wrong, incomplete, or subtly off in a way a non-expert would have missed. What was the error? How did you find it? What would have happened if you had shipped it? This is the story that separates engineers who use AI from engineers who use AI well.

**The limits story.** Be ready to name the class of tasks where you do not reach for Claude Code. There should be one. Security-sensitive credential handling, deeply context-dependent architectural decisions, anything touching production infra that needs to be fully understood before executing — these are reasonable examples.

As one interview preparation resource notes, "interviewers want to understand how you think, so explain your thought process and decision making throughout the interview. Remember they are not only evaluating your technical ability, but also how you solve problems"[^4]. That principle applies directly to AI tool discussions. The output is not the point. Your reasoning process is.

**Action:** Write out answers to these three questions as if you were in a 90-second interview answer: (1) Describe a time you delegated to Claude Code and then verified the result. (2) Describe a time the AI output was wrong and how you caught it. (3) What tasks do you explicitly not use AI assistance for, and why?

---

## Lesson 3 — LinkedIn: Visibility Without Overselling

LinkedIn operates on a different signal economy than a resume. A resume is read once, in private, by someone already evaluating you. LinkedIn is scanned repeatedly, in public, by people who have not decided yet whether to care. The goal is to make your AI-assisted work legible without making it the only thing visible.

The most durable signal on LinkedIn is a pinned project. If you have shipped something where Claude Code was a genuine part of the workflow, make it visible: a GitHub repo with a commit history that shows iterative AI-assisted development, a README that mentions the tooling you used and what decisions you still made yourself, a post or project description that frames the outcome before the method.

The key word is "genuine." Recruiters and hiring managers are becoming fluent in AI-assisted work. The tell of overselling is when the AI gets the agency: "I used Claude Code to build X" is weaker than "I built X, using Claude Code to accelerate the async refactor and migration testing." One positions you as a passenger; the other positions you as the driver with better tools.

The principle here mirrors how executive communication works with AI tools: "use AI for speed. Use your judgment for substance"[^5]. Your LinkedIn presence should reflect the judgment, not just the speed.

Practical signals that work without sounding like a marketing pitch:

- A project with a visible commit history where you have commit messages that show review and revision of AI output, not just acceptance of it.
- An About section that lists Claude Code alongside your other tools — not in a dedicated "AI Skills" subsection, but as part of the natural flow of your technical stack.
- A post or article describing a specific technical problem you solved, with an honest account of where AI assistance helped and where you had to correct it. Posts with specific failure modes and recoveries read as credible. Posts that describe seamless AI-generated success do not.

What to avoid: a standalone "AI Tools" skills section that lists six assistants with no context. This reads the same way "proficient in Microsoft Office" read in 2005. It is the absence of specificity, not its presence, that marks the listing as filler.

**Action:** Audit your LinkedIn profile for two things: (1) Is there a pinned project that shows a real outcome where AI tooling was part of the work? If not, identify one project that qualifies and draft a three-sentence description. (2) Does your About section or experience bullets include any AI tool mention that is not backed by a concrete task? If so, replace it with a specific line using the formula from Lesson 1.

---

## Module Summary

Generic AI mentions on a resume are noise; specific bullets that follow the action-technology-scale-result formula are hire signals. In interviews, the question behind every AI question is whether you can describe what you delegated, what went wrong, and what you did to catch it — hiring managers are testing judgment, not tool familiarity. On LinkedIn, pin real work with honest framing: the AI was a multiplier, you were the engineer making the calls, and your profile should make both of those things visible.

## Sources

[^1]: resumegeni.com
[^2]: arxiv.org
[^3]: anthropic.com
[^4]: dev.to
[^5]: winningpresentations.com
