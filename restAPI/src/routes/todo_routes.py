from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide

from container.injector import Injecto

blueprint = Blueprint("todo_routes",__name__)


@blueprint.route('', methods=['GET'])
@inject
def get_todos(todo_service= Provide[Injecto.todo_service]):
    todos = todo_service.get_todos()

    return todos, 200 

