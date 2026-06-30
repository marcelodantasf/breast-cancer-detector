# Backend Architecture Definition

This backend should be implemented as a **FastAPI application** whose main responsibility is to expose a clean API for breast cancer diagnostic analysis.

At this stage, the project is intentionally skipping model training. Therefore, the backend architecture should be prepared to receive feature values, validate them, call a future analysis/prediction service, and return a structured response. The model implementation can be plugged in later without changing the public API.

## Main Requirement

The main endpoint must be:

```http
POST /analysis
```

This endpoint should receive the selected WDBC predictor variables from the exploratory analysis and return an analysis result.

## Recommended Directory Structure

The existing scaffold already suggests a good separation of responsibilities:

```text
src/app/
├── api/
│   ├── __init__.py
│   └── routes.py
├── core/
│   ├── __init__.py
│   └── config.py
├── ml/
│   ├── __init__.py
│   ├── features.py
│   └── predictor.py
├── services/
│   ├── __init__.py
│   └── analysis_service.py
├── __init__.py
└── main.py
```

## Responsibility of Each Layer

### `main.py`

This file should create the FastAPI application instance.

Responsibilities:

- initialize the FastAPI app;
- include API routers;
- define application metadata such as title, version, and description;
- optionally expose a simple health endpoint such as `GET /health`.

`main.py` should stay small. It should not contain validation rules, prediction logic, or business logic.

### `api/routes.py`

This file should define HTTP endpoints.

Responsibilities:

- define `POST /analysis`;
- receive and validate request bodies using Pydantic schemas;
- call the analysis service;
- return structured API responses.

The route should not directly load models or calculate predictions. Its job is to translate HTTP requests into service calls.

### `services/analysis_service.py`

This file should contain the application-level analysis workflow.

Responsibilities:

- receive validated input data from the API layer;
- convert the request into the feature order expected by the ML layer;
- call the future predictor;
- format the result into a response object;
- centralize business rules such as confidence interpretation.

This service acts as the bridge between the API and machine learning code.

### `ml/features.py`

This file should define the selected features and their expected order.

The selected features from the EDA are:

```python
SELECTED_FEATURES = [
    "worst_concave_points",
    "worst_perimeter",
    "mean_compactness",
    "se_radius",
    "worst_texture",
    "worst_smoothness",
    "worst_symmetry",
    "se_concave_points",
]
```

Keeping this list in one place is important because model training and model inference must use the same feature order.

### `ml/predictor.py`

This file should eventually load and use the trained Gaussian Naive Bayes model.

Responsibilities after model training exists:

- load the serialized model from `/models`;
- receive a feature vector in the correct order;
- return predicted class and probabilities;
- hide model-specific details from the API and service layers.

For now, this module can expose a placeholder interface so the rest of the backend can be designed without training the model yet.

### `core/config.py`

This file should centralize configuration.

Possible configuration values:

- project name;
- API version;
- model path;
- allowed CORS origins;
- debug mode.

Keeping configuration separate avoids hardcoding paths and environment-specific values inside route or service files.

## `POST /analysis` Request Contract

The request body should contain the selected quantitative predictor variables.

Example:

```json
{
  "worst_concave_points": 0.2654,
  "worst_perimeter": 184.6,
  "mean_compactness": 0.2776,
  "se_radius": 1.095,
  "worst_texture": 17.33,
  "worst_smoothness": 0.1622,
  "worst_symmetry": 0.4601,
  "se_concave_points": 0.01587
}
```

All fields should be numeric because they are quantitative continuous variables derived from the WDBC dataset.

## Validation Rules

The API should validate input using Pydantic.

Recommended rules:

- all selected features are required;
- all selected features must be numbers;
- values should be non-negative because the WDBC measurements represent physical quantities;
- unknown or extra fields should be rejected to avoid accidental mismatch with the model feature set.

Strict validation is important because the model will assume that the input has the same structure as the training data.

## `POST /analysis` Response Contract

Once the model is available, the response should include:

```json
{
  "prediction": "M",
  "prediction_label": "malignant",
  "probabilities": {
    "benign": 0.03,
    "malignant": 0.97
  },
  "selected_features_used": [
    "worst_concave_points",
    "worst_perimeter",
    "mean_compactness",
    "se_radius",
    "worst_texture",
    "worst_smoothness",
    "worst_symmetry",
    "se_concave_points"
  ],
  "model_type": "Gaussian Naive Bayes"
}
```

During the period before model training, the response may instead return a clear placeholder message, for example:

```json
{
  "status": "model_not_available",
  "message": "The analysis endpoint is defined, but the model has not been trained yet.",
  "selected_features_received": [
    "worst_concave_points",
    "worst_perimeter",
    "mean_compactness",
    "se_radius",
    "worst_texture",
    "worst_smoothness",
    "worst_symmetry",
    "se_concave_points"
  ]
}
```

## Why This Architecture Fits the Project

This structure separates concerns cleanly:

- FastAPI handles HTTP communication.
- Pydantic schemas handle input validation.
- The service layer handles application workflow.
- The ML layer handles feature ordering and prediction.
- The configuration layer handles project settings.

This makes the backend easier to test, easier to explain in a university project, and easier to extend once the Gaussian Naive Bayes model is trained.

## Suggested Implementation Order

1. Create the FastAPI app in `main.py`.
2. Define Pydantic request and response schemas.
3. Implement `POST /analysis` in `api/routes.py`.
4. Store the selected feature list in `ml/features.py`.
5. Implement `analysis_service.py` with a temporary placeholder response.
6. After model training, implement `ml/predictor.py` and connect it to the service.

This order allows the API contract to be developed now while postponing model training until the project reaches that stage.
