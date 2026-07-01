from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.api.routes import router
from src.app.core.config import ALLOWED_CORS_ORIGINS, APP_NAME, APP_VERSION


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="API para detecção de câncer de mama usando um modelo Naive Bayes Gaussiano treinado",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
