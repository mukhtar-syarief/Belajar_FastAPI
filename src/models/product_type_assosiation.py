from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.models import Base



class ProductTypeAssosiation(Base):
    __tablename__ = "product_type_assosiation"
    id = Column(Integer, primary_key = True)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE"))
    product_type_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE"))

    product = relationship("Product")
    product_type = relationship("ProductType")
