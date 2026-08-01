---
name: 7dejv-agent-contract-builder
description: Convert a descriptive 7DEJV agent profile into a versioned machine-readable execution contract with explicit inputs, outputs, permissions, approvals, retries and stop conditions. Use before runtime integration or agent approval.
---

# 7DEJV Agent Contract Builder

## Inputs
- agent profile,
- related workflow stages,
- input and output schemas,
- tool-permission policy,
- ownership and runtime requirements.

## Procedure
1. Preserve one primary responsibility.
2. Define version, owner and status.
3. Link input and output schemas.
4. Define allowed tools, denied actions and required approvals.
5. Define timeout, retries, stop conditions and error policy.
6. Add test and audit references.
7. Return unresolved assumptions for review.

## Output
Return a complete agent contract in JSON or YAML plus a change report and status `DRAFT` or `READY_FOR_REVIEW`.

## Errors and stop conditions
Return `HOLD` when role boundaries or tool permissions are unclear. Return `BLOCKED` when the requested permissions contradict security policy.

## Limits
Do not widen permissions, invent schemas or mark the agent approved.

## Examples
An agent using web research should receive read-only web access and no publishing or purchase permission.

## Tests and acceptance criteria
The contract passes when all mandatory fields exist and policy references resolve to real repository paths.
