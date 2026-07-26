#!/usr/bin/env python3
"""Build a deterministic zip-compatible .skill archive."""
from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "specify"
OUTPUT = ROOT / "dist" / "specify.skill"
EPOCH = (2020, 1, 1, 0, 0, 0)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in sorted(SOURCE.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        relative = Path(SOURCE.name) / path.relative_to(SOURCE)
        info = zipfile.ZipInfo(relative.as_posix(), EPOCH)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, path.read_bytes())
print(OUTPUT)
