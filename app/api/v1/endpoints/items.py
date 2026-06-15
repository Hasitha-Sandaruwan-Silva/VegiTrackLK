"""
app/api/v1/endpoints/items.py
================================
GET /api/v1/items
GET /api/v1/items/markets
"""

from fastapi import APIRouter, Depends

from app.api.deps import get_price_service
from app.core.constants import MARKET_COLUMNS
from app.services.price_service import PriceService

router = APIRouter()


@router.get("/")
def get_items(price_service: PriceService = Depends(get_price_service)):
    items = price_service.get_items()
    return {"count": len(items), "items": items}


@router.get("/markets")
def get_markets():
    return {"count": len(MARKET_COLUMNS), "markets": MARKET_COLUMNS}