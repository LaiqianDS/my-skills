# Atomic Habits

Turns Claude into a habit designer instead of a habit summariser: it diagnoses which stage of your habit loop is broken before it prescribes anything.

## What it does

Ask most assistants for help with a habit and you get the four laws as a listicle.
This skill forces the diagnostic first, then prescribes on the stage that is actually failing.

- **Diagnosis before prescription**: pins down your cue, craving, response, and immediate reward, with a time and a place, before proposing anything.
- **Environment over willpower**: every prescription must be a change to environment, schedule, or wording that you could make today. "Be more disciplined" is not an allowed answer.
- **A floor and a recovery rule**: every plan ships with a two-minute version and the never-miss-twice rule, so a bad day does not end the habit.
- **Identity framing**: plans come back as "I am someone who...", not as a target to hit.
- **Self-contained**: one file, no attachments. The whole book framework travels with the skill.

## Use cases

- Building a new habit that keeps failing to start
- Quitting a habit that self-control has not fixed
- Working out why a routine that used to run collapsed
- Restarting after a broken streak
- A habit that still runs but has gone boring, sloppy, or all-consuming
- Turning a goal ("run a marathon") into a system ("train 30 minutes each morning")
- Not for addiction, self-harm, or disordered eating. The skill will say so and point you to a professional.

## Example prompts

- "I have tried to start going to the gym four times this year and it never lasts past week two"
- "Help me stop checking my phone first thing in the morning"
- "I have been doing this habit for three weeks and I see no results"
- "My reading habit has got boring, I keep skipping it"
- "Turn my goal of learning Python into a system"

## How it works

Everything lives in a single `SKILL.md`, in the order the model needs it:

1. **The loop and the four laws** - the table that maps each stage to its law and its inversion.
2. **Three frames** - compounding, systems over goals, identity over outcome. These apply to every case.
3. **The procedure** - five steps, each ending on a condition that must be true before the next one starts.
4. **Hard rules** - the constraints that keep the answer specific.
5. **Three reference sections** - the four laws forward, the four inversions, and the advanced tactics. Only the section matching your branch gets used.

The procedure sits above the reference on purpose: reference placed first buries the steps, and the steps are what make the skill more than a book summary.

## Install

**Claude.ai**: upload `SKILL.md` in **Customize > Skills**.

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
