---
name: 7dejv-repository-quality-audit-skill
description: Audit a 7DEJV repository by comparing declared capabilities with actual files, schemas, tests, workflow artifacts and runtime evidence. Use before merge, release, readiness claims or major architectural changes.
---

# 7DEJV Repository Quality Audit Skill

## Inputs
- repository tree or changed-file list,
- relevant README and status files,
- agent, skill and workflow definitions,
- test artifacts and CI results when available.

## Procedure
1. Inventory actual files.
2. Compare documentation claims with repository evidence.
3. Score structure, agents, skills, workflows, schemas, tests, security, maintainability and runtime readiness.
4. Cite exact paths for every material finding.
5. Return `PASS`, `HOLD` or `BLOCKED` using the quality gate rules.

## Output
Return `overall_score`, category scores, findings by severity, evidence paths, missing artifacts, recommended actions and readiness statuses.

## Rules
Do not infer completed tests from test definitions. Do not infer runtime readiness from design documents. Missing evidence lowers the score and may force `HOLD`.
