from fastapi import FastAPI
from pydantic import BaseModel
from .model import predict
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()


class PredictResponse(BaseModel):
    is_toxic: bool


cnt = Counter("app_http_inference_count", "Number of HTTP inference calls")


@app.get("/predict", response_model=PredictResponse)
def predict_get(text: str):
    cnt.inc()
    return {"is_toxic": predict(text)}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
