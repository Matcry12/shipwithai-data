---
title: "react-ultimate-resume by WeLoveDevs.com"
topic: "github-portfolio"
career_level:
  - entry
source_url: "https://github.com/welovedevs/react-ultimate-resume"
source_domain: "github.com"
word_count: 1077
text_to_link_ratio: 0.6588
signal_score: 0.6588
is_curated: false
tags:
  - remote
  - open-source
ingested_at: "2026-05-05"
---

# react-ultimate-resume by WeLoveDevs.com
[![npm \(scoped\)](https://camo.githubusercontent.com/3a8cfd1885e5b78e41dbe47d6fb7078609b98317720a295b18af38567684153f/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f4077656c6f7665646576732f72656163742d756c74696d6174652d726573756d653f636f6c6f723d253233323230444144)](https://www.npmjs.com/package/@welovedevs/react-ultimate-resume) [![npm](https://camo.githubusercontent.com/0e904f69c507f5bb9bf5483be08c7642a3ae003058b2d501871ee2cd648529c5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f4077656c6f7665646576732f72656163742d756c74696d6174652d726573756d653f636f6c6f723d253233323230444144)](https://www.npmjs.com/package/@welovedevs/react-ultimate-resume)
**react-ultimate-resume** is an open-source customizable software developer resume to highlight your skills and experiences.
Discover a modern approach of the traditional CV that includes animations and latest front-end technologies. Impress recruiters or customers with your projects, hobbies and experiences as never before.
We used [JSON Resume](https://github.com/jsonresume), a community driven open source initiative to create a JSON based standard for resumes. Discover the official schema [here](https://jsonresume.org/schema/). We added a few extra-fields to JSON Resume standard to fit developers needs. Learn more about them [here](https://github.com/welovedevs/react-ultimate-resume#json-resume-extra-fields).
This app is built using the popular [create-react-app](https://github.com/facebook/create-react-app). You will find a lot of resources to understand how to edit and publish your resume directly on <https://create-react-app.dev/>
### Preview
[![Resume Preview](https://camo.githubusercontent.com/578f828ff27307b8741b7ed1af4ab5294a0b6cf78d37bb5623bf0b33acd95395/68747470733a2f2f63646e2e66696c65737461636b636f6e74656e742e636f6d2f636f6d70726573732f726573697a653d77696474683a3530302f7266585938544e415264616f3944645153614a65)](https://vincent-cotro.welovedevs.com)
### Docs
Docs can be found [Here](https://welovedevs.com/react-ultimate-resume/docs/home).
Feel free to improve it with a PR ♥️
### Features
The resume is designed with 10 Cards (we plan to add more !)
  * 🙂 Basics: Your basics : Where are you ? When did you start coding ...
  * 📊 Skills: Beautiful Graphs to show your skills
  * 💼 Dream job: Explain easily to recruiters what is your dream job
  * 💾 Experiences: Describe your professional experiences
  * 🎓 Studies: How did you learn to code ?
  * ✨ Projects: Highlight your best projects
  * 📺 Hobbies: Show your hobbies with GIF !
  * 🎶 Music: Add your favorite Spotify Playlist
  * 🔭 Interested by: Tell more about technologies you would love to learn
  * 🌎 Languages: What language do you master?


Each cards comes with an edit dialog to edit your JSON Resume directly inside the app
### Customize your Profile
🎨 This resume is fully customizable with an included set of nice color palettes :
[![Customize your profile](https://camo.githubusercontent.com/080f299a3230bbeec2fb2210cb673e569755b9041630e13651d9804a1d484578/68747470733a2f2f63646e2e66696c65737461636b636f6e74656e742e636f6d2f636f6d70726573732f75514c4843346554524b754a32344e6f4a4e6b53)](https://camo.githubusercontent.com/080f299a3230bbeec2fb2210cb673e569755b9041630e13651d9804a1d484578/68747470733a2f2f63646e2e66696c65737461636b636f6e74656e742e636f6d2f636f6d70726573732f75514c4843346554524b754a32344e6f4a4e6b53)
### Getting started
Fork this repository. `git clone` your fork 💪
Install

```
yarn install

```

Run

```
yarn start

```

See the website on localhost with the following url:

```
localhost:3000

```

Replace the default JSON Resume with yours

```
/src/data/json_stub.json

```

### Deploy on you own server
You can deploy your resume on your own server in few minutes. Follow our [HOW TO documentation](https://welovedevs.com/react-ultimate-resume/docs/Deploy/deploy-fork).
### Use inside your project
You can install the resume directly inside your project.

```
npm i @welovedevs/react-ultimate-resume

```

Then

```
import DeveloperProfile from '@welovedevs/react-ultimate-resume';

```

### Parameters
| **Parameter**  | **Type**  | **Description**  |  
| mode  | "edit" | "readOnly"  | Use this to activate or disable the Edit mode. In "edit" mode you will be able to update and customize your resume. Use "readOnly" in production.  |  
| data  | JSONResume  | This is your stringified JSONResume  |  
| options  | Object  | See options for more informations [here](https://github.com/welovedevs/react-ultimate-resume#options)  |  
| onCustomizationChanged  | Callback  | Get the current customization if the customization is updated.  |  
| additionalNodes  | Object  | Additional nodes is used to add react components directly inside the resume. This is an advanced feature that will be documented later.  |  
#### Options
| **Parameter**  | **Type**  | **Description**  |  
| locale  | "fr" | "en"  | Resume locale (Default to "en")  |  
| side  | "front" | "back"  | Cards default side (Default to "front")  |  
| apiKeys  | { giphy : string }  | Api keys for 3thd party librairies. For instance Giphy in edit mode.  |  
| endpoint  | { devicons : string, unsplashProxy: string }  | Endpoints for 3thd party services. Used to get the technology list and use unsplash.  |  
| customization  | Object  | Current resume customization.  |  
### JSON-Resume Extra Fields
| **Category**  | **Field name**  | **Type**  | **Description**  |  
| basics  | visaSponsorship  | Boolean  | True if you need a visa sponsorship to work in your dream country.  |  
| basics  | personalDescription  | String  | A short description that will be displayed below your name in the resume header. Example: "Passionate React Developer".  |  
| dreamJob  | locations  | Array<{ name : string, title: string }>  | Your dream job cities. Example: "San Francisco, US".  |  
| work  | remote  | String  | Give here more information about the frequency if your dream job is a remote job. Example: "regularly"  |  
| education  | studiesLevel  | Number  | What is your highest level of formal education? (Bachelor = 3 years post graduate. Master = 5 years post graduate)  |  
| work  | contractTypes  | Array<"fixedTerm" | "permanent" | "internship" | "apprenticeship" | "freelance">  | Your dream job contract types. Example: ['fixedTerm']  |  
| work  | codingYears  | Number  | How long have you been coding (in years)? Example: 5  |  
| work  | codingReason  | String  | What motivates you to wake up every day to code?  |  
| work  | searchState  | "activelySearching" | "openOpportunities" | "dreamjobOnly" | "notSearching"  | Are you open to new job opportunities?  |  
| work  | experienceYears  | Number  | How many years of professional experience do you have?  |  
| sound  | embedUrl  | String  | Your favorite Spotify playlist.  |  
| interestedBy  |   | String  | What languages do you want to learn? Example: Angular and Vue.js  |  
### Hosted for free on WeLoveDevs.com
Don't want to host your profile ?  
Create your JSONResume and get your free subdomain in less than 10 minutes by registering on [welovedevs.com](https://welovedevs.com/app/register_developer).
We added a few extra features that you will love :
  * ⚡ Server side rendering for ultra fast loading
  * 🔒 Secured using reCAPTCHA v3, HTTPS and Cloudflare


### i18n
The resume is currently available in English, French and Turkish. Feel free to contribute with your language translation file !
### Built by the community 💖
<https://web-develop.me/> - by [@liorchalma](https://github.com/liorchamla)
### Contributors
This project exists thanks to all the people who contribute.  
|  [![](https://avatars.githubusercontent.com/u/18561703?v=3)  
**Thomas Grivet**](https://github.com/thomasgrivet)  
 |  [![](https://avatars.githubusercontent.com/u/5870982?v=3)  
**Clément Devos**](https://github.com/clementdevos)  
 |  [![](https://avatars.githubusercontent.com/u/9655206?v=3)  
**Vincent Cotro**](https://github.com/VincentCtr)  
 |  [![](https://avatars.githubusercontent.com/u/6273310?v=3)  
**Antonin Catrix**](https://github.com/catrx)  
 |  
Chat with us on [Discord](https://discord.gg/udbbbAq) !
### License
react-ultimate-resume is relased under [GNU AGPL v3 license](https://github.com/welovedevs/developer-profile/blob/master/LICENSE.md)
## About WeLoveDevs.com
WeLoveDevs.com is a website crafted for developers (by Developers) looking for new career opportunities. More than 1700 companies use WeLoveDevs.com to find their talents. Discover your next company [here](https://welovedevs.com/app/companies)
## About
💼 🎨 A modern software developer resume built with React and JSONResume 
[ react ](https://github.com/topics/react "Topic: react") [ resume-template ](https://github.com/topics/resume-template "Topic: resume-template") [ resume ](https://github.com/topics/resume "Topic: resume") [ github-pages ](https://github.com/topics/github-pages "Topic: github-pages") [ hobbies ](https://github.com/topics/hobbies "Topic: hobbies")
###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/welovedevs/react-ultimate-resume).
##  [Releases](https://github.com/welovedevs/react-ultimate-resume/releases)
##  [Packages 0](https://github.com/orgs/welovedevs/packages?repo_name=react-ultimate-resume)
No packages published   

###  Uh oh! 
There was an error while loading. [Please reload this page](https://github.com/welovedevs/react-ultimate-resume).
##  [Contributors 20](https://github.com/welovedevs/react-ultimate-resume/graphs/contributors)
  * [ ![@clementdevos](https://avatars.githubusercontent.com/u/5870982?s=64&v=4) ](https://github.com/clementdevos)
  * [ ![@thomasgrivet](https://avatars.githubusercontent.com/u/18561703?s=64&v=4) ](https://github.com/thomasgrivet)
  * [ ![@catrx](https://avatars.githubusercontent.com/u/6273310?s=64&v=4) ](https://github.com/catrx)
  * [ ![@VincentCtr](https://avatars.githubusercontent.com/u/9655206?s=64&v=4) ](https://github.com/VincentCtr)
  * [ ![@ardacebi](https://avatars.githubusercontent.com/u/17576065?s=64&v=4) ](https://github.com/ardacebi)
  * [ ![@nicklamyeeman](https://avatars.githubusercontent.com/u/32619823?s=64&v=4) ](https://github.com/nicklamyeeman)
  * [ ![@well-oo](https://avatars.githubusercontent.com/u/38964651?s=64&v=4) ](https://github.com/well-oo)
  * [ ![@NetworkMonk](https://avatars.githubusercontent.com/u/40229991?s=64&v=4) ](https://github.com/NetworkMonk)
  * [ ![@thedamfr](https://avatars.githubusercontent.com/u/2880446?s=64&v=4) ](https://github.com/thedamfr)
  * [ ![@dependabot\[bot\]](https://avatars.githubusercontent.com/in/29110?s=64&v=4) ](https://github.com/apps/dependabot)
  * [ ![@baptpln](https://avatars.githubusercontent.com/u/64689165?s=64&v=4) ](https://github.com/baptpln)
  * [ ![@flexbox](https://avatars.githubusercontent.com/u/360936?s=64&v=4) ](https://github.com/flexbox)
  * [ ![@dmcwhorter](https://avatars.githubusercontent.com/u/1111095?s=64&v=4) ](https://github.com/dmcwhorter)
  * [ ![@roboflank](https://avatars.githubusercontent.com/u/6532631?s=64&v=4) ](https://github.com/roboflank)


## Languages
  * Other 0.5%
