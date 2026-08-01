---
name: 7dejv-agent-overlap-detector
description: Detect overlapping responsibilities, duplicated ownership and missing boundaries across 7DEJV agent profiles and workflow stages. Use before adding agents, restructuring workflows or approving an agent catalog.
---

# 7DEJV Agent Overlap Detector

## Inputs
- agent profiles or registry,
- workflow stage registry,
- skill catalog,
- ownership rules.

## Procedure
1. Extract responsibilities, inputs, outputs, stages and tools for every agent.
2. Compare responsibility and stage overlap.
3. Distinguish valid collaboration from duplicate ownership.
4. Detect stages with zero or multiple primary owners.
5. Recommend merge, boundary clarification or delegation changes.

## Output
Return overlap pairs, orphan stages, duplicate owners, severity, evidence and recommended changes.

## Errors and stop conditions
Return `HOLD` when profiles are too vague for reliable comparison. Return `BLOCKED` when two agents can independently perform the same risky action.

## Limits
Do not delete or merge agents automatically. Do not infer ownership absent from approved workflow data.

## Examples
Research collection and competitor analysis may collaborate, but only one agent should own the final stage decision.

## Tests and acceptance criteria
Every workflow stage must have exactly one primary owner or an explicit human-only handler.
