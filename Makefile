all:
	echo please select a specific target

server_install:
	cd server && python3 -m venv venv
	source server/venv/bin/activate
	pip install -r server/requirements.txt

server_env:
	source ./server/venv/bin/activate

server_run: server_env
	cd server && sh run.sh

server_test:
	export API_KEY=123qwe
	export BASE_DIR=../examples
	echo $API_KEY
	# cd server && pytest

server_build:
	cd server && docker build -t chief-plat:latest .
