# Contributing to Claude Skills

Thank you for your interest in contributing to the Claude Skills repository! We welcome new skills, improvements to existing skills, and bug fixes that enhance the Claude ecosystem.

## Ways to Contribute
1. **Reporting Issues:** Found a bug in a skill? The output is unpredictable? Please open an issue.
2. **Improving Documentation:** Fix typos, add examples, or clarify skill instructions.
3. **Submitting New Skills:** Have a great workflow you use with Claude? Package it as a skill and share it!

## Anatomy of a Skill
Every skill on this repository must be placed in its own directory and adhere to the Agent Skills standard:

```
skill-name/          # Directory must be named after the skill (kebab-case)
├── SKILL.md         # Required. The Claude prompt containing YAML frontmatter
├── README.md        # Required. Instructions for human users on how to use it
```

Check out the `_template/` folder in the root of the repository as a starting point.

## Proposing a New Skill
1. **Open an Issue:** Before spending time building out a complex skill or porting existing knowledge bases, open an Issue or Discussion to see if it aligns with the goals of this repo and isn't a duplicate.
2. **Copy the Template:** Duplicate the `_template` folder and rename it to your skill idea.
3. **Write the SKILL.md:** Include the required YAML frontmatter (with `name` and `description`). Write clear, structured instructions mapping out the behavioral adjustments or knowledge. Keep the instructions directed at the AI agent (Claude).
4. **Write the README.md:** Write instructions directed at the human user explaining value propositon, trigger examples, and how it works under the hood.

### The `SKILL.md` Frontmatter Requirement
To ensure the skill imports cleanly into Claude.ai, your `SKILL.md` must start with the following YAML frontmatter:

```yaml
---
name: your-skill-name
description: Explicit trigger conditions and details stating exactly when Claude should utilize this skill.
---
```

## Pull Request Process
1. Fork the repository and create your feature branch from `main`.
2. Format your files, double checking that the YAML frontmatter uses proper markdown blocks in `SKILL.md`.
3. Submit a Pull Request. Ensure the description clearly outlines the changes made and the problem the skill addresses.
4. Wait for a review from the maintainers.

## Code of Conduct
Please be respectful and patient when interacting in Issues and Pull Requests. All contributors are expected to uphold a welcoming and inclusive environment.
