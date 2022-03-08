# -*- coding: utf-8 -*-
def test_login(test_client):
    responce = test_client.post(
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
    assert responce.status_code == 200


def test_login_wrong_username(test_client):
    responce = test_client.post(
        "/token/",
        data={
            "grant_type": "",
            "username": "404",
            "client_id": "",
            "client_secret": "",
            "password": "404society",
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    assert responce.status_code == 400


def test_login_wrong_password(test_client):
    responce = test_client.post(
        "/token/",
        data={
            "grant_type": "",
            "username": "visitor",
            "client_id": "",
            "client_secret": "",
            "password": "wrong_password",
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    assert responce.status_code == 400
