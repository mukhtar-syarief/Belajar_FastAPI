from src.controller.user import find_user_by_username
from fastapi import APIRouter
from pydantic import BaseModel, validator

login = APIRouter()

class Login(BaseModel):
    username: str
    password: str


@login.get('/login')
def login_page():
    return {"message": "Silahkan Login Terlebih Dahulu"}

@login.post("/login")
def login_page(payload: Login):
    user = find_user_by_username(payload.username)
    return {"username": user.username,
            "first_name": user.first_name,
            "middle_name": user.middle_name,
            "last_name": user.last_name,
            "email": user.email,
            "password": user.password}