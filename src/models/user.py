from sqlalchemy import Column, DateTime, Integer, Text, func
from sqlalchemy.orm import relationship
from src.models.models import Base
from src.models.post import Post

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(Text)
    middle_name = Column(Text)
    last_name = Column(Text)
    username = Column(Text, unique = True)
    email = Column(Text, unique = True)
    password = Column(Text)
    created_at = Column(DateTime, default = func.now())
    last_modified = Column(DateTime, default = func.now(), onupdate = func.now())
    posts = relationship("Post", back_populates = "user", cascade = "all, delete")

    def __repr__(self):
        return f"User(id = {self.id},  first_name = {self.first_name}, middle_name = {self.middle_name}, last_name = {self.last_name}, username = {self.username}, email = {self.email}, created_at = {self.created_at}, last_modified = {self.last_modified})"