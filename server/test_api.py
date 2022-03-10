import pytest
from api import app
from werkzeug.wrappers import Response

@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def runner():
    return app.test_cli_runner()

def test_unauthorized(client):
    resp: Response = client.get("/projects")
    assert resp.status_code == 401
    assert "Unauthorized" in resp.get_data(as_text=True)

# TODO auth

def test_projects(client):
    resp: Response = client.get("/projects")

def test_project_start(client):
    resp = client.get("/project/test-app/start")

def test_project_stop(client):
    resp = client.get("/project/test-app/stop")

def test_project_logs(client):
    resp = client.get("/project/test-app/logs")
