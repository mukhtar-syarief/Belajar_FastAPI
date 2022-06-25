from fastapi import APIRouter, Depends
from src.controller.product import get_product_by_id, get_product_by_user
from src.helper.hash_password_jwt import get_current_user
from src.schemes.product import ProductResp


product = APIRouter()

@product.get("/myproduct", response_model=ProductResp)
def get_product(current_user = Depends(get_current_user)):
    product = get_product_by_user(current_user.id)
    return {product}
