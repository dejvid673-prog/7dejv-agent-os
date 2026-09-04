# Project Completion Workflow

Status: `canonical`

## Goal

Drive multi-stage projects from defined scope to verified completion without losing accepted behavior or stopping after partial progress.

## Stages

1. `DISCOVER`
   - read repository source of truth, project docs, state and relevant history;
   - identify target repo/branch and dependencies.
2. `DEFINE`
   - define scope IN/OUT;
   - create measurable acceptance criteria and feature matrix;
   - identify explicit approvals and stop conditions.
3. `PLAN`
   - create a staged implementation/verification plan;
   - order work so high-risk dependencies are proven early.
4. `EXECUTE`
   - implement the smallest complete stage;
   - preserve known-good behavior;
   - record commands/actions and changed files.
5. `VERIFY`
   - run deterministic checks first;
   - run functional/runtime verification where required;
   - compare actual behavior against acceptance criteria.
6. `AUDIT`
   - review architecture, security, regressions, documentation and source-of-truth consistency;
   - classify unresolved findings.
7. `REPAIR`
   - fix verified defects within scope;
   - re-run affected verification.
8. `COMPLETE`
   - confirm all acceptance criteria have evidence;
   - update durable project state/handoff;
   - report remaining risks and next action.

## Evidence contract

A stage is not complete because an agent says it is complete. Evidence must match the claim, for example:

- static/type/build checks for compile/readiness claims;
- automated tests for tested behavior;
- runtime/API/browser evidence for connected/functional claims;
- diff/commit/artifact for repository-change claims.

If the required evidence cannot be produced, report `HOLD` or `BLOCKED` rather than `PASS`.

## Parallel work

Use independent branches/worktrees for concurrent code changes. Parallel agents may analyze/review the same source, but only one owner should mutate a given implementation scope at a time unless the work is explicitly partitioned.

## Completion gate

Return `PASS` only when every in-scope acceptance criterion has evidence and no blocking finding remains. Otherwise return `HOLD` or `BLOCKED` with the exact missing evidence or blocker.
