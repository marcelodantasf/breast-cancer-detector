from functools import lru_cache
from typing import Dict

import joblib
import pandas as pd

from src.app.core.config import MODEL_PATH
from src.app.ml.features import SELECTED_FEATURES


class ModelNotAvailableError(RuntimeError):
    pass


class BreastCancerPredictor:
    def __init__(self, model_path=MODEL_PATH):
        self.model_path = model_path
        self.model = None

    @property
    def is_available(self) -> bool:
        return self.model_path.exists()

    def load(self):
        if self.model is None:
            if not self.model_path.exists():
                raise ModelNotAvailableError(f"Model file not found: {self.model_path}")
            self.model = joblib.load(self.model_path)
        return self.model

    def predict(self, feature_values: Dict[str, float]) -> Dict[str, object]:
        model = self.load()
        ordered_values = [feature_values[feature] for feature in SELECTED_FEATURES]
        frame = pd.DataFrame([ordered_values], columns=SELECTED_FEATURES)

        predicted_class = int(model.predict(frame)[0])
        probabilities = self._class_probabilities(model, frame)

        return {
            "class_id": predicted_class,
            "probabilities": probabilities,
        }

    @staticmethod
    def _class_probabilities(model, frame) -> Dict[str, float]:
        if not hasattr(model, "predict_proba"):
            return {"benign": 0.0, "malignant": 0.0}

        raw_probabilities = model.predict_proba(frame)[0]
        class_probabilities = {
            int(class_id): float(probability)
            for class_id, probability in zip(model.classes_, raw_probabilities)
        }

        return {
            "benign": class_probabilities.get(0, 0.0),
            "malignant": class_probabilities.get(1, 0.0),
        }


@lru_cache
def get_predictor() -> BreastCancerPredictor:
    return BreastCancerPredictor()
