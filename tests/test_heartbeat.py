
def test_login(test_client):
    responce = test_client.get("/health/heartbeat")
    assert responce.status_code == 200