# Agent Definition Review

Status: `canonical`

Provenance: adapted from `sources/7dejv-skills-prompts/main/04_workflows/quality/agent-definition-review.md` (source blob `ec7f9b6ec451a1a706cd665a0c05518593d02399`).

## Purpose

Turn an agent candidate into an explicit executable contract or keep it out of the canonical catalog.

## Sequence

```text
AGENT_CANDIDATE
→ ROLE_AUDIT
→ CONTRACT_BUILD
→ TOOL_PERMISSION_AUDIT
→ OVERLAP_CHECK
→ SAFETY_CHECK
→ TEST_REFERENCE_CHECK
→ QUALITY_SCORE
→ REVIEW
→ PASS / HOLD / BLOCKED
```

## Required contract

A canonical agent must define:

- one primary responsibility and explicit non-responsibilities;
- accepted inputs and validation rules;
- structured outputs and evidence requirements;
- allowed tools/actions using least privilege;
- stop/failure behavior, including ambiguous input handling;
- handoff behavior for multi-agent work;
- overlap/routing relationship to existing canonical agents;
- tests or an executable validation plan.

## Status

### `PASS`

All required contract fields are explicit, overlap is resolved, permissions are minimal and validation evidence exists.

### `HOLD`

Required metadata, tests, schemas, ownership, routing or role boundaries remain incomplete/ambiguous.

### `BLOCKED`

The candidate introduces unsafe permissions, unresolved high-risk responsibility overlap, protected-data exposure or behavior inconsistent with canonical policy.

## Promotion rule

`PASS` permits promotion review; it does not silently promote the candidate. Promotion must preserve provenance and update the canonical agent registry when one exists.
