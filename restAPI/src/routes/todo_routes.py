from flask import Blueprint,request, jsonify
from dependency_injector.wiring import inject, Provide
from models.todo import Todo 
from models.database import db 
from models.todo import Tag  
from container.injector import Injecto

blueprint = Blueprint("todo_routes",__name__)


@blueprint.route('/getAll', methods=['GET'])
@inject
def get_todos(todo_service= Provide[Injecto.todo_service]):
    """
    Get a List of all todos
    --- 
    tags:
      - todo
    description:
      Test if this works
    responses:
      200:
        description: List of Todos
    """
    todos = todo_service.get_todos()
    return todos, 200 

@blueprint.route('/todo/<int:id>', methods=['GET'])
@inject
def get_todo(id,todo_service = Provide[Injecto.todo_service]):
    """
    Get a Todo based on the given id
    --- 
    parameters:
      - in: body
        name: body
        schema:
          id: Todo
    responses:
      200: 
        description: returns specific Todo
      400:
        description: could not find the specified Todo
    """
    wanted_todo = todo_service.get_todo(id)
    return wanted_todo

@blueprint.route('/post',methods=['POST'])
@inject
def post_todo(todo_service = Provide[Injecto.todo_service]):
    output = todo_service.post_todo(request.json)
    return output,201

@blueprint.route('/todo/<int:id>', methods=['DELETE'])
@inject
def delete_todo(id,todo_service = Provide[Injecto.todo_service]):
    """
    Delete a Todo based on id
    --- 
    parameters:
      - in: body
        name: body
        schema:
          id: Todo
    responses:
      200: 
        description: returns specific deleted Todo
      400:
        description: could not find the specified Todo to delete
    """
    delete_target = todo_service.delete_todo(id)
    return delete_target

@blueprint.route('/todo/<int:id>', methods=['PUT'])
@inject
def update_todo(id,todo_service = Provide[Injecto.todo_service]):
    update_target = todo_service.update_todo(id,request.json)
    return update_target

#TODO: change this; maybe allow only with authentication
@blueprint.route('/deleteAll')
def delete_todos():
    db.session.query(Todo).delete()
    db.session.commit()
    return "Delete Success"


