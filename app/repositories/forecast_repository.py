"""
app/repositories/forecast_repository.py
=========================================
Forecast CSV repository.
"""

from __future__ import annotations

import pandas as pd

from app.core.config import settings
from app.core.logger import logger
from app.repositories.csv_repository import CSVRepository


class ForecastRepository(CSVRepository):
    def __init__(self) -> None:
        super().__init__(
            settings.FORECASTS_DIR / settings.FORECAST_CSV
        )
        self._df: pd.DataFrame | None = None

    def get_df(self) -> pd.DataFrame:
        if self._df is None:
            self._df = self._load_and_clean()
        return self._df

    def _load_and_clean(self) -> pd.DataFrame:
        df = self.load_data()

        if df.empty:
            return df

        # Normalize column names
        if "predicted_price" not in df.columns and "predicted" in df.columns:
            df = df.rename(columns={"predicted": "predicted_price"})
        if "market" not in df.columns:
            df["market"] = "Retail_Pettah (RF Forecast)"

        logger.info("ForecastRepository ready | rows=%d", len(df))
        return df