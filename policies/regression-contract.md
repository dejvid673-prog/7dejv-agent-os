# 7DEJV Regression Contract

Status: canonical

## Principle

Every implementation follows `PRESERVE -> MODIFY -> VERIFY`.

## Before editing

Record a change contract containing:

- objective;
- files/components allowed to change;
- areas explicitly out of scope;
- behavior and UI that must remain unchanged;
- baseline evidence where available;
- risks and rollback point.

## During implementation

- prefer the smallest coherent change;
- do not refactor unrelated code without a documented reason;
- do not delete or replace working behavior merely to simplify the current task;
- preserve public contracts, data shape, navigation and accepted UI unless change is explicitly required.

## After implementation

Recheck every `MUST PRESERVE` item. A successful implementation with a regression elsewhere is `FAIL`, not `DONE`.

## UI baseline

For visual work, verification should cover applicable pages/components, interaction states, empty/loading/error states and required breakpoints. Where screenshots or rendered artifacts are available, compare before/after evidence.

## Regression severity

- P0: data loss, security issue, unusable core flow.
- P1: previously working required function broken.
- P2: material visual/UX regression or secondary feature broken.
- P3: minor cosmetic/documentation inconsistency.

Unresolved P0/P1 blocks completion.
