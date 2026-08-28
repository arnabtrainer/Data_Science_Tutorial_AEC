import pandas as pd
import pytest
from src.production_example.features import MODEL_FEATURES, select_features, validate_training_frame

def valid_frame():
    row = {
        "tenure_months": 12, "monthly_charges": 70.0, "support_tickets_90d": 1,
        "weekly_usage_hours": 20.0, "contract_type": "Month-to-month",
        "internet_service": "Fiber", "autopay": 1, "senior_citizen": 0, "churn": 0,
    }
    return pd.DataFrame([row])

def test_select_features_order():
    result = select_features(valid_frame())
    assert list(result.columns) == MODEL_FEATURES

def test_validation_rejects_missing_target():
    with pytest.raises(ValueError):
        validate_training_frame(valid_frame().drop(columns=["churn"]))
