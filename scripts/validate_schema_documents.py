#!/usr/bin/env python3
"""Validate that canonical JSON Schema documents are syntactically valid and self-describing."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
errors: list[str] = []

if not SCHEMAS.is_dir():
    errors.append("missing schemas directory")
else:
    files = sorted(SCHEMAS.glob("*.json"))
    if not files:
        errors.append("no JSON Schema documents found")
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path.name}: schema root must be an object")
            continue
        if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errors.append(f"{path.name}: expected JSON Schema draft 2020-12")
        if not isinstance(data.get("$id"), str) or not data["$id"]:
            errors.append(f"{path.name}: missing non-empty $id")
        if not isinstance(data.get("title"), str) or not data["title"]:
            errors.append(f"{path.name}: missing non-empty title")
        if data.get("type") != "object":
            errors.append(f"{path.name}: canonical schema root type must be object")

for item in errors:
    print(f"ERROR: {item}")
print(json.dumps({"status": "PASS" if not errors else "BLOCKED", "errors": len(errors)}, sort_keys=True))
sys.exit(1 if errors else 0)
