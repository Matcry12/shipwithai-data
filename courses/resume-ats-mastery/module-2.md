# Module 2 — Resume Structure That Passes

**Objective:** Build a resume the parser reads cleanly the first time.

---

## Lesson 1 — The Six Sections Every Tech Resume Needs, in Order

The ATS does not read your resume the way a human does. It navigates by section. If a section is missing or mislabeled, the parser either skips it or misfiles the content inside — and that data is gone before a recruiter ever sees your name.

For a software engineer resume, the correct order is: **Header → Professional Summary (or Objective) → Technical Skills → Professional Experience → Projects → Education**.[^1]

Each section earns its place:

- **Header:** Your name, professional email, phone number, LinkedIn URL, and GitHub URL. City and state only — no full street address. Keep it in the body of the document, never in a Word header or footer, because many ATS parsers skip header and footer regions entirely.[^2]
- **Professional Summary / Objective:** If you have work experience, write a 2–3 sentence summary that names your role, top skills, and one concrete achievement. If you are a bootcamp grad or career-changer with no direct experience, use an objective statement that names transferable skills and what you are targeting.[^1]
- **Technical Skills:** Group by category — Languages, Frameworks, Cloud & DevOps, Databases. This structure helps the ATS match your skills to job description keywords and lets a recruiter scan your stack in two seconds.[^1]
- **Professional Experience:** Reverse-chronological, achievement-focused bullets. This is covered in depth in Module 3.
- **Projects:** Critical for juniors and career-changers. Link to GitHub repos or live demos. This section is your proof of skill when your work history is thin.
- **Education:** Degree, major, school, graduation year. If you are self-taught, list relevant certifications here.

Less than ten years of experience? Keep it to one page. That constraint forces focus and matches recruiter expectations during a 6–8 second first pass.[^1]

**Action:** List your current resume sections on paper and compare them to the six above. Note any that are missing, out of order, or use different names.

---

## Lesson 2 — The Formatting Rules That Make the Parser Happy

Design choices that look clean to a human eye can destroy your resume in an ATS. The parser reads left to right, top to bottom, as plain text. Anything that breaks that flow — a table, a text box, a two-column layout, a graphic — gets garbled or dropped.

The rules are not suggestions. Apply them all.

**Layout:** Single-column only. Two-column layouts cause content to get read out of sequence. The parser will interleave your skills column with your experience column and produce nonsense.[^3]

**Fonts:** Arial, Calibri, Cambria, Garamond, Georgia, Helvetica, or Times New Roman. Font size 10–12pt for body text. These are the fonts ATS software is trained to parse. Decorative, script, or custom fonts may not render at all.[^3]

**Margins:** 0.5–1 inch on all sides. Tighter than 0.5 inches and some parsers clip content.[^3]

**Avoid completely:** tables, text boxes, columns, graphics, images, icons, logos, headers, and footers. These elements are visually appealing to humans but are either invisible or read as garbage by ATS software.[^4]

**Dates:** Use a consistent format throughout — "January 2022" or "01/2022", never "Jan '22" one place and "2022" another. Inconsistent date formats prevent the ATS from calculating your total years of experience, which is used to auto-filter candidates.[^3]

**File format:** Submit .docx as the default safe choice. If you use PDF, it must be a text-based PDF — not a scan, not an export from Canva or InDesign. Test it by opening the PDF and trying to select text. If you cannot highlight a word, the ATS sees a blank page.[^3]

**Quick test:** Paste your resume into a plain-text editor like Notepad. If the sections are out of order, columns have merged, or contact info has disappeared, the ATS is reading the same mess. Fix the source document before you apply anywhere.[^1]

**Action:** Open your resume, remove every table, text box, and graphic, convert it to single-column, and save a copy as .docx.

---

## Lesson 3 — Standard Headers and Why Creative Labels Get You Rejected

The ATS is trained on hundreds of thousands of resumes. It recognizes "Work Experience," "Education," and "Skills" instantly. It does not recognize "My Journey," "Where I've Made an Impact," "Toolkit," or "What I Bring to the Table." When it cannot identify a section heading, it either skips that section or dumps its contents in the wrong bucket.[^5]

The safe headers for each section:

| Section | Use This | Not This |
|---|---|---|
| Contact | Contact Information | "Reach Me At" |
| Summary | Professional Summary | "About Me", "My Story" |
| Experience | Work Experience | "Career Journey", "Where I've Worked" |
| Education | Education | "Learning", "Alma Mater" |
| Skills | Skills / Technical Skills | "Toolbox", "Stack", "What I Know" |
| Certifications | Certifications | "Badges", "Credentials" |

[^5]

The rule is blunt: use the same label that a hundred other resumes use. The ATS is trained on common patterns, not creative ones.[^5]

One more placement rule that catches people: your contact information belongs in the main body of the document, not in a Word or Google Docs header element. ATS parsers frequently ignore document headers and footers entirely, which means your phone number and email vanish before the recruiter gets the file.[^2]

The same logic applies to your LinkedIn and GitHub URLs — they go in the body, in the Header section, as plain text. Not in a sidebar, not as icons, not in a footer.

**Action:** Rename every section in your resume to match the standard labels in the table above, and move your contact information out of any document header or footer into the body text.

---

*Next: Module 3 — Bullets That Signal Impact. You will learn to replace responsibility statements with quantified achievements using the action verb + what + how + result formula.*

## Sources

[^1]: blog.scale.jobs
[^2]: huntr.co
[^3]: uwork.org
[^4]: wahresume.com
[^5]: resumeadapter.com
