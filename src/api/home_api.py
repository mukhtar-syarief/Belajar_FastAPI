from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.helper.hash_password_jwt import get_current_user

# from src.helper.hash_password_jwt import get_current_active_user

home = APIRouter()

class Home(BaseModel):
    welcome: str

@home.get('/', response_model=Home)
def home_page(current_user = Depends(get_current_user)):
    return {"welcome": f"Welcome {current_user.first_name} {current_user.middle_name} {current_user.last_name} to the home page using FastAPI!"}

