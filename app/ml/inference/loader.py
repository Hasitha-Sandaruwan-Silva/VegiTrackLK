"""
app/ml/inference/loader.py
===========================
Loads pkl model files at startup.
Singleton pattern - load once, reuse everywhere.
"""

from __future__ import annotations

from pathlib import Path

import joblib

from app.core.config import settings
from app.core.logger import logger


class ModelLoader:
    def __init__(self) -> None:
        self.rf_model = None
        self.lr_model = None
        self.le       = None
        self._load_all()

    def _load_all(self) -> None:
        self.rf_model = self._load(settings.MODELS_DIR / settings.RF_MODEL_FILE, "Random Forest")
        self.lr_model = self._load(settings.MODELS_DIR / settings.LR_MODEL_FILE, "Linear Regression")
        self.le       = self._load(settings.MODELS_DIR / settings.LE_FILE, "Label Encoder")

        if self.le is not None:
            logger.info("Label Encoder classes: %s", list(self.le.classes_))

    def _load(self, path: Path, name: str):
        if path.exists():
            obj = joblib.load(path)
            logger.info("%s loaded from %s", name, path.name)
            return obj
        logger.warning("%s NOT found at %s", name, path)
        return None


# Singleton
model_loader = ModelLoader()