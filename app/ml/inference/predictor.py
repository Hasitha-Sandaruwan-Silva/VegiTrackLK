"""
app/ml/inference/predictor.py
==============================
Uses loaded models to predict vegetable prices.
"""

from __future__ import annotations

from datetime import datetime

from fastapi import HTTPException

from app.ml.inference.feature_builder import build_features
from app.ml.inference.loader import ModelLoader


class Predictor:
    def __init__(self, loader: ModelLoader) -> None:
        self.loader = loader

    def _encode_item(self, item: str) -> int:
        le = self.loader.le
        if le is None:
            raise HTTPException(status_code=503, detail="Label encoder not loaded")

        lower_map = {c.lower(): c for c in le.classes_}
        canonical = lower_map.get(item.lower())
        if canonical is None:
            raise HTTPException(
                status_code=404,
                detail=f"Item '{item}' not found in ML encoder. "
                       f"Available: {list(le.classes_)}",
            )
        return int(le.transform([canonical])[0])

    def predict(
        self,
        item: str,
        pred_dt: datetime,
        avg_wholesale_price: float,
        price_spread: float = 0.0,
        is_crisis_period: int = 0,
        model_name: str = "random_forest",
    ) -> float:
        item_encoded = self._encode_item(item)

        X = build_features(
            item_encoded=item_encoded,
            pred_dt=pred_dt,
            avg_wholesale_price=avg_wholesale_price,
            price_spread=price_spread,
            is_crisis_period=is_crisis_period,
        )

        model_name = model_name.lower()

        if model_name == "linear_regression":
            model = self.loader.lr_model
            label = "Linear Regression"
        else:
            model = self.loader.rf_model
            label = "Random Forest"

        if model is None:
            raise HTTPException(
                status_code=503,
                detail=f"{label} model not loaded. Run ml/train/train_models.py first.",
            )

        return float(model.predict(X)[0])