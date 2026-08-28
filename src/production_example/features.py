from __future__ import annotations
import pandas as pd

TARGET = "churn"
ID_COLUMN = "customer_id"
NUMERIC_FEATURES = [
    "tenure_months", "monthly_charges", "support_tickets_90d",
    "weekly_usage_hours", "autopay", "senior_citizen",
]
CATEGORICAL_FEATURES = ["contract_type", "internet_service"]
MODEL_FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES

def validate_training_frame(df: pd.DataFrame) -> None:
    required = set(MODEL_FEATURES + [TARGET])
    missing = sorted(required - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if not set(df[TARGET].dropna().unique()).issubset({0, 1}):
        raise ValueError("Target must contain only 0 and 1.")

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(set(MODEL_FEATURES) - set(df.columns))
    if missing:
        raise ValueError(f"Missing inference features: {missing}")
    return df.loc[:, MODEL_FEATURES].copy()
