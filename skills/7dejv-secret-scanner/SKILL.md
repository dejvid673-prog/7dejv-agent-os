---
name: 7dejv-secret-scanner
description: Scan a 7DEJV repository for exposed credentials, private keys, tokens, passwords and sensitive connection strings. Use before commits, pull requests, releases and runtime deployment.
---

# 7DEJV Secret Scanner

## Inputs
- repository root,
- include and exclude patterns,
- approved placeholder patterns,
- optional previous scan baseline.

## Procedure
1. Traverse text files while excluding generated and binary paths.
2. Apply high-confidence credential and private-key patterns.
3. Redact detected values in all reports.
4. Classify findings by confidence and severity.
5. Compare against approved placeholders and false-positive rules.
6. Return a non-zero result for blocking findings.

## Output
Return `status`, scan totals and findings containing only path, line, rule, severity, fingerprint and remediation.

## Errors and stop conditions
Return `BLOCKED` for an active private key or high-confidence credential. Return `HOLD` for ambiguous sensitive values requiring review.

## Limits
Never print, store or commit complete detected values. A removed credential must still be rotated when exposure is possible.

## Examples
Environment-variable references are allowed; hard-coded credential values are not.

## Tests and acceptance criteria
Must detect test fixtures representing private keys and credential formats while ignoring explicit placeholders and environment references.
