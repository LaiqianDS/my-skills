---
name: atomic-habits
description: Design, diagnose, or repair a habit with the Atomic Habits framework, and return it as a written plan document. Use when someone wants to build a habit, quit a bad one, work out why a routine collapsed, push past boredom with a habit that stopped working, turn a goal into a system, or review and update a habit plan written earlier.
---

# Atomic Habits

Habits are designed, not willed.
Every habit runs the same four-stage **loop**, and every fix is a change to one stage of that loop.

Your job is to find the broken stage and change it, then hand the user a plan they can reopen.
A summary of the four laws is not the job, and neither is advice that lives only in the conversation.
You get the specifics by asking, in short rounds, and the work ends in the document under **The plan document**.

## The loop and the four laws

| Stage | Build a good habit | Break a bad one |
|---|---|---|
| **Cue** | 1st law: make it obvious | make it invisible |
| **Craving** | 2nd law: make it attractive | make it unattractive |
| **Response** | 3rd law: make it easy | make it hard |
| **Reward** | 4th law: make it satisfying | make it unsatisfying |

Building applies a law.
Breaking applies its **inversion**: same loop, opposite direction.

## Bundled files

The techniques are not in this file.
They sit in three reference files, one per branch.
Read the one that matches the user's case and leave the other two unread, because reading all three costs context and buys nothing: the branches never apply at once.

| The user wants to | Read |
|---|---|
| Build a habit | `references/build.md`, the four laws forward |
| Quit a habit | `references/break.md`, the four laws inverted |
| Fix a habit that already runs but has gone stale, boring, sloppy, or all-consuming | `references/sustain.md` |

`references/example-plan.md` holds one filled plan and the three things a review changes in it.
Read it at step 6, before writing a document.

One case skips the procedure: a user who comes back with a plan written earlier.
That one goes to **Update an existing plan**.

## Three frames that come before any technique

Every branch needs these.
Apply them whatever the user asks.

**Small compounds.**
1% better daily is 37x in a year (`1.01^365 = 37.78`), 1% worse is near zero (`0.99^365 = 0.03`).
Progress is not linear: results bank up out of sight, the way a room climbs from -3° to 0° with the ice unmoved until it melts all at once.
Most people quit just before the inflection.
When someone reports weeks of effort and no results, this is the answer, not a new plan.

**Systems, not goals.**
A goal is the result wanted; a system is the process that produces it.
Winners and losers share the same goals, so the goal was never what separated them.
A goal is also a one-off change that postpones happiness ("I'll be happy when...").
Fix the system and the problem stops coming back.

**Identity, not outcome.**
Three layers: outcome (be thin), process (go to the gym), identity (be an athlete).
Lasting change runs from identity outward, and the relationship is two-way: people do what they believe they are.
Each repetition is a **vote** for the person the user is becoming.
So decide who they want to be, then let small wins be the evidence.

## Procedure

Work these in order.
Each step names what must be true before you start the next one.
Step 1 is the user's; steps 2 to 6 are yours, so never ask the user which stage is broken or which technique to apply.

### 1. Interview in rounds

Ask in rounds of **at most three questions**, and wait for the answer before opening the next round.
**Three rounds is the ceiling.**
When the third round closes, or the moment the user asks for the plan, write it with what you have and record every gap under **Assumptions**.

| Round | What you are after |
|---|---|
| 1 | **The loop**: what fires it, at what time and in what place, what they do, and what they get **immediately** after. |
| 2 | **The evidence**: what happened the last times it broke, and what their worst day looks like. |
| 3 | **The stakes**: who they want to become, what they could enjoy right after the habit, and what the environment will not let them change. |

Never ask what the user has already told you.
A repeated question reads as not listening, and it spends a round you cannot get back.

Done when the four stages hold the user's own details and the cue has a **time and a place**, or the ceiling is reached and the missing pieces are written down as assumptions.
A cue you cannot put on a clock or a map is not a cue yet, it is a topic.

### 2. Name the broken stage

Decide which of the four stages is failing, and say which.
A habit that never starts is usually a cue or a friction problem.
A habit that starts and dies is usually a reward problem.

Done when one stage is named as the failure point and you have quoted the user's own account as the evidence for choosing it.

### 3. Prescribe on that stage

Read the reference file for the user's branch now, and take techniques from the failing stage first.
Never prescribe from memory: the technique has to come from the file, or it comes out as a book summary.
Name at most two per stage, because a plan with ten moves is a reading list, not a plan.
Instantiate each one with the user's own cue, place, and reward.

Done when every prescription is a change to environment, schedule, or wording that the user could make today, and none of them asks for more motivation.

### 4. Set the floor and the recovery rule

Shrink the habit to a two-minute version, and state the never-miss-twice rule for this specific habit.
The streak will break; what decides the outcome is the speed of return.

Done when both are written out in the user's own terms, not as general advice.

### 5. Build the ladder

Take the two-minute floor as rung zero and write the two or three rungs above it, using *Scale by stages* under the 3rd law in `references/build.md`.

Each rung carries the condition that unlocks it, and that condition is a **behaviour, never a date**.
A date arrives whether or not the habit held, so a calendar promotes a habit that is already failing.

Done when every rung reads "when [observable behaviour holds], I move to [next version]", and the top rung still sits short of the user's stated ambition.
Leave room above the ladder: a ceiling reached is boredom scheduled.

### 6. Write the plan

Read `references/example-plan.md`, then fill in the template under **The plan document** and hand it over.
Identity opens the document, so the rest reads as evidence rather than as a list of tasks.

Write it to `habit-plan-<slug>.md` in the working directory when you can write files, and print it in the reply when you cannot.
Say where it went.

Done when every section of the template is filled with the user's own terms, and anything you supplied for them appears under **Assumptions** instead of passing as their answer.

## The plan document

The deliverable.
One habit per plan.

```markdown
# Habit plan: <the habit, in the user's words>

## Identity
I am someone who <identity>.
Each repetition is a vote for it.

## The loop
- **Cue**: <time> at <place>, after <anchor habit>
- **Craving**: <what they are actually after>
- **Response**: <the habit, exactly as it will be done>
- **Reward**: <what lands immediately after>

## The floor
<the two-minute version>
This is the version for the worst day, and it counts as a full repetition.

## Techniques
Broken stage: <stage>, because <the user's own words>.
- **<technique>**: <instantiated with their cue, place, or reward>
- **<technique>**: <instantiated with their cue, place, or reward>

## The ladder
| Rung | Version | Unlocks when |
|---|---|---|
| 0 | <the floor> | now |
| 1 | <harder version> | <observable behaviour> |
| 2 | <harder version> | <observable behaviour> |

## Maintenance
- **Never miss twice**: <what "twice" means for this habit>
- **Metric**: <one representative measure>, which must not become the target itself
- **Review**: <date>, against this document

## Assumptions
- <anything the user did not answer, written as what you assumed>

## Log
- <date>: plan written
```

Three things the template does not say on its own:

- **Set the review date**: one week out for a new habit, one month out once a rung has held. A review with no date never happens, and a ladder nobody reviews never moves.
- **On the breaking branch, two sections change meaning**: the floor becomes the smallest cut the user can hold on their worst day, and the ladder climbs by removing more, not by doing more.
- **More than one habit**: plan the first and park the rest under a `## Waiting list` heading, each with the condition that starts it, which is the current habit held through one full review period. A document that details two habits at once breaks the law of least effort before the user has started.

## Update an existing plan

When the user returns with a plan, work from it.
Rewriting it from scratch throws away the only record of what already held.
The end of `references/example-plan.md` shows the three things a review changes and the one it does not.

1. Read the document, then ask **one** round of at most three questions: what held, what broke, and what changed around them.
2. Move on the ladder. One rung up when the current rung held through the review period. One rung **down** when it broke twice or more, plus one change to the failing stage. Pushing a rung that is already failing is how a habit dies.
3. Add a rung on top whenever the ladder runs out, so there is always something above.
4. Rewrite the same file. Keep the identity line unless the user changed it, clear the assumptions the round answered, and append one line to the log.

Done when the document reflects the review and the ladder still has an unreached rung.

## Hard rules

- Three questions per round, three rounds at most. A plan built from partial answers with the gaps written down beats a full interview the user walked out of.
- Never present an assumption as the user's answer. What you filled in for them goes under **Assumptions**, where they can correct it.
- One habit per plan, and one rung at a time. Two habits detailed at once is the same mistake as starting at rung two.
- Instantiate every technique with the user's own cue, place, and reward. A technique named without their specifics is a summary, not advice.
- Prescribe environment changes first, and reserve willpower for the gap the environment cannot close. **Friction** decides behaviour, not motivation.
- Size the first version so it survives their worst day, not their best one.
- When the subject is addiction, self-harm, or disordered eating, say plainly that this framework is not the right tool and point to a professional.

