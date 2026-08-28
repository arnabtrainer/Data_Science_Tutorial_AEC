from __future__ import annotations
from pathlib import Path
import joblib
import pandas as pd

from .config import Settings
from .features import select_features

def load_model(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Model not found: {path}. Run training first.")
    return joblib.load(path)

def predict_records(df: pd.DataFrame, settings: Settings = Settings()) -> pd.DataFrame:
    model = load_model(settings.model_path)
    X = select_features(df)
    probability = model.predict_proba(X)[:, 1]
    result = df.copy()
    result["churn_probability"] = probability
    result["churn_prediction"] = (probability >= settings.decision_threshold).astype(int)
    return result
