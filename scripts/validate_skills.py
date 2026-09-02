#!/usr/bin/env python3
"""Validate the minimum repository contract for bundled OpenClaw skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)


def parse_simple_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    metadata = parse_simple_frontmatter(text)
    name = metadata.get("name", "")
    description = metadata.get("description", "")

    if not name:
        errors.append(f"{skill_file}: missing frontmatter name")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"{skill_file}: invalid skill name {name!r}")
    elif name != skill_dir.name:
        errors.append(f"{skill_file}: name must match directory {skill_dir.name!r}")

    if not description:
        errors.append(f"{skill_file}: missing frontmatter description")

    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (skill_dir / target).resolve()
        if not resolved.exists():
            errors.append(f"{skill_file}: broken local reference {target!r}")

    return errors


def main(root: Path) -> int:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        print("missing skills directory", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_dirs:
        print("no skill directories found", file=sys.stderr)
        return 1

    errors = [error for path in skill_dirs for error in validate_skill(path)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"validated {len(skill_dirs)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(__file__).resolve().parents[1]))
