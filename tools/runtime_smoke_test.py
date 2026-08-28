from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import time
import traceback
from pathlib import Path

import matplotlib.pyplot as plt
import nbformat

ROOT = Path(__file__).resolve().parents[1]

def execute_notebook(path: Path) -> dict:
    namespace = {"__name__": "__main__"}
    started = time.perf_counter()
    output = io.StringIO()
    try:
        notebook = nbformat.read(path, as_version=4)
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            for index, cell in enumerate(notebook.cells):
                if cell.cell_type != "code" or not cell.source.strip():
                    continue
                code = compile(cell.source, f"{path.name}:cell_{index}", "exec")
                exec(code, namespace, namespace)
        return {
            "file": str(path.relative_to(ROOT)),
            "status": "pass",
            "seconds": round(time.perf_counter() - started, 3),
        }
    except Exception as exc:
        return {
            "file": str(path.relative_to(ROOT)),
            "status": "fail",
            "seconds": round(time.perf_counter() - started, 3),
            "error": repr(exc),
            "traceback": traceback.format_exc(),
            "captured_output_tail": output.getvalue()[-3000:],
        }
    finally:
        plt.close("all")

def select_paths(group: str) -> list[Path]:
    if group == "lessons_1_5":
        folders = [ROOT / f"{i:02d}_" for i in []]  # placeholder for readability
        names = [
            "01_Python_Foundation", "02_NumPy_and_Pandas", "03_Data_Visualization",
            "04_Statistics_and_Mathematics", "05_Exploratory_Data_Analysis",
        ]
        paths = []
        for name in names:
            paths.extend(p for p in sorted((ROOT/name).glob("*.ipynb")) if p.name != "00_Phase_Overview.ipynb")
        return paths
    if group == "lessons_6_10":
        names = [
            "06_Machine_Learning_Fundamentals", "07_Supervised_Learning",
            "08_Unsupervised_Learning", "09_Deep_Learning",
            "10_Real_World_ML_and_MLOps",
        ]
        paths = []
        for name in names:
            paths.extend(p for p in sorted((ROOT/name).glob("*.ipynb")) if p.name != "00_Phase_Overview.ipynb")
        return paths
    if group == "solutions":
        return sorted((ROOT/"solutions").glob("*Lab_Solution.ipynb"))
    if group == "capstones":
        return sorted((ROOT/"11_Worked_Capstones").glob("*.ipynb"))
    raise ValueError(group)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("group", choices=["lessons_1_5","lessons_6_10","solutions","capstones"])
    args = parser.parse_args()
    os.chdir(ROOT)
    results = []
    for path in select_paths(args.group):
        result = execute_notebook(path)
        results.append(result)
        print(result["status"].upper(), result["file"], result["seconds"], flush=True)
    report = {
        "group": args.group,
        "executed": len(results),
        "passed": sum(r["status"] == "pass" for r in results),
        "failed": sum(r["status"] == "fail" for r in results),
        "total_seconds": round(sum(r["seconds"] for r in results), 3),
        "results": results,
    }
    out = ROOT / f"runtime_smoke_{args.group}.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="results"}, indent=2))
    if report["failed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
