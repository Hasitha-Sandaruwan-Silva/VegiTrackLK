"""
app/services/forecast_service.py
==================================
Business logic for forecast data.
"""

from __future__ import annotations

import numpy as np

from app.repositories.forecast_repository import ForecastRepository


class ForecastService:
    def __init__(self, repo: ForecastRepository) -> None:
        self.repo = repo

    def _nan_to_none(self, records: list[dict]) -> list[dict]:
        for rec in records:
            for k, v in rec.items():
                if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
                    rec[k] = None
        return records

    def get_forecast(self, item: str | None = None) -> dict:
        df = self.repo.get_df().copy()

        if item is not None and "item" in df.columns:
            df = df[df["item"] == item]

        records = self._nan_to_none(df.to_dict(orient="records"))
        return {"count": len(records), "forecast": records}