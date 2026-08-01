---
name: 7dejv-skill-linter
description: Perform deterministic structural checks on 7DEJV skill folders and SKILL.md files. Use before skill review, merge, release or benchmark execution.
---

# 7DEJV Skill Linter

## Procedure
1. Discover every `SKILL.md` under the configured skills directory.
2. Parse frontmatter and headings.
3. Apply structural, naming, reference and secret-detection rules.
4. Detect duplicate skill names.
5. Generate JSON and Markdown reports.
6. Return a non-zero exit code when blocking errors exist.

## Required checks
1. A skill folder contains `SKILL.md`.
2. YAML frontmatter starts and ends correctly.
3. `name` and `description` exist.
4. Name uses lowercase letters, digits and hyphens only.
5. Skill names are unique in the repository.
6. Description explains both capability and triggering context.
7. Required sections exist: inputs, procedure, output, limits or stop conditions.
8. Referenced paths exist.
9. No obvious secrets, tokens, passwords or private keys are present.
10. Test or audit paths declared by the skill exist.

## Output
Return machine-readable findings with `path`, `rule_id`, `severity`, `message` and `suggested_fix`.

## Limits
Do not modify audited skills. Do not print detected secret values. Do not treat warnings as proof of failure unless the configured quality gate requires it.

## Status
Return `PASS` only when no `ERROR` findings exist. Warnings require review but do not automatically block.
