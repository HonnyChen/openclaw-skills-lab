# OpenClaw Skills Lab

A community-oriented collection of reusable OpenClaw skills developed from practical workflows.

這是一個將實際需求整理成可重複使用 OpenClaw Skills 的實驗室。公開內容會先完成去識別化、安全檢查與基本驗證。

## Skills

| Skill | Purpose | Status |
| --- | --- | --- |
| [`travel-itinerary-spreadsheet-format`](skills/travel-itinerary-spreadsheet-format/) | Create or normalize detailed travel itinerary spreadsheets in an accessible existing sheet or a portable Excel workbook, with a consistent 12-column landscape layout. | Draft |

## Install a skill

1. Copy the selected directory under `skills/` into your OpenClaw workspace skills directory.
2. Keep the directory name the same as the skill `name` in `SKILL.md`.
3. Run `openclaw skills check --agent <agent-id>` to verify that the skill is discoverable and usable.
4. Start a new agent turn and request a task matching the skill description.

OpenClaw and installation details can vary by deployment. Review each skill's README and requirements before use.

## Quality and publication policy

Every published skill should:

- solve a reusable problem with explicit triggers and outcomes;
- avoid personal accounts, private document identifiers, credentials, tokens, and internal-only paths;
- document required tools and limitations;
- include a verification workflow;
- pass repository validation and a clean review before release.

## Collaboration

- Concept and product direction: **Honny**
- Skill implementation and documentation: **蝦蝦, an OpenClaw agent**

Ideas and improvements are welcome through GitHub Issues and Pull Requests. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
