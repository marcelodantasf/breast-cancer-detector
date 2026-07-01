from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
MODEL_PATH = PROJECT_ROOT / "models" / "naive_bayes_model.joblib"

APP_NAME = "Breast Cancer Detector API"
APP_VERSION = "0.1.0"
MODEL_TYPE = "Gaussian Naive Bayes"

ALLOWED_CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]
