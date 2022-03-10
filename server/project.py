import os.path
import os
from dataclasses import dataclass
import yaml
from typing import List, Optional
import glob
import docker

cli = docker.from_env()

class InvalidProjectConfigError(Exception):
    pass


@dataclass
class Project:
    name: str
    containers: List[str]
    start: str
    stop: str
    description: str
    urls: List[str]

    def get_logs(self):
        res = {}
        for c in self.containers:
            container = cli.containers.get(c)
            res[c] = str(container.logs())
        return res

    def get_status(self):
        res = []
        for c in self.containers:
            container = cli.containers.get(c)
            res.append({
                "name": c,
                "status": container.status
            })
        return res


def all_projects() -> List[Project]:
    p = os.path.abspath(os.getenv("BASE_DIR"))
    res = []
    for file in glob.glob(f"{p}/*.yml"):
        print(file.split("/")[-1][:-4])
        p = Project.find_project(file.split("/")[-1][:-4])
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
    containers = conf["containers"]
    start = ""
    stop = ""
    description = ""
    urls = []

    if conf["type"] == "native":
        start = conf["start"]
        stop = conf["stop"]
        urls = conf["urls"]
        description = conf["description"]
    else:
        raise NotImplementedError

    return Project(name=name, containers=containers, start=start, stop=stop, description=description, urls=urls)
