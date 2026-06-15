"""
app/schemas/analytics.py
=========================
Analytics summary and trends schemas.
"""

from __future__ import annotations

from pydantic import BaseModel


class SummaryRecord(BaseModel):
    item: str
    mean: float | None
    min: float | None
    max: float | None
    std: float | None
    count: int


class SummaryResponse(BaseModel):
    market: str
    count: int
    summary: list[SummaryRecord]


class MarketAvgRecord(BaseModel):
    item: str
    Wholesale_Pettah: float | None = None
    Wholesale_Dambulla: float | None = None
    Retail_Pettah: float | None = None
    Retail_Dambulla: float | None = None
    Retail_Narahenpita: float | None = None


class MarketsResponse(BaseModel):
    period: str | None
    count: int
    markets: list[MarketAvgRecord]


class TrendRecord(BaseModel):
    period: str
    year: int
    month: int
    avg_price: float


class TrendsResponse(BaseModel):
    item: str
    market: str
    count: int
    trends: list[TrendRecord]