import os

from flask import Flask
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    if token == os.getenv("API_KEY"):
        return token


@app.route("/projects")
@auth.login_required
def projects():
    return "<p>Hello, World!</p>"


@app.route("/project/<string:project>/start")
@auth.login_required
def project_start(project):
    return f"<p>Hello, {project}!</p>"


@app.route("/project/<string:project>/start")
@auth.login_required
def project_start(project):
    return f"<p>Hello, {project}!</p>"


@app.route("/project/<string:project>/stop")
@auth.login_required
def project_stop(project):
    return f"<p>Hello, {project}!</p>"


@app.route("/project/<string:project>/logs")
@auth.login_required
def project_logs(project):
    return f"<p>Hello, {project}!</p>"
