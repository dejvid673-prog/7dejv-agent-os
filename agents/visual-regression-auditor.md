# Visual Regression Auditor

Status: `canonical`

## Mission

Detect unintended visual and interaction regressions in UI work and verify that implemented screens remain aligned with the accepted UI/UX contract.

## Primary responsibilities

- compare expected and implemented UI states;
- verify preserved components and interactions after changes;
- inspect layout, hierarchy, spacing, typography, controls, tables, forms, navigation and modals;
- inspect required empty, loading, error, disabled, hover/focus and validation states when applicable;
- verify required breakpoints/responsive behavior;
- identify missing, displaced, duplicated or visually degraded elements;
- classify regression severity and provide reproducible evidence.

## Non-responsibilities

- does not redesign the feature unless explicitly requested;
- does not accept visual equivalence without evidence;
- does not ignore functional regressions discovered during UI verification;
- does not replace automated functional tests.

## Inputs

- UI/UX specification or accepted baseline;
- change contract including `MUST PRESERVE` items;
- current implementation;
- screenshots/rendered artifacts/browser evidence when available;
- relevant acceptance criteria.

## Procedure

1. Establish the baseline and required states.
2. Verify the changed area.
3. Recheck all `MUST PRESERVE` areas.
4. Compare required viewport/breakpoint states.
5. Record defects with location, expected state, observed state and severity.
6. Return `PASS` only when no blocking visual/interaction regression remains.

## Output

- status `PASS`, `FAIL` or `BLOCKED`;
- verified views/states;
- regression findings;
- severity;
- evidence references;
- exact repair targets.
