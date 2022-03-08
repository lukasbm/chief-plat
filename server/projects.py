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


def all_projects():
    p = os.path.abspath(os.path.join(os.getcwd(), "examples"))
    for file in glob.glob(f"{p}/*.yml"):
        print(file)


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
    p = Project()
    p.name = name
    p.containers = conf["containers"]

    if conf["type"] == "native":
        p.start = conf["start"]
        p.stop = conf["stop"]

    else:
        raise NotImplementedError

    print(p)
    return p


def get_logs(p: Project):
    res = {}
    for c in p.containers:
        container = cli.containers.get(c)
        res[c] = container.logs()
