from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from src.models.models import Base
from src.models.post import Post
from src.models.user_detail import UserDetail
from src.models.product import Product

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    username = Column(String, unique = True)
    password = Column(Text)
    
    detail = relationship("UserDetail", back_populates = "user", uselist=False, cascade = "all, delete")
    product = relationship("Product", back_populates = "user", cascade = "all, delete")

    def __repr__(self):
        return f"User(id = {self.id}, first_name = {self.first_name}, middle_name = {self.middle_name}, last_name = {self.last_name}, jenis_kelamin = {self.jenis_kelamin}, username = {self.username}, email = {self.email}, nomor_telepon = {self.nomor_telepon})"
    