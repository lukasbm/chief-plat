import os.path
import os
from dataclasses import dataclass
import yaml
from typing import List, Optional, Callable
import glob
import docker

cli = docker.from_env()


@dataclass
class Project:
    name: str
    containers: List[str]
    _start: str
    _stop: str
    description: Optional[str]
    urls: Optional[List[str]]

    def get_logs(self):
        res = {}
        for c in self.containers:
            try:
                container = cli.containers.get(c)
                res[c] = str(container.logs())
            except docker.errors.APIError:
                return None
            except docker.errors.NotFound:
                continue
        return res

    def get_status(self):
        res = []
        for c in self.containers:
            try:
                container = cli.containers.get(c)
                res.append({
                    "name": c,
                    "status": container.status,
                })
            except docker.errors.APIError:
                continue
            except docker.errors.NotFound:
                continue
        return res


def all_projects() -> List[Project]:
    p = os.path.abspath(os.getenv("BASE_DIR"))
    res = []
    for file in glob.glob(f"{p}/*.yml"):
        p = find_project(os.path.split(file)[-1][:-4])
        if p is not None:
            res.append(p)
    return res


def find_project(name: str) -> Optional[Project]:
    bd = os.path.abspath(os.getenv("BASE_DIR"))
    p = os.path.join(bd, f"{name}.yml")
    if os.path.commonprefix((os.path.realpath(p), bd)) != bd:
        return None

    if not os.path.exists(p):
        return None

    conf = {}
    try:
        with open(p, "r") as file:
            conf = yaml.safe_load(file)
    except:
        return None

    # Parse config into project
    containers = None
    start = None
    stop = None
    description = None
    urls = None

    if "description" in conf:
        description = conf["description"]

    if "urls" in conf:
        urls = conf["urls"]

    try:
        containers = conf["containers"]
        start = conf["start"]
        stop = conf["stop"]
    except KeyError:
        return None

    return Project(name=name, containers=containers, _start=start, _stop=stop, description=description, urls=urls)
