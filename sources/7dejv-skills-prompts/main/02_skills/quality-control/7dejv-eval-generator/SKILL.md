---
name: 7dejv-eval-generator
description: Generate complete evaluation cases and measurable assertions for a 7DEJV skill. Use when a skill needs positive, boundary, negative, security or regression tests before approval.
---

# 7DEJV Eval Generator

## Inputs
- skill path and version,
- skill purpose and contract,
- known failure modes,
- representative user requests,
- required output schema.

## Procedure
1. Identify core capability, boundaries and prohibited behavior.
2. Generate at least three positive, two boundary, two negative and one security case.
3. Add expected outcome and objective assertions where possible.
4. Mark assertions requiring human qualitative review.
5. Ensure each case tests one primary risk or capability.
6. Save the suite as `evals/evals.json`.

## Output
Return an evaluation suite containing `skill_name`, `schema_version`, test cases, expected outcomes, assertions, tags and required input files.

## Errors and stop conditions
Stop with `HOLD` when the skill contract is too vague to define a meaningful expected result. Reject tests that merely repeat wording from the skill without checking behavior.

## Limits
Do not mark tests as executed. Do not invent runtime results, timings or pass rates.

## Examples
A router skill should include valid transitions, illegal jumps, missing fields and attempts to bypass human approval.

## Tests and acceptance criteria
A generated suite passes structural review when every case has a unique ID, prompt, expected outcome, category and at least one assertion or explicit qualitative-review flag.
