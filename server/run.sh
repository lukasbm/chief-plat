#!/bin/bash
if [ ! -d venv ]; then
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
fi
source ./venv/bin/activate

export FLASK_DEBUG=1
export API_KEY=123qwe
export FLASK_APP=./server.py
export BASE_DIR=../examples
flask run
