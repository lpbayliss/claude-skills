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
    ROOT / "docs" / "skill-design-research.md",
    ROOT / "docs" / "specification-workflow-basis.md",
    SKILL / "SKILL.md",
    SKILL / "references" / "artifact-transformation.md",
    SKILL / "references" / "specification-workflow.md",
    SKILL / "references" / "spec-template.md",
    SKILL / "references" / "review-checklist.md",
    SKILL / "references" / "mini-spec-example.md",
    SKILL / "evals" / "evals.json",
    SKILL / "evals" / "trigger-evals.json",
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
    SKILL / "evals" / "trigger-evals.json",
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

for reference in (SKILL / "references").glob("*.md"):
    reference_text = read(reference)
    if len(reference_text.splitlines()) > 100 and "## Contents" not in reference_text:
        fail(f"reference over 100 lines needs a Contents section: {reference.relative_to(ROOT)}")

try:
    evals = json.loads(read(SKILL / "evals" / "evals.json"))
    cases = evals.get("evals", [])
    ids = [item.get("id") for item in cases]
    if len(ids) < 6 or len(ids) != len(set(ids)):
        fail("evals must contain at least six uniquely identified cases")
    for item in cases:
        if not item.get("prompt") or not item.get("expected_output"):
            fail(f"eval {item.get('id')} needs prompt and expected_output")
        assertions = item.get("assertions", [])
        if len(assertions) < 4 or not all(isinstance(value, str) and value for value in assertions):
            fail(f"eval {item.get('id')} needs at least four non-empty assertions")
        for relative in item.get("files", []):
            target = SKILL / relative
            if not target.is_file():
                fail(f"eval {item.get('id')} references missing file: {relative}")
except (json.JSONDecodeError, AttributeError):
    pass

try:
    trigger_evals = json.loads(read(SKILL / "evals" / "trigger-evals.json"))
    if not isinstance(trigger_evals, list) or len(trigger_evals) != 20:
        fail("trigger evals must contain exactly 20 cases")
    else:
        positives = sum(item.get("should_trigger") is True for item in trigger_evals)
        negatives = sum(item.get("should_trigger") is False for item in trigger_evals)
        if positives != 10 or negatives != 10:
            fail("trigger evals must contain ten positive and ten negative cases")
        if any(not isinstance(item.get("query"), str) or not item["query"].strip() for item in trigger_evals):
            fail("every trigger eval needs a non-empty query")
except (json.JSONDecodeError, AttributeError, TypeError):
    pass

if ERRORS:
    print("Repository checks failed:", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)
print(f"Repository checks passed ({len(required)} required artifacts).")
