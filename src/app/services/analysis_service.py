from src.app.core.config import MODEL_TYPE
from src.app.ml.features import SELECTED_FEATURES
from src.app.ml.predictor import BreastCancerPredictor
from src.app.schemas.analysis import AnalysisRequest, AnalysisResponse


CLASS_LABELS = {
    0: ("B", "benign"),
    1: ("M", "malignant"),
}


class AnalysisService:
    def __init__(self, predictor: BreastCancerPredictor):
        self.predictor = predictor

    def analyze(self, request: AnalysisRequest) -> AnalysisResponse:
        feature_values = (
            request.model_dump() if hasattr(request, "model_dump") else request.dict()
        )
        result = self.predictor.predict(feature_values)

        prediction, prediction_label = CLASS_LABELS[int(result["class_id"])]

        return AnalysisResponse(
            prediction=prediction,
            prediction_label=prediction_label,
            probabilities=result["probabilities"],
            model_type=MODEL_TYPE,
            features_used=SELECTED_FEATURES,
        )
