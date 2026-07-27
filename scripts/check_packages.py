#!/usr/bin/env python3
"""Verify generated individual-skill and plugin archives."""
from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
FORBIDDEN_PARTS = {"node_modules", "__pycache__", ".git"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def archive_names(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise SystemExit(f"corrupt archive member in {path.name}: {bad_member}")
        return archive.namelist()


skill_names = sorted(path.name for path in SKILLS.iterdir() if (path / "SKILL.md").is_file())
if not skill_names:
    raise SystemExit("no skills discovered")

for skill_name in skill_names:
    skill_archive = DIST / f"{skill_name}.skill"
    desktop_archive = DIST / f"{skill_name}.zip"
    for archive in (skill_archive, desktop_archive):
        if not archive.is_file():
            raise SystemExit(f"missing archive: {archive.relative_to(ROOT)}")
        names = archive_names(archive)
        required = f"{skill_name}/SKILL.md"
        if required not in names:
            raise SystemExit(f"{archive.name} is missing {required}")
        prefix = f"{skill_name}/"
        if any(not name.startswith(prefix) for name in names):
            raise SystemExit(f"{archive.name} contains files outside {prefix}")
        if any(FORBIDDEN_PARTS.intersection(Path(name).parts) for name in names):
            raise SystemExit(f"{archive.name} contains a forbidden cache/dependency path")
    if digest(skill_archive) != digest(desktop_archive):
        raise SystemExit(f"{skill_archive.name} and {desktop_archive.name} differ")

plugin_archive = DIST / "lpbayliss-skills.zip"
if not plugin_archive.is_file():
    raise SystemExit(f"missing archive: {plugin_archive.relative_to(ROOT)}")
plugin_names = archive_names(plugin_archive)
for skill_name in skill_names:
    required = f"skills/{skill_name}/SKILL.md"
    if required not in plugin_names:
        raise SystemExit(f"{plugin_archive.name} is missing {required}")
if any(FORBIDDEN_PARTS.intersection(Path(name).parts) for name in plugin_names):
    raise SystemExit(f"{plugin_archive.name} contains a forbidden cache/dependency path")

expected = {
    *(f"{name}.skill" for name in skill_names),
    *(f"{name}.zip" for name in skill_names),
    "lpbayliss-skills.zip",
}
actual = {path.name for pattern in ("*.skill", "*.zip") for path in DIST.glob(pattern)}
if actual != expected:
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    raise SystemExit(f"archive set mismatch; missing={missing}, unexpected={unexpected}")

print(f"Package checks passed ({len(skill_names)} skills, {len(expected)} archives).")
