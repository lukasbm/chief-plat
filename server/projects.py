import os.path
from dataclasses import dataclass

import yaml
from typing import List, Optional


@dataclass
class Project:
    name: str
    containers: List[str]
    start: str
    install: str
    stop: str

def find_project(name: str) -> Optional[Project]:
    p = os.path.abspath(os.path.join(os.getcwd(), "examples", f"{name}.yml"))
    if not os.path.exists(p):
        return None

    with open(p, "r") as file:
        try:
            print(yaml.safe_load(file))
        except yaml.YAMLError as exc:
            print(exc)
