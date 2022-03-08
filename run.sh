#!/bin/bash
source ./server/venv/bin/activate
pip install -r ./server/requirements.txt
export FLASK_DEBUG=1
export API_KEY=123qwe
export FLASK_APP=./server/server.py
flask run
