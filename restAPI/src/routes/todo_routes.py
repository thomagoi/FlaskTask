from flask import Blueprint,request, jsonify
from dependency_injector.wiring import inject, Provide
from models.todo import Todo 
from models.database import db 
from models.todo import Tag  
from container.injector import Injecto

blueprint = Blueprint("todo_routes",__name__)


@blueprint.route('', methods=['GET'])
@inject
def get_todos(todo_service= Provide[Injecto.todo_service]):
    todos = todo_service.get_todos()
    return todos, 200 

@blueprint.route('/post',methods=['POST'])
@inject
def post_todo(todo_service = Provide[Injecto.todo_service]):
    todo_data = request.json #returns dict
    output = todo_service.post_todo(todo_data)
    return output,201

@blueprint.route('/delete')
def delete_todos():
    db.session.query(Todo).delete()
    db.session.commit()
    return "Delete Success"

