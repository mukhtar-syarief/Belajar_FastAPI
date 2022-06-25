from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from src.models.models import Base


class UserDetail(Base):
    __tablename__ = "user_detail"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE", onupdate = "CASCADE"))
    name = Column(String, ForeignKey("users.name", ondelete="CASCADE", onupdate="CASCADE"))
    jenis_kelamin = Column(Text)
    address = Column(Text)
    username = Column(Text, ForeignKey("users.username", ondelete="CASCADE", onupdate="CASCADE"))
    email = Column(Text, unique = True)
    nomor_telepon = Column(Text, unique = True)
    password = Column(Text, ForeignKey("users.password"))
    created_at = Column(DateTime, default = func.now())
    last_modified = Column(DateTime, default = func.now(), onupdate = func.now())

    user = relationship("User")

    def __repr__(self):
        return f"UserDetail(id = {self.id}, user_id = {self.user_id}, first_name = {self.first_name}, middle_name = {self.middle_name}, last_name = {self.last_name}, jenis_kelamin = {self.jenis_kelamin}, address = {self.address}, username = {self.username}, email = {self.email}, nomor_telepon = {self.nomor_telepon}, password = {self.password}, created_at = {self.created_at}, last_modified = {self.last_modified})"
