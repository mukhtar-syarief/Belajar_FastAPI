from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel, validator

signup = APIRouter()


class Signup(BaseModel):
    first_name : str
    middle_name : Optional[str]
    last_name : str
    username: str
    password: str
    confirm_password: str


@signup.get('/signup')
def signup_page():
    return {"message": "Silahkan Signup Terlebih Dahulu"}

@signup.post("/signup")
def signup_page(payload: Signup):
    return {"firts_name": payload.first_name,
            "middle_name": payload.middle_name,
            "last_name": payload.last_name,
            "username": payload.username,
            "password": payload.password,
            "confirm_password": payload.confirm_password}