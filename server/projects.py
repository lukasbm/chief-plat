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


def all_projects() -> List[Project]:
    p = os.path.abspath(os.path.join(os.getcwd(), "examples"))
    res = []
    for file in glob.glob(f"{p}/*.yml"):
        print(file.split("/")[-1][:-4])
        p = find_project(file.split("/")[-1][:-4])
        if p is not None:
            res.append(p)
    return res


def find_project(name: str) -> Optional[Project]:
    p = os.path.abspath(os.path.join(os.getcwd(), "examples", f"{name}.yml"))
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

    if conf["type"] == "native":
        start = conf["start"]
        stop = conf["stop"]
    else:
        raise NotImplementedError

    return Project(name=name, containers=containers, start=start, stop=stop)


def get_logs(p: Project):
    res = {}
    for c in p.containers:
        container = cli.containers.get(c)
        res[c] = str(container.logs())
    return res
