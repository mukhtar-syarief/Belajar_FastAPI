from src.models.product import Product
from src.models.models import s
from src.controller.user import find_user_by_username
#add product
def add_product(user, name, price, stock):
    user = find_user_by_username(user)
    product = Product(name = name, price = price, stock = stock, user = user)
    s.add(product)
    s.commit()
    return {"message": "Product Berhasil dibuat"}

def get_product_by_user(user):
    product = s.query(Product).filter(Product.user_id == user.id).all()
    return product

def get_product_by_id(product_id):
    product = s.query(Product).filter(Product.id == product_id).first()
    return product