import pytest
from src.models.user import User
from server import app
from fastapi.testclient import TestClient
from src.controller.user import find_user_by_email, find_user_by_username
from src.models.models import s


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(scope="function")
def user_baru():
    
    new_user = {"first_name" : "Rizki", 
                "middle_name" : "Ridho", 
                "last_name" : "Saputra", 
                "jenis_kelamin" : "Laki-Laki", 
                "username" : "rizkisaputra", 
                "email" : "rizkisaputra@gmaail.com", 
                "nomor_telepon" : "081687245965", 
                "password" : "123456789",
                "address" : "Jl. Raya Cimanggis No.1"}
    yield new_user
    user = find_user_by_username(new_user["username"])
    user.delete()
    s.commit()

@pytest.fixture(scope="function")
def user_baru_2():
    new_user = {"username" : "sultan.sekartaji",
              "password" : "123456789"} 
    yield new_user