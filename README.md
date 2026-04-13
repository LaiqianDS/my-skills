# Claude Skills

A collection of custom skills for [Claude](https://claude.ai) by [Laiqian Ji](https://github.com/LaiqianDS).

Skills are modular instruction packages that extend Claude's capabilities on specialized tasks. Each skill teaches Claude a repeatable workflow, whether that's writing high-conversion cold emails, structuring technical documents, or automating a specific analysis.

## Skills

| Skill | Description |
|-------|-------------|
| [cold-email](./cold-email/) | Generate cold emails, DMs, and follow-up sequences with a proven 40%+ reply rate framework. Handles B2B outreach, investor emails, job pitches, scholarship asks, and networking. |

## Installation

### Claude.ai

1. Download this repo as a ZIP, or download an individual skill folder as a ZIP
2. Make sure the ZIP contains the skill folder at root (e.g., `cold-email/SKILL.md`)
3. Go to **Customize > Skills** in [Claude.ai](https://claude.ai/customize/skills)
4. Upload the ZIP (or rename to `.skill`)
5. Enable the skill

### Claude Code

```bash
# Option 1: Clone and symlink
git clone https://github.com/LaiqianDS/my-skills.git
ln -s $(pwd)/my-skills/cold-email ~/.claude/skills/cold-email

# Option 2: Copy directly
cp -r my-skills/cold-email ~/.claude/skills/
```

### API

Skills are available via the `/v1/skills` endpoint. See [Skills API docs](https://docs.claude.com) for integration details.

## Skill Structure

Each skill follows the [Agent Skills standard](https://agentskills.io):

```
skill-name/
├── SKILL.md          # Required. YAML frontmatter + instructions.
├── scripts/          # Optional. Executable code for deterministic tasks.
├── references/       # Optional. Supplemental docs loaded as needed.
└── assets/           # Optional. Templates, fonts, icons.
```

## Contributing

If you find a bug or want to suggest an improvement to a skill, open an issue. PRs welcome for fixes. If you want to add a new skill, open an issue first to discuss scope.

## License

MIT
