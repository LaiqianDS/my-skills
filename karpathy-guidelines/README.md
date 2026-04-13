# Karpathy Guidelines

Behavioral guidelines for reducing common LLM coding mistakes, derived from Andrej Karpathy's observations.

## What it does

When writing, reviewing, or refactoring code, this skill enforces four principles:

- **Think before coding**: Surface assumptions, present interpretations, push back when warranted
- **Simplicity first**: Minimum code that solves the problem — no speculative features or abstractions
- **Surgical changes**: Touch only what the request demands, preserve surrounding style and structure
- **Goal-driven execution**: Convert vague tasks into verifiable success criteria before implementing

## Use cases

- Implementing new features
- Bug fixes and debugging sessions
- Code review and refactoring
- Any task where overcomplication or scope creep is a risk

## Example prompts

- `/karpathy-guidelines` before starting a complex implementation
- "Refactor this module" — skill prevents unrelated cleanup and scope expansion
- "Add validation to this form" — skill converts the ask into testable success criteria first

## Install

Download this folder as a ZIP and upload it in **Claude.ai > Customize > Skills**.

## Credits

Based on [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls. Skill definition by [forrestchang](https://github.com/forrestchang/andrej-karpathy-skills).
