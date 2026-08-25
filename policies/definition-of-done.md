# 7DEJV Definition of Done

Status: canonical

## Purpose

No task, stage, feature, module, panel or project may be marked `DONE` unless completion is supported by explicit evidence.

## Allowed execution statuses

- `ANALYZED` — analyzed only; no implementation claim.
- `PLANNED` — implementation plan exists; no implementation claim.
- `IMPLEMENTED` — repository artifacts were changed.
- `TESTED` — declared tests were executed and results recorded.
- `VISUALLY_VERIFIED` — relevant UI states were inspected against the expected visual/UX contract.
- `REGRESSION_VERIFIED` — preserved behavior and previously accepted areas were rechecked.
- `VERIFIED` — acceptance criteria have evidence.
- `DONE` — all required acceptance criteria are `PASS`, all mandatory gates pass, and no unresolved P0/P1 item exists.
- `BLOCKED` — a concrete external dependency, permission, missing required input, failing environment or unresolved decision prevents safe continuation.

## Hard DONE gate

A task/project is `DONE` only when all applicable conditions are true:

1. Scope and acceptance criteria are explicit.
2. All acceptance criteria have status `PASS`.
3. No required item is `TODO`, `PARTIAL`, `FAIL`, `UNKNOWN` or `UNVERIFIED`.
4. Build/lint/static checks required by the repository pass.
5. Relevant automated tests pass.
6. Manual/smoke tests required by the feature pass.
7. UI work has visual verification for required views, states and breakpoints.
8. Regression verification confirms protected behavior still works.
9. Security/compliance gates pass when applicable.
10. Documentation/state artifacts are current.
11. Evidence references are recorded: commit, test output, log, screenshot/artifact or equivalent.
12. No agent may infer completion from absence of new user feedback.

## Evidence rule

Claims are not evidence. A report saying `tests passed` is valid only when the execution result is available in the current run, CI, logs, committed artifacts, or another traceable evidence source.

## Partial completion

If work is useful but incomplete, report the exact status and remaining criteria. Never collapse partial completion into `DONE`.

## Fix loop

Any `FAIL`, regression or missing acceptance criterion routes back to implementation. The cycle repeats until `PASS` or a valid `BLOCKED` state is established.
