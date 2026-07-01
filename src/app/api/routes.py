from fastapi import APIRouter, Depends, HTTPException, status

from src.app.core.config import MODEL_TYPE
from src.app.ml.features import SELECTED_FEATURES
from src.app.ml.predictor import (
    BreastCancerPredictor,
    ModelNotAvailableError,
    get_predictor,
)
from src.app.schemas.analysis import (
    AnalysisRequest,
    AnalysisResponse,
    HealthResponse,
    ModelMetadataResponse,
)
from src.app.services.analysis_service import AnalysisService


router = APIRouter()


def get_analysis_service(
    predictor: BreastCancerPredictor = Depends(get_predictor),
) -> AnalysisService:
    return AnalysisService(predictor)


@router.get("/health", response_model=HealthResponse)
def health(
    predictor: BreastCancerPredictor = Depends(get_predictor),
) -> HealthResponse:
    return HealthResponse(status="ok", model_available=predictor.is_available)


@router.get("/model/metadata", response_model=ModelMetadataResponse)
def model_metadata(
    predictor: BreastCancerPredictor = Depends(get_predictor),
) -> ModelMetadataResponse:
    return ModelMetadataResponse(
        model_type=MODEL_TYPE,
        model_available=predictor.is_available,
        required_features=SELECTED_FEATURES,
        class_labels={"B": "benign", "M": "malignant"},
    )


@router.post("/analysis", response_model=AnalysisResponse)
def analyze(
    request: AnalysisRequest,
    service: AnalysisService = Depends(get_analysis_service),
) -> AnalysisResponse:
    try:
        return service.analyze(request)
    except ModelNotAvailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
