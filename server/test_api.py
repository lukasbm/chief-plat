import pytest
from api import app
from werkzeug.wrappers import Response
import os
from test_project import container

@pytest.fixture
def client():
    return app.test_client()


def test_unauthorized(client):
    resp: Response = client.get("/projects")
    assert resp.status_code == 401
    assert "Unauthorized" in resp.get_data(as_text=True)


def test_projects(client):
    headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    resp: Response = client.get("/projects", headers=headers)
    # assert resp.status_code == 200
    # assert b"test-app" in resp.data
    # assert "test-app" in resp.json


def test_project_start(client):
    headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    resp = client.get("/project/test-app/start", headers=headers)
    # assert resp.status_code == 200
    # assert resp.data == b""


def test_project_stop(client, container):
    headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    resp = client.get("/project/test-app/stop", headers=headers)
    # assert resp.status_code == 200
    # assert resp.data == b""


def test_project_logs(client, container):
    headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    resp = client.get("/project/test-app/logs", headers=headers)
    # assert resp.status_code == 200
    # assert "test-app" in resp.json
    # assert container.logs() == resp.json["test-app"]
