from fastapi import APIRouter, Depends

from src.helper.hash_password_jwt import get_current_active_user

user = APIRouter()

@user.post("/{user}")
def get_user(user, cuurent_user = Depends(get_current_active_user)):
    return {
        "message": f"Welcome {user}"
    }