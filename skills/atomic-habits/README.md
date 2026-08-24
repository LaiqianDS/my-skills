# Atomic Habits

Turns Claude into a habit designer instead of a habit summariser: it interviews you, diagnoses which stage of your habit loop is broken, and hands you a written plan you can reopen.

## What it does

Ask most assistants for help with a habit and you get the four laws as a listicle.
This skill asks you first, diagnoses the stage that is actually failing, and ends in a document.

- **It asks, you answer**: up to three rounds of three questions. Say "just give me the plan" at any point and it writes what it has, with every gap listed as an assumption instead of passed off as your answer.
- **A document, not a chat**: the plan comes back as `habit-plan-<name>.md` when Claude can write files, and in the reply when it cannot.
- **Diagnosis before prescription**: pins down your cue, craving, response, and immediate reward, with a time and a place, before proposing anything.
- **Environment over willpower**: every prescription must be a change to environment, schedule, or wording that you could make today. "Be more disciplined" is not an allowed answer.
- **A floor and a recovery rule**: every plan ships with a two-minute version and the never-miss-twice rule, so a bad day does not end the habit.
- **A ladder that moves on behaviour**: each harder version unlocks on something you did, never on a date. A calendar promotes a habit that is already failing.
- **Identity framing**: the plan opens with "I am someone who...", so the rest reads as evidence rather than as a list of tasks.
- **Come back later**: bring the plan back and it reviews it, moves you a rung up or down, and rewrites the same file.
- **Loads what it needs**: the procedure is always in context, the techniques only when your branch calls for them.

## What you get

```
# Habit plan: <your habit>

## Identity        who you become by doing it
## The loop        cue with a time and a place, craving, response, immediate reward
## The floor       the two-minute version that survives your worst day
## Techniques      at most two, on the stage that is broken, in your own terms
## The ladder      harder versions, each with the behaviour that unlocks it
## Maintenance     never miss twice, one metric, a review date
## Assumptions     anything you did not answer, written down
## Log             what changed at each review
```

## Use cases

- Building a new habit that keeps failing to start
- Quitting a habit that self-control has not fixed
- Working out why a routine that used to run collapsed
- Restarting after a broken streak
- A habit that still runs but has gone boring, sloppy, or all-consuming
- Turning a goal ("run a marathon") into a system ("train 30 minutes each morning")
- Reviewing a plan you wrote weeks ago and raising the bar
- Not for addiction, self-harm, or disordered eating. The skill will say so and point you to a professional.

## Example prompts

- "I have tried to start going to the gym four times this year and it never lasts past week two"
- "Help me stop checking my phone first thing in the morning"
- "I have been doing this habit for three weeks and I see no results"
- "My reading habit has got boring, I keep skipping it"
- "Turn my goal of learning Python into a system"
- "Here is my habit plan from last month, I held it three weeks out of four"

## How it works

```
atomic-habits/
├── SKILL.md                      always loaded when the skill triggers
└── references/
    ├── build.md                  read only when you are building a habit
    ├── break.md                  read only when you are quitting one
    ├── sustain.md                read only when the habit runs but has gone stale
    └── example-plan.md           read when the document gets written
```

`SKILL.md` holds what every case needs, in the order the model needs it:

1. **The loop and the four laws** - the table that maps each stage to its law and its inversion.
2. **Bundled files** - which reference to open for your case, and which two to leave shut.
3. **Three frames** - compounding, systems over goals, identity over outcome. These apply to every case.
4. **The procedure** - six steps, each ending on a condition that must be true before the next one starts. Step 1 is the interview, step 6 writes the document.
5. **The plan document** - the template that every answer has to fill.
6. **Update an existing plan** - the branch for a plan you bring back.
7. **Hard rules** - the constraints that keep the answer specific.

The split is not tidiness. Skills load in stages: the frontmatter always, `SKILL.md` when the skill triggers, and a reference file only when Claude reads it. The three branches are mutually exclusive, so a single file makes every conversation pay for two sets of techniques it will not use.

The procedure sits above the reference on purpose: reference placed first buries the steps, and the steps are what make the skill more than a book summary.
The question rounds are capped for the same reason a habit starts at two minutes. An interview you abandon produces nothing, so a partial plan with its gaps marked beats a perfect one you never reached.

## Install

**Claude.ai**: zip the folder, not the files inside it, and upload the zip in **Customize > Skills**.
Needs code execution enabled in **Settings > Capabilities**, which is what lets Claude read the reference files.

```bash
cd skills && zip -r atomic-habits.zip atomic-habits
```

**Claude Code**:

```bash
# The whole collection
claude plugin marketplace add LaiqianDS/laiqiands-skills
claude plugin install laiqiands-skills@laiqiands

# Or this skill alone, from a clone
ln -s "$PWD/laiqiands-skills/skills/atomic-habits" ~/.claude/skills/atomic-habits
```

## Credits

Based on *Atomic Habits* by [James Clear](https://jamesclear.com/atomic-habits).
Skill definition by [Laiqian Ji](https://github.com/LaiqianDS), condensed from personal reading notes.
