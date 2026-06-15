"""
app/services/model_service.py
==============================
Exposes ML model health status.
"""

from __future__ import annotations

from app.ml.inference.loader import ModelLoader


class ModelService:
    def __init__(self, loader: ModelLoader) -> None:
        self.loader = loader

    def status(self) -> dict:
        return {
            "rf_model_ready": self.loader.rf_model is not None,
            "lr_model_ready": self.loader.lr_model is not None,
            "le_ready":       self.loader.le is not None,
            "items":          list(self.loader.le.classes_)
                              if self.loader.le is not None else [],
        }