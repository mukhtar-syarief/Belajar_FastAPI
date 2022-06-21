from src.controller.user import find_user_by_email, new_user, all_user
from src.models.user_detail import UserDetail
from src.models.models import s

# sultan_mahmud_sekartaji = new_user("Sultan", 
#                                 "Mahmud", 
#                                 "Sekartaji", 
#                                 "sultan.sekartaji", 
#                                 "mahmud.sultansekartaji@gmail.com", 
#                                 "123456789")


# janji_sehidup_semati = new_user("Janji",
#                                 "sehidup",
#                                 "semati",
#                                 "janji.sehidupsemati",
#                                 "laki-laki",
#                                 "sehidupsemati@gmail.com",
#                                 "6281212121212",
#                                 "Jln. sehidup semati",
#                                 "123456789")




# print(all_user())
user =find_user_by_email("sehidupsemati@gmail.com") 
print(user)
print(user.detail)
users = s.query(UserDetail).filter(UserDetail.user_id == 4).first()
print(users)
print(users.user)
# import jwt

# SECRET = "AkuTanpamuButiranDebu"
# ALGORITHM = "HS256"


# payload = {
#     "user":"Mahardika",
#     "email":"mahardika@gmail.com",
#     "role":"admin"}

# def encode_payload(payload):
#     encode = jwt.encode(payload, SECRET, ALGORITHM)
#     return encode

# print(encode_payload(payload))

# def decode_payload(encode):
#     decode = jwt.decode(encode, SECRET, ALGORITHM)
#     return decode

# print(decode_payload(encode_payload(payload)))