# ChiefPlat

## Run

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
export FLASK_DEBUG=1
export FLASK_APP=server.py
flask run
```

## Run with docker

```shell
docker build -t chief-plat:latest .

docker run --rm --name chief-plat \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -v ../examples:/projects \
 -e "BASE_DIR=/projects" \
 -e "API_KEY=123qwe" \
 chief-plat:latest
```
