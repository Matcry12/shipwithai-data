---
title: "Creating my GitHub profile Readme.md"
topic: "github-portfolio"
career_level:
  - mid
source_url: "https://dev.to/farrahdlsdionisio/creating-my-github-profile-readmemd-3393"
source_domain: "dev.to"
word_count: 634
text_to_link_ratio: 0.9802
signal_score: 1.0
is_curated: false
tags:
  - GitHub README
  - profile customization
  - portfolio
  - markdown
  - developer branding
  - social widgets
ingested_at: "2026-05-25"
doc_type: "how-to-guide"
core_question: "How can developers create an impressive GitHub profile README?"
tldr: "Guide to building a professional GitHub profile README with sections for introduction, technologies, stats, social links, and resume."
---

# Creating my GitHub profile Readme.md

**Link of my profile: My GitHub Profile**

I am currently looking for a new organization to join. While doing so, I decided to build a stronger online presence as a software engineer. The first thing I'm going to improve is my GitHub profile. I drafted a plan in my notebook that includes six sections: a header, a quick introduction, a list of technologies I've used, GitHub stats, links to my social media accounts, and my resume for potential employers who will visit my profile.

The first section is the header, which I designed to be simple yet eye-catching using Figma.

After that, I researched some fun widgets to add to my profile. I found the profile views badges by Anton Komarev: GitHub Profile Views Counter

To apply it add this to your readme.md (change it to your username)

```
![](https://komarev.com/ghpvc/?username=yourusername&color=FF7A8A&style=for-the-badge)
```

or in my case I used it with **img** tag

```
<img align="left" src="https://komarev.com/ghpvc/?username=farrahdlsdionisio&color=FF7A8A&style=for-the-badge" alt="Profile Views" style="max-width: 49%;"/>
```

I love listening to music while working, as I was searching for a cool GitHub profile I stumbled upon a widget where you can show what's currently playing on your Spotify so I decided to use it as well. I got it from here: Spotify GitHub Profile

To apply it to your readme.md, go to the link that I provided, connect your Spotify and grant permission

You'll be redirected to where you can choose your theme, change the color of the player, etc. Click copy to clipboard and apply it to your readme.md

I applied mine as an **img** tag because I want a specific format between the profile views and Spotify widget

```
<section style="width: 100%; display: flex;">
<img align="left" src="https://komarev.com/ghpvc/?username=farrahdlsdionisio&color=FF7A8A&style=for-the-badge" alt="Profile Views" style="max-width: 49%;"/>
<img align="right" src="https://spotify-github-profile.kittinanx.com/api/view?uid=*******&cover_image=true&theme=novatorem&show_offline=false&background_color=6f87be&interchange=false&bar_color=ff7a8a&bar_color_cover=false" alt="Spotify Profile" style="max-width: 49%;"/>
<section>
```

Result is as follows:

The next section of my profile is a short introduction about me, I used the default template given by GitHub but you can be more creative with this, anything that will showcase yourself as a developer

After the introduction, I showcased the technologies that I am using, I simply added logos of them:

The next section displays my GitHub data. I found this widget from Anurag Hazra that pulls your total stars earned, total commits(current year), total PRs, total issues, and contributed to(last year). You can check it here: Github Stats Go check the documentation as it offers a lot of customization for your needs. For me, I just used the default view and changed the theme.

To apply it to your readme you can do it as follows (change it to your username):

```
<p align="center"> <img src="https://github-readme-stats.vercel.app/api?username=yourusername&theme=prussian&show_icons=true" alt="yourusername" /></p>
```

In the next section, I added my social media links where people can follow me, I tried using HTML's **a** tag because I wanted to use the target attribute with the value of "_blank" to open another tab when you click it but apparently GitHub's limited markdown syntax doesn't allow it so I used markdown's link syntax instead.

Lastly, as my target audience for my github profile is not just the developer community but potential employers I added my resume. It's a simple link that redirects to my resume uploaded on my Google Drive.

I also added this GIF as the footer that I got from Giphy which I believe to be from a scene in a Studio Ghibli film.

As I add more personal projects, contribute to open-source, and learn new technologies, I'll update my GitHub profile accordingly.

I wrote this article to contribute to the developer community and to help software engineers who are looking to start their personal brand and build their online presence. GitHub, as a well-known repository hosting service with a vast open-source community, is an excellent platform to showcase our skills.\
