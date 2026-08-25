# Claude Skills

A collection of custom skills for [Claude](https://claude.ai) by [Laiqian Ji](https://github.com/LaiqianDS).

Skills are modular instruction packages that extend Claude's capabilities on specialized tasks.
Each skill teaches Claude a repeatable workflow, whether that's writing high-conversion cold emails, structuring technical documents, or automating a specific analysis.

## Skills

| Skill | Description |
|-------|-------------|
| [atomic-habits](./skills/atomic-habits/) | Design, diagnose, or repair a habit with the Atomic Habits framework. Finds the broken stage of the habit loop before prescribing, and answers with environment changes rather than willpower. |
| [cold-email](./skills/cold-email/) | Generate cold emails, DMs, and follow-up sequences with a proven 40%+ reply rate framework. Handles B2B outreach, investor emails, job pitches, scholarship asks, and networking. |
| [teach-me](./skills/teach-me/) | Teach a subject one to one across sessions. Probes what you already hold, maps the subject as a dependency graph, then teaches one node at a time and makes you prove it stuck. |

## Installation

### Claude Code (recommended)

This repository is a Claude Code marketplace.
Installing the plugin brings in every skill at once, and `/plugin update` keeps them current.

```bash
claude plugin marketplace add LaiqianDS/laiqiands-skills
claude plugin install laiqiands-skills@laiqiands
```

To install a single skill instead, symlink it into `~/.claude/skills/`:

```bash
git clone https://github.com/LaiqianDS/laiqiands-skills.git
ln -s "$PWD/laiqiands-skills/skills/cold-email" ~/.claude/skills/cold-email
```

### Claude.ai

1. Download an individual skill folder from `skills/` as a ZIP
2. Make sure the ZIP contains the skill folder at root (e.g., `cold-email/SKILL.md`)
3. Go to **Customize > Skills** in [Claude.ai](https://claude.ai/customize/skills)
4. Upload the ZIP (or rename to `.skill`)
5. Enable the skill

### API

Skills are available via the `/v1/skills` endpoint.
See [Skills API docs](https://docs.claude.com) for integration details.

## Repository Structure

```
laiqiands-skills/
├── .claude-plugin/
│   ├── marketplace.json   # Marketplace manifest
│   └── plugin.json        # Plugin manifest. Skills are auto-discovered from skills/
├── skills/                # One directory per skill. Everything here ships.
│   ├── atomic-habits/
│   ├── cold-email/
│   └── teach-me/
└── _template/             # Starting point for a new skill. Not installed.
```

Each skill follows the [Agent Skills standard](https://agentskills.io):

```
skill-name/
├── SKILL.md          # Required. YAML frontmatter + instructions.
├── README.md         # Required here. Human-facing usage notes.
├── scripts/          # Optional. Executable code for deterministic tasks.
├── references/       # Optional. Supplemental docs loaded as needed.
└── assets/           # Optional. Templates, fonts, icons.
```

## Validation

Every push and pull request runs `claude plugin validate --strict` plus a check that each skill's `name` matches its directory.
Run the same checks locally before opening a PR:

```bash
claude plugin validate . --strict
claude plugin validate skills --strict
python3 scripts/check_skill_names.py
```

## Contributing

If you find a bug or want to suggest an improvement to a skill, open an issue.
PRs welcome for fixes.
If you want to add a new skill, open an issue first to discuss scope.
Please review our [Contribution Guidelines](CONTRIBUTING.md) to get started with creating a new skill using the provided `_template/`.

## License

MIT
