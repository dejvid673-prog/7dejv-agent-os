---
name: 7dejv-product-pipeline-router
description: Route STAW EXPERT product-development tasks to the correct stage, agent and skill. Use whenever a product record, research candidate, formulation draft, dosage plan, product name, description, label or release audit must advance through the product pipeline.
---

# 7DEJV Product Pipeline Router

Read the current product record and the workflow transition matrix.

## Procedure
1. Validate `product_id`, `stage`, `status` and `input_version`.
2. Check whether the current stage has all required inputs.
3. Select exactly one next skill.
4. Reject illegal stage jumps.
5. Return the normalized pipeline object.

## Output
Return JSON containing `product_id`, `stage`, `status`, `missing_data`, `risks`, `human_review_required` and `next_stage`.

## Stop conditions
Stop with `HOLD` for missing data, `BLOCKED` for unsafe or prohibited work, and `ERROR` for invalid structure. Never approve formulation, commercial dosage, production, publication or purchasing.
