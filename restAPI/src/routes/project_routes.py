from flask import Blueprint, request
from container.injector import Injecto
from dependency_injector.wiring import inject, Provide

blueprint = Blueprint('project_routes',__name__)

@blueprint.route('/post', methods=["POST"])
@inject 
def post_todo(project_service = Provide[Injecto.project_service]):
    output = project_service.post_project(request.json)
    return output,201

@blueprint.route('/getAll', methods=['GET'])
@inject 
def getAll(project_service = Provide[Injecto.project_service]):
    output = project_service.get_projects()
    return output

@blueprint.route("/project/<int:id>", methods=["GET"])
@inject 
def get_project(id,project_service = Provide[Injecto.project_service]):
    output = project_service.get_project(id)
    return output

@blueprint.route("/project/<int:id>/todos", methods=["GET"])
@inject 
def get_todos_of_project(id,project_service = Provide[Injecto.project_service]):
    output = project_service.get_todos(id)
    return output

@blueprint.route("/project/<int:id>", methods=["PUT"])
@inject 
def update_project(id,project_service = Provide[Injecto.project_service]):
    output = project_service.update_project(id, request.json)
    return output

@blueprint.route("/project/<int:id>", methods=["DELETE"])
@inject 
def delete_project(id,project_service = Provide[Injecto.project_service]):
    output = project_service.delete_project(id)
    return output

@blueprint.route('/deleteAll')
def deleteAll():
    from models.database import db
    from models.todo import Project
    db.session.query(Project).delete()
    db.session.commit()
    return "Delete Projects Success"