"""
app/core/config.py
==================
Central configuration using pydantic-settings.
All paths and env vars managed here.
"""

from __future__ import annotations

import os
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ── Project ──────────────────────────────────────────
    PROJECT_NAME: str = "VegiTrack LK"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Sri Lanka Vegetable Price Intelligence API"
    API_V1_STR: str = "/api/v1"

    # ── Paths ─────────────────────────────────────────────
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    RAW_DIR: Path = DATA_DIR / "raw"
    PROCESSED_DIR: Path = DATA_DIR / "processed"
    MODELS_DIR: Path = BASE_DIR / "artifacts" / "models"
    FORECASTS_DIR: Path = BASE_DIR / "artifacts" / "forecasts"
    REPORTS_DIR: Path = BASE_DIR / "artifacts" / "reports"

    # ── Data files ────────────────────────────────────────
    RAW_CSV: str = "vegetable_prices.csv"
    CLEAN_CSV: str = "vegetable_prices_clean.csv"
    FORECAST_CSV: str = "next_week_forecast.csv"

    # ── ML model files ────────────────────────────────────
    RF_MODEL_FILE: str = "random_forest.pkl"
    LR_MODEL_FILE: str = "linear_regression.pkl"
    LE_FILE: str = "label_encoder.pkl"

    # ── CORS ──────────────────────────────────────────────
    CORS_ORIGINS: list[str] = ["*"]

    # ── Pagination ────────────────────────────────────────
    DEFAULT_LIMIT: int = 500
    MAX_LIMIT: int = 5000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()