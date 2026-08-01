---
name: 7dejv-product-data-contract-validator
description: Validate and normalize STAW EXPERT product-pipeline JSON records against the repository contract. Use before and after every agent, n8n sub-workflow, approval gate or external-tool call.
---

# 7DEJV Product Data Contract Validator

Use `04_workflows/staw-expert-product-pipeline/data-contract.schema.json` as the source of truth.

## Procedure
1. Parse the input without inventing missing values.
2. Validate required fields, enums and product ID format.
3. Normalize arrays and null values.
4. Detect unsupported stage/status combinations.
5. Return validation errors with exact field paths.

## Output
Return `valid`, `normalized_record`, `errors`, `warnings` and `recommended_status`.

## Rules
Never convert assumptions into evidence. Never silently remove risks or missing data. Invalid records return `ERROR`; incomplete but structurally valid records return `HOLD`.
