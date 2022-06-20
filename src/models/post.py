from sqlalchemy import Column, Text, Integer, func, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.models import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(Text)
    content = Column(Text)
    crated_at = Column(DateTime, default = func.now())
    last_modified = Column(DateTime, default = func.now(), onupdate = func.now())
    user = relationship("User", back_populates = "posts")

    def __repr__(self):
        return f"Post(id = {self.id}, user_id = {self.user_id}, title = {self.title}, content = {self.content}, crated_at = {self.crated_at}, last_modified = {self.last_modified})"