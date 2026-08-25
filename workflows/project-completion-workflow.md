# Project Completion Workflow

Status: canonical

## Goal

Drive multi-stage projects from defined scope to verified completion without losing accepted behavior or stopping after partial progress.

## Stages

1. `DISCOVER`
   - read repository source of truth, project docs, state and relevant history;
   - identify target repo/branch and dependencies.
2. `DEFINE`
   - define scope IN/OUT;
   - create measurable acceptance criteria and feature matrix;
   - establish Definition of Done and applicable gates.
3. `BASELINE`
   - record current verified commit/ref;
   - record critical existing behavior and UI that must be preserved;
   - capture available test/screenshot/runtime evidence.
4. `PLAN_STAGE`
   - split work into the smallest coherent stage that can end in a verifiable result;
   - define change contract and rollback point.
5. `IMPLEMENT`
   - execute only the approved stage scope;
   - record changed files and technical decisions.
6. `TECH_VERIFY`
   - run applicable build/lint/static/unit/integration/smoke checks;
   - record real execution evidence.
7. `VISUAL_VERIFY`
   - when UI is involved, run Visual Regression Auditor against baseline/specification and required states.
8. `REGRESSION_VERIFY`
   - recheck all `MUST PRESERVE` behavior and previously accepted criteria affected by the change.
9. `UPDATE_STATE`
   - update project state, feature matrix, blockers, regressions and evidence.
10. `COMPLETION_GATE`
   - if every required criterion is `PASS` and Definition of Done passes -> `DONE`;
   - otherwise generate the next repair/implementation batch and return to `PLAN_STAGE`;
   - if a concrete external blocker prevents continuation -> `BLOCKED` with evidence.

## Rules

- A report of defects is not completion; defects become input to the next repair batch.
- No stage may silently remove an earlier accepted criterion.
- Scope changes require an explicit decision and feature-matrix update.
- Conversation boundaries do not change project state.
- Every stage must end with a repository-resident state update for multi-stage projects.

## Recommended routing

`Coordinator -> Product/Domain Architect -> UX/UI (if applicable) -> Executor -> technical checks -> Visual Regression Auditor (if applicable) -> QA/domain audit -> Project Completion Owner`

Specialists such as PrestaShop, Allegro, Security, Product or Compliance agents are inserted only when their domain is relevant.
