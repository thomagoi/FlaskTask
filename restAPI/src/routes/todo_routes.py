from flask import Blueprint,request, jsonify
from dependency_injector.wiring import inject, Provide
from models.todo import Todo 
from models.database import db 
from container.injector import Injecto

blueprint = Blueprint("todo_routes",__name__)


@blueprint.route('/getAll', methods=['GET'])
@inject
def get_todos(todo_service= Provide[Injecto.todo_service]):
    """
    Get a list of all Todos
    --- 
    response:
      200:
        description: returns list of Todos
    """
    todos = todo_service.get_todos()
    return todos, 200 

@blueprint.route('/todo/<int:id>', methods=['GET'])
@inject
def get_todo(id,todo_service = Provide[Injecto.todo_service]):
    """
    Get a Todo based on the given ID
    --- 
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Todo
          properties:
            title:
              type: String
              description: Title of the Todo
            description:
              type: String
              description: short description of the Todo for more information
            completed:
              type: boolean
              description: flag for completion of the Todo, done = True
            tag:
              type: integer
              description: foreign key to a Tag Object
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
    """
    Create a new Todo
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: Todo
          required:
            - title
    """
    output = todo_service.post_todo(request.json)
    return output,201

@blueprint.route('/todo/<int:id>', methods=['DELETE'])
@inject
def delete_todo(id,todo_service = Provide[Injecto.todo_service]):
    """
    Delete a Todo based on ID
    --- 
    parameters:
      - in: path
        name: id
        required: true
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
    """
    Update an existing Todo specified by ID
    --- 
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Todo
    responses:
      200: 
        description: returns specific updated Todo
      400:
        description: could not find the specified Todo to update
    """
    update_target = todo_service.update_todo(id,request.json)
    return update_target

#TODO: change this; maybe allow only with authentication
@blueprint.route('/deleteAll')
def delete_todos():
    db.session.query(Todo).delete()
    db.session.commit()
    return "Delete Todos Success"


