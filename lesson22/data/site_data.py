from pydantic import BaseModel
from typing import List

from pydantic.utils import Optional

from lesson22.data.ponchik_info import Ponchik


class CartResponse(BaseModel):
    products: Optional[List[Ponchik]] = None #Необязательное поле, может быть либо Ponchik, либо None


class FavoriteProduct(BaseModel):
    ID: str
