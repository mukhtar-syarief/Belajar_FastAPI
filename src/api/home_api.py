from fastapi import APIRouter
from pydantic import BaseModel

home = APIRouter()

class Home(BaseModel):
    welcome: str

@home.get('/', response_model=Home)
def home_page():
    return {"welcome": "Welcome to the home page using FastAPI!"}

