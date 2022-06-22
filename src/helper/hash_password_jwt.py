# from fastapi import Depends, HTTPException, status
# from passlib.context import CryptContext
# from pydantic import BaseModel
# from typing import Union
# from fastapi.security import OAuth2PasswordBearer
# import jwt
# from jose import JWTError
# from src.controller.user import find_user_by_username

# SECRET = "19ea98c90e2828085d0082baea05b584"
# ALGORITHM = "H256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# class TokenData(BaseModel):
#     username: Union[str, None] = None



# def verify_password(password, hashed_password):
#     return pwd_context.verify(password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def authenticate_user(username, password):
#     user = find_user_by_username(username)
#     if not user:
#         return False
#     if not verify_password(password, user.detail.password):
#         return False
#     return user

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = find_user_by_username(token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user

# def get_current_active_user(current_user = Depends(get_current_user)):
#     if not current_user.status:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

import os
from fastapi import Depends, HTTPException
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any

SECRET = os.environ["AuthenticateKey"]
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY'] 

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"

pwd_context = CryptContext(scheme=["bycrypt"], depecrate = "auto")


def get_haslib_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = expires_delta + datetime.utcnow()
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encode_jwt = jwt.encode(to_encode, SECRET, ALGORITHM)
    return encode_jwt

def create_refresh_token(subject: Union[str,Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=JWT_REFRESH_SECRET_KEY)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encode_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encode_jwt

