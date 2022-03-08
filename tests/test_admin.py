# -*- coding: utf-8 -*-
import json
import pytest

payload = {
    "username": "visitorX",
    "email": "string",
    "full_name": "string",
    "disabled": True,
    "role_name": "visitor",
    "password": "gsociety",
}

update_payload = {
    "username": "visitorX",
    "email": "string",
    "full_name": "new_full_name",
    "disabled": True,
    "role_name": "visitor",
    "password": "string",
}


@pytest.mark.dependency()
def test_add_user(test_client, admins_token):

    response = test_client.post(
        "/admin/add/",
        data=json.dumps(payload),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
            "Content-Type": "application/json",
        },
    )
    assert response.status_code == 200


@pytest.mark.dependency(depends=["test_add_user"])
def test_add_preexisting_user(test_client, admins_token):

    response = test_client.post(
        "/admin/add/",
        data=json.dumps(payload),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
            "Content-Type": "application/json",
        },
    )
    assert response.status_code == 409


@pytest.mark.dependency(depends=["test_add_user"])
def test_update_user(test_client, admins_token):

    response = test_client.patch(
        "/admin/update/",
        data=json.dumps(update_payload),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
            "Content-Type": "application/json",
        },
    )
    assert response.status_code == 200


def test_add_user_no_admin(test_client, visitors_token):

    response = test_client.post(
        "/admin/add/",
        data=json.dumps(payload),
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {visitors_token}",
            "Content-Type": "application/json",
        },
    )
    assert response.status_code == 401


@pytest.mark.dependency(depends=["test_add_user"])
def test_remove_user(test_client, admins_token):

    response = test_client.delete(
        f"/admin/delete/?username={payload['username']}",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
        },
    )
    assert response.status_code == 200


@pytest.mark.dependency(depends=["test_add_user"])
def test_remove_user_no_admin(test_client, visitors_token):

    response = test_client.delete(
        f"/admin/delete/?username={payload['username']}",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {visitors_token}",
        },
    )
    assert response.status_code == 401


@pytest.mark.dependency(depends=["test_add_user", "test_remove_user"])
def test_remove_user_not_existing(test_client, admins_token):

    response = test_client.delete(
        f"/admin/delete/?username={payload['username']}",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
        },
    )
    assert response.status_code == 409


def test_get_all_users(test_client, admins_token):

    response = test_client.get(
        "/admin/show",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {admins_token}",
        },
    )

    assert response.status_code == 200


def test_get_all_user_no_admin(test_client, visitors_token):

    response = test_client.get(
        "/admin/show",
        headers={
            "accept": "applicaton/json",
            "Authorization": f"Bearer {visitors_token}",
        },
    )
    assert response.status_code == 401
