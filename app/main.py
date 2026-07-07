import logging
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.predict import ModelService


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="MLOps Model Service",
    description="Simple ML model API for Iris classification",
    version="1.0.0"
)

model_service = ModelService()


class PredictionRequest(BaseModel):
    features: List[float] = Field(
        ...,
        min_length=4,
        max_length=4,
        description="Iris flower features: sepal length, sepal width, petal length, petal width"
    )


class PredictionResponse(BaseModel):
    prediction: int
    class_name: str


@app.get("/") # сервис живой
def root():
    return {
        "service": "mlops-model-service",
        "status": "running"
    }


@app.get("/health") # ewndpoint для healthcheck
def health_check():
    return {
        "status": "ok"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest): # endpoint для предсказания
    logger.info(f"Received prediction request: {request.features}")

    try:
        result = model_service.predict(request.features)
        logger.info(f"Prediction result: {result}")
        return result

    except Exception as error:
        logger.error(f"Prediction error: {error}")
        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )