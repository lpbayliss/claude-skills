#!/usr/bin/env python3
"""Build deterministic .skill/.zip archives for every skill and the complete plugin."""
from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
EPOCH = (2020, 1, 1, 0, 0, 0)


def add_file(archive: zipfile.ZipFile, path: Path, relative: Path) -> None:
    info = zipfile.ZipInfo(relative.as_posix(), EPOCH)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, path.read_bytes())


def build_skill(source: Path, extension: str) -> Path:
    output = DIST / f"{source.name}{extension}"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file() and not {"__pycache__", "node_modules"}.intersection(path.parts):
                add_file(archive, path, Path(source.name) / path.relative_to(source))
    return output


def build_plugin() -> Path:
    output = DIST / "lpbayliss-skills.zip"
    include_roots = [ROOT / ".claude-plugin", ROOT / "skills"]
    include_files = [ROOT / "README.md", ROOT / "LICENSE"]
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for base in include_roots:
            for path in sorted(base.rglob("*")):
                if path.is_file() and not {"__pycache__", "node_modules"}.intersection(path.parts):
                    add_file(archive, path, path.relative_to(ROOT))
        for path in include_files:
            add_file(archive, path, path.relative_to(ROOT))
    return output


DIST.mkdir(parents=True, exist_ok=True)
for stale in DIST.glob("*.skill"):
    stale.unlink()
for stale in DIST.glob("*.zip"):
    stale.unlink()

skill_sources = [path for path in sorted(SKILLS.iterdir()) if (path / "SKILL.md").is_file()]
outputs = [build_skill(path, extension) for path in skill_sources for extension in (".skill", ".zip")]
outputs.append(build_plugin())
for output in outputs:
    print(output)
