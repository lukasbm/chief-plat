import os
import sys

from projects import find_project

if "API_KEY" not in os.environ:
    sys.exit("no API_KEY provided")

find_project("test-app")
# from api import app
