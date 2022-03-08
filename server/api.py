import json
import os
from werkzeug.exceptions import HTTPException
from flask import Flask, abort, jsonify
from flask_httpauth import HTTPTokenAuth
from projects import all_projects, find_project, get_logs

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    if token == os.getenv("API_KEY"):
        return token


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
    else:
        return jsonify({
            "code": 500,
            "name": "Internal Server Error",
            "description": str(e)
        }), 500


@app.route("/projects")
@auth.login_required
def projects():
    all_projects()
    return "/projects"


@app.route("/project/<string:project>/start")
@auth.login_required
def project_start(project: str):
    p = find_project(project)
    if p is None:
        return abort(404)

    os.system(p.start)
    
    return f"<p>Hello, {project}!</p>"



@app.route("/project/<string:project>/stop")
@auth.login_required
def project_stop(project: str):
    p = find_project(project)
    if p is None:
        return abort(404)

    os.system(p.stop)
    
    return f"<p>Hello, {project}!</p>"



@app.route("/project/<string:project>/logs")
@auth.login_required
def project_logs(project: str):
    p = find_project(project)
    if not p:
        return abort(404)

    return jsonify(get_logs(p))
