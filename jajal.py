import jwt

password = {
    "password" : "secret"
}
SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

password = jwt.encode(password, SECRET, ALGORITHM)
print(password)

# from src.controller.user import find_user_by_username




# print(find_user_by_username("johndoe"))