---
name: 7dejv-stage-registry-builder
description: Build and validate a machine-readable registry mapping 7DEJV workflow stages to skills, required inputs, allowed statuses, human gates and next stages. Use when routing must become deterministic.
---

# 7DEJV Stage Registry Builder

## Inputs
- ordered workflow stages,
- transition matrix,
- skill catalog,
- required data for each stage,
- human approval rules.

## Procedure
1. Create one registry entry per stage.
2. Assign exactly one primary skill or explicit human-only handler.
3. Define allowed statuses and legal next stages.
4. Define required input fields and human-gate behavior.
5. Mark terminal stages explicitly.
6. Compare all stage and status values with JSON Schema.
7. Validate reachability and detect dead ends or illegal cycles.

## Output
Return a versioned JSON registry, validation findings, unreachable stages, missing skills and status `PASS`, `HOLD` or `BLOCKED`.

## Errors and stop conditions
Return `BLOCKED` for unknown skills, impossible transitions, duplicate stages or routes bypassing required human approval.

## Limits
Do not infer transitions that are absent from the approved workflow. Do not assign an unapproved skill to a production route.

## Examples
`ANALYZED` may route only to `COMPOSITION_EVIDENCE` after `PASS` and requires stored evidence and source URLs.

## Tests and acceptance criteria
Every schema stage must exist exactly once in the registry and every non-terminal stage must have at least one legal next stage.
