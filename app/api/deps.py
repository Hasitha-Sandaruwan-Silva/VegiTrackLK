"""
app/api/deps.py
================
Dependency injection for FastAPI endpoints.
All services created once and injected.
"""

from __future__ import annotations

from functools import lru_cache

from app.ml.inference.loader import model_loader
from app.ml.inference.predictor import Predictor
from app.repositories.forecast_repository import ForecastRepository
from app.repositories.price_repository import PriceRepository
from app.services.analytics_service import AnalyticsService
from app.services.forecast_service import ForecastService
from app.services.model_service import ModelService
from app.services.prediction_service import PredictionService
from app.services.price_service import PriceService

# ── Repositories (singleton) ──────────────────────────────────────────────────
price_repo    = PriceRepository()
forecast_repo = ForecastRepository()

# ── ML ────────────────────────────────────────────────────────────────────────
predictor = Predictor(loader=model_loader)

# ── Services (singleton) ──────────────────────────────────────────────────────
price_service      = PriceService(repo=price_repo)
forecast_service   = ForecastService(repo=forecast_repo)
analytics_service  = AnalyticsService(repo=price_repo)
prediction_service = PredictionService(predictor=predictor)
model_service      = ModelService(loader=model_loader)


# ── FastAPI dependency functions ──────────────────────────────────────────────
def get_price_service() -> PriceService:
    return price_service

def get_forecast_service() -> ForecastService:
    return forecast_service

def get_analytics_service() -> AnalyticsService:
    return analytics_service

def get_prediction_service() -> PredictionService:
    return prediction_service

def get_model_service() -> ModelService:
    return model_service

def get_price_repo() -> PriceRepository:
    return price_repo