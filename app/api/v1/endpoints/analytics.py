"""
app/api/v1/endpoints/analytics.py
===================================
GET /api/v1/analytics/summary
GET /api/v1/analytics/markets
GET /api/v1/analytics/trends
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query

from app.api.deps import get_analytics_service, get_price_service
from app.services.analytics_service import AnalyticsService
from app.services.price_service import PriceService
from app.utils.validators import validate_item, validate_market

router = APIRouter()


@router.get("/summary")
def get_summary(
    market: str           = Query(..., description="Market column name"),
    item:   str | None    = Query(None, description="Filter by vegetable"),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
    price_service:     PriceService     = Depends(get_price_service),
):
    validate_market(market)
    exact_item = None
    if item:
        exact_item = validate_item(item, price_service.get_items())

    return analytics_service.get_summary(market=market, item=exact_item)


@router.get("/markets")
def get_markets(
    analytics_service: AnalyticsService = Depends(get_analytics_service),
):
    return analytics_service.get_markets()


@router.get("/trends")
def get_trends(
    item:   str = Query(..., description="Vegetable name"),
    market: str = Query(..., description="Market column name"),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
    price_service:     PriceService     = Depends(get_price_service),
):
    validate_market(market)
    exact_item = validate_item(item, price_service.get_items())
    return analytics_service.get_trends(item=exact_item, market=market)