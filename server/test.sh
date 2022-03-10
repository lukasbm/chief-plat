#!/bin/bash
if [ ! -d venv ]; then
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
fi
source ./venv/bin/activate

export API_KEY=123qwe
export BASE_DIR=../examples
pytest
