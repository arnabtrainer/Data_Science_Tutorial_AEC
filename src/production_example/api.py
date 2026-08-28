from __future__ import annotations
from functools import lru_cache
from typing import Literal
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .config import Settings
from .features import MODEL_FEATURES

app = FastAPI(title="Churn Prediction API", version="1.0.0")
settings = Settings()

class ChurnRequest(BaseModel):
    tenure_months: int = Field(ge=0, le=120)
    monthly_charges: float = Field(ge=0)
    support_tickets_90d: int = Field(ge=0)
    weekly_usage_hours: float | None = Field(default=None, ge=0)
    contract_type: Literal["Month-to-month", "One year", "Two year"]
    internet_service: Literal["Fiber", "DSL", "None"]
    autopay: Literal[0, 1]
    senior_citizen: Literal[0, 1]

@lru_cache(maxsize=1)
def get_model():
    if not settings.model_path.exists():
        raise RuntimeError("Model artifact is absent. Train the model before serving.")
    return joblib.load(settings.model_path)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}

@app.post("/predict")
def predict(request: ChurnRequest) -> dict[str, float | int]:
    try:
        frame = pd.DataFrame([request.model_dump()])[MODEL_FEATURES]
        probability = float(get_model().predict_proba(frame)[:, 1][0])
        return {
            "churn_probability": round(probability, 6),
            "churn_prediction": int(probability >= settings.decision_threshold),
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
