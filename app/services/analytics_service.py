"""
app/services/analytics_service.py
===================================
Business logic for analytics endpoints.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from app.core.constants import MARKET_COLUMNS
from app.core.logger import logger
from app.repositories.price_repository import PriceRepository


class AnalyticsService:
    def __init__(self, repo: PriceRepository) -> None:
        self.repo = repo

    def _nan_to_none(self, records: list[dict]) -> list[dict]:
        for rec in records:
            for k, v in rec.items():
                if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
                    rec[k] = None
        return records

    def get_summary(
        self,
        market: str,
        item: str | None = None,
    ) -> dict:
        df = self.repo.get_df()

        if item:
            df = df[df["item"] == item]

        group = (
            df.groupby("item")[market]
            .agg(mean="mean", min="min", max="max", std="std", count="count")
            .reset_index()
            .sort_values("item")
        )

        for col in ["mean", "min", "max", "std"]:
            group[col] = pd.to_numeric(group[col], errors="coerce").round(2)
        group["count"] = group["count"].astype(int)

        records = self._nan_to_none(group.to_dict(orient="records"))
        return {"market": market, "count": len(records), "summary": records}

    def get_markets(self) -> dict:
        df = self.repo.get_df()
        latest_date = df["date"].max()

        if pd.isna(latest_date):
            return {"period": None, "count": 0, "markets": []}

        ly = int(latest_date.year)
        lm = int(latest_date.month)
        latest_df = df[(df["year"] == ly) & (df["month"] == lm)].copy()

        if latest_df.empty:
            return {"period": f"{ly}-{lm:02d}", "count": 0, "markets": []}

        market_avg = (
            latest_df.groupby("item")[MARKET_COLUMNS]
            .mean()
            .reset_index()
            .sort_values("item")
        )
        market_avg[MARKET_COLUMNS] = market_avg[MARKET_COLUMNS].round(2)
        records = self._nan_to_none(market_avg.to_dict(orient="records"))

        return {
            "period": f"{ly}-{lm:02d}",
            "count":  len(records),
            "markets": records,
        }

    def get_trends(self, item: str, market: str) -> dict:
        df = self.repo.get_df()
        item_df = df[df["item"] == item].dropna(subset=[market]).copy()

        if item_df.empty:
            return {"item": item, "market": market, "count": 0, "trends": []}

        monthly = (
            item_df.groupby(["year", "month"])[market]
            .mean()
            .reset_index()
            .rename(columns={market: "avg_price"})
            .sort_values(["year", "month"])
        )
        monthly["avg_price"] = monthly["avg_price"].round(2)
        monthly["period"]    = monthly.apply(
            lambda r: f"{int(r['year'])}-{int(r['month']):02d}", axis=1
        )

        records = monthly[["period", "year", "month", "avg_price"]].to_dict(
            orient="records"
        )
        return {
            "item":   item,
            "market": market,
            "count":  len(records),
            "trends": records,
        }