from __future__ import annotations
from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .config import Settings
from .features import (
    CATEGORICAL_FEATURES, MODEL_FEATURES, NUMERIC_FEATURES, TARGET,
    validate_training_frame,
)

def build_pipeline() -> Pipeline:
    numeric = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("one_hot", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocessing = ColumnTransformer([
        ("numeric", numeric, NUMERIC_FEATURES),
        ("categorical", categorical, CATEGORICAL_FEATURES),
    ])
    return Pipeline([
        ("preprocessing", preprocessing),
        ("model", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])

def train(data_path: Path, settings: Settings = Settings()) -> dict[str, float]:
    df = pd.read_csv(data_path)
    validate_training_frame(df)
    X, y = df[MODEL_FEATURES], df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=settings.test_size, random_state=settings.random_seed,
        stratify=y,
    )
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)
    probabilities = pipeline.predict_proba(X_test)[:, 1]
    predictions = (probabilities >= settings.decision_threshold).astype(int)
    metrics = {
        "roc_auc": float(roc_auc_score(y_test, probabilities)),
        "accuracy": float((predictions == y_test.to_numpy()).mean()),
    }
    settings.model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, settings.model_path)
    print(classification_report(y_test, predictions))
    return metrics

if __name__ == "__main__":
    train(Path("datasets/customer_churn.csv"))
