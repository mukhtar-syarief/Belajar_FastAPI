import re
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
    return {"username": payload.username, 
            "password": payload.password}