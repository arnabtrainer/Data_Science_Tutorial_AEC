from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    random_seed: int = 42
    test_size: float = 0.20
    decision_threshold: float = 0.40
    model_path: Path = Path("artifacts/churn_pipeline.joblib")
