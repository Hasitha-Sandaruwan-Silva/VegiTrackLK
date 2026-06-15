"""
app/ml/inference/feature_builder.py
=====================================
Builds feature vector for ML prediction.
"""

from __future__ import annotations

from datetime import datetime

import pandas as pd

from app.core.constants import FEATURE_COLS


def build_features(
    item_encoded: int,
    pred_dt: datetime,
    avg_wholesale_price: float,
    price_spread: float,
    is_crisis_period: int,
) -> pd.DataFrame:
    """
    Returns a single-row DataFrame with FEATURE_COLS order.
    """
    feat = {
        "item_encoded":        item_encoded,
        "year":                pred_dt.year,
        "month":               pred_dt.month,
        "day":                 pred_dt.day,
        "day_of_week":         pred_dt.weekday(),
        "week_of_year":        pred_dt.isocalendar()[1],
        "quarter":             (pred_dt.month - 1) // 3 + 1,
        "is_weekend":          int(pred_dt.weekday() >= 5),
        "is_crisis_period":    is_crisis_period,
        "avg_wholesale_price": avg_wholesale_price,
        "price_spread":        price_spread,
    }
    return pd.DataFrame([feat])[FEATURE_COLS]