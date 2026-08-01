---
name: 7dejv-skill-contract-builder
description: Expand a draft 7DEJV skill into a complete execution contract with explicit inputs, outputs, tools, errors, stop conditions, examples, tests and safety rules. Use when a skill is only a short outline or fails quality review.
---

# 7DEJV Skill Contract Builder

## Procedure
1. Preserve the original purpose and triggering context.
2. Define required and optional inputs without inventing domain data.
3. Define an exact output structure and status model.
4. List allowed tools, dependencies and permissions.
5. Add error handling, partial-result behavior and stop conditions.
6. Add positive, boundary, negative and safety examples.
7. Define measurable acceptance criteria and required tests.
8. Identify unresolved assumptions for human review.

## Required sections
- Purpose and trigger,
- Inputs,
- Tools and dependencies,
- Procedure,
- Output contract,
- Errors and stop conditions,
- Safety and prohibited actions,
- Examples,
- Tests and acceptance criteria.

## Output
Return the proposed complete `SKILL.md`, a change summary, unresolved questions and status `DRAFT` or `READY_FOR_REVIEW`.

## Limits
Do not change the business purpose, widen permissions, invent evidence or mark a skill approved. Stop with `HOLD` when the source intent or required dependencies are unclear.
