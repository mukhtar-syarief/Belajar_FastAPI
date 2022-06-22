from src.models.user import User
from src.models.user_detail import UserDetail
from src.models.models import s
from src.helper.hash_password_md5 import hash_password


#Find_user_by_id
def find_user_by_id(id):
    user = s.query(User).filter(User.id == id).first()
    return user

#Find user by username
def find_user_by_username(username):
    user = s.query(User).filter(User.username == username).first()
    return user

#Find user by email
def find_user_by_email(email):
    email = email.lower()
    user = s.query(User).filter(User.email == email).first()
    return user

#Create a new user
def new_user(first_name, middle_name, last_name, username, jenis_kelamin, email, nomor_telepon, address, password):
    new_user = User(first_name = first_name,
                    middle_name = middle_name,
                    last_name = last_name,
                    jenis_kelamin = jenis_kelamin,
                    username = username,
                    email = email.lower(),
                    nomor_telepon = nomor_telepon)
    s.add(new_user)
    s.commit()
    user_detail = UserDetail(first_name = first_name,
                            middle_name = middle_name,
                            last_name = last_name,
                            jenis_kelamin = jenis_kelamin,
                            username = username,
                            email = email.lower(),
                            address = address,
                            nomor_telepon = nomor_telepon,
                            password = hash_password(password),
                            user = new_user)
    s.add(user_detail)
    s.commit()
    user = find_user_by_email(email)
    return user

#All user
def all_user():
    users = s.query(User).all()
    return users

