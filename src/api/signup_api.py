from typing import Optional
from src.controller.user import find_user_by_username, find_user_by_email, new_user
from fastapi import APIRouter
from pydantic import BaseModel, validator

signup = APIRouter()


class GetSignup(BaseModel):
    message: Optional[str]
    first_name : str
    middle_name : str
    last_name : str
    jenis_kelamin : str
    username: str
    email: str
    nomor_telepon: str
    address: str
    password: str
    confirm_password: str

class Signup(BaseModel):
    first_name : str
    middle_name : str
    last_name : str
    jenis_kelamin : str
    username: str
    email: str
    nomor_telepon: str
    address: str
    

@signup.get('/signup', response_model= GetSignup)
def signup_page():
    return {"message": "Silahkan Signup Terlebih Dahulu",
            "first_name": "Masukkan Nama Depan Anda",
            "middle_name": "Masukkan Nama Tengah Anda",
            "last_name": "Masukkan Nama Belakang Anda",
            "jenis_kelamin": "Masukkan Jenis Kelamin Anda",
            "username": "Masukkan Username Anda",
            "email": "Masukkan Email Anda",
            "nomor_telepon": "Masukkan Nomor Telepon Anda",
            "address": "Masukkan Alamat Anda",
            "password": "Masukkan Password Anda",
            "confirm_password": "Masukkan Password Anda"}

@signup.post("/signup")
def signup_page(payload: GetSignup):
    try:
        user = find_user_by_username(payload.username)
        if user:
            return {"message": "Username Sudah Terdaftar"}
        else:
            user = find_user_by_email(payload.email)
            if user:
                return {"message": "Email Sudah Terdaftar"}
            else:
                user = new_user(payload.first_name, payload.middle_name, payload.last_name, payload.username, payload.jenis_kelamin, payload.email, payload.nomor_telepon, payload.address, payload.password)
                return {"first_name": user.first_name,
                        "middle_name": user.middle_name,
                        "last_name": user.last_name,
                        "jenis_kelamin": user.jenis_kelamin,
                        "username": user.username,
                        "email": user.email,
                        "nomor_telepon": user.nomor_telepon,
                        "address": user.address}
    except ValueError:
        return None