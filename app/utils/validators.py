# Custom validators
"""
app/utils/validators.py
========================
Shared validation helpers used across endpoints.
"""

from __future__ import annotations

from fastapi import HTTPException

from app.core.constants import MARKET_COLUMNS


def validate_market(market: str) -> None:
    if market not in MARKET_COLUMNS:
        raise HTTPException(
            status_code=400,
            detail={
                "error":         f"Invalid market '{market}'",
                "valid_markets": MARKET_COLUMNS,
            },
        )


def validate_item(item: str, items_list: list[str]) -> str:
    lower_map = {i.lower(): i for i in items_list}
    exact = lower_map.get(item.lower())
    if exact is None:
        raise HTTPException(
            status_code=404,
            detail=f"Item '{item}' not found. Use /api/v1/items to see available items.",
        )
    return exact