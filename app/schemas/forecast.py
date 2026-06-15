"""
app/schemas/forecast.py
========================
Forecast response schemas.
"""

from __future__ import annotations

from pydantic import BaseModel


class ForecastRecord(BaseModel):
    date: str
    item: str
    predicted_price: float | None
    market: str | None
    currency: str | None
    unit: str | None
    model: str | None


class ForecastResponse(BaseModel):
    count: int
    forecast: list[ForecastRecord]