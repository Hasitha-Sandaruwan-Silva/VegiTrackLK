"""
app/schemas/price.py
=====================
Price request/response schemas.
"""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, Field


class PriceRecord(BaseModel):
    date: str
    item: str
    market: str
    price: float | None


class PricesResponse(BaseModel):
    total: int
    limit: int
    offset: int
    count: int
    prices: list[PriceRecord]


class MarketRecord(BaseModel):
    market: str
    avg_price: float | None


class PriceComparisonResponse(BaseModel):
    item: str
    period: str | None
    cheapest_market: str | None
    cheapest_price: float | None
    comparison: list[MarketRecord]