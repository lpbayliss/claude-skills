#!/usr/bin/env python3
"""Dependency-free checks for the skill repository."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "specify"
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        fail("SKILL.md frontmatter is not closed")
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


required = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    SKILL / "SKILL.md",
    SKILL / "references" / "artifact-transformation.md",
    SKILL / "references" / "spec-template.md",
    SKILL / "references" / "review-checklist.md",
    SKILL / "references" / "mini-spec-example.md",
    SKILL / "references" / "source-basis.md",
    SKILL / "evals" / "evals.json",
]
for path in required:
    read(path)

text = read(SKILL / "SKILL.md")
meta = parse_frontmatter(text)
name = meta.get("name", "")
description = meta.get("description", "")
if name != SKILL.name:
    fail(f"skill name {name!r} must match directory {SKILL.name!r}")
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
    fail("skill name must be lowercase kebab-case")
if len(name) > 64:
    fail("skill name exceeds 64 characters")
if not description or len(description) > 1024:
    fail("skill description must contain 1-1024 characters")
if len(text.splitlines()) > 500:
    fail("SKILL.md exceeds the recommended 500 lines")

json_paths = [
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    SKILL / "evals" / "evals.json",
]
for path in json_paths:
    try:
        json.loads(read(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")

try:
    marketplace = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
    plugins = marketplace.get("plugins", [])
    if len(plugins) != 1 or plugins[0].get("source") != "./":
        fail("marketplace must expose the repository-root plugin with source './'")
    if marketplace.get("name") != "lpbayliss-skills":
        fail("unexpected marketplace name")
except (json.JSONDecodeError, AttributeError):
    pass

for reference in set(re.findall(r"references/[A-Za-z0-9._-]+\.md", text)):
    target = SKILL / reference
    if not target.is_file():
        fail(f"broken SKILL.md reference: {reference}")

try:
    evals = json.loads(read(SKILL / "evals" / "evals.json"))
    ids = [item.get("id") for item in evals.get("evals", [])]
    if len(ids) < 4 or len(ids) != len(set(ids)):
        fail("evals must contain at least four uniquely identified cases")
except (json.JSONDecodeError, AttributeError):
    pass

if ERRORS:
    print("Repository checks failed:", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)
print(f"Repository checks passed ({len(required)} required artifacts).")
