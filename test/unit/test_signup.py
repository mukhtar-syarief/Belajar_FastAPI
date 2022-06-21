from ..fixture.consftest import user_baru, client
import pytest
from src.models.models import s

def test_signup(client, user_baru):
    response = client.post("/signup", json=user_baru)
    assert response.status_code == 200