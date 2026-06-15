"""
app/api/v1/endpoints/forecasts.py
===================================
GET /api/v1/forecasts
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query

from app.api.deps import get_forecast_service, get_price_service
from app.services.forecast_service import ForecastService
from app.services.price_service import PriceService
from app.utils.validators import validate_item

router = APIRouter()


@router.get("/")
def get_forecast(
    item: str | None = Query(None, description="Filter by vegetable name"),
    forecast_service: ForecastService = Depends(get_forecast_service),
    price_service:    PriceService    = Depends(get_price_service),
):
    exact_item = None
    if item is not None:
        exact_item = validate_item(item, price_service.get_items())

    return forecast_service.get_forecast(item=exact_item)