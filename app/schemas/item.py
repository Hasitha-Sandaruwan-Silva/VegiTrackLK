"""
app/schemas/item.py
====================
Item schemas.
"""

from pydantic import BaseModel


class ItemsResponse(BaseModel):
    count: int
    items: list[str]