"""
app/api/v1/endpoints/predictions.py
=====================================
POST /api/v1/predict
"""

from fastapi import APIRouter, Depends

from app.api.deps import get_prediction_service, get_price_service
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction_service import PredictionService
from app.services.price_service import PriceService
from app.utils.validators import validate_item

router = APIRouter()


@router.post("/", response_model=PredictionResponse)
def predict_price(
    req: PredictionRequest,
    prediction_service: PredictionService = Depends(get_prediction_service),
    price_service:      PriceService      = Depends(get_price_service),
):
    exact_item = validate_item(req.item, price_service.get_items())

    return prediction_service.predict(
        item=exact_item,
        predict_date=req.predict_date,
        avg_wholesale_price=req.avg_wholesale_price,
        price_spread=req.price_spread,
        is_crisis_period=req.is_crisis_period,
        model=req.model,
    )