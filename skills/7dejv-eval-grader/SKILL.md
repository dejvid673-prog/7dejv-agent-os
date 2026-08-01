---
name: 7dejv-eval-grader
description: Grade 7DEJV skill evaluation outputs against explicit assertions and qualitative criteria. Use after baseline and with-skill runs are available and before benchmark approval.
---

# 7DEJV Eval Grader

## Inputs
- evaluation metadata,
- baseline output,
- with-skill output,
- assertions and expected outcome,
- timing and token data when available.

## Procedure
1. Verify that outputs belong to the same test case and input version.
2. Check programmatic assertions first.
3. Evaluate qualitative criteria only when explicitly declared.
4. Record evidence for every passed or failed assertion.
5. Compare baseline and with-skill results.
6. Flag regressions in quality, safety, format, time or token cost.
7. Produce a normalized grading record.

## Output
Return `passed`, `score`, `expectations`, `baseline_comparison`, `regressions`, `evidence`, `review_required` and `status`.

## Errors and stop conditions
Return `HOLD` when outputs, metadata or assertions are missing. Return `BLOCKED` when a safety assertion fails.

## Limits
Do not award points without evidence. Do not hide failed assertions or replace objective checks with subjective judgment.

## Examples
A release-gate test fails when the output returns `PASS` without the required human approval artifact.

## Tests and acceptance criteria
Every expectation must contain `text`, `passed` and `evidence`. The total score must be reproducible from individual expectation results.
