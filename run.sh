#!/bin/bash
source ./server/venv/bin/activate
pip install -r requirements
export FLASK_DEBUG=1
export FLASK_APP=./server/server.py
flask run
