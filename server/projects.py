import os.path
from dataclasses import dataclass

from typing import List, Optional


@dataclass
class Project:
    name: str
    containers: List[str]

    def get_path(self) -> str:
        return os.path.abspath(os.path.join(os.getcwd(), "examples", self.name))


def find_project(name: str) -> Optional[Project]:
    p = Project(name=name, containers=[])
    if not os.path.exists(p.get_path()):
        return None

    # TODO make error tolerant
    with open(os.path.join(p.get_path(), "containers.txt")) as f:
        p.containers = f.readlines()

    return p
