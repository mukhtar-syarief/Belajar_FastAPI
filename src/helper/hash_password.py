import hashlib

def hash_password(password):
    password = hashlib.md5(password.encode()).hexdigest()
    return password