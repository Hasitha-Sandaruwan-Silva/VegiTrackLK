"""
app/core/constants.py
======================
Project-wide constants.
"""

# Market column names - matches CSV headers exactly
MARKET_COLUMNS: list[str] = [
    "Wholesale_Pettah",
    "Wholesale_Dambulla",
    "Retail_Pettah",
    "Retail_Dambulla",
    "Retail_Narahenpita",
]

WHOLESALE_MARKETS: list[str] = [
    "Wholesale_Pettah",
    "Wholesale_Dambulla",
]

RETAIL_MARKETS: list[str] = [
    "Retail_Pettah",
    "Retail_Dambulla",
    "Retail_Narahenpita",
]

# ML feature columns - order matters for model prediction
FEATURE_COLS: list[str] = [
    "item_encoded",
    "year",
    "month",
    "day",
    "day_of_week",
    "week_of_year",
    "quarter",
    "is_weekend",
    "is_crisis_period",
    "avg_wholesale_price",
    "price_spread",
]

# Primary prediction target market
TARGET_MARKET: str = "Retail_Pettah"

# Currency info
CURRENCY: str = "LKR"
UNIT: str = "per kg"