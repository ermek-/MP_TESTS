"""Common pytest fixtures for API tests."""

import os

import pytest  # pylint: disable=import-error
import requests  # pylint: disable=import-error
from dotenv import load_dotenv  # pylint: disable=import-error

load_dotenv()
HOST = "http://www.api.dev.pkmt.tech"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

@pytest.fixture(scope="session")
def auth_token():
    """Return authentication token for API calls."""

    response = requests.post(
        f"{HOST}/login/users/tokens/",
        json={"username": USERNAME, "password": PASSWORD},
    )
    response.raise_for_status()
    return response.json()["access"]

@pytest.fixture
def auth_headers(auth_token):
    """Authorization headers for authenticated requests."""

    return {"Authorization": f"JWT {auth_token}"}
