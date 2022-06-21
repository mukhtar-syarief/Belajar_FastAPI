from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from src.models.models import Base
from src.models.post import Post
from src.models.user_detail import UserDetail

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(Text)
    middle_name = Column(Text)
    last_name = Column(Text)
    jenis_kelamin = Column(Text)
    username = Column(Text, unique = True)
    email = Column(Text, unique = True)
    nomor_telepon = Column(Text, unique = True)
    detail = relationship("UserDetail", back_populates = "user", uselist=False, cascade = "all, delete")
    posts = relationship("Post", back_populates = "user", cascade = "all, delete")

    def __repr__(self):
        return f"User(id = {self.id}, first_name = {self.first_name}, middle_name = {self.middle_name}, last_name = {self.last_name}, jenis_kelamin = {self.jenis_kelamin}, username = {self.username}, email = {self.email}, nomor_telepon = {self.nomor_telepon})"
    