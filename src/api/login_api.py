from src.schemes.login import Login, ResponLogin
from src.helper.hash_password_jwt import create_access_token, create_refresh_token, verify_password
from src.controller.user import find_user_by_username
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

login = APIRouter()

@login.get('/login', response_model = Login)
def login_page():
    return {
            "username": "Masukkan Username Anda",
            "password": "Masukkan Password Anda"
        }

@login.post("/login", response_model = ResponLogin)
def login_page(form_data: OAuth2PasswordRequestForm = Depends()):
    user = find_user_by_username(form_data.username)
    if user:
        hash_password = user.detail.password
        if not verify_password(form_data.password, hash_password):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Password yang Anda masukkan salah.!"
            )
        else:
            return {
                "access_token": create_access_token(user.email),
                "refresh_token": create_refresh_token(user.email)}
    else:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Username Yang Anda Masukkan Tidak Terdaftar.!"
        ) 
    