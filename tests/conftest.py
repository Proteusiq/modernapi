import pytest
from starlette.testclient import TestClient

from mapi.main import app


@pytest.fixture()
def test_client():
    with TestClient(app) as test_client:
        yield test_client
