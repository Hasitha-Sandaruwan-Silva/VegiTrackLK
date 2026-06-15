"""
app/schemas/health.py
======================
Health check response schema.
"""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    version: str
    prices_loaded: bool
    prices_rows: int
    forecast_loaded: bool
    forecast_rows: int
    items_count: int
    rf_model_ready: bool
    lr_model_ready: bool