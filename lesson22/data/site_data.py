from pydantic import BaseModel
from typing import List
from data.ponchik_info import Ponchik


class CartResponse(BaseModel):
    products: List[Ponchik]


class FavoriteProduct(BaseModel):
    ID: str
