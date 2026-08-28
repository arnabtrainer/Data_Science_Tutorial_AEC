from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main() -> None:
    notebooks = sorted(ROOT.rglob("*.ipynb"))
    errors: list[dict[str, str]] = []
    code_cells = 0
    markdown_cells = 0
    for path in notebooks:
        try:
            nb = nbformat.read(path, as_version=4)
        except Exception as exc:
            errors.append({"file": str(path.relative_to(ROOT)), "error": f"parse: {exc}"})
            continue
        if not nb.cells:
            errors.append({"file": str(path.relative_to(ROOT)), "error": "notebook has no cells"})
        for index, cell in enumerate(nb.cells):
            if cell.cell_type == "code":
                code_cells += 1
                try:
                    ast.parse(cell.source or "")
                except SyntaxError as exc:
                    errors.append({
                        "file": str(path.relative_to(ROOT)),
                        "error": f"cell {index} syntax: {exc}",
                    })
            elif cell.cell_type == "markdown":
                markdown_cells += 1
    required = [
        ROOT / "README.md",
        ROOT / "COURSE_INDEX.md",
        ROOT / "datasets" / "DATA_DICTIONARY.md",
        ROOT / "requirements-core.txt",
        ROOT / "requirements-advanced.txt",
        ROOT / "src" / "course_utils.py",
    ]
    for path in required:
        if not path.exists():
            errors.append({"file": str(path.relative_to(ROOT)), "error": "required file missing"})

    report = {
        "root": str(ROOT),
        "notebooks": len(notebooks),
        "code_cells": code_cells,
        "markdown_cells": markdown_cells,
        "python_files": len(list(ROOT.rglob("*.py"))),
        "dataset_files": len([p for p in (ROOT / "datasets").rglob("*") if p.is_file()]),
        "errors": errors,
        "status": "pass" if not errors else "fail",
    }
    (ROOT / "verification_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
