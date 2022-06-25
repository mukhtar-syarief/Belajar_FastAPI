from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from ..models.models import Base
from ..models.product import Product
from ..models.product_type import ProductType


class ProductTypeAssosiation(Base):
    __tablename__ = "product_type_assosiation"
    id = Column(Integer, primary_key = True)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE"))
    product_type_id = Column(Integer, ForeignKey("product_type.id", ondelete="CASCADE", onupdate="CASCADE"))

    product = relationship("Product")
    product_type = relationship("ProductType")

    def __repr__(self):
        return f"ProductTypeAssosiation(id = {self.id}, product_id = {self.product_id}, product_type_id = {self.product_type_id})"