# import jwt

# password = {
#     "password" : "secret"
# }
# SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"

# password = jwt.encode(password, SECRET, ALGORITHM)
# print(password)

# from src.controller.user import find_user_by_username

# print(find_user_by_username("johndoe"))


from src.controller.user import find_user_by_username
from src.helper.hash_password_jwt import get_haslib_password, verify_password

print("#############################")
print(get_haslib_password("secret"))

print("#############################")
print(get_haslib_password("rahasia"))

print("#############################")

user = find_user_by_username("johndoe")

# def apa_password_sama(password, hash_password):
#     if verify_password(password, hash_password):
#         return True
#     return False

# print(apa_password_sama("secret", user.detail.password))


# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}


