from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.models import Base


class ProductType(Base):
    __tablename__ = "product_type"
    id = Column(Integer, primary_key = True)
    type = Column(String)

    product = relationship("ProductTypeAssosiation", back_populates = "product_type")

    def __repr__(self):
        return f"ProductType(id = {self.id}, type = {self.type})"