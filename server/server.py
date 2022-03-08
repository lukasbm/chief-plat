import os
import sys

if "API_KEY" not in os.environ:
    sys.exit("no API_KEY provided")

from api import app
