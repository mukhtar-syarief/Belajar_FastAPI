from ..fixture.consftest import client, user_baru, user_baru_2

def test_login(client):
    response = client.get("/login")
    assert response.status_code == 200

def test_login_post(client, user_baru_2):
    response = client.post("/login", json=user_baru_2)
    assert response.status_code == 200