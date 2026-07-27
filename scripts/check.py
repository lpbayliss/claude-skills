#!/usr/bin/env python3
"""Dependency-free checks for the multi-skill plugin repository."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path):
    try:
        return json.loads(read(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return None


def parse_frontmatter(text: str, skill_name: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(f"skills/{skill_name}/SKILL.md must start with YAML frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        fail(f"skills/{skill_name}/SKILL.md frontmatter is not closed")
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


required_root = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "docs" / "skill-design-research.md",
    ROOT / "docs" / "specification-workflow-basis.md",
    ROOT / "docs" / "metrics-design-basis.md",
    ROOT / "docs" / "evaluation.md",
    ROOT / "scripts" / "package_skill.py",
]
for path in required_root:
    read(path)

skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if (path / "SKILL.md").is_file())
if len(skill_dirs) < 2:
    fail("repository must expose at least two skills")

for skill in skill_dirs:
    skill_name = skill.name
    text = read(skill / "SKILL.md")
    meta = parse_frontmatter(text, skill_name)
    name = meta.get("name", "")
    description = meta.get("description", "")
    if name != skill_name:
        fail(f"skill name {name!r} must match directory {skill_name!r}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(f"skill name must be lowercase kebab-case: {skill_name}")
    if len(name) > 64:
        fail(f"skill name exceeds 64 characters: {skill_name}")
    if not description or len(description) > 1024:
        fail(f"skill description must contain 1-1024 characters: {skill_name}")
    if len(text.splitlines()) > 500:
        fail(f"SKILL.md exceeds the recommended 500 lines: {skill_name}")

    for reference in set(re.findall(r"references/[A-Za-z0-9._-]+\.md", text)):
        if not (skill / reference).is_file():
            fail(f"broken SKILL.md reference in {skill_name}: {reference}")

    for reference in (skill / "references").glob("*.md"):
        reference_text = read(reference)
        if len(reference_text.splitlines()) > 100 and "## Contents" not in reference_text:
            fail(f"reference over 100 lines needs a Contents section: {reference.relative_to(ROOT)}")

    eval_path = skill / "evals" / "evals.json"
    trigger_path = skill / "evals" / "trigger-evals.json"
    evals = load_json(eval_path)
    trigger_evals = load_json(trigger_path)

    if isinstance(evals, dict):
        if evals.get("skill_name") != skill_name:
            fail(f"eval skill_name must match directory: {skill_name}")
        cases = evals.get("evals", [])
        ids = [item.get("id") for item in cases if isinstance(item, dict)]
        if len(ids) < 3 or len(ids) != len(set(ids)):
            fail(f"{skill_name} evals must contain at least three uniquely identified cases")
        for item in cases:
            if not isinstance(item, dict):
                fail(f"{skill_name} eval entries must be objects")
                continue
            if not item.get("kind") or not item.get("prompt") or not item.get("expected_output"):
                fail(f"{skill_name} eval {item.get('id')} needs kind, prompt, and expected_output")
            assertions = item.get("assertions", [])
            if len(assertions) < 4 or not all(isinstance(value, str) and value for value in assertions):
                fail(f"{skill_name} eval {item.get('id')} needs at least four non-empty assertions")
            for relative in item.get("files", []):
                if not (skill / relative).is_file():
                    fail(f"{skill_name} eval {item.get('id')} references missing file: {relative}")

        if skill_name == "specify":
            kinds = {item.get("kind") for item in cases}
            required_kinds = {"blocker", "ready", "conditional", "greenfield-ready", "update-roll-forward", "spike"}
            if not required_kinds.issubset(kinds):
                fail("specify evals must retain blocker, ready, conditional, greenfield, update/roll-forward, and spike coverage")
            if sum(item.get("kind") == "blocker" for item in cases) < 5:
                fail("specify evals must retain at least five blocker-oriented cases")
            roll_forward_case = next((item for item in cases if item.get("kind") == "update-roll-forward"), None)
            contract = " ".join([roll_forward_case.get("expected_output", ""), *roll_forward_case.get("assertions", [])]) if roll_forward_case else ""
            if "before rotation begins" not in contract:
                fail("roll-forward eval must preserve the accepted pre-rotation rehearsal timing")
            if "does not require passing before rotation begins" not in contract:
                fail("roll-forward eval must keep activity timing separate from pass-result timing")

    if not isinstance(trigger_evals, list) or len(trigger_evals) != 20:
        fail(f"{skill_name} trigger evals must contain exactly 20 cases")
    else:
        positives = sum(item.get("should_trigger") is True for item in trigger_evals if isinstance(item, dict))
        negatives = sum(item.get("should_trigger") is False for item in trigger_evals if isinstance(item, dict))
        if positives != 10 or negatives != 10:
            fail(f"{skill_name} trigger evals must contain ten positive and ten negative cases")
        if any(not isinstance(item, dict) or not isinstance(item.get("query"), str) or not item["query"].strip() for item in trigger_evals):
            fail(f"every {skill_name} trigger eval needs a non-empty query")

plugin = load_json(ROOT / ".claude-plugin" / "plugin.json")
marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
if isinstance(plugin, dict):
    if plugin.get("name") != "lpbayliss":
        fail("plugin namespace must be lpbayliss")
    if not plugin.get("version"):
        fail("plugin manifest needs an explicit version")
if isinstance(marketplace, dict):
    plugins = marketplace.get("plugins", [])
    if len(plugins) != 1 or plugins[0].get("source") != "./":
        fail("marketplace must expose the repository-root plugin with source './'")
    if marketplace.get("name") != "lpbayliss-skills":
        fail("unexpected marketplace name")

for markdown in ROOT.rglob("*.md"):
    if ".git" in markdown.parts or "dist" in markdown.parts:
        continue
    markdown_text = read(markdown)
    for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", markdown_text):
        relative = target.split("#", 1)[0]
        if not relative or "://" in relative or relative.startswith("mailto:"):
            continue
        if not (markdown.parent / relative).resolve().exists():
            fail(f"broken relative link in {markdown.relative_to(ROOT)}: {target}")

if ERRORS:
    print("Repository checks failed:", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)
print(f"Repository checks passed ({len(skill_dirs)} skills, {len(required_root)} root artifacts).")
