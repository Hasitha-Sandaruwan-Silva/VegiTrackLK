"""
app/schemas/prediction.py
==========================
ML prediction request/response schemas.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    item: str = Field(..., example="Tomato")
    predict_date: str = Field(..., example="2025-08-15")
    avg_wholesale_price: float = Field(..., example=120.0)
    price_spread: float = Field(default=0.0, example=15.0)
    is_crisis_period: int = Field(default=0, ge=0, le=1)
    model: str = Field(
        default="random_forest",
        example="random_forest",
        description="random_forest | linear_regression",
    )


class PredictionResponse(BaseModel):
    item: str
    predict_date: str
    model: str
    predicted_price: float
    currency: str
    unit: str