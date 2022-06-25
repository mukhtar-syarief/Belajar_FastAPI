from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship
from models.models import Base


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key = True )
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"))
    name = Column(String)
    price = Column(Numeric)
    stock = Column(Numeric)

    user = relationship("User")
    product_type = relationship("ProductTypeAssosiation", back_populates = "product", cascade = "all, delete")

    def __repr__(self):
        return f"Product(id = {self.id}, user_id = {self.user_id}, name = {self.name}, price = {self.price}, stoct = {self.stock})"
