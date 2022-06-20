from src.models.user import User
from src.models.models import s
from src.helper.hash_password import hash_password


#Find user by email
def find_user_by_email(email):
    email = email.lower()
    user = s.query(User).filter(User.email == email).first()
    return user

#Create a new user
def new_user(first_name, middle_name, last_name, username, email, password):
    new_user = User(first_name = first_name,
                    middle_name = middle_name,
                    last_name = last_name,
                    username = username,
                    email = email.lower(),
                    password = hash_password(password))
    s.add(new_user)
    s.commit()
    user = find_user_by_email(email)
    return user

#All user
def all_user():
    users = s.query(User).all()
    return users

sultan_mahmud_sekartaji = new_user("Sultan", 
                                "Mahmud", 
                                "Sekartaji", 
                                "sultan.sekartaji", 
                                "mahmud.sultansekartaji@gmail.com", 
                                "123456789")

print(all_user())