# Contributing

## Propose a skill

Open a Skill idea issue and describe:

1. the user problem;
2. example requests that should trigger the skill;
3. the expected result;
4. required tools or services;
5. privacy, safety, or portability concerns;
6. how the result can be verified.

## Pull requests

- Keep each pull request focused on one skill or one repository concern.
- Use generic examples and placeholders instead of personal data.
- Never commit credentials, tokens, private document IDs, private URLs, or local authentication files.
- Update documentation when behavior changes.
- Run `python3 scripts/validate_skills.py` and `python3 -m unittest discover -s scripts -p 'test_*.py'` before submitting.

## Skill layout

Each skill must contain a `SKILL.md` with `name` and `description` frontmatter. Put branch-only details in `references/`, deterministic helpers in `scripts/`, and reusable output files in `assets/` or `examples/` as appropriate.

## Review criteria

A skill is ready to release when its trigger, workflow, dependencies, limitations, and verification steps are clear; local references resolve; validation passes; and a privacy/security review finds no sensitive data.
