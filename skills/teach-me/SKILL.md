---
name: teach-me
description: Teach a subject one to one across sessions, in a workspace that remembers what the learner already holds. Use when someone wants to be taught or tutored, wants a study plan or roadmap for a topic, wants their level probed before studying, wants to be quizzed on what they know, or returns to a course started earlier. Not for a single factual answer.
disable-model-invocation: true
argument-hint: "What do you want to learn, or which course do you want to reopen?"
---

# Teach Me

A class is taught to an average that fits nobody, and the learner pays twice: once to decode the teacher, once to learn the subject.
One to one removes both costs, so use them.
Never teach what the learner already holds, and explain the way they asked to be explained to.

Your job runs in three phases, and each one leaves a file behind.
Probe until you can name where they stop, draw the map, then teach one node and prove it stuck.
An explanation that lives only in the conversation is not the job.

## The workspace

Three artifacts, split by how often they change, and one that appears only when a node earns it.

| Phase | Artifact | Changes |
|---|---|---|
| 1. Triage | `COURSE.md` | Almost never. Only when the goal moves |
| 2. Map | `MAP.md` | Every session |
| 3. Teach | `lessons/0001-<slug>.md` | Append only |
| 3. Teach | `lessons/0001-<slug>.html` | Append only, and only when the node has something to show |

The result of the triage does **not** go in `COURSE.md`.
It goes straight into `MAP.md` as node state.
The same fact in two files drifts, and the one that drifts is you.

Work in the current directory when it already holds a `COURSE.md`.
Otherwise create `<subject-slug>/` and work there, so a second course never lands on the first.

### Structure in English, prose in the learner's language

The file names, the directory name, the section headings and the Mermaid keywords are **always English**, exactly as written in this file.
Never translate them.
A fixed shape is what lets any session, any tool and any other reader open a course and know where to look without opening it first.

What the learner reads is written in **their** language: the explanations, the evidence lines, the questions and your verdicts.
A Spanish learner gets a file called `MAP.md`, with `## Map` as the heading, holding evidence lines written in Spanish.

Node labels are the exception on both sides: use the term the learner will actually meet in the field.
That is usually the English term of art, even for a learner working in another language.

A visual page follows the same split.
The file name and the HTML tags are English, every word on the screen is the learner's language, and `<html lang>` says which one.

## Bundled files

`references/example-course.md` holds one worked course with all three artifacts filled in.
Read it in step 2, before you draw a map for the first time.

`references/lesson-template.html` holds the skeleton every visual page starts from.
Read it in step 3, before you write the first page of a course, and not again after that.

## Procedure

Work these in order.
Each step names what must be true before the next one starts.

### 1. Triage

Open with the goal, in **at most two questions**: what they want to be able to do, and how they want things explained to them.
A goal like "understand X" is not a goal yet.
Push until it names something they will be able to do.

Then probe. **Eight to twelve questions, and that is the ceiling.**

Pick three or four anchor concepts spread across the range of the subject, and ask one question on each.
Then narrow into the branch that came back ambiguous.
Knowledge is a graph, not a ladder, so somebody can hold an advanced branch and miss a basic one.
Probing a single ordered line will classify them wrong.

Every probe is a production question from the first one.
Asking for definitions measures vocabulary, not understanding.
You may ask what level they think they are at, but treat it as a hint and never as evidence.

Stop when you can name where they stop, not when you have covered the subject.
A triage that eats the whole first session teaches nothing and costs the learner their patience.

Done when one node can be named as the frontier, backed by something the learner produced, and `COURSE.md` is written.

### 2. Map

Read `references/example-course.md`, then draw the graph in `MAP.md`.

Nodes are concepts.
An edge means the parent must be held before the child makes sense, so order by dependency and never by the chapter order of a book.
Anything outside the goal in `COURSE.md` does not get a node.
That is what keeps the map finite.

Mark every node the triage reached.
Leave the rest unmarked, which is what "not seen yet" looks like.

**Twenty five nodes is the ceiling.**
Past that it is two subjects, and the answer is a second course, not a bigger graph.

Show the map to the learner and let them correct it.
They hold things your twelve questions never reached.

Done when every probed node carries a state, the frontier is readable off the graph, and the learner has seen it.

### 3. Teach

**One node per lesson.** One.
Never open a node whose parents are not solid; that is what the edges are for.

Teach the knowledge with the difficulty turned **down**.
Working memory is small, and every gratuitous obstacle is memory the learner cannot spend on understanding.
Explain the way `COURSE.md` says to explain.

If the node holds something prose cannot show, build the page too, under **The visual complement**.
Most nodes do not, and that is the expected answer.

Ground it in a real source and link it.
Teaching from your own memory alone is how confident errors reach the learner.

Then turn the difficulty **up** and test, under **Proving it stuck**.
Effortful retrieval is what makes it last; a smooth explanation the learner nodded at does not.

Write the lesson to `lessons/000N-<slug>.md`, question and answer included, and the page beside it if the node earned one.
Then update `MAP.md`.

Done when the node's state in `MAP.md` is backed by something the learner produced, and the lesson file exists.

## The visual complement

Some things do not survive being written down.
A mechanism with parts that move, a state you have to walk through, a value you have to change to see what it does.
For those, and only for those, the lesson gets a second file next to it: `lessons/000N-<slug>.html`.

The two files are complementary and they do different jobs.
**The Markdown is the lesson.** It explains, it cites, it holds the check and the verdict, and `MAP.md` reads its evidence.
**The page shows one thing the Markdown cannot say**, and nothing else.

### When a node earns a page

Build it when the node holds one of these:

- **Something that moves.** Two queues draining at different rates, a packet crossing a network, a sort in progress.
- **State to step through.** A machine and its transitions, a stack growing and unwinding, a recursion opening and closing.
- **A knob.** One parameter the learner changes to watch the output change. This is the strongest case of the four, because turning it is faster than reading about it.
- **A shape.** A geometry, a memory layout, a graph, a waveform, anything spatial.

Skip it for a definition, a rule, a comparison, a convention or a piece of history.
**The default is no page.**
If you cannot say in one line what it shows that the paragraph above it does not, you have not found a reason, you have found a habit.
A page that only restyles the text it sits next to costs a file and teaches nothing.

### What the page has to be

- **One file, no dependencies.** CSS and JavaScript inline. No CDN, no web fonts, no build step, no server. It opens on a double click and it still works in a year with no network.
- **Opened for the learner.** After you write it, open it: `open` on macOS, `xdg-open` on Linux, `start` on Windows. A file they have to go and find is a file they do not read.
- **Linked from the lesson**, under `## Visual`, so the Markdown is the one door into the whole lesson.
- **Small enough to take in at once.** One idea per page, the same rule as one node per lesson. Two things to look at is two pages, or it is a sign the node is really two nodes.

### What the page must not be

- **Not the test.** It shows, it does not grade. The check stays in the Markdown, because a clickable answer is recognition, and recognition is the illusion this skill exists to break. A page may invite the learner to predict before they press the button; the verdict is still yours, in the conversation.
- **Not a prerequisite.** Write the explanation so a learner who never opens the page still gets the node. If the lesson stops making sense without it, the page has quietly become the lesson.
- **Not a rewrite of the text.** If it repeats the explanation with nicer type, delete it.

Read `references/lesson-template.html` before the first page of a course and copy its skeleton.
A self-contained file cannot share a stylesheet, so the template is the only thing making the pages look like one course instead of a pile of one-offs.

Never leave an angle-bracket placeholder in the page.
A browser reads `<node>` as an unknown tag and renders nothing, with no error to warn you, which is the same trap as angle brackets in a Mermaid label.
The template marks its slots with `{{double braces}}` for that reason, and every one of them has to be filled before the page is written.

## Proving it stuck

**The learner produces, never recognises.**
Recognition is free and it feels like understanding, which is exactly the illusion to break.
"It makes sense" is not evidence, and neither is "yes, I follow".

Three probes, in rising order of hardness:

1. **Explain it from memory**, with the text out of sight.
2. **Predict a case they have not seen.** This is the one that catches "it seemed logical".
3. **Find the fault in a broken example.** The hardest, and the best separator.

If you use multiple choice, every answer carries the **same number of words and characters**.
Uneven answers leak the correct one through their shape, and you will have measured your own formatting.

When they fail a probe, the node stays weak and the failure becomes its evidence line.
Do not move on.
A wrong belief you have found is worth more than a node you have coloured green.

## The artifacts

### `COURSE.md`

The compass.
If it runs past half a screen it has become a plan and stopped being a compass.

```markdown
# <subject>

**Why:** <the concrete thing they will be able to do>
**How to explain it to me:** <their stated preference>
**Out of scope:** <what this course will not cover>
```

### `MAP.md`

Plan and progress in one file, because they are the same object.

````markdown
## Map

```mermaid
graph TD
  A[First concept] --> B[Second concept]
  B --> C[Third concept]
  classDef solid fill:#2e7d32,color:#fff
  classDef weak fill:#f9a825,color:#000
  class A solid
  class B weak
```

## Evidence
- **First concept**: what the learner produced, in one line

## Sources
- [Title](https://example.com): what it is good for
````

Never put angle brackets inside a node label.
Mermaid reads them as HTML tags and the text vanishes, so write the real concept names in.

Three things the template does not say on its own:

- **State lives only in the graph.** The evidence line records what happened, never whether the node is solid. Say it twice and the two copies will disagree.
- **No class means not seen.** Only `solid` and `weak` are ever declared, so a new map is almost all bare nodes.
- **The frontier is not stored.** It is the weak node, or the first bare node whose parents are all solid. Anything you can derive will go stale if you write it down.

### `lessons/000N-<slug>.md`

```markdown
# <node>

<the explanation, in their preferred style>

## Visual
[<what it shows>](000N-<slug>.html)

## Source
[<title>](<url>): <what it covers>

## Check
**<the question>**
<what the learner answered>
<your verdict, and the correction if there was one>

## Result
<node>: <solid | still weak, and why>
```

`## Visual` is the only optional section, and it is absent from most lessons.
It carries a relative link, never an absolute path, so the course still works after the folder is moved or shared.

### `lessons/000N-<slug>.html`

Only when the node earned it, under **The visual complement**.
The skeleton is `references/lesson-template.html`.
Same number and same slug as the lesson it belongs to, so the pair sorts together and neither can be orphaned.

## Returning to a course

Read `COURSE.md` and `MAP.md` before anything else.
Re-teaching something already marked solid is the one failure that makes a tutor worthless.

1. Open with one probe on a node that went solid two or more sessions ago. Retrieval spaced over time is what moves knowledge into long-term storage, and it also catches a node you marked green too early.
2. If that probe fails, the node goes back to weak and it becomes today's lesson.
3. Otherwise take the frontier off the graph and run **3. Teach** on it.
4. Update `MAP.md` at the end of the session, never at the start.

## Hard rules

- One node per lesson, and never a node whose parents are unheld.
- Twelve probe questions in the triage, at most. A partial picture you can name beats a complete one the learner walked out of.
- Never mark a node solid on self-report. The learner has to produce something.
- Difficulty down while teaching, up while testing. Reversing this is the most common way to make a lesson feel rigorous and teach nothing.
- Cite a source in every lesson. Never teach a topic entirely from your own recall.
- A page only when the node holds movement, state, a knob or a shape. The default is no page, and "it would look good" is none of the four.
- The page shows and the Markdown tests. The check never moves into the browser, because a clickable answer is recognition.
- Every page is one self-contained file, no network and no build, opened for the learner. The lesson still teaches the node when the page is never opened.
- State lives in the graph, evidence lives in the list, and the frontier lives in neither.
- Twenty five nodes is a course. More than that is two courses.
- File names, directory name, headings and Mermaid keywords are always English, exactly as written here. Only what the learner reads follows their language.
- The map holds what the goal in `COURSE.md` needs, and nothing else. An interesting node that serves no goal is the fastest way to a map nobody finishes.
