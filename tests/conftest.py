import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()
host = 'http://www.api.dev.pkmt.tech'
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(f"{host}/login/users/tokens/", json={
        "username": USERNAME,
        "password": PASSWORD
    })
    response.raise_for_status()
    return response.json()["access"]

@pytest.fixture
def auth_headers(auth_token):
    return {"Authorization": f"JWT {auth_token}"}