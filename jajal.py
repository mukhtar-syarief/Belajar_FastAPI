import jwt

password = {
    "password" : "123456789"
}
SECRET = "secret"
ALGORITHM = "HS256"

password = jwt.encode(password, SECRET, ALGORITHM)
print(password)
