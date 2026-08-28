import numpy as np
import pandas as pd
from src.course_utils import classification_summary, dataframe_audit, regression_metrics

def test_regression_metrics_perfect_prediction():
    metrics = regression_metrics([1, 2, 3], [1, 2, 3])
    assert metrics["mae"] == 0
    assert metrics["rmse"] == 0
    assert metrics["r2"] == 1

def test_classification_summary_counts():
    summary = classification_summary([0, 0, 1, 1], [0, 1, 1, 1])
    assert summary["tp"] == 2
    assert summary["tn"] == 1
    assert summary["fp"] == 1
    assert summary["fn"] == 0

def test_dataframe_audit_reports_missing_values():
    audit = dataframe_audit(pd.DataFrame({"x": [1, np.nan]}))
    assert audit.loc[0, "missing"] == 1
