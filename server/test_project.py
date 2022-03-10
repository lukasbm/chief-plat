from project import Project, all_projects, find_project


def test_get_logs():
    pass


def test_get_status():
    pass


def test_all_projects():
    pass


def test_find_project():
    p = find_project("test-app")
    assert p.name == "test-app"
    assert p.containers == ["test-app-redis"]
