---
title: 'GitHub - sb2nov/resume: Software developer resume in Latex'
source_url: https://github.com/sb2nov/resume
source_domain: github.com
topic: github-portfolio
author: Sb
published_date: '2015-10-11'
fetched_at: '2026-05-25T06:39:28.642734+00:00'
language: en
word_count: 151
reading_time: 1
signal_score: 0.6258
status: quarantined
content_hash: sha256:f4ea56a71cd2fb383dc23fe38884bb5d11594ed89927a742e441b1b6d95f6e74
---

# GitHub - sb2nov/resume: Software developer resume in Latex

A single-page, one-column resume for software developers. It uses the base latex templates and fonts to provide ease of use and installation when trying to update the resume. The different sections are clearly documented and custom commands are used to provide consistent formatting. The three main sections in the resume are education, experience, and projects.

I created this template as managing a resume on Google Docs was hard and changing any formatting was too difficult since it had to be applied in multiple places.

Most currently available templates either focus on two columns, or are multiple pages long that didn't work well for career fairs or online applications.

Get started quickly using Overleaf template.

```
docker build -t latex .
docker run --rm -i -v "$PWD":/data latex pdflatex sourabh_bajaj_resume.tex
```

Format is MIT but all the data is owned by Sourabh Bajaj.
