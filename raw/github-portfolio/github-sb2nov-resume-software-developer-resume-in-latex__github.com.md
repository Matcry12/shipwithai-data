---
source_url: "https://github.com/sb2nov/resume"
source_domain: "github.com"
topic: "github-portfolio"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-25T06:39:28.642734+00:00"
word_count: 142
stage: "raw-extracted"
---

A single-page, one-column resume for software developers. It uses the base latex templates and fonts to provide ease of use and installation when trying to update the resume. The different sections are clearly documented and custom commands are used to provide consistent formatting. The three main sections in the resume are education, experience, and projects.

I created this template as managing a resume on Google Docs was hard and changing any formatting was too difficult since it had to be applied in multiple places.

Most currently available templates either focus on two columns, or are multiple pages long that didn't work well for career fairs or online applications.

Get started quickly using Overleaf template.

```
docker build -t latex .
docker run --rm -i -v "$PWD":/data latex pdflatex sourabh_bajaj_resume.tex
```

Format is MIT but all the data is owned by Sourabh Bajaj.