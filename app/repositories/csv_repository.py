"""
app/repositories/csv_repository.py
====================================
Base CSV repository.
Swap load_data() with DB query later when PostgreSQL is added.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from app.core.logger import logger


class CSVRepository:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        if not self.file_path.exists():
            logger.error("CSV file not found: %s", self.file_path)
            return pd.DataFrame()

        try:
            df = pd.read_csv(self.file_path)
            logger.info(
                "Loaded CSV: %s | rows=%d cols=%d",
                self.file_path.name,
                len(df),
                len(df.columns),
            )
            return df
        except Exception as exc:
            logger.exception("Failed to load CSV %s: %s", self.file_path, exc)
            return pd.DataFrame()