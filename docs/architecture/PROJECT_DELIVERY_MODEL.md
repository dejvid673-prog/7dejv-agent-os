# 7DEJV Project Delivery Model

Status: canonical

## Objective

Provide one repeatable operating model for delivering multi-stage software, UI, automation and integration projects to verified completion.

## Core roles

### Coordinator
Owns routing, sequencing and task framing. Does not claim implementation without evidence.

### Product / Domain Architect
Owns problem definition, scope, constraints, architecture and acceptance criteria for the domain.

### UX/UI Designer
Owns interaction and visual specification when a user interface is involved.

### Executor / Developer
Implements the approved stage using the smallest coherent change and records changed artifacts and executed checks.

### Visual Regression Auditor
Verifies UI implementation and detects unintended visual/interaction regressions.

### QA / Domain Auditor
Verifies functional quality, edge cases and domain-specific requirements.

### Project Completion Owner
Owns the feature matrix, persistent project state, fix loop and final completion gate.

### Conditional specialists
Security, PrestaShop, Allegro, Product, Compliance, Graphics/DTP and other specialists are inserted only when relevant.

## Mandatory project artifacts

For every multi-stage project:

1. `PROJECT_STATE.md`
2. `FEATURE_MATRIX.md`

For each implementation stage:

3. `CHANGE_CONTRACT.md`

For completion:

4. verification evidence and completion report.

## Delivery lifecycle

`DISCOVER -> DEFINE -> BASELINE -> PLAN_STAGE -> IMPLEMENT -> TECH_VERIFY -> VISUAL_VERIFY (if UI) -> REGRESSION_VERIFY -> UPDATE_STATE -> COMPLETION_GATE`

Failure at a verification gate creates a repair batch and returns to `PLAN_STAGE`.

## Stage sizing

A stage must be:

- small enough to verify completely;
- large enough to produce a coherent user-visible or architectural result;
- bounded by explicit IN/OUT scope;
- reversible or anchored to a known baseline;
- independently auditable.

Avoid stages such as "finish frontend" or "improve panel". Prefer bounded outcomes such as "complete left navigation and all navigation states" or "implement orders table with sorting, pagination and empty/loading/error states".

## UI project rule

UI work is incomplete if it only renders the main happy-path screen. Applicable interaction states, validation, loading, empty, error, disabled states and required breakpoints belong in the acceptance matrix.

## Evidence hierarchy

Strong evidence includes executed CI/tests, command output, runtime/browser verification, screenshots/rendered artifacts, commit/ref and reproducible logs. Documentation claims without execution evidence do not establish readiness.

## Continuity rule

Chat history can provide context, but repository-resident project state is authoritative for resuming work. At the start of a continuation, read project state, feature matrix, applicable decisions, latest baseline and open blockers before changing files.

## Destructive-change rule

Before deleting, replacing or consolidating an existing mechanism, identify its consumers and dependency references. If a supposedly redundant artifact is active in a registry/workflow/runtime path, migrate dependencies before deletion.

## Completion invariant

A project reaches `DONE` only when all required acceptance criteria are `PASS` with evidence and every applicable mandatory gate from `policies/definition-of-done.md` passes.
