import os
import sys

if "API_KEY" not in os.environ:
    sys.exit("no API_KEY provided")

if "BASE_DIR" not in os.environ:
    sys.exit("no BASE_DIR provided")

from api import app
