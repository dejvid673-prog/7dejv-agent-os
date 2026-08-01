---
name: 7dejv-json-schema-hardener
description: Strengthen 7DEJV JSON Schema contracts by replacing loose types with explicit enums, required fields, structured objects, date formats and conditional business rules. Use before routing, runtime integration or schema approval.
---

# 7DEJV JSON Schema Hardener

## Inputs
- current JSON Schema,
- workflow stages and statuses,
- sample valid and invalid records,
- compatibility requirements.

## Procedure
1. Identify unconstrained strings, arrays and objects.
2. Add enums, patterns, formats and required fields.
3. Define reusable `$defs` for evidence, risks and approvals.
4. Add conditional rules for human approval and terminal stages.
5. Set `additionalProperties` deliberately.
6. Add schema version and migration notes.
7. Validate representative positive and negative examples.

## Output
Return the hardened schema, compatibility classification, migration requirements, unresolved risks and validation results.

## Errors and stop conditions
Return `HOLD` when workflow semantics are ambiguous. Return `BLOCKED` when a breaking change has no migration plan.

## Limits
Do not silently remove supported data. Do not treat a generic object as a complete contract. Do not approve the schema without executable tests.

## Examples
A `stage` field should use an enum, and an approval object should require decision, reviewer and reviewed timestamp when present.

## Tests and acceptance criteria
The schema passes when valid fixtures are accepted, invalid fixtures are rejected and registry values match schema enums.
