from flask import Blueprint
from todo import DI, Todo, TodoService
from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide

blueprint = Blueprint('todo_routes', __name__)
 
@blueprint.route("/<id>", methods=["GET"])
@inject
def get_todo(id: str, todo_service: TodoService = Provide[DI.todo_service]):
    todo: Todo = todo_service.get_todo(int(id))
 
    return jsonify(todo.json()), 200