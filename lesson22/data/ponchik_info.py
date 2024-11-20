from pydantic import BaseModel


class Ponchik(BaseModel):
    name: str
    price: str
    product_id: str
    quantity: int
    add_id: str
    category: str
