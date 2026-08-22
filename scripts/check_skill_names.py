#!/usr/bin/env python3
"""Check the two skill invariants that `claude plugin validate --strict` misses.

1. Every directory under skills/ contains a SKILL.md. A directory without one is
   silently ignored at install time, so the skill ships as nothing.
2. The `name` in the frontmatter matches the directory name.

Standard library only, so contributors need no packages to run this.
"""

import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"
NAME_PATTERN = re.compile(r"^name:[ \t]*(.+?)[ \t]*$", re.MULTILINE)


def frontmatter_name(skill_md: Path) -> str | None:
    """Return the `name` field, or None if the frontmatter has no usable one."""
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    match = NAME_PATTERN.search(text[4:end])
    if match is None:
        return None
    return match.group(1).strip("\"'")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"error: no skills directory at {SKILLS_DIR}", file=sys.stderr)
        return 1

    errors = []
    checked = 0

    for entry in sorted(SKILLS_DIR.iterdir()):
        if not entry.is_dir():
            continue

        skill_md = entry / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"skills/{entry.name}/: no SKILL.md, so nothing ships")
            continue

        checked += 1
        name = frontmatter_name(skill_md)
        if name is None:
            errors.append(f"skills/{entry.name}/SKILL.md: no `name` in frontmatter")
        elif name != entry.name:
            errors.append(
                f"skills/{entry.name}/SKILL.md: name is '{name}' "
                f"but the directory is '{entry.name}'"
            )

    for error in errors:
        print(f"error: {error}", file=sys.stderr)

    print(f"checked {checked} skill(s), found {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
