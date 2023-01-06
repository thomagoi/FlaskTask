from flask import Blueprint, request
from container.injector import Injecto
from dependency_injector.wiring import inject, Provide

blueprint = Blueprint('project_routes',__name__)

@blueprint.route('/post', methods=["POST"])
@inject 
def post_todo(project_service = Provide[Injecto.project_service]):
    """
    Create a new Project
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: Project
          properties: 
            id: 
              type: int
              description: id of Project
            title:
              type: string
              description: name of Project
            description:
              type: string
              description: short description of the Project
            todos_of_project:
              type: list
              description: list of Todos belonging to the Project
          required:
          - title
    """
    output = project_service.post_project(request.json)
    return output,201

@blueprint.route('/getAll', methods=['GET'])
@inject 
def getAll(project_service = Provide[Injecto.project_service]):
    """
    Get a list of all Projects
    --- 
    response:
      200:
        description: returns list of Projects
    """
    output = project_service.get_projects()
    return output

@blueprint.route("/project/<int:id>", methods=["GET"])
@inject 
def get_project(id,project_service = Provide[Injecto.project_service]):
    """
    Get a specific Project by ID
    ---
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Project
    responses:
      200:
        description: returns specified Project
      400: 
        description: could not find the specified Project
    """
    output = project_service.get_project(id)
    return output

@blueprint.route("/project/<int:id>/todos", methods=["GET"])
@inject 
def get_todos_of_project(id,project_service = Provide[Injecto.project_service]):
    """
    Returns list of Todos for Project specified by ID
    ---
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Project
    responses:
      200: 
        description: returns list of associated Projects
      400:
        description: could not find the specified Project
    """
    output = project_service.get_todos(id)
    return output

@blueprint.route("/project/<int:id>", methods=["PUT"])
@inject 
def update_project(id,project_service = Provide[Injecto.project_service]):
    """
    Update a specified Project
    ---
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Project
    responses:
        200: 
          description: returns updated Project
        400: 
          description: could not find the specified Project
    """
    output = project_service.update_project(id, request.json)
    return output

@blueprint.route("/project/<int:id>", methods=["DELETE"])
@inject 
def delete_project(id,project_service = Provide[Injecto.project_service]):
    """
    Delete Project by ID
    --- 
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Project
    responses:
      200:
        description: returns deleted Project
      400:
        description: could not find specified Project
    """
    output = project_service.delete_project(id)
    return output

@blueprint.route('/deleteAll')
def deleteAll():
    from models.database import db
    from models.todo import Project
    db.session.query(Project).delete()
    db.session.commit()
    return "Delete Projects Success"