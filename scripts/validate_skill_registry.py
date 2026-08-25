#!/usr/bin/env python3
"""Validate registry/skills.json against canonical skills/*/SKILL.md files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^name:\s*([^\s]+)\s*$", re.MULTILINE)
errors: list[str] = []

try:
    data = json.loads((ROOT / "registry" / "skills.json").read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    print(f"ERROR: cannot load registry/skills.json: {exc}")
    raise SystemExit(1)

entries = data.get("skills") if isinstance(data, dict) else None
if not isinstance(data.get("schema_version") if isinstance(data, dict) else None, int):
    errors.append("skills registry schema_version must be an integer")
if not isinstance(entries, list) or not entries:
    errors.append("skills registry must contain a non-empty skills array")
    entries = []

seen_names: set[str] = set()
seen_paths: set[str] = set()
for index, entry in enumerate(entries):
    if not isinstance(entry, dict):
        errors.append(f"skills[{index}] must be an object")
        continue
    name = entry.get("name")
    rel_path = entry.get("path")
    if not isinstance(name, str) or not name:
        errors.append(f"skills[{index}] missing valid name")
        continue
    if name in seen_names:
        errors.append(f"duplicate registered skill name: {name}")
    seen_names.add(name)
    if entry.get("status") != "canonical":
        errors.append(f"registered skill {name} must have canonical status")
    if not isinstance(rel_path, str) or not rel_path.startswith("skills/") or not rel_path.endswith("/SKILL.md"):
        errors.append(f"invalid registered path for {name}: {rel_path!r}")
        continue
    if rel_path in seen_paths:
        errors.append(f"duplicate registered skill path: {rel_path}")
    seen_paths.add(rel_path)
    path = ROOT / rel_path
    if not path.is_file():
        errors.append(f"registered skill path does not exist: {rel_path}")
        continue
    text = path.read_text(encoding="utf-8")
    match = NAME_RE.search(text)
    if not match:
        errors.append(f"registered skill lacks frontmatter name: {rel_path}")
    elif match.group(1).strip('"\'') != name:
        errors.append(f"skill registry/frontmatter mismatch: {name} != {match.group(1)} in {rel_path}")

actual_paths = {
    str(path.relative_to(ROOT)).replace("\\", "/")
    for path in (ROOT / "skills").glob("*/SKILL.md")
}
for rel_path in sorted(actual_paths - seen_paths):
    errors.append(f"unregistered canonical skill: {rel_path}")
for rel_path in sorted(seen_paths - actual_paths):
    errors.append(f"registry references non-canonical/missing skill: {rel_path}")

for item in errors:
    print(f"ERROR: {item}")
print(json.dumps({"status": "PASS" if not errors else "BLOCKED", "errors": len(errors)}, sort_keys=True))
sys.exit(1 if errors else 0)
