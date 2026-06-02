---
source_url: "https://www.infoworld.com/article/4078884/what-is-vibe-coding-ai-writes-the-code-so-developers-can-think-big.html"
source_domain: "infoworld.com"
topic: "github-ai-vibe"
extractor: "trafilatura-2.0"
fetched_at: "2026-05-29T13:38:40.549535+00:00"
word_count: 1941
stage: "raw-extracted"
---

## A new generation of developers is letting AI do the coding while they focus on ideas, flow, and outcomes. But can ‘structured creativity’ scale from prototypes to production?

## Why is vibe coding is called vibe coding?

Vibe coding is a methodology in software development where the traditional act of writing code gives way to conversational instructions and collaboration with a generative AI tool. Rather than outlining detailed specifications and handing them off to engineers, product managers, domain experts — or anyone with an idea — can describe what they want in plain language and let AI tools build software in real-time. The idea is less about automating engineering and more about shifting how intent is expressed, evaluated, and refined.

The term “vibe coding” was coined by AI researcher and OpenAI co-founder Andrej Karpathy in early 2025. In a post on X (formerly Twitter), he wrote, “There’s a new kind of coding I call ‘vibe coding,’ where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.”

This captured an emerging shift in mindset: Why not trust the AI to do the mechanics, and focus instead on direction, feedback, flow, and, well, vibes? As the models underpinning Cursor, GitHub Copilot, or other tools become more capable, developers increasingly see programming less as line-by-line syntax and more as a dialogue with AI — where the code “just works” as long as the prompts and corrections do.

That’s not to say that problems can’t emerge, as AI tools still hallucinate and, in ways that are more human than we might like, don’t always follow quality guidelines or security best practices. Still, the technique is increasingly popular, and we spoke to a number of developers to get a vibe check on the whole thing.

## How vibe coding differs from ‘traditional’ AI programming

The line between programming and prompting has been blurring for years, but vibe coding pushes that evolution to its logical extreme. Early AI coding tools such as GitHub Copilot were built to assist developers as they worked — completing functions, filling in syntax, or generating boilerplate code from comments. In vibe coding, the human doesn’t start by writing code at all.

“Traditional AI coding suggests completions while you write code,” said Amy Mortlock, vice president of marketing at ShadowDragon. “Vibe coding flips this: you describe what you want in plain English, then the AI generates the entire application. You focus on outcomes while AI handles all technical details.”

That inversion of control changes both the workflow and the mindset. Kostas Pardalis, a data infrastructure engineer and co-founder of Typedef, described it as a new kind of collaboration. “In traditional AI-assisted coding, the human writes the intent in natural language and the model completes or translates it into code.

In vibe coding, you’re collaborating with the model in a shared space — exploring ideas, iterating quickly, and steering through feedback rather than fixed instructions. You’re optimizing for flow and expressiveness, not syntax.” That’s a shift that turns programming into something closer to live prototyping than traditional software development.

## Can you implement vibe coding in an enterprise environment?

Enterprise development teams can experiment with vibe coding — but only if they balance creativity with control. As Anaconda Field CTO Steve Croce put it, “Not only is it possible to implement vibe coding in a structured enterprise setting, but it’s also the responsible way to utilize the technology.”

Croce’s team’s recent survey of more than 300 AI practitioners found that “only 34% of enterprise organizations had formal policies and tools in place for AI-assisted coding,” revealing what he called “a huge lag in adapting security and governance to new AI technologies.”

That gap underscores a theme emerging across enterprise AI adoption: enthusiasm often outpaces oversight and structured governance.

Steve Morris, founder and CEO at Newmedia.com, said his organization solved that problem by embedding security directly into the AI workflow. “Enterprise dev orgs can absolutely vibe code, if they use security-driven AI workflows to defeat entropy,” he said. “We’ve rolled out custom GPT-based assistants with prompt profiles that reference OWASP and company coding guidelines. We also pass every block of code generated through a second AI agent whose sole purpose is to red team and code review it at turbo speed.” The results: a 40% drop in monthly bug tickets and “no critical exploit made it to production since.”

Charles Ma, software engineer at Chronosphere, said his team takes a similar layered approach. “Many of our engineers use tools like Cursor and Claude Code. We even encourage their use via a usage leaderboard,” he said. “However, we treat them as assistants, not replacements. Our code review process still applies to any production code, and we don’t tend to connect many if any external tools to [AI].”

## What is a typical vibe coding workflow or life cycle?

There’s no single blueprint for vibe coding. It flexes depending on the goal, the organization, and the level of structure applied. But two of the practitioners we spoke to offered their somewhat different takes. Typedef’s Pardalis described an agile, creative four-step process:

**Exploration**: Define “the vibe: the tone, purpose, and constraints.”**Shaping**: Build and refine “a working prototype.”**Grounding**: Add structure and data integrity.**Operationalizing**: Apply “versioning, evaluation, and governance.”

“At Typedef,” he said, “we think of this as the evolution from prompting to pipelining.”

Anaconda’s Croce, meanwhile, says that any workflow “really depends on what the goal of the app is,” whether it’s “a prototype, an interim solution, or even a full production application.” But ultimately his vision aligns more closely with traditional software life cycles. His breakdown:

**Planning and requirements analysis:**Product managers and UX teams can “vibe code entirely in this phase,” creating clickable prototypes and feasibility tests before formal development.**Design:**AI can help generate architectures and documentation, though “this may be a phase in an organization where you want a senior engineer or architect to step in” to ensure standards and reuse of internal systems.**Implementation and testing:**“This is the core part of the vibe coding experience.” The agent can “build your entire application,” even structure repositories and run tests — but enterprise teams should add human review, test coverage, and compliance checks.**Deployment and maintenance:**AI can deploy and maintain apps, but “to stay in accordance with corporate requirements, this portion can be handled entirely outside of the vibe coding experience.”

## Tips for effective vibe coding

If you’re planning to dig into the vibe coding process, experts have some tips for you to make the most of it:

**Start with goals, not features.**Achint Agarwal, VP of product at Pramata, suggests teams begin by “describing the desired user experience you’re going for and the main business problems you’re trying to solve.” Don’t over-specify every button or screen: “You’ll be surprised by what the AI recommends.” Being “as specific as possible about what you want to achieve” helps the model generate more relevant solutions.**Plan and design ahead.**Typedef’s Pardalis warned that “vibe coding won’t substitute for a good architecture.” Before invoking the model, “make sure you have designed and specced your work well enough.” Good upfront planning makes it easier for the AI to translate intent into coherent systems.**Treat AI as a collaborator, not an oracle.**ShadowDragon’s Mortlock said it’s best to treat vibe coding “as a collaborative effort” with your AI tools, “guiding and reviewing rather than accepting everything blindly.” Anaconda’s Croce echoed that advice: “Don’t assume the agent is right. Don’t hesitate to question the logic.”**Use frameworks, context, and examples.**Mortlock suggested leveraging “established frameworks instead of building the application from scratch.” Croce added that you can “give [the AI] examples or similar applications” and even extend capabilities by adding “trusted and approved MCP servers for managing context on bigger projects.”**Keep humans — and security — in the loop.**Chronosphere’s Ma recommended limiting “AI’s access only to the tools it needs” and maintaining review gates. “Good engineering practice should also still apply,” he said: generate tests, verify functionality, and “use AI as a tool to help with creativity and productivity but not as a replacement for your skills and knowledge.”**Iterate and instrument.**Pardalis encouraged developers to “stay in conversation” and “embrace imperfection early.” Track prompts, cache checkpoints, and refine outputs until the “flow” turns into reliable functionality.

## What are good vibe coding tools?

Vibe coding tools span a broad range — from low-barrier, conversational builders designed for nontechnical teams to integrated developer environments that give engineers deep control and production-grade reliability. Picking the right one depends on your team’s skills, the goal of your project, and how much governance you need.

**Cursor**sits at the high-control end of the spectrum. It’s an AI-integrated IDE that lets you edit across multiple files and maintain full visibility into generated code. Anaconda’s Croce listed Cursor among “AI-included vibe coding friendly IDE[s],” while Pramata’s Agarwal said it’s ideal for “something more robust that will become the foundation for actual production code.”**Replit**remains a go-to for browser-based collaboration. ShadowDragon’s Mortlock said it “can be best for collaborations,” while Agarwal added that it bridges prototyping and formal development.**Bolt**and**Lovable**. For fast ideation and low technical lift, Mortlock called Lovable and Bolt “beginner-friendly,” and Agarwal said tools like these let you “go from idea to working prototype without any coding knowledge.”**Windsurf****and Zed**. Developers comfortable in full IDEs can extend their workflow with Cursor, Windsurf, or Zed, according to Croce. These tools aim to blend vibe coding features into traditional environments.

## What are vibe coding quality and security concerns?

Despite its benefits, vibe coding also introduces real risks around maintainability, vulnerability, and blind spots in generated logic. As practitioners push the boundaries of model-driven development, several key concerns repeatedly surface.

ShadowDragon’s Mortlock warns that “the main issues are security vulnerability concerns and technical debt. AI can sometimes introduce insecure patterns or even outdated libraries, and generated code is also longer most of the time, which makes debugging very long and tedious. AI can also reference non-existent packages that malicious actors can use to exploit.” In short: what looks like working code may carry hidden traps.

Newmedia.com’s Morris brings a deeper cautionary example. He recounts building a vibe-coded reporting portal where “55% of function blocks generated by LLMs in our code base had security holes in repeated scans of code from earlier in the year.” He adds that “LLMs are as blind now to cross-site scripting or log injection as they were in 2021,” and that hallucinated package imports open the door to supply chain attacks. To guard against that, his team now “require[s] manual approval of every package name and import from AI-generated code before running a single test.” That single change, he says, pushed exploitable blocks effectively to zero.

Chronosphere’s Ma adds that complacency and overpermissive access expand the attack surface. “Even experienced engineers may become complacent … miss problems they would have otherwise found.” Moreover, when AI tools link into external systems or perform web searches, prompt injections or tool-chain exploits become possible.

Typedef’s Pardalis frames the issue in terms of volatility and visibility: “Because vibe coding encourages rapid iteration and model autonomy, the main risks are uncontrolled variability and opaque provenance.” To combat these problems, he urges:

**Lineage tracking**: Commit every version, and use frameworks with built-in traceability**Evaluation loops**: Run automated quality and regression checks**Governance layers**: Audit prompt histories, and filter sensitive data

Pardalis believes that expressive, model-driven development and deterministic infrastructure aren’t oppositional—they can coexist under disciplined guardrails. Because in the end, the promise of vibe coding is not chaos, but structured creativity. You ideate fast, but you deploy safely. In other words: freedom up front, discipline as you go deeper — that’s how vibe coding can actually scale in production settings.