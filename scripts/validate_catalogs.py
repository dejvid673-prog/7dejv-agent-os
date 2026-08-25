#!/usr/bin/env python3
"""Validate canonical agent, workflow and prompt registries against repository files."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def load(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        fail(f"cannot load {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
        return {}
    return value


def validate_registry(filename: str, collection_key: str, base_dir: str) -> None:
    path = ROOT / "registry" / filename
    data = load(path)
    entries = data.get(collection_key)
    if not isinstance(data.get("schema_version"), int):
        fail(f"{filename}: schema_version must be an integer")
    if not isinstance(entries, list) or not entries:
        fail(f"{filename}: {collection_key} must be a non-empty array")
        return

    seen_names: set[str] = set()
    seen_paths: set[str] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(f"{filename}[{index}] must be an object")
            continue
        name = entry.get("name")
        rel_path = entry.get("path")
        status = entry.get("status")
        if not isinstance(name, str) or not name:
            fail(f"{filename}[{index}] missing valid name")
            continue
        if name in seen_names:
            fail(f"{filename}: duplicate name {name}")
        seen_names.add(name)
        if status != "canonical":
            fail(f"{filename}: active registry entry {name} must be canonical")
        if not isinstance(rel_path, str) or not rel_path.startswith(base_dir + "/"):
            fail(f"{filename}: invalid path for {name}: {rel_path!r}")
            continue
        if rel_path in seen_paths:
            fail(f"{filename}: duplicate path {rel_path}")
        seen_paths.add(rel_path)
        full_path = ROOT / rel_path
        if not full_path.is_file():
            fail(f"{filename}: registered path does not exist: {rel_path}")
            continue
        text = full_path.read_text(encoding="utf-8")
        if "Status: `canonical`" not in text:
            fail(f"{filename}: registered canonical artifact lacks explicit canonical status: {rel_path}")

    actual_files = {
        str(p.relative_to(ROOT)).replace("\\", "/")
        for p in (ROOT / base_dir).rglob("*.md")
        if p.name.lower() != "readme.md"
    }
    unregistered = sorted(actual_files - seen_paths)
    if unregistered:
        fail(f"{filename}: canonical directory contains unregistered artifacts: {unregistered}")


def main() -> int:
    validate_registry("agents.json", "agents", "agents")
    validate_registry("workflows.json", "workflows", "workflows")
    validate_registry("prompts.json", "prompts", "prompts")
    for item in ERRORS:
        print(f"ERROR: {item}")
    print(json.dumps({"status": "PASS" if not ERRORS else "BLOCKED", "errors": len(ERRORS)}, sort_keys=True))
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
