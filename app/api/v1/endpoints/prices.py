"""
app/api/v1/endpoints/prices.py
================================
GET /api/v1/prices
GET /api/v1/prices/comparison
"""

from __future__ import annotations

from datetime import date

from fastapi import APIRouter, Depends, Query

from app.api.deps import get_price_service
from app.core.config import settings
from app.services.price_service import PriceService
from app.utils.validators import validate_item, validate_market

router = APIRouter()


@router.get("/")
def get_prices(
    item:       str         = Query(..., description="Vegetable name"),
    market:     str         = Query(..., description="Market column name"),
    year:       int | None  = Query(None),
    month:      int | None  = Query(None, ge=1, le=12),
    start_date: date | None = Query(None, description="YYYY-MM-DD"),
    end_date:   date | None = Query(None, description="YYYY-MM-DD"),
    limit:      int         = Query(500, ge=1, le=5000),
    offset:     int         = Query(0, ge=0),
    price_service: PriceService = Depends(get_price_service),
):
    validate_market(market)
    exact_item = validate_item(item, price_service.get_items())

    return price_service.get_prices(
        item=exact_item,
        market=market,
        year=year,
        month=month,
        start_date=str(start_date) if start_date else None,
        end_date=str(end_date) if end_date else None,
        limit=limit,
        offset=offset,
    )


@router.get("/comparison")
def get_price_comparison(
    item: str = Query(..., description="Vegetable name"),
    price_service: PriceService = Depends(get_price_service),
):
    exact_item = validate_item(item, price_service.get_items())
    return price_service.get_price_comparison(item=exact_item)