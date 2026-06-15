"""
ml/train/train_models.py
=========================
VegiTrack LK - ML Training Pipeline

Input  : data/processed/vegetable_prices_clean.csv
Output : artifacts/models/random_forest.pkl
         artifacts/models/linear_regression.pkl
         artifacts/models/label_encoder.pkl
         artifacts/forecasts/next_week_forecast.csv
         artifacts/reports/model_metrics.json
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# ── Make app/ importable ──────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from app.core.config import settings           # noqa: E402
from app.core.constants import (                # noqa: E402
    FEATURE_COLS,
    RETAIL_MARKETS,
    TARGET_MARKET,
    WHOLESALE_MARKETS,
)
from app.core.logger import logger              # noqa: E402


# ── Ensure artifact dirs exist ────────────────────────────────────────────────
settings.MODELS_DIR.mkdir(parents=True, exist_ok=True)
settings.FORECASTS_DIR.mkdir(parents=True, exist_ok=True)
settings.REPORTS_DIR.mkdir(parents=True, exist_ok=True)


# ── 1. Load Data ──────────────────────────────────────────────────────────────
def load_data() -> pd.DataFrame:
    path = settings.PROCESSED_DIR / settings.CLEAN_CSV
    logger.info("Loading data: %s", path)

    if not path.exists():
        raise FileNotFoundError(
            f"Data file not found: {path}\n"
            f"Copy vegetable_prices_clean.csv to data/processed/ first."
        )

    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"]).sort_values("date").reset_index(drop=True)

    logger.info("Loaded: %d rows | %d cols", len(df), len(df.columns))
    logger.info("Items: %s", df["item"].unique().tolist())
    logger.info(
        "Date range: %s → %s",
        df["date"].min().date(),
        df["date"].max().date(),
    )
    return df


# ── 2. Feature Engineering ────────────────────────────────────────────────────
def engineer_features(df: pd.DataFrame) -> tuple[pd.DataFrame, LabelEncoder]:
    logger.info("Engineering features...")

    le = LabelEncoder()
    df["item_encoded"] = le.fit_transform(df["item"].astype(str).str.strip())

    df["year"]         = df["date"].dt.year.astype(int)
    df["month"]        = df["date"].dt.month.astype(int)
    df["day"]          = df["date"].dt.day.astype(int)
    df["day_of_week"]  = df["date"].dt.dayofweek.astype(int)
    df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)
    df["quarter"]      = df["date"].dt.quarter.astype(int)
    df["is_weekend"]   = (df["date"].dt.dayofweek >= 5).astype(int)

    # avg wholesale price
    available_ws = [c for c in WHOLESALE_MARKETS if c in df.columns]
    df["avg_wholesale_price"] = df[available_ws].mean(axis=1, skipna=True)

    # price spread (retail max - retail min)
    available_ret = [c for c in RETAIL_MARKETS if c in df.columns]
    df["price_spread"] = (
        df[available_ret].max(axis=1, skipna=True)
        - df[available_ret].min(axis=1, skipna=True)
    )

    # is_crisis_period - if missing
    if "is_crisis_period" not in df.columns:
        crisis_start = pd.Timestamp("2021-04-01")
        crisis_end   = pd.Timestamp("2023-03-31")
        df["is_crisis_period"] = (
            (df["date"] >= crisis_start) & (df["date"] <= crisis_end)
        ).astype(int)
    else:
        df["is_crisis_period"] = df["is_crisis_period"].fillna(0).astype(int)

    logger.info("Feature engineering done. Classes: %s", list(le.classes_))
    return df, le


# ── 3. Train Models ───────────────────────────────────────────────────────────
def train_models(
    df: pd.DataFrame,
) -> tuple[RandomForestRegressor, LinearRegression, dict]:

    required = FEATURE_COLS + [TARGET_MARKET]
    df_model = df.dropna(subset=required).copy()
    logger.info("Training rows after cleaning: %d", len(df_model))

    if len(df_model) < 50:
        raise ValueError(
            f"Not enough training data ({len(df_model)} rows). "
            f"Check that {TARGET_MARKET} has values in CSV."
        )

    X = df_model[FEATURE_COLS].copy()
    y = df_model[TARGET_MARKET].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True
    )

    # ── Random Forest ──────────────────────────────────────────────────────
    logger.info("Training Random Forest...")
    rf = RandomForestRegressor(
        n_estimators=200,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1,
    )
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    rf_metrics = {
        "MAE":  round(float(mean_absolute_error(y_test, rf_pred)), 4),
        "RMSE": round(float(np.sqrt(mean_squared_error(y_test, rf_pred))), 4),
        "R2":   round(float(r2_score(y_test, rf_pred)), 4),
    }
    logger.info(
        "RF → MAE: %.4f | RMSE: %.4f | R²: %.4f",
        rf_metrics["MAE"], rf_metrics["RMSE"], rf_metrics["R2"],
    )

    # ── Linear Regression ──────────────────────────────────────────────────
    logger.info("Training Linear Regression...")
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    lr_metrics = {
        "MAE":  round(float(mean_absolute_error(y_test, lr_pred)), 4),
        "RMSE": round(float(np.sqrt(mean_squared_error(y_test, lr_pred))), 4),
        "R2":   round(float(r2_score(y_test, lr_pred)), 4),
    }
    logger.info(
        "LR → MAE: %.4f | RMSE: %.4f | R²: %.4f",
        lr_metrics["MAE"], lr_metrics["RMSE"], lr_metrics["R2"],
    )

    metrics = {
        "trained_at":        datetime.now().isoformat(),
        "training_rows":     len(df_model),
        "target_market":     TARGET_MARKET,
        "random_forest":     rf_metrics,
        "linear_regression": lr_metrics,
    }
    return rf, lr, metrics


# ── 4. Generate Next Week Forecast ────────────────────────────────────────────
def generate_forecast(
    df: pd.DataFrame,
    rf: RandomForestRegressor,
    le: LabelEncoder,
) -> pd.DataFrame:
    logger.info("Generating next 7 days forecast...")

    today      = datetime.today().date()
    next_dates = [today + timedelta(days=i) for i in range(1, 8)]
    items      = list(le.classes_)

    # Compute per-item recent stats (last 30 rows)
    item_stats: dict[str, dict] = {}
    for item in items:
        sub = df[df["item"] == item].sort_values("date").tail(30)

        ws_vals  = sub[[c for c in WHOLESALE_MARKETS if c in sub.columns]].values.flatten()
        ret_vals = sub[[c for c in RETAIL_MARKETS    if c in sub.columns]].values.flatten()

        ws_vals  = ws_vals[~np.isnan(ws_vals)]
        ret_vals = ret_vals[~np.isnan(ret_vals)]

        item_stats[item] = {
            "avg_wholesale_price": float(np.mean(ws_vals)) if len(ws_vals)  > 0 else 100.0,
            "price_spread":        float(np.ptp(ret_vals)) if len(ret_vals) > 1 else 0.0,
            "is_crisis_period":    0,
        }

    rows: list[dict] = []
    for pred_date in next_dates:
        dt = datetime(pred_date.year, pred_date.month, pred_date.day)
        for item in items:
            enc   = int(le.transform([item])[0])
            stats = item_stats[item]

            feat = {
                "item_encoded":        enc,
                "year":                dt.year,
                "month":               dt.month,
                "day":                 dt.day,
                "day_of_week":         dt.weekday(),
                "week_of_year":        dt.isocalendar()[1],
                "quarter":             (dt.month - 1) // 3 + 1,
                "is_weekend":          int(dt.weekday() >= 5),
                "is_crisis_period":    stats["is_crisis_period"],
                "avg_wholesale_price": stats["avg_wholesale_price"],
                "price_spread":        stats["price_spread"],
            }

            X    = pd.DataFrame([feat])[FEATURE_COLS]
            pred = round(float(rf.predict(X)[0]), 2)

            rows.append({
                "date":            pred_date.isoformat(),
                "item":            item,
                "predicted_price": pred,
                "market":          f"{TARGET_MARKET} (RF Forecast)",
                "currency":        "LKR",
                "unit":            "per kg",
                "model":           "random_forest",
            })

    forecast_df = (
        pd.DataFrame(rows)
        .sort_values(["date", "item"])
        .reset_index(drop=True)
    )
    logger.info("Forecast generated: %d rows", len(forecast_df))
    return forecast_df


# ── 5. Save Artifacts ─────────────────────────────────────────────────────────
def save_artifacts(
    rf: RandomForestRegressor,
    lr: LinearRegression,
    le: LabelEncoder,
    forecast_df: pd.DataFrame,
    metrics: dict,
) -> None:

    # Models
    joblib.dump(rf, settings.MODELS_DIR / settings.RF_MODEL_FILE)
    logger.info("Saved: %s", settings.RF_MODEL_FILE)

    joblib.dump(lr, settings.MODELS_DIR / settings.LR_MODEL_FILE)
    logger.info("Saved: %s", settings.LR_MODEL_FILE)

    joblib.dump(le, settings.MODELS_DIR / settings.LE_FILE)
    logger.info("Saved: %s", settings.LE_FILE)

    # Forecast CSV
    forecast_path = settings.FORECASTS_DIR / settings.FORECAST_CSV
    forecast_df.to_csv(forecast_path, index=False)
    logger.info("Saved: %s", forecast_path.name)

    # Metrics JSON
    metrics_path = settings.REPORTS_DIR / "model_metrics.json"
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    logger.info("Saved: %s", metrics_path.name)


# ── Main Pipeline ─────────────────────────────────────────────────────────────
def main() -> None:
    logger.info("=" * 60)
    logger.info("VegiTrack LK - ML Training Pipeline START")
    logger.info("=" * 60)

    df          = load_data()
    df, le      = engineer_features(df)
    rf, lr, mx  = train_models(df)
    forecast_df = generate_forecast(df, rf, le)
    save_artifacts(rf, lr, le, forecast_df, mx)

    logger.info("=" * 60)
    logger.info("DONE! All artifacts saved.")
    logger.info("  Models    → %s", settings.MODELS_DIR)
    logger.info("  Forecast  → %s", settings.FORECASTS_DIR)
    logger.info("  Reports   → %s", settings.REPORTS_DIR)
    logger.info("=" * 60)

    # Console preview
    print("\n📊 NEXT WEEK FORECAST PREVIEW (first 14 rows):")
    print(forecast_df.head(14).to_string(index=False))

    print("\n📈 MODEL METRICS:")
    for name, m in mx.items():
        if isinstance(m, dict) and "MAE" in m:
            print(f"\n  {name.upper()}")
            print(f"    MAE  : {m['MAE']}")
            print(f"    RMSE : {m['RMSE']}")
            print(f"    R²   : {m['R2']}")


if __name__ == "__main__":
    main()