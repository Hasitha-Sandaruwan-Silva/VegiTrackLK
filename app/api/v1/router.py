"""
app/api/v1/router.py
=====================
Master router - all v1 endpoints registered here.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    analytics,
    forecasts,
    health,
    items,
    predictions,
    prices,
)

api_router = APIRouter()

api_router.include_router(health.router,      prefix="/health",      tags=["Health"])
api_router.include_router(items.router,       prefix="/items",       tags=["Items"])
api_router.include_router(prices.router,      prefix="/prices",      tags=["Prices"])
api_router.include_router(forecasts.router,   prefix="/forecasts",   tags=["Forecasts"])
api_router.include_router(analytics.router,   prefix="/analytics",   tags=["Analytics"])
api_router.include_router(predictions.router, prefix="/predict",     tags=["Predictions"])