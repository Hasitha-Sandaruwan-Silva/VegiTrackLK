"""
app/api/v1/endpoints/health.py
================================
GET /api/v1/health
"""

from fastapi import APIRouter, Depends

from app.api.deps import get_model_service, get_price_repo, get_forecast_service
from app.core.config import settings
from app.repositories.price_repository import PriceRepository
from app.services.forecast_service import ForecastService
from app.services.model_service import ModelService

router = APIRouter()


@router.get("/")
def health_check(
    price_repo:       PriceRepository  = Depends(get_price_repo),
    forecast_service: ForecastService  = Depends(get_forecast_service),
    model_service:    ModelService     = Depends(get_model_service),
):
    price_df    = price_repo.get_df()
    forecast    = forecast_service.get_forecast()
    model_stat  = model_service.status()

    return {
        "status":          "ok",
        "version":         settings.VERSION,
        "prices_loaded":   not price_df.empty,
        "prices_rows":     len(price_df),
        "forecast_loaded": forecast["count"] > 0,
        "forecast_rows":   forecast["count"],
        "items_count":     len(price_repo.get_items()),
        "rf_model_ready":  model_stat["rf_model_ready"],
        "lr_model_ready":  model_stat["lr_model_ready"],
    }