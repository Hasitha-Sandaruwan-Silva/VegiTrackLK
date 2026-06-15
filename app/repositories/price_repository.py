"""
app/repositories/price_repository.py
======================================
Price data repository.
Loads and caches the cleaned vegetable price CSV.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from app.core.config import settings
from app.core.constants import MARKET_COLUMNS
from app.core.logger import logger
from app.repositories.csv_repository import CSVRepository


class PriceRepository(CSVRepository):
    def __init__(self) -> None:
        super().__init__(
            settings.PROCESSED_DIR / settings.CLEAN_CSV
        )
        self._df: pd.DataFrame | None = None

    def get_df(self) -> pd.DataFrame:
        """Return cached dataframe. Load once on first call."""
        if self._df is None:
            self._df = self._load_and_clean()
        return self._df

    def _load_and_clean(self) -> pd.DataFrame:
        df = self.load_data()

        if df.empty:
            return df

        # Parse dates
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"]).copy()

        # Ensure year/month columns
        df["year"]  = df["date"].dt.year.astype(int)
        df["month"] = df["date"].dt.month.astype(int)
        df["item"]  = df["item"].astype(str).str.strip()

        # Numeric market columns
        for col in MARKET_COLUMNS:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
            else:
                df[col] = np.nan

        df = df.sort_values("date").reset_index(drop=True)
        logger.info(
            "PriceRepository ready | rows=%d items=%s",
            len(df),
            sorted(df["item"].unique().tolist()),
        )
        return df

    def get_items(self) -> list[str]:
        df = self.get_df()
        if df.empty:
            return []
        return sorted(df["item"].dropna().unique().tolist())