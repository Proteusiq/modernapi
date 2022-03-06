import json
import pytest
from starlette.testclient import TestClient
from mapi.main import app



create_visitor = {
    "username": "visitor",
    "email": "visitor@nonexists.co",
    "full_name": "Joe Visitor",
    "disabled": True,
    "role_name": "visitor",
    "password": "gsociety",
}

@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    def clean_up():
        """logic to cleanup"""
        ...
    request.addfinalizer(clean_up)

@pytest.fixture()
def test_client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def admins_token(test_client):

    response = test_client.post(
        "/token/",
        data={
            "grant_type": "",
            "username": "MrRobot",
            "client_id": "",
            "client_secret": "",
            "password": "fsociety",
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    yield response.json()["access_token"]


@pytest.fixture()
def visitors_token(test_client, admins_token):

    _ = test_client.post(
        "/admin/add/",
        data=json.dumps(create_visitor),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
            "Content-Type": "application/json",
        },
    )

    response = test_client.post(
        "/token/",
        data={
            "grant_type": "",
            "username": "visitor",
            "client_id": "",
            "client_secret": "",
            "password": "gsociety",
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    yield response.json()["access_token"]
