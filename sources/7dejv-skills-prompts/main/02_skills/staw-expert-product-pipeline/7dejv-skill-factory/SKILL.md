---
name: 7dejv-skill-factory
description: Create, improve, test and audit Agent Skills for 7DEJV. Use whenever a workflow or agent needs a new SKILL.md, an existing skill needs optimization, or skill triggering, tests, safety and repository compliance must be evaluated.
---

# 7DEJV Skill Factory

## Procedure
1. Search the repository for duplicates and reusable components.
2. Capture intent, triggering contexts, expected output and dependencies.
3. Define the input/output contract and stop conditions.
4. Create a self-contained skill folder with `SKILL.md` and only necessary resources.
5. Add realistic positive, boundary and negative test prompts.
6. Compare skill-assisted results against a baseline.
7. Improve the skill and repeat the audit.
8. Prepare a report and PR.

## Required checks
- valid YAML frontmatter,
- unique lowercase hyphenated name,
- precise triggering description,
- minimal permissions,
- no secrets or client data,
- no copied external code without license review,
- no destructive behavior,
- measurable success criteria.

## Output
Return the created paths, test coverage, findings, unresolved risks and status: `DRAFT`, `TESTING`, `HOLD`, `BLOCKED`, `READY_FOR_REVIEW` or `APPROVED`.

## Limits
Do not overwrite an approved skill without a versioned review. Do not copy external code without license and security checks. Do not store secrets, widen permissions or mark a skill `APPROVED` without completed tests and human approval.
