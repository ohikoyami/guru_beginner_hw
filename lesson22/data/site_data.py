from pydantic import BaseModel
from typing import List


# Модели данных с использованием pydantic
class Product(BaseModel):
    id: str
    name: str
    price: float
    category: str
    quantity: str


class CartResponse(BaseModel):
    products: List[Product]


class FavoriteProduct(BaseModel):
    ID: str


class AuthData(BaseModel):
    username: str
    password: str
