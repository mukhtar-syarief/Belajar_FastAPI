import numbers
from pydantic import BaseModel

class Product(BaseModel):
    id = int
    user_id: int
class ProductResp(BaseModel):
    id: int
    user_id: int
    name: str
    price: float
    stock: float