#!/bin/bash
source ./venv/bin/activate
pip install -r requirements.txt
cd ..
export FLASK_DEBUG=1
export API_KEY=123qwe
export FLASK_APP=./server/server.py
flask run
