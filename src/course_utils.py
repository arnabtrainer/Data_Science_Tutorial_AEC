"""Small, dependency-light helpers shared by course notebooks.

The functions intentionally favor clarity over feature-completeness. They are
safe building blocks for lessons, exercises, and capstones.
"""
from __future__ import annotations

import json
import os
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np
import pandas as pd


def set_seed(seed: int = 42) -> None:
    """Seed Python and NumPy; also seed PyTorch when it is installed."""
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def locate_course_root(start: str | Path | None = None) -> Path:
    """Find the course root by walking upward until the datasets folder exists."""
    current = Path(start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "datasets").is_dir() and (candidate / "README.md").exists():
            return candidate
    raise FileNotFoundError(
        "Could not locate the course root. Start Jupyter inside the extracted course folder."
    )


def load_csv(name: str, **kwargs: Any) -> pd.DataFrame:
    """Load a CSV from the course datasets folder."""
    root = locate_course_root()
    path = root / "datasets" / name
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path, **kwargs)


def dataframe_audit(df: pd.DataFrame) -> pd.DataFrame:
    """Return a compact data-quality summary for every column."""
    rows: list[dict[str, Any]] = []
    for col in df.columns:
        s = df[col]
        rows.append(
            {
                "column": col,
                "dtype": str(s.dtype),
                "rows": len(s),
                "missing": int(s.isna().sum()),
                "missing_pct": round(float(s.isna().mean() * 100), 2),
                "unique": int(s.nunique(dropna=True)),
                "duplicate_values": int(s.duplicated().sum()),
                "sample": s.dropna().iloc[0] if s.notna().any() else None,
            }
        )
    return pd.DataFrame(rows)


def regression_metrics(y_true: Sequence[float], y_pred: Sequence[float]) -> dict[str, float]:
    """Calculate common regression metrics without hiding the formulas."""
    y_true_arr = np.asarray(y_true, dtype=float)
    y_pred_arr = np.asarray(y_pred, dtype=float)
    error = y_true_arr - y_pred_arr
    mae = np.mean(np.abs(error))
    mse = np.mean(error**2)
    rmse = np.sqrt(mse)
    denominator = np.sum((y_true_arr - y_true_arr.mean()) ** 2)
    r2 = 1 - np.sum(error**2) / denominator if denominator > 0 else float("nan")
    return {"mae": float(mae), "mse": float(mse), "rmse": float(rmse), "r2": float(r2)}


def classification_summary(
    y_true: Sequence[int], y_pred: Sequence[int]
) -> dict[str, float | int]:
    """Calculate binary classification counts and core metrics."""
    yt = np.asarray(y_true)
    yp = np.asarray(y_pred)
    tp = int(np.sum((yt == 1) & (yp == 1)))
    tn = int(np.sum((yt == 0) & (yp == 0)))
    fp = int(np.sum((yt == 0) & (yp == 1)))
    fn = int(np.sum((yt == 1) & (yp == 0)))
    safe = lambda n, d: float(n / d) if d else 0.0
    return {
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "accuracy": safe(tp + tn, len(yt)),
        "precision": safe(tp, tp + fp),
        "recall": safe(tp, tp + fn),
        "specificity": safe(tn, tn + fp),
        "f1": safe(2 * tp, 2 * tp + fp + fn),
    }


def population_stability_index(
    expected: Sequence[float],
    actual: Sequence[float],
    bins: int = 10,
    epsilon: float = 1e-6,
) -> float:
    """Calculate a simple PSI drift statistic for one numeric feature."""
    exp = np.asarray(expected, dtype=float)
    act = np.asarray(actual, dtype=float)
    boundaries = np.unique(np.quantile(exp, np.linspace(0, 1, bins + 1)))
    if len(boundaries) < 3:
        return 0.0
    boundaries[0], boundaries[-1] = -np.inf, np.inf
    exp_count, _ = np.histogram(exp, bins=boundaries)
    act_count, _ = np.histogram(act, bins=boundaries)
    exp_pct = np.maximum(exp_count / max(exp_count.sum(), 1), epsilon)
    act_pct = np.maximum(act_count / max(act_count.sum(), 1), epsilon)
    return float(np.sum((act_pct - exp_pct) * np.log(act_pct / exp_pct)))


@dataclass(frozen=True)
class ExperimentResult:
    """A minimal experiment record used in the MLOps lessons."""
    run_name: str
    parameters: dict[str, Any]
    metrics: dict[str, float]
    artifact_path: str | None = None


def save_experiment(result: ExperimentResult, output_path: str | Path) -> None:
    """Append a JSON-lines experiment record."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_name": result.run_name,
        "parameters": result.parameters,
        "metrics": result.metrics,
        "artifact_path": result.artifact_path,
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, default=str) + "\n")
