# Teach Me

Turns Claude into a one to one tutor instead of an explainer: it probes what you already hold, maps the subject as a dependency graph, then teaches one node at a time and makes you prove it stuck.

## What it does

Ask most assistants to teach you something and you get a well-written explanation you nod along to and forget.
Nodding is recognition, and recognition feels exactly like understanding without being it.
This skill is built to break that illusion.

- **It probes before it teaches**: eight to twelve production questions to find where you actually stop, capped so the first session does not become an exam.
- **It knows knowledge is a graph, not a ladder**: you can be solid on promises and weak on the event loop that sits underneath them. A straight walk from easy to hard would classify you wrong.
- **A map you can see**: a Mermaid graph of the subject, ordered by dependency, coloured by what you hold. It is the plan and the progress record at once.
- **One node per lesson**: never a concept whose prerequisites are unheld, and never more than one at a time.
- **You produce, you never recognise**: explain from memory, predict an unseen case, or find the fault in a broken example. "It makes sense" is not accepted as evidence.
- **Difficulty down, then up**: easy while you take the knowledge in, hard while you prove it landed. Reversing that is how a lesson feels rigorous and teaches nothing.
- **A page when the text is not enough**: a node with something that moves, a state to step through, a knob to turn or a shape to see also gets a self-contained HTML page beside the lesson. It opens on a double click, with no server and no network. Most nodes do not need one, and do not get one.
- **The page shows, it never grades**: the check stays in the lesson, because clicking the right answer out of four is recognition, and recognition is the thing being broken here.
- **It cites**: every lesson links a real source, so nothing rests on the model's recall alone.
- **Come back later**: it reopens the map, re-probes something you marked solid a while ago, and picks the next node off the graph.
- **A standard shape, your words**: the file names and headings are always the same, so any course opens the same way. What you read inside is written in your language.

## What you get

```
<subject>/
├── COURSE.md              why you are learning it, how you want it explained, what is out of scope
├── MAP.md                 the Mermaid graph, one evidence line per node touched, the sources
└── lessons/
    ├── 0001-<slug>.md     the explanation, its source, the check, and the verdict
    └── 0002-<slug>.html   only when the node has something the text cannot show
```

Three files, split by how often they change: `COURSE.md` almost never, `MAP.md` every session, `lessons/` append only.
The HTML pages are the exception, not the rule. They sit next to the lesson they belong to, share its number and slug, and hold nothing the Markdown needs in order to teach.

**The layout above is fixed.** File names, headings and Mermaid keywords are always English, so every course has the same shape. The explanations, the evidence lines and the questions come out in whatever language you learn in.

## Use cases

- Learning a subject over weeks, without re-explaining your level every time
- Finding out what you actually know before you start studying
- Getting a roadmap for a topic that follows dependencies instead of chapter order
- Being quizzed properly, on things the explanation did not walk through
- Reviving a course you abandoned a month ago
- Catching a misconception you have been carrying without noticing
- Not for a single factual answer. Ask the question directly instead.

## How you start it

You type `/teach-me`. The model never reaches for this on its own, by design: a tutor that starts teaching because your question sounded like a question is a tutor that interrupts. Each lesson is its own invocation, and the folder is what carries the course, not the conversation.

## Example prompts

- "Teach me how the JavaScript event loop actually works"
- "I want to learn linear algebra for machine learning, start by working out what I already know"
- "Quiz me on what I said I understood last week"
- "Give me a study map for Rust ownership"
- "I keep mixing up covariance and contravariance, teach me properly"
- "Reopen my concurrency course and carry on"

## How it works

```
teach-me/
├── SKILL.md                       always loaded when you invoke the skill
└── references/
    ├── example-course.md          read in step 2, before drawing a map for the first time
    └── lesson-template.html       read in step 3, before writing the first page of a course
```

`SKILL.md` holds the three phases, the templates, and the rules:

1. **The workspace** - three artifacts and the lifecycle rule that decides what goes in which.
2. **Procedure** - triage, map, teach. Each step ends on a condition that must be true before the next one starts.
3. **The visual complement** - what earns an HTML page, what the page has to be, and what it must never become.
4. **Proving it stuck** - the production rule and its three probes.
5. **The artifacts** - the templates, plus the three things the templates cannot say on their own.
6. **Returning to a course** - the branch for a map that already exists.
7. **Hard rules** - the constraints that keep the tutor from drifting back into being an explainer.

Both references sit outside `SKILL.md` because each is needed once per course, not once per turn.
A filled-in artifact teaches the model more than three paragraphs describing one, but it should not be loaded on every turn of every lesson.

Three design choices are worth naming, because they are what keep the system small:

**State lives only in the graph.** The evidence list records what the learner produced, never whether a node is solid. A fact written in two places drifts, and the writer here is a language model with no memory of what it wrote last week.

**The frontier is never stored.** It is derivable: the weak node, or the first bare node whose parents are all solid. Anything derivable goes stale the moment the map moves, so it is recomputed instead of saved.

**No shared stylesheet.** A self-contained page cannot link one, so the pages would drift apart into a pile of one-offs. The consistency comes from `lesson-template.html`, which lives in the skill and is copied, never linked. That buys the look of one course without adding a directory to yours.

## Install

**Claude.ai**: zip the folder, not the files inside it, and upload the zip in **Customize > Skills**.
Needs code execution enabled in **Settings > Capabilities**, which is what lets Claude read the reference file and write the workspace.

```bash
cd skills && zip -r teach-me.zip teach-me
```

**Claude Code**:

```bash
# The whole collection
claude plugin marketplace add LaiqianDS/laiqiands-skills
claude plugin install laiqiands-skills@laiqiands

# Or this skill alone, from a clone
ln -s "$PWD/laiqiands-skills/skills/teach-me" ~/.claude/skills/teach-me
```

## Credits

The workspace idea, the mission-first rule, the self-contained HTML lesson, and the equal-length answers rule come from the `teach` skill by [Matt Pocock](https://github.com/mattpocock).
The three-phase shape, the level triage, and the concept graph as a planning output come from personal notes by [Laiqian Ji](https://github.com/LaiqianDS).
The learning principles underneath are Bjork's storage strength against retrieval fluency, and Vygotsky's zone of proximal development.
