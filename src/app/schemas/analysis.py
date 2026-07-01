from typing import Dict, List, Literal

from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    worst_concave_points: float = Field(..., ge=0)
    worst_perimeter: float = Field(..., ge=0)
    mean_compactness: float = Field(..., ge=0)
    se_radius: float = Field(..., ge=0)
    worst_texture: float = Field(..., ge=0)
    worst_smoothness: float = Field(..., ge=0)
    worst_symmetry: float = Field(..., ge=0)
    se_concave_points: float = Field(..., ge=0)

    class Config:
        extra = "forbid"


class AnalysisResponse(BaseModel):
    prediction: Literal["B", "M"]
    prediction_label: Literal["benign", "malignant"]
    probabilities: Dict[str, float]
    model_type: str
    features_used: List[str]


class HealthResponse(BaseModel):
    status: Literal["ok"]
    model_available: bool


class ModelMetadataResponse(BaseModel):
    model_type: str
    model_available: bool
    required_features: List[str]
    class_labels: Dict[str, str]
