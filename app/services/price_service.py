"""
app/services/price_service.py
==============================
Business logic for price data.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from app.core.constants import MARKET_COLUMNS
from app.core.logger import logger
from app.repositories.price_repository import PriceRepository


class PriceService:
    def __init__(self, repo: PriceRepository) -> None:
        self.repo = repo

    def get_items(self) -> list[str]:
        return self.repo.get_items()

    def get_prices(
        self,
        item: str,
        market: str,
        year: int | None = None,
        month: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        limit: int = 500,
        offset: int = 0,
    ) -> dict:
        df = self.repo.get_df()

        f = df[df["item"] == item].copy()

        if year:
            f = f[f["year"] == year]
        if month:
            f = f[f["month"] == month]
        if start_date:
            f = f[f["date"] >= pd.Timestamp(start_date)]
        if end_date:
            f = f[f["date"] <= pd.Timestamp(end_date)]

        f = f.dropna(subset=[market]).sort_values("date")
        total = len(f)
        f = f.iloc[offset: offset + limit]

        records = [
            {
                "date":   row["date"].date().isoformat(),
                "item":   row["item"],
                "market": market,
                "price":  round(float(row[market]), 2),
            }
            for _, row in f.iterrows()
        ]

        return {
            "total":   total,
            "limit":   limit,
            "offset":  offset,
            "count":   len(records),
            "prices":  records,
        }

    def get_price_comparison(self, item: str) -> dict:
        df = self.repo.get_df()
        item_df = df[df["item"] == item].copy()

        if item_df.empty:
            return {"item": item, "period": None, "comparison": []}

        latest_date = item_df["date"].max()
        ly = int(latest_date.year)
        lm = int(latest_date.month)
        month_df = item_df[
            (item_df["year"] == ly) & (item_df["month"] == lm)
        ]

        comparison = []
        for col in MARKET_COLUMNS:
            vals = month_df[col].dropna()
            avg  = round(float(vals.mean()), 2) if not vals.empty else None
            comparison.append({"market": col, "avg_price": avg})

        valid    = [c for c in comparison if c["avg_price"] is not None]
        cheapest = min(valid, key=lambda x: x["avg_price"]) if valid else None

        return {
            "item":            item,
            "period":          f"{ly}-{lm:02d}",
            "cheapest_market": cheapest["market"]    if cheapest else None,
            "cheapest_price":  cheapest["avg_price"] if cheapest else None,
            "comparison":      comparison,
        }