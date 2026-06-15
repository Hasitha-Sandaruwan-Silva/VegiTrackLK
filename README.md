<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=2E8B57&center=true&vCenter=true&width=600&lines=VegiTrack+LK+%F0%9F%A5%A6;Sri+Lanka+Vegetable+Price+AI;Production-Ready+Microservice" alt="Typing SVG" />

<br/>

# 🥦 VegiTrack LK
## Sri Lanka Vegetable Price Intelligence System

> *An end-to-end Data Science & Backend Engineering project that collects, cleans, analyzes, and predicts vegetable prices across Sri Lankan markets using Machine Learning — built as a production-ready REST API microservice.*

<br/>

<!-- Tech Stack Badges -->
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit--Learn](https://img.shields.io/badge/Scikit_Learn-1.4-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-499848?style=for-the-badge)

<br/>

<!-- Status Badges -->
[![ML Accuracy](https://img.shields.io/badge/ML_Accuracy_(R²)-98.7%25-brightgreen?style=flat-square&logo=google-analytics)]()
[![Endpoints](https://img.shields.io/badge/API_Endpoints-10-blue?style=flat-square)]()
[![Architecture](https://img.shields.io/badge/Architecture-Clean_/_Layered-purple?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=flat-square)]()
[![Data Rows](https://img.shields.io/badge/Price_Records-4%2C704-orange?style=flat-square)]()
[![Markets](https://img.shields.io/badge/Markets_Tracked-5-red?style=flat-square)]()

</div>

---

## 📖 Table of Contents

1. [🎯 Project Overview](#-project-overview)
2. [🌟 The Problem We Solve](#-the-problem-we-solve)
3. [✨ Key Features](#-key-features)
4. [🏗️ System Architecture](#️-system-architecture)
5. [🛠️ Full Tech Stack Explained](#️-full-tech-stack-explained)
6. [📊 Dataset Deep Dive](#-dataset-deep-dive)
7. [🤖 Machine Learning Pipeline](#-machine-learning-pipeline)
8. [📁 Project Structure Explained](#-project-structure-explained)
9. [⚙️ Installation & Setup](#️-installation--setup)
10. [🚀 Running the Service](#-running-the-service)
11. [📡 Complete API Reference](#-complete-api-reference)
12. [🐳 Docker Deployment](#-docker-deployment)
13. [🧪 Testing the API](#-testing-the-api)
14. [🗺️ Roadmap](#️-roadmap)
15. [🤝 GoviyaNet Integration](#-goviyanet-integration)

---

## 🎯 Project Overview

**VegiTrack LK** is a standalone, **production-grade REST API microservice** that serves as the *Price Intelligence Engine* for Sri Lanka's agricultural digital ecosystem.

The project covers the **complete Data Science + Software Engineering lifecycle**:

```
📥 Data Collection (CBSL)
        │
        ▼
🧹 Data Cleaning & EDA
        │
        ▼
⚙️  Feature Engineering
        │
        ▼
🤖 ML Model Training (Random Forest + Linear Regression)
        │
        ▼
💾 Model Serialization (.pkl artifacts)
        │
        ▼
🚀 Production API (FastAPI Microservice)
        │
        ▼
📱 Consumer Apps (Flutter / Web)
```

This is NOT just a notebook project.
Every component — from raw data ingestion to ML inference to the REST API — is **production-engineered**, **containerized**, and built following **Clean Architecture principles**.

---

## 🌟 The Problem We Solve

Sri Lanka's agricultural market suffers from severe **information asymmetry**:

| 😤 Real Problem | 💡 VegiTrack LK Solution |
|----------------|--------------------------|
| Farmers don't know which market gives the best price | `/api/v1/prices/comparison` — finds cheapest market instantly |
| Vendors can't plan stock without price forecasts | `/api/v1/forecasts` — ML-powered 7-day predictions |
| Consumers overpay due to lack of market data | `/api/v1/analytics/summary` — min/max/avg transparency |
| Researchers have no clean API for price trends | `/api/v1/analytics/trends` — monthly trend data per item/market |
| Developers can't integrate price intelligence into apps | Clean REST API + Swagger UI + CORS enabled |
| No prediction tool for economic planning | `/api/v1/predict` — custom ML inference endpoint |

---

## ✨ Key Features

### 🗄️ Data Layer
- **4,704 daily price records** from CBSL (Central Bank of Sri Lanka)
- Covers **January 2023 to May 2026**
- **6 vegetables**: Beans, Brinjal, Cabbage, Carrot, Pumpkin, Tomato
- **5 markets**: 2 Wholesale (Pettah, Dambulla) + 3 Retail (Pettah, Dambulla, Narahenpita)
- Built-in **economic crisis period flag** for 2021–2023 anomaly handling

### 🤖 Machine Learning Layer
- **Dual-model architecture**: Random Forest (production) + Linear Regression (baseline)
- **11 engineered features** combining temporal signals + market indicators
- **98.7% prediction accuracy** (R² = 0.987) on Retail Pettah prices
- **Automated 7-day rolling forecast** generated at training time
- **On-demand inference** via REST endpoint with model selection

### 🏛️ Engineering Layer
- **Clean Architecture**: API → Services → Repositories → Data — no layer leakage
- **Dependency Injection**: All services injected via FastAPI `Depends()`
- **Singleton Repositories**: CSV data loaded once into memory, reused across requests
- **Singleton ML Loader**: `.pkl` models loaded once at startup, not per-request
- **Pydantic v2 Schemas**: Full type safety on all request/response models
- **Centralized Config**: All paths, filenames, constants managed via `pydantic-settings`
- **Structured Logging**: Timestamped, leveled logs via centralized logger
- **CORS enabled**: Ready for Flutter/React/Vue frontends
- **OpenAPI/Swagger**: Auto-generated interactive docs at `/docs`
- **Docker-ready**: Dockerfile + docker-compose included

---

## 🏗️ System Architecture

### High-Level Microservice View

```
┌──────────────────────────────────────────────────────────────┐
│                    EXTERNAL CLIENTS                          │
│         Flutter App │ Web Dashboard │ Postman │ cURL         │
└─────────────────────────────┬────────────────────────────────┘
                              │ HTTPS / JSON
                              ▼
┌──────────────────────────────────────────────────────────────┐
│              API GATEWAY (Future: Kong / KrakenD)            │
│           Route: /vegitrack/** → localhost:8000              │
└─────────────────────────────┬────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│           VEGITRACK LK MICROSERVICE (Port 8000)              │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                   FASTAPI APP                          │  │
│  │              app/main.py (Entry Point)                 │  │
│  └────────────────────┬───────────────────────────────────┘  │
│                       │                                      │
│  ┌────────────────────▼───────────────────────────────────┐  │
│  │                  API LAYER                             │  │
│  │  app/api/v1/endpoints/                                 │  │
│  │  health │ items │ prices │ forecasts │ analytics       │  │
│  │  predictions                                           │  │
│  └────────────────────┬───────────────────────────────────┘  │
│                       │ Depends() injection                  │
│  ┌────────────────────▼───────────────────────────────────┐  │
│  │               SERVICE LAYER                            │  │
│  │  app/services/                                         │  │
│  │  PriceService │ ForecastService │ AnalyticsService     │  │
│  │  PredictionService │ ModelService                      │  │
│  └──────────┬─────────────────────────┬───────────────────┘  │
│             │                         │                      │
│  ┌──────────▼──────────┐  ┌───────────▼───────────────────┐  │
│  │  REPOSITORY LAYER   │  │     ML INFERENCE LAYER        │  │
│  │  app/repositories/  │  │     app/ml/inference/         │  │
│  │  PriceRepository    │  │     ModelLoader (Singleton)   │  │
│  │  ForecastRepository │  │     FeatureBuilder            │  │
│  │  CSVRepository(Base)│  │     Predictor                 │  │
│  └──────────┬──────────┘  └───────────┬───────────────────┘  │
│             │                         │                      │
│  ┌──────────▼──────────┐  ┌───────────▼───────────────────┐  │
│  │     DATA LAYER      │  │      ARTIFACT LAYER           │  │
│  │  data/processed/    │  │  artifacts/models/            │  │
│  │  *.csv              │  │  random_forest.pkl            │  │
│  │                     │  │  linear_regression.pkl        │  │
│  │                     │  │  label_encoder.pkl            │  │
│  │                     │  │  artifacts/forecasts/         │  │
│  │                     │  │  next_week_forecast.csv       │  │
│  └─────────────────────┘  └───────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

### Internal Layer Rules (Clean Architecture)

| Layer | Can Talk To | Cannot Talk To |
|-------|-------------|----------------|
| `endpoints/` | `services/` only | `repositories/`, `ml/` directly |
| `services/` | `repositories/`, `ml/inference/` | `endpoints/`, FastAPI internals |
| `repositories/` | `data/`, `artifacts/` files | `services/`, `endpoints/` |
| `ml/inference/` | `artifacts/models/` | `repositories/`, `endpoints/` |
| `ml/train/` | `data/`, `artifacts/` | `app/` runtime code |

---

## 🛠️ Full Tech Stack Explained

| Category | Tool | Version | Why We Chose It |
|----------|------|---------|-----------------|
| **Language** | Python | 3.11 | Mature DS ecosystem, async support |
| **API Framework** | FastAPI | 0.109 | Auto Swagger, async, Pydantic v2 native |
| **ASGI Server** | Uvicorn | 0.27 | Fastest Python ASGI server |
| **Data Validation** | Pydantic v2 | 2.6 | Type-safe, fast Rust-based validation |
| **Config Management** | pydantic-settings | 2.1 | `.env` based config with type hints |
| **Data Processing** | Pandas | 2.2 | Industry-standard DataFrame operations |
| **Numerics** | NumPy | 1.26 | Vectorized math for ML features |
| **ML Models** | Scikit-Learn | 1.4 | RF + LR with consistent API |
| **Model Storage** | Joblib | 1.3 | Efficient `.pkl` serialization for large arrays |
| **Containerization** | Docker | latest | Environment-independent deployment |
| **Orchestration** | Docker Compose | v3.8 | Multi-service local dev |
| **Future DB** | PostgreSQL + SQLAlchemy | — | Swap CSVRepository → DBRepository |

---

## 📊 Dataset Deep Dive

### Source
**Central Bank of Sri Lanka (CBSL)** — Weekly vegetable price monitoring data.

### Dataset Statistics

| Attribute | Value |
|-----------|-------|
| Raw Records | 4,704 rows |
| Feature Columns | 20 |
| Date Range | 2023-01-02 → 2026-05-11 |
| Vegetables Covered | 6 |
| Markets Covered | 5 |
| Missing Data Handling | `dropna()` per market column |
| Crisis Period Flagged | 2021-04-01 → 2023-03-31 |

### Markets Monitored

| Market | Type | Coverage |
|--------|------|----------|
| `Wholesale_Pettah` | Wholesale | Full |
| `Wholesale_Dambulla` | Wholesale | Partial |
| `Retail_Pettah` | Retail | Full ← *ML target* |
| `Retail_Dambulla` | Retail | Partial |
| `Retail_Narahenpita` | Retail | Full |

### Price Snapshot (from ML Forecast — June 2026)

| Vegetable | Predicted Price (LKR/kg) |
|-----------|--------------------------|
| 🫘 Beans | 449.89 |
| 🍆 Brinjal | 251.65 |
| 🥬 Cabbage | 124.44 |
| 🥕 Carrot | 286.16 |
| 🎃 Pumpkin | 108.37 |
| 🍅 Tomato | 189.23 |

---

## 🤖 Machine Learning Pipeline

### Complete Training Flow

```
┌─────────────────────────────────────────────────────────────┐
│           ml/train/train_models.py (Pipeline)               │
├─────────────────────────────────────────────────────────────┤
│ 1. Data Ingestion: Load vegetable_prices_clean.csv          │
│ 2. Filtering: Select 'Retail_Pettah' as target market       │
│ 3. Temporal Features: Day, Month, Year, DayOfWeek           │
│ 4. Cyclic Features: sin/cos encoding for Month & Day        │
│ 5. Market Features: Wholesale price + Price spread          │
│ 6. Encoding: LabelEncoder for Vegetable Names               │
│ 7. Splitting: 80% Train / 20% Test (Time-based)             │
│ 8. Training: Random Forest (n=100) + Linear Regression      │
│ 9. Evaluation: MAE, RMSE, R² Score                          │
│ 10. Forecasting: Generate next 7-day input vectors          │
│ 11. Serialization: Save models + encoders + forecasts       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure Explained

```bash
vegitrack-service/
├── 📂 app/                              # ── BACKEND CORE ──
│   ├── main.py                          # FastAPI Entry point
│   ├── 📂 api/                          # API Routes
│   │   └── 📂 v1/
│   │       └── 📂 endpoints/            # Controllers (items, prices, etc.)
│   ├── 📂 core/                         # Config, Logging, Constants
│   ├── 📂 schemas/                      # Pydantic Models (Req/Res)
│   ├── 📂 services/                     # Business Logic
│   ├── 📂 repositories/                 # Data Access (CSV/DB)
│   └── 📂 ml/
│       └── 📂 inference/                # ML Runtime (Loader, Predictor)
│
├── 📂 ml/                               # ── DATA SCIENCE ──
│   ├── 📂 train/                        # Training scripts
│   ├── 📂 notebooks/                    # EDA & Experimentation
│   └── 📂 data_prep/                    # Cleaning scripts
│
├── 📂 data/                             # ── DATA STORAGE ──
│   ├── 📂 raw/                          # Original CBSL files
│   └── 📂 processed/                    # Cleaned CSVs
│
├── 📂 artifacts/                        # ── ML ASSETS ──
│   ├── 📂 models/                       # .pkl files (RF, LR, Encoders)
│   └── 📂 forecasts/                    # Pre-generated CSV forecasts
│
├── 📂 deployment/                       # ── DEVOPS ──
│   ├── 📂 docker/                       # Dockerfile
│   └── 📂 compose/                      # docker-compose.yml
│
├── 📂 tests/                            # ── QUALITY ASSURANCE ──
│   ├── 📂 unit/                        # Service + repository unit tests
│   ├── 📂 integration/                 # API endpoint integration tests
│   ├── 📂 e2e/                         # Full flow end-to-end tests
│   └── conftest.py                     # Pytest fixtures
│
├── 📂 docs/                             # ── DOCUMENTATION ──
│   ├── architecture.md                 # System design docs
│   ├── api_contract.md                 # Endpoint contracts
│   └── local_setup.md                  # Dev environment guide
│
├── 📄 requirements.txt                  # All Python dependencies pinned
├── 📄 .env.example                      # Template for environment variables
├── 📄 .gitignore                        # Excludes .env, venv/, data/, artifacts/
└── 📄 README.md                         # This file 📖
```

---

## ⚙️ Installation & Setup

### Prerequisites

| Requirement | Version | Check |
|-------------|---------|-------|
| Python | 3.11+ | `python --version` |
| pip | latest | `pip --version` |
| (Optional) Docker | latest | `docker --version` |

### Step-by-Step Setup

```bash
# ── Step 1: Clone & Navigate ─────────────────────────────
git clone <repository-url>
cd vegitrack-service

# ── Step 2: Create Virtual Environment ───────────────────
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# ── Step 3: Install All Dependencies ─────────────────────
pip install -r requirements.txt

# ── Step 4: Setup Environment Variables ──────────────────
copy .env.example .env      # Windows
cp .env.example .env        # Linux/Mac
# Edit .env if needed

# ── Step 5: Add Data Files ────────────────────────────────
# Place files in correct locations:
# → data/raw/vegetable_prices.csv
# → data/processed/vegetable_prices_clean.csv

# ── Step 6: Train ML Models (ONE-TIME STEP) ───────────────
python ml/train/train_models.py

# Expected output:
# ✅ RF  → MAE: 8.28 | RMSE: 18.82 | R²: 0.987
# ✅ LR  → MAE: 16.44 | RMSE: 24.18 | R²: 0.978
# ✅ Forecast: 42 rows generated
# ✅ Artifacts saved to artifacts/
```

---

## 🚀 Running the Service

### Development Mode (with hot reload)
```bash
uvicorn app.main:app --reload --port 8000
```

### Production Mode (multi-worker)
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Using Helper Script
```bash
# Windows
scripts\run_dev.sh

# Linux/Mac
bash scripts/run_dev.sh
```

### Verify It's Running
```bash
curl http://localhost:8000/api/v1/health
```

✅ **Service URLs:**

| URL | Purpose |
|-----|---------|
| `http://localhost:8000` | API Root |
| `http://localhost:8000/docs` | 📋 Swagger Interactive Docs |
| `http://localhost:8000/redoc` | 📄 ReDoc Documentation |
| `http://localhost:8000/openapi.json` | 🔧 OpenAPI Schema |

---

## 📡 Complete API Reference

**Base URL:** `http://localhost:8000/api/v1`

---

### 1️⃣ Health Check
```
GET /health
```
Returns service status, loaded data stats, and ML model readiness.

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "prices_loaded": true,
  "prices_rows": 4704,
  "forecast_loaded": true,
  "forecast_rows": 42,
  "items_count": 6,
  "rf_model_ready": true,
  "lr_model_ready": true
}
```

---

### 2️⃣ Get All Vegetables
```
GET /items
```
**Response:**
```json
{
  "count": 6,
  "items": ["Beans", "Brinjal", "Cabbage", "Carrot", "Pumpkin", "Tomato"]
}
```

---

### 3️⃣ Historical Prices (Paginated + Filtered)
```
GET /prices?item=Tomato&market=Retail_Pettah&year=2024&limit=5
```

| Query Param | Type | Required | Description |
|-------------|------|----------|-------------|
| `item` | string | ✅ | Vegetable name |
| `market` | string | ✅ | Market column name |
| `year` | int | ❌ | Filter by year |
| `month` | int | ❌ | Filter by month (1-12) |
| `start_date` | date | ❌ | From date (YYYY-MM-DD) |
| `end_date` | date | ❌ | To date (YYYY-MM-DD) |
| `limit` | int | ❌ | Records per page (default: 500) |
| `offset` | int | ❌ | Pagination offset (default: 0) |

**Response:**
```json
{
  "total": 365,
  "limit": 5,
  "offset": 0,
  "count": 5,
  "prices": [
    {"date": "2024-01-02", "item": "Tomato", "market": "Retail_Pettah", "price": 210.5}
  ]
}
```

---

### 4️⃣ Price Comparison (Cheapest Market)
```
GET /prices/comparison?item=Tomato
```
**Response:**
```json
{
  "item": "Tomato",
  "period": "2026-05",
  "cheapest_market": "Wholesale_Pettah",
  "cheapest_price": 165.0,
  "comparison": [
    {"market": "Wholesale_Pettah", "avg_price": 165.0},
    {"market": "Retail_Pettah", "avg_price": 189.5},
    {"market": "Retail_Narahenpita", "avg_price": 195.0}
  ]
}
```

---

### 5️⃣ 7-Day ML Forecast
```
GET /forecasts
GET /forecasts?item=Tomato
```
**Response:**
```json
{
  "count": 7,
  "forecast": [
    {
      "date": "2026-06-16",
      "item": "Tomato",
      "predicted_price": 189.23,
      "market": "Retail_Pettah (RF Forecast)",
      "currency": "LKR",
      "unit": "per kg",
      "model": "random_forest"
    }
  ]
}
```

---

### 6️⃣ Analytics: Summary Stats
```
GET /analytics/summary?market=Retail_Pettah
GET /analytics/summary?market=Retail_Pettah&item=Tomato
```
**Response:**
```json
{
  "market": "Retail_Pettah",
  "count": 6,
  "summary": [
    {"item": "Tomato", "mean": 195.4, "min": 80.0, "max": 450.0, "std": 62.3, "count": 784}
  ]
}
```

---

### 7️⃣ Analytics: Monthly Trend
```
GET /analytics/trends?item=Tomato&market=Retail_Pettah
```
**Response:**
```json
{
  "item": "Tomato",
  "market": "Retail_Pettah",
  "count": 28,
  "trends": [
    {"period": "2024-01", "year": 2024, "month": 1, "avg_price": 198.5},
    {"period": "2024-02", "year": 2024, "month": 2, "avg_price": 205.2}
  ]
}
```

---

### 8️⃣ Custom ML Prediction
```
POST /predict
Content-Type: application/json
```
**Request Body:**
```json
{
  "item": "Tomato",
  "predict_date": "2025-12-25",
  "avg_wholesale_price": 150.0,
  "price_spread": 20.0,
  "is_crisis_period": 0,
  "model": "random_forest"
}
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `item` | string | ✅ | — | Vegetable name |
| `predict_date` | string | ✅ | — | Target date (YYYY-MM-DD) |
| `avg_wholesale_price` | float | ✅ | — | Expected wholesale price |
| `price_spread` | float | ❌ | 0.0 | Retail price range |
| `is_crisis_period` | int | ❌ | 0 | Economic crisis flag (0/1) |
| `model` | string | ❌ | `random_forest` | `random_forest` or `linear_regression` |

**Response:**
```json
{
  "item": "Tomato",
  "predict_date": "2025-12-25",
  "model": "random_forest",
  "predicted_price": 189.45,
  "currency": "LKR",
  "unit": "per kg"
}
```

---

## 🐳 Docker Deployment

### Build & Run

```bash
# Build image
docker build -t vegitrack-service -f deployment/docker/Dockerfile .

# Run container
docker run -d \
  --name vegitrack \
  -p 8000:8000 \
  vegitrack-service

# Check logs
docker logs vegitrack -f
```

### Docker Compose (Recommended)

```bash
cd deployment/compose
docker-compose up -d

# Stop
docker-compose down
```

### Verify Container is Healthy
```bash
curl http://localhost:8000/api/v1/health
```

---

## 🧪 Testing the API

### Option 1: Swagger UI (Zero Setup)
👉 Open **http://localhost:8000/docs**
Every endpoint has a **"Try it out"** button. Test directly in the browser.

### Option 2: Quick cURL Tests

```bash
# Health
curl http://localhost:8000/api/v1/health

# Items
curl http://localhost:8000/api/v1/items

# Tomato prices in Retail Pettah - 2024
curl "http://localhost:8000/api/v1/prices?item=Tomato&market=Retail_Pettah&year=2024&limit=5"

# Cheapest market for Beans
curl "http://localhost:8000/api/v1/prices/comparison?item=Beans"

# Forecast for Carrot
curl "http://localhost:8000/api/v1/forecasts?item=Carrot"

# Price trend for Cabbage
curl "http://localhost:8000/api/v1/analytics/trends?item=Cabbage&market=Retail_Pettah"

# Custom prediction
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{"item":"Tomato","predict_date":"2025-12-25","avg_wholesale_price":150.0,"model":"random_forest"}'
```

---

## 🗺️ Roadmap

### ✅ Phase 1 — Foundation (COMPLETED)
- [x] Clean Architecture scaffolding (API → Service → Repository → Data)
- [x] CSV-based data repositories with caching
- [x] ML training pipeline (Random Forest + Linear Regression)
- [x] 11 feature engineering steps
- [x] 7-day automated forecast generation
- [x] 10 production REST API endpoints
- [x] Pydantic v2 type-safe schemas
- [x] Dependency injection via FastAPI `Depends()`
- [x] Singleton ML model loader
- [x] Centralized config, logging, constants
- [x] Docker + docker-compose setup
- [x] OpenAPI/Swagger documentation

### 🔄 Phase 2 — Persistence & Security (Next)
- [ ] PostgreSQL integration via SQLAlchemy 2.0
- [ ] Alembic database migrations
- [ ] JWT Authentication middleware
- [ ] API Key authentication for GoviyaNet Gateway
- [ ] Redis caching for high-traffic endpoints
- [ ] API rate limiting

### 🚀 Phase 3 — Intelligence Upgrade
- [ ] LSTM / Prophet time-series models for better seasonality detection
- [ ] Celery + Redis for automated daily ML retraining
- [ ] Real-time CBSL price data scraper
- [ ] Price anomaly detection alerts
- [ ] Confidence intervals on predictions

### ☁️ Phase 4 — Cloud Native
- [ ] Kubernetes deployment manifests (k8s/)
- [ ] Horizontal Pod Autoscaling (HPA)
- [ ] Prometheus metrics endpoint
- [ ] Grafana monitoring dashboard
- [ ] GitHub Actions CI/CD pipeline
- [ ] AWS ECS / Azure Container Apps deployment

---

## 🤝 GoviyaNet Integration

VegiTrack LK is designed as **one microservice** within the larger **GoviyaNet** agricultural platform.

```
┌────────────────────────────────────────────────────────────┐
│                    GoviyaNet Ecosystem                     │
│                                                            │
│  ┌─────────────┐    ┌────────────────────────────────┐     │
│  │ Flutter App │───►│    API Gateway (Kong/KrakenD)  │     │
│  └─────────────┘    └──────────┬─────────────────────┘     │
│                                │                           │
│          ┌─────────────────────┼────────────────────┐      │
│          │                     │                    │      │
│          ▼                     ▼                    ▼      │
│  ┌──────────────┐   ┌─────────────────┐   ┌──────────────┐ │
│  │ AuthService  │   │ VegiTrack LK ✅ │   │FarmerService │ │
│  │  (JWT/Auth)  │   │ (Price Intel)   │   │  (Profiles)  │ │
│  └──────────────┘   └─────────────────┘   └──────────────┘ │
│                                                            │
│  ┌──────────────┐   ┌─────────────────┐                    │
│  │MarketService │   │  Notification   │                    │
│  │ (Inventory)  │   │    Service      │                    │
│  └──────────────┘   └─────────────────┘                    │
└────────────────────────────────────────────────────────────┘
```

**Gateway Routing:**
```
/vegitrack/health  → VegiTrack LK :8000/api/v1/health
/vegitrack/prices  → VegiTrack LK :8000/api/v1/prices
/vegitrack/predict → VegiTrack LK :8000/api/v1/predict
```

---

<div align="center">

---

## 🌾 Built for Sri Lankan Agriculture 🇱🇰

**VegiTrack LK** — Bringing data-driven price transparency to Sri Lanka's agricultural sector.

*Connecting farmers, vendors, and consumers through intelligent price data.*

---

### 📊 Project Stats

| Metric | Value |
|--------|-------|
| 📝 Lines of Code | ~2,500+ |
| 📁 Total Files | 50+ |
| 🔌 API Endpoints | 10 |
| 🤖 ML Models | 2 |
| 📊 Price Records | 4,704 |
| 🎯 ML Accuracy | 98.7% |
| 🏛️ Architecture | Clean / Layered |
| 🐳 Deployment | Docker Ready |

---

**Made with ❤️ using FastAPI + Scikit-Learn + lots of ☕**

⭐ *If this project helped you, give it a star on GitHub!*

</div>
