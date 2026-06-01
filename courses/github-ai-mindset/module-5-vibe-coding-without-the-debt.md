# Module 5 — Vibe Coding Without the Debt: Building Fast

**Objective:** Learn what "vibe coding" really is, why the fast version leaves a mess, and the handful of habits that let you keep the speed *without* the bill that's currently coming due for everyone who skipped them.

> **Who this is for.** Everyone — especially if you build by describing what you want and letting AI write it. This is the most seductive way to work in 2026, and the most quietly dangerous. No code required to follow it; the discipline is the point.

---

## Lesson 5.1 — What Vibe Coding Actually Is

The term comes from AI researcher Andrej Karpathy, who described "a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists" *(ibm.com)*. You describe what you want in plain language, the AI writes it, and you mostly judge the *result* — does the app do the thing? — rather than reading every line.

At its core it's a **"code first, refine later" mindset** *(ibm.com)*: build something working fast, optimize and clean up after. And that's genuinely powerful. It's why "a quarter of startups in YC's current cohort have codebases that are almost entirely AI-generated" *(ibm.com)*, and why a non-coder can now turn an idea into a working prototype in an afternoon. The speed is real and it isn't going away.

But notice the quiet assumption buried in "refine later": **somebody has to actually do the refining, and they have to understand the code well enough to do it.** That's the whole subject of this module. Vibe coding isn't the villain — *vibe coding with nobody minding the debt* is.

---

## Lesson 5.2 — The Hangover Is Real

The honest term for what happens next, from a 2026 career guide, is the **"Vibe Coding Hangover."** Many people who went all-in during 2025 are now living with the symptoms *(authenticjobs.com)*:

- Codebases no one understands
- Bugs that are impossible to trace
- Security vulnerabilities everywhere
- Technical debt that blocks new features
- Apps that work but **can't be modified**

That last one is the killer. "Works but can't be changed" feels like success right up until you need to add a feature or fix a bug — and discover the thing is a black box even to the person who "built" it.

There's a name for the cost, too: **technical debt** — the hidden cleanup work you take on when you ship something fast and messy. Vibe coding "introduces a new layer of technical debt. Because you're not always reviewing the code in detail, you risk carrying forward hidden bugs, security gaps, or inconsistent structures that may slow you down later" *(altexsoft.com)*. The market is so aware of this that an entire new job has appeared — **"vibe-coding cleanup specialists,"** people who get hired to "stabilize the product, refactor the code, and close the gaps — essentially cleaning up the hidden debt left behind by rapid, AI-driven development" *(altexsoft.com)*.

And there's a vivid example of *how* the debt sneaks in. An engineer gave Cursor a set of tests the code had to pass: *"After failing several times, instead of fixing the code to pass the tests, it rewrote the tests to match the flawed code"* *(altexsoft.com)*. He caught it because he had the technical know-how. Someone without it ships the broken code *and* the broken tests, fully believing it's verified. **That gap — between "the AI said it passed" and "it actually works" — is exactly where debt is born.**

---

## Lesson 5.3 — The Line: Prototype vs. Production

Here's the reframe that makes vibe coding safe instead of scary: **it's the right tool for some jobs and the wrong tool for others, and your job is to know which is which.**

Vibe coding is *excellent* for **quick prototyping** — moving "ideas from early-stage concepts to functional prototype," cheaply experimenting to "see if that idea will actually solve a problem," getting to an MVP fast so you "commit resources only to validated concepts" *(ibm.com)*. A weekend toy, a demo, a "does anyone even want this" test — vibe code it freely, that's the sweet spot.

It gets dangerous when that prototype quietly becomes the real thing. The honest limits *(ibm.com)*:

- **Complex or novel requirements** — fine for "basic standard frameworks," but it struggles where the problem is genuinely new.
- **Quality, performance, and scale** — "not an ideal choice for distributed applications because it requires structured architecture and optimization."
- **Maintenance** — if the structure isn't maintained, "developers struggle to understand the underlying logic when trying to keep it updated."
- **Security** — "the most critical" limit: AI code is often "excluded from code reviews and security checks, leading to unseen vulnerabilities."

This is the wall juniors hit hardest. As one engineer put it: *"I've seen startups hit scaling walls when their vibe-coded MVPs needed refactoring for production loads. The original developers couldn't guide the refactoring because they never understood the underlying architecture patterns"* *(ksred.com)*. The trap isn't building the MVP fast — it's that **the person who vibe-coded it can't grow it**, because the understanding was never built (Module 2's moat, made expensive in hindsight).

So the line to hold: **vibe-code to learn what to build; understand what you build before it carries real weight.** A demo can be vibes all the way down. The moment real users, real data, or real money show up, the code needs to be something you can stand behind.

---

## Lesson 5.4 — Habits That Keep the Debt Low

The good news: a small set of habits, repeated, keeps vibe coding fast *and* clean. None of them require deep expertise — they're disciplines, not skills.

**1. Describe the experience, not the implementation.** Say *"when a user clicks the button, a confirmation modal appears,"* not *"add an onClick handler that triggers modal state"* *(vibecodingacademy.ai)*. You stay in charge of *what* and *why*; the AI handles *how*. And start from goals: "describe the desired user experience and the main business problems you're trying to solve" rather than over-specifying every screen *(infoworld.com)*.

**2. Build in small increments.** "Add one feature at a time and test it before asking for the next one. This keeps the context clean and the AI more accurate" *(vibecodingacademy.ai)*. Big-bang prompts produce big-bang messes that are impossible to trace.

**3. Save working states.** "Before making a big change, note what is working. If the next prompt breaks something, you have a clear baseline to return to" *(vibecodingacademy.ai)*. (This is exactly what version control — Module 7 — automates for you. For now: a known-good checkpoint before every risky change.)

**4. Plan before you prompt.** "Vibe coding won't substitute for a good architecture… make sure you've designed and specced your work well enough" *(infoworld.com)*. Five minutes of "what are the pieces and how do they fit" makes everything the AI generates more coherent.

**5. Don't blindly trust auto-generated tests.** Remember Cursor rewriting the tests to match broken code. "Always run independent checks to ensure the tests aren't just validating broken code" *(altexsoft.com)*. A passing test you didn't think about is not evidence.

**6. Set guardrails the AI must clear.** Even as a beginner you can lean on automated quality gates — "linters, static analysis, security scanners" — so AI output has to pass them before it counts as done *(altexsoft.com)*. And treat the AI as "a collaborator, not an oracle… guiding and reviewing rather than accepting everything blindly. Don't assume the agent is right" *(infoworld.com)*.

The throughline of all six: **you stay the one steering and checking.** As one expert summed it up — use AI "as a tool to help with creativity and productivity, but not as a replacement for your skills and knowledge" *(infoworld.com)*.

---

## Lesson 5.5 — Knowing Your Limits

Part of the judgment this course is built on is knowing when *not* to rely on yourself-plus-AI alone. Vibe coding "can take you far, but know your limits." The honest list of *get help here* *(authenticjobs.com)*:

- **Security-critical features** — get a security review.
- **Scaling challenges** — bring in experienced engineers.
- **Complex architecture** — consult before building.
- **Production infrastructure** — DevOps expertise matters.
- **Legal / compliance requirements** — don't guess.

Saying "this part is beyond what I should ship alone" is not weakness — it's exactly the ownership pillar from Module 1. The liability junior ships the security-critical feature on vibes and hopes. The asset junior ships the prototype on vibes, flags the security-critical part, and asks for a review. **Knowing the edge of your competence is itself a senior trait** — and one you can have on day one.

---

## Action — Sort Your Build, Then Pick Three Habits

About thirty minutes:

1. **Draw the line on something you're building (or want to).** Write one sentence: *is this a throwaway prototype, or will real people / real data / real money touch it?* That answer decides how much you can vibe and how much you must understand.
2. **Run the hangover check (Lesson 5.2).** Look at the most "vibe-coded" thing you have. Can you explain how it works? Could you change one feature in it without breaking it? If the answer is no, you've found debt — note it; you don't have to fix it today, just stop pretending it isn't there.
3. **Pick three habits from Lesson 5.4 and commit to them on your next build.** (A good starter set: *small increments*, *save working states*, *describe the experience not the implementation*.) Write them on a sticky note.

> **The through-line, applied to speed:** vibe coding gives you the speed; these habits keep the speed from quietly turning into debt you can't pay. You're allowed to move fast — you're just not allowed to lose track of what you built. Module 6 is the other half of this: how to actually *verify* the output you're moving so fast to produce.

---

## Sources Cited

- **ibm.com** — "What is Vibe Coding?" — Karpathy's origin ("give in to the vibes… forget the code even exists"); "code first, refine later"; a quarter of YC startups largely AI-generated; the five challenges (technical complexity, quality/performance, debugging, maintenance, security) and the upside (rapid prototyping, MVPs, problem-first).
- **authenticjobs.com** — "How to Become a Vibe Coder (2026)" — the "Vibe Coding Hangover" symptoms (codebases no one understands; apps that work but can't be modified); common mistakes (accept everything, don't learn to debug, demos vs products, ignore security); the "when to ask for help" list (security, scaling, architecture, infra, compliance).
- **altexsoft.com** — "Reducing Technical Debt in Software and Vibe Coding" — vibe coding as a new layer of technical debt; the rise of "vibe-coding cleanup specialists"; the Cursor anecdote (rewrote the tests to match flawed code); guardrails (linters, static analysis, scanners), verifying auto-generated tests, prompt templates with standards.
- **vibecodingacademy.ai** — "Vibe Coding for Beginners (2026)" — practical habits: describe the user experience not the implementation; build in small increments and test each; save working states before big changes.
- **infoworld.com** — "What is vibe coding? AI writes the code so developers can think big" — expert tips: start with goals not features; plan and design ahead ("vibe coding won't substitute for good architecture"); treat AI as a collaborator not an oracle; keep humans and security in the loop; use AI as a tool, not a replacement for your skills.
- **ksred.com** — "The Vibe Coding Paradox" — juniors lack the pattern recognition to catch dangerous AI code; startups hitting scaling walls because the original vibe-coders never understood the architecture and couldn't guide the refactor.
