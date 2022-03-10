#!/bin/bash
source ./venv/bin/activate
pip install -r requirements.txt
export FLASK_DEBUG=1
export API_KEY=123qwe
export FLASK_APP=./server.py
export BASE_DIR=../examples
flask run
