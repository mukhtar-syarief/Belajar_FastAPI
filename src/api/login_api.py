from src.controller.user import find_user_by_username
from src.helper.hash_password import hash_password
from fastapi import APIRouter
from pydantic import BaseModel

login = APIRouter()

class GetLogin(BaseModel):
    message: str
    username: str
    password: str

class Login(BaseModel):
    username = str
    first_name = str
    middle_name = str
    last_name = str
    email = str
    password = str


@login.get('/login', response_model = GetLogin)
def login_page():
    return {"message": "Silahkan Login Terlebih Dahulu",
            "username": "Masukkan Username Anda",
            "password": "Masukkan Password Anda"}

@login.post("/login", response_model=Login)
def login_page(payload: GetLogin):
    user = find_user_by_username(payload.username)
    if user:
        if user.password == hash_password(payload.password):
            return {"username": user.username,
                "first_name": user.first_name,
                "middle_name": user.middle_name,
                "last_name": user.last_name,
                "email": user.email,
                "password": user.password}
        else:
            return {"message": "Password Salah"}
    else:
        return {"message": "Username Yang Anda Masukkan Tidak Terdaftar"} 
    
    