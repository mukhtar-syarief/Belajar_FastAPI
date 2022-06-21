import pytest
from server import app
from fastapi.testclient import TestClient
from ..fixture.consftest import client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


