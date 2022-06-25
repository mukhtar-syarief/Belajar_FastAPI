from pydantic import BaseModel


class ResponLogin(BaseModel):
    access_token: str
    refresh_token: str

class Login(BaseModel):
    username: str
    password: str

