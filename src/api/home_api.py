from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.helper.hash_password_jwt import get_current_active_user

home = APIRouter()

class Home(BaseModel):
    welcome: str

@home.get('/', response_model=Home)
def home_page(current_user = Depends(get_current_active_user)):
    return {"welcome": f"Welcome {current_user.name} to the home page using FastAPI!"}

