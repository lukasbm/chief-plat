from project import Project, all_projects, find_project, cli
import os
import pytest


@pytest.fixture
def container():
    p = find_project("test-app")
    c = cli.containers.run("redis", detach=True, name=p.containers[0])
    yield c
    c.stop()
    c.remove()


def test_get_logs(container):
    p = find_project("test-app")
    l = p.get_logs()
    assert len(l) == len(p.containers)
    assert len(l) == 1
    assert "redis" in l[p.containers[0]]


def test_get_status(container):
    p = find_project("test-app")
    s = p.get_status()

    assert len(s) == 1
    assert s[0]["name"] == p.containers[0]
    assert s[0]["status"] is not None


def test_all_projects():
    ps = all_projects()
    p = find_project("test-app")

    assert ps == [p]


def test_find_project():
    p = find_project("test-app")
    assert p.name == "test-app"
    assert p.containers == ["test-app-redis"]
    assert p.description == "simple redis test app"
    assert p.urls == ["http://localhost:6379"]
