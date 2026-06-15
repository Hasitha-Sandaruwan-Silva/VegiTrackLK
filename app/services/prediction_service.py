"""
app/services/prediction_service.py
====================================
Business logic for ML predictions.
Calls ml/inference/predictor.
"""

from __future__ import annotations

from datetime import datetime

from app.core.constants import CURRENCY, UNIT
from app.ml.inference.predictor import Predictor


class PredictionService:
    def __init__(self, predictor: Predictor) -> None:
        self.predictor = predictor

    def predict(
        self,
        item: str,
        predict_date: str,
        avg_wholesale_price: float,
        price_spread: float = 0.0,
        is_crisis_period: int = 0,
        model: str = "random_forest",
    ) -> dict:
        pred_dt = datetime.strptime(predict_date, "%Y-%m-%d")

        predicted_price = self.predictor.predict(
            item=item,
            pred_dt=pred_dt,
            avg_wholesale_price=avg_wholesale_price,
            price_spread=price_spread,
            is_crisis_period=is_crisis_period,
            model_name=model,
        )

        return {
            "item":            item,
            "predict_date":    predict_date,
            "model":           model,
            "predicted_price": round(predicted_price, 2),
            "currency":        CURRENCY,
            "unit":            UNIT,
        }