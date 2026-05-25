# Recrawl failure report — Stage 1–2

- **total objects:** 770
- **extracted OK:** 692  (89%)
- **failed:** 78

## Failures by recrawl strategy

| strategy | count | what to do |
|---|---|---|
| `render-retry` | 37 | Refetch with `wait_until=networkidle` + delay; else drop |
| `anti-bot` | 28 | Stealth/undetected browser retry; reader proxy if paywalled |
| `fetch-retry` | 11 | Longer timeout / JS retry |
| `rate-limited` | 1 | Slow down, retry later |
| `dead` | 1 | 404/410 — drop from corpus |

---

## `render-retry` — 37 (Fetched but extractor found no body → retry with wait_until=networkidle + delay_before_return, or it's a non-article page (drop))

### resumeworded.com (6)
- [extract-failed/200] https://resumeworded.com/director-of-software-engineering-cv-examples
- [extract-failed/200] https://resumeworded.com/director-of-software-engineering-resume-examples
- [extract-failed/200] https://resumeworded.com/engineering-director-resume-example
- [extract-failed/200] https://resumeworded.com/engineering-manager-resume-examples
- [extract-failed/200] https://resumeworded.com/entry-level-software-engineer-resume-example
- [extract-failed/200] https://resumeworded.com/lead-software-engineer-resume-example

### dev.to (6)
- [extract-failed/200] https://dev.to/report-abuse?billboard=239338
- [extract-failed/200] https://dev.to/report-abuse?billboard=238629
- [extract-failed/200] https://dev.to/report-abuse
- [extract-failed/200] https://dev.to/report-abuse?billboard=259985
- [extract-failed/200] https://dev.to/report-abuse?billboard=239387
- [extract-failed/200] https://dev.to/sonar

### kickresume.com (4)
- [extract-failed/200] https://www.kickresume.com/dashboard/create/chief-technology-officer/
- [extract-failed/200] https://www.kickresume.com/en/help-center/authors/milan-sarzik/
- [extract-failed/200] https://www.kickresume.com/dashboard/create/software-engineering-intern-piworks/
- [extract-failed/200] https://www.kickresume.com/en/help-center/authors/tomas-ondrejka/

### wozber.com (3)
- [extract-failed/200] https://www.wozber.com/en-gb/cv-templates/ats-friendly
- [extract-failed/200] https://www.wozber.com/en-gb/cv-examples/executive-and-management/chief-technology-officer-cv-example
- [extract-failed/200] https://www.wozber.com/en-gb/cv-examples/software-engineering/staff-software-engineer-cv-example

### app.enhancv.com (3)
- [extract-failed/200] https://app.enhancv.com/resume/new?amplitudeId=f9fba747-2e40-4ad0-afd8-2f5c72f0998f&example=predefined-PzfmGavoJ0SIcBgh2nMFpNGto0MMVTh98yg1dtJR
- [extract-failed/200] https://app.enhancv.com/resume/new?amplitudeId=3bc7b785-879e-4013-b662-247f90e151c4&example=predefined-P47aFWaUgrazXvUP5Enw0vr9POg0YQUERMY6HCca
- [extract-failed/200] https://app.enhancv.com/resume/new?amplitudeId=795dc11e-20a2-4e89-87a4-8b7f2b691b1e&example=predefined-37HpEyIQ1isPnbXW8dLg7ONCAfWiK4tqlApPAdAB

### skillcrush.com (2)
- [extract-failed/200] https://skillcrush.com/blog/10-job-titles-for-making-a-career-change-into-tech/
- [extract-failed/200] https://skillcrush.com/blog/optimize-your-github-profile-get-jobs/

### teamblind.com (2)
- [extract-failed/200] https://www.teamblind.com/post/Explain-a-2-year-career-break-LEkftARP
- [extract-failed/200] https://www.teamblind.com/post/First-Time-Negotiating-Advice-erFaSAQR

### help.resumeworded.com (1)
- [extract-failed/200] https://help.resumeworded.com/article/16-how-do-i-get-in-touch-with-you

### borderlesshr.com (1)
- [extract-failed/200] https://borderlesshr.com/blog/5-effective-ways-to-optimize-your-linkedin-profile-as-a-software-developer/

### word.cloud.microsoft (1)
- [extract-failed/200] https://word.cloud.microsoft/create/en/ats-templates/

### algomaster.io (1)
- [extract-failed/200] https://algomaster.io/learn/git/collaboration-workflows

### gothired.ai (1)
- [extract-failed/200] https://www.gothired.ai/blog/cover-letter-underqualified-role

### sproutern.com (1)
- [extract-failed/200] https://www.sproutern.com/resources/github-profile

### zety.com (1)
- [extract-failed/200] https://zety.com/about/hanna-woloszyn

### karangupta.com (1)
- [extract-failed/200] https://www.karangupta.com/blog/how-to-build-a-github-portfolio-that-gets-you-hired-guide-for-indian-cs-students

### lockedinai.com (1)
- [extract-failed/200] https://www.lockedinai.com/blog/linkedin-profile-optimization-get-5x-more-recruiter-views

### scopetechnical.com (1)
- [extract-failed/200] https://scopetechnical.com/recruiting-blog/f/software-engineer-resume-guide-tips-for-entry-to-mid-career?blogcategory=Job+Seekers

### resumegemini.com (1)
- [extract-failed/200] https://www.resumegemini.com/

---

## `anti-bot` — 28 (Blocked → retry with stealth UA / undetected browser; if paywalled, try a reader proxy)

### indeed.com (16)
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/career-break-resume-samples
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/career-change-resume-example
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/chief-technology-officer-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/cover-letter-for-returning-to-workforce
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/distribution-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/employment-gaps-on-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/engineer-manager-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/entry-level-engineer-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/listing-accomplishments-on-your-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/principal-engineer-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/remote-work-resume-sample
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/software-engineering-resume-keywords
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/staff-engineer-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/tech-executive-resume
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/transferable-skills
- [fetch-failed/403] https://www.indeed.com/career-advice/resumes-cover-letters/vp-engineering-resume

### resumeworded.com (5)
- [fetch-failed/403] https://resumeworded.com/skills-and-keywords/engineering-skills-group
- [fetch-failed/403] https://resumeworded.com/senior-software-engineer-resume-example
- [fetch-failed/403] https://resumeworded.com/software-developer-resume-examples
- [fetch-failed/403] https://resumeworded.com/software-engineering-lead-resume-example
- [fetch-failed/403] https://resumeworded.com/skills-and-keywords/vice-president-of-engineering-skills

### workplace.stackexchange.com (4)
- [fetch-failed/403] https://workplace.stackexchange.com/questions/183365/is-there-a-point-where-you-can-list-open-source-work-as-experience-on-your-res
- [fetch-failed/403] https://workplace.stackexchange.com/questions/143735/resume-how-to-quantify-my-contributions-as-a-software-engineer
- [fetch-failed/403] https://workplace.stackexchange.com/questions/127152/should-i-mention-that-i-am-underqualified-in-my-cover-letter
- [fetch-failed/403] https://workplace.stackexchange.com/questions/85653/writing-resume-job-description-vs-achievements-in-a-software-developers-resume

### kodeco.com (1)
- [fetch-failed/403] https://www.kodeco.com/36875585-how-to-write-the-perfect-resume-after-graduating-a-coding-bootcamp

### aarp.org (1)
- [fetch-failed/403] https://www.aarp.org/work/job-search/resume-employment-gaps/

### softwareengineering.stackexchange.com (1)
- [fetch-failed/403] https://softwareengineering.stackexchange.com/questions/79730/what-should-a-self-taught-no-experience-programmers-resume-look-like

---

## `fetch-retry` — 11 (No HTML after retries → timeout/JS; retry with longer page_timeout, or site needs JS interaction)

### indeed.com (1)
- [fetch-failed/307] https://www.indeed.com/career-advice/resumes-cover-letters/automated-screening-resume

### ivyexec.com (1)
- [fetch-failed/200] https://ivyexec.com/career-advice/2026/crafting-an-executive-resume-that-grabs-recruiters-attention

### stackoverflow.com (1)
- [fetch-failed/307] https://stackoverflow.com/questions/2428722/git-branch-strategy-for-small-dev-team

### pon.harvard.edu (1)
- [fetch-failed/200] https://www.pon.harvard.edu/daily/salary-negotiations/how-to-negotiate-a-higher-salary-after-a-job-offer/

### deployhq.com (1)
- [fetch-failed/0] https://www.deployhq.com/blog/how-to-use-git-with-claude-code-understanding-the-co-authored-by-attribution

### workplace.stackexchange.com (1)
- [fetch-failed/307] https://workplace.stackexchange.com/questions/102818/i-am-writing-the-following-letter-to-counter-a-job-offer-here-is-my-reasoning

### careerproguider.com (1)
- [fetch-failed/307] https://careerproguider.com/linkedIn-profile-optimization

### resumeworded.com (1)
- [fetch-failed/307] https://resumeworded.com/senior-software-developer-resume-example

### old.dlg.org (1)
- [fetch-failed/0] https://old.dlg.org/lead-digest/showcase-your-skills-github-projects-for-your-resume-1767647381

### softwareengineering.stackexchange.com (1)
- [fetch-failed/307] https://softwareengineering.stackexchange.com/questions/117775/tailoring-your-resume-for-a-career-switch-within-programming

### himalayas.app (1)
- [fetch-failed/307] https://himalayas.app/resumes/technical-lead

---

## `rate-limited` — 1 (429 → slow down, retry later with longer per-domain delay)

### news.ycombinator.com (1)
- [fetch-failed/429] https://news.ycombinator.com/item?id=43596864

---

## `dead` — 1 (Dead link (404/410) → drop from corpus)

### linkedinrank.com (1)
- [fetch-failed/404] https://linkedinrank.com/linkedin-headline-software-engineers

---
