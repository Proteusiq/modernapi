import json
import pytest

payload = {
    "username": "string_random",
    "email": "string",
    "full_name": "string",
    "disabled": True,
    "role_name": "GUEST",
    "password": "string",
}

update_payload = {
    "username": "string_random",
    "email": "string",
    "full_name": "new_full_name",
    "disabled": True,
    "role_name": "GUEST",
    "password": "string",
}


@pytest.mark.dependency()
def test_add_user(test_client, admins_token):

    responce = test_client.post(
        "/admin/add/",
        data=json.dumps(payload),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
            "Content-Type": "application/json",
        },
    )
    assert responce.status_code == 200


@pytest.mark.dependency(depends=["test_add_user"])
def test_add_preexisting_user(test_client, admins_token):

    responce = test_client.post(
        "/admin/add/",
        data=json.dumps(payload),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
            "Content-Type": "application/json",
        },
    )
    assert responce.status_code == 409


@pytest.mark.dependency(depends=["test_add_user"])
def test_update_user(test_client, admins_token):

    responce = test_client.post(
        "/admin/update/",
        data=json.dumps(update_payload),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
            "Content-Type": "application/json",
        },
    )
    assert responce.status_code == 200


def test_add_user_no_admin(test_client, visitors_token):

    responce = test_client.post(
        "/admin/add/",
        data=json.dumps(payload),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {visitors_token}",
            "Content-Type": "application/json",
        },
    )
    assert responce.status_code == 401


@pytest.mark.dependency(depends=["test_add_user"])
def test_remove_user(test_client, admins_token):

    responce = test_client.delete(
        f"/admin/delete/?username={payload['username']}",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
        },
    )
    assert responce.status_code == 200


@pytest.mark.dependency(depends=["test_add_user"])
def test_remove_user_no_admin(test_client, visitors_token):

    responce = test_client.delete(
        f"/admin/delete/?username={payload['username']}",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {visitors_token}",
        },
    )
    assert responce.status_code == 401


@pytest.mark.dependency(depends=["test_add_user", "test_remove_user"])
def test_remove_user_not_existing(test_client, admins_token):

    responce = test_client.delete(
        f"/admin/delete/?username={payload['username']}",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
        },
    )
    assert responce.status_code == 409


def test_get_all_users(test_client, admins_token):

    responce = test_client.get(
        "/admin/",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
        },
    )

    assert responce.status_code == 200


def test_get_all_user_no_admin(test_client, visitors_token):

    responce = test_client.get(
        "/admin/",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {visitors_token}",
        },
    )
    assert responce.status_code == 401
