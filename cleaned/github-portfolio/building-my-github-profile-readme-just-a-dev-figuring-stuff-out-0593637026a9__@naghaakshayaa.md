---
title: "Building Your GitHub Profile README Portfolio"
topic: "github-portfolio"
career_level:
  - entry
source_url: "https://medium.com/@naghaakshayaa/building-my-github-profile-readme-just-a-dev-figuring-stuff-out-0593637026a9"
source_domain: "medium.com"
word_count: 968
text_to_link_ratio: 0.7945
signal_score: 0.7945
is_curated: false
tags:
  - open-source
  - linkedin
ingested_at: "2026-05-05"
---


### Introduction

Hey folks, I'm Nagha Akshayaa and this is my very first blog post — *cue applause*! 🎉

I finished my B.Tech. in 2024 and started working as a Software Engineer — but honestly, I never really understood how useful GitHub could be in my college. And I know I'm not alone.

Back in my third year, during placement season in 2023, I quickly filled out my GitHub profile with whatever the form asked. That was it. Nothing special. But recently, I felt like it deserved more. After all, GitHub sticks with us — it showcases our projects, tracks our progress, and becomes a kind of portfolio.

So I decided to finally give it some love.

I started digging into blogs and examples that inspired me to build something of my own. I didn't know where to start (still kinda don't 😅), but I knew I didn't want just a list of repos. I wanted a little space that said:
**"Hey, this is me. This is what I do. And here's what I'm learning."**

### Lets get Started

There's no shortage of cool ideas out there, but I wanted to keep it simple and reflect only what I've done so far. Nothing flashy — just honest and clean.

👉 **See mine**: [My GitHub Profile](https://github.com/NAGHA-AKSHAYAA)

To get started with your own:

* Create a **new repository** with the **exact same name as your GitHub username**.
  *(Example: if your username is* *`naghaakshyaa`**, your repo should also be* *`naghaakshyaa`**)** **Make sure to check the box that says** **`Add a README file`****.*** Also, **set the repo to public** — otherwise it won't show up on your profile.* Now if you go to your GitHub profile, it should show your new README section right at the top!

![None](https://miro.medium.com/v2/resize:fit:700/1*heajaZa7lykGQtwE41Ujuw.png)

Creating a repo for GitHub Profile

### How to Edit Your README

1. Go to your GitHub profile.- Click on the repo named after your username.- Inside it, open the `README.md` file.- Hit the ✏️ pencil icon to edit it.- Start typing in **Markdown**

### Let's Talk About the Fun Stuff You Can Add

So below are the usual items people add to their GitHub profile:

* **Bio** — Who you are, what you're studying or working on.* **Skills Badges** — Frontend, Backend, Tools (React, Node.js, AWS, etc.).* **Pinned Projects or Repositories** — Highlight your best work.* **Currently Learning** — New tech you're exploring.* **Blog/Medium/Twitter Links** — Links to your content or social media.* **Fun Stuff** — GitHub stats, visitor badges, quotes, or memes.* **Contact Information** — Email, LinkedIn, Twitter.* **Achievements/Certifications** — Key certifications or accomplishments.* **Contributions/Open Source Work** — Highlight your open-source contributions.* **Fun Fact** — Something quirky or unique about yourself.

### Start With a Cool Header

I made one using this awesome typing header generator:
👉 [readme-typing-svg.herokuapp.com](https://readme-typing-svg.herokuapp.com/demo/?font=Jetbrains+Mono&size=48&color=7432F7&center=true&vCenter=true&lines=Hello)

It gives your profile a chill animated vibe. Just add the image link in your markdown like this.

```
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Merriweather&size=48&duration=2500&pause=9999&color=7AE2CF&center=true&vCenter=true&width=1000&height=80&lines=R+Nagha+Akshayaa" alt="R Nagha Akshayaa" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Jetbrains+Mono&size=22&duration=2500&pause=250&color=077A7D&center=true&vCenter=true&width=1000&height=50&lines=Backend+Engineer;Building+Scalable+Systems;Innovating+with+AI-Powered+Automation" alt="Software Engineer" />
</p>
```

![None](https://miro.medium.com/v2/resize:fit:700/1*ivRZLY8UHLInQN8yV-SUtw.gif)

My Profile Header — <https://github.com/NAGHA-AKSHAYAA>

### Bio as Code (Yaml Style, Because Why Not?)

We aren't code, but formatting our bio like code looks *so* cool 😎
Just wrap it inside triple backticks and label it as `yaml`:

```
```yaml
name: Nagha Akshyaa
role: Software Engineer
education: BTech in Computer Science
currently_learning: FastAPI, Redis
```
```

![None](https://miro.medium.com/v2/resize:fit:700/1*ySotwnI9_GuwqamBcIo18Q.png)

### GitHub Stats (if they're flex-worthy 😅)

This tool shows all your stats: contributions, streaks, most used languages, etc.
Link: [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats)

```
![Nagha's GitHub stats](https://github-readme-stats.vercel.app/api?username=naghaakshyaa&show_icons=true&theme=radical)
```

![None](https://miro.medium.com/v2/resize:fit:700/1*I0fs5tfHb9vA54jUg5EJ6Q.png)

Example for GitHub Stats

### Skills and Badges

Badges are super helpful to give people a quick look at your stack.
I used [Shields.io](https://shields.io/) + this amazing repo by [@kimjisub](https://gist.github.com/kimjisub/360ea6fc43b82baaf7193175fd12d2f7) to pick literally every icon you need.

```
<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
<img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
```

And the same works for contact info too!

```
<a href="https://linkedin.com/in/naghaakshyaa">
  <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin" />
</a>
<a href="mailto:nagha@example.com">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>
```

![None](https://miro.medium.com/v2/resize:fit:700/1*hIFihVsHrg0fYktZmqiRWw.png)

### **Customize It Your Way**

All the lines of code you see — whether it's for banners, shields, or widgets — are **totally customizable**. You can tweak the font, size, color, alignment, text, links… basically everything to match your vibe ✨

Here's a quick example using the **typing banner**:

```
![Name banner](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=FF61A6&center=true&vCenter=true&width=435&lines=Hey+there!+I'm+Nagha+Akshyaa;Software+Engineer+%7C+Backend+Dev;Loves+APIs+%7C+FastAPI+%7C+Redis)
```

You can **change the text**, font, color codes (`color=FF61A6`), size, even the duration of typing — just play around with the URL parameters.

```
font=Fira+Code
size=22
duration=3000
pause=1000
color=FF61A6
center=true
width=435
```

Another example for LinkedIn Badge with Icon (all the attributes could be customised, read more from [Shields.io](https://shields.io/) )

```
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)
Background Colour = 00557 (customisable with any colour)
logoColour = While  (customisable with any colour)
logo=linkedin (adds the LinkedIn icon)
style = flat
```

🔁 **And don't forget** — **replace all the links** (GitHub, LinkedIn, email, etc.) with **your own** so your profile.

### Tips

We all take inspiration from others, don't we? 😄
If you see a cool GitHub profile and wanna use the way someone else has done it — go for it! It's super simple:

1. Head to their GitHub profile.- Click on the repo (usually named the same as their username).- Open the `README.md` file.- Click on the "**Code**" button to view or copy the raw markdown.

![None](https://miro.medium.com/v2/resize:fit:700/1*95-hu6CVyHO54Lu-bh3HeA.png)

The **Preview** tab to see how it *looks,* the **Code** tab to see the *markdown* used to build it

Here's mine as an example, click it and you will see the buttons like the above on the top left corner:
👉 [naghaakshyaa/README.md](https://github.com/NAGHA-AKSHAYAA/NAGHA-AKSHAYAA/blob/main/README.md)

Peek in, get ideas, tweak your own — we're all just figuring it out as we go 🚀

And hey, if you're looking for a bunch of awesome profiles to take inspiration from (without going on a GitHub scavenger hunt), this site has got you covered:

👉 **[Awesome GitHub Profiles — zzetao.github.io](https://zzetao.github.io/awesome-github-profile/)**

### Conclusion

Since this is my **first ever blog**, I'm super excited that I now have a *Blog* section to proudly add to my GitHub profile — yipee 🥳

If you have any suggestions, tips, or just wanna say hi, feel free to reach out!
I'm always happy to help ❤️

📧 **Email**: naghaakshayaa@gmail.com
🔗 **LinkedIn**: [Nagha Akshayaa](https://www.linkedin.com/in/nagha-akshayaa/)
