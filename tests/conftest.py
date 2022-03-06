import pytest
from starlette.testclient import TestClient

from mapi.main import app


@pytest.fixture()
def test_client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def admins_token(test_client):

    responce = test_client.post(
        "/token/",
        data={
            "grant_type": "",
            "username": "admin",
            "client_id": "",
            "client_secret": "",
            "password": "Admin_Super_Secret_#666",
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    yield responce.json()["access_token"]


@pytest.fixture()
def visitors_token(test_client):

    response = test_client.post(
        "/token/",
        data={
            "grant_type": "",
            "username": "visitor",
            "client_id": "",
            "client_secret": "",
            "password": "Visitor_Super_Secret_#616",
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    yield response.json()["access_token"]
