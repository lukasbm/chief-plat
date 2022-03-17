import json
import os
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from flask import Flask, abort, jsonify
from flask_httpauth import HTTPTokenAuth
from project import Project, find_project, all_projects

app = Flask(__name__)
CORS(app)
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
    ps = all_projects()
    res = []
    for p in ps:
        res.append({
            "name": p.name,
            "containers": p.containers,
            "description": p.description,
            "urls": p.urls,
            "status": p.get_status()
        })
    return jsonify(res)


@app.route("/project/<string:project>")
@auth.login_required
def project(project: str):
    p = find_project(project)
    if p is None:
        abort(404)

    return jsonify({
        "name": p.name,
        "containers": p.containers,
        "description": p.description,
        "urls": p.urls,
        "status": p.get_status()
    })


@app.route("/project/<string:project>/start")
@auth.login_required
def project_start(project: str):
    p = find_project(project)
    if p is None:
        return abort(404)

    os.system(p._start)


@app.route("/project/<string:project>/stop")
@auth.login_required
def project_stop(project: str):
    p = find_project(project)
    if p is None:
        return abort(404)

    os.system(p._stop)


@app.route("/project/<string:project>/logs")
@auth.login_required
def project_logs(project: str):
    p = find_project(project)
    if not p:
        return abort(404)

    l = p.get_logs()
    if l is None:
        abort(500)
    return jsonify(l)
