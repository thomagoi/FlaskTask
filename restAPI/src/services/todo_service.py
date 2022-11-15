from .repos import TodoRepository
from models.todo import Todo 
from flask import jsonify

class TodoClient(TodoRepository):
    def get_todos():
        todos = Todo.query.all()
        return todos 

class MockClient(TodoRepository):
    todo_list = [Todo(title="todo1", completed=False), Todo(title="todo2", completed=False)]
    
    def get_todos(self):
        return self.todo_list

from schemas.todo import TodoSchema

class TodoService:
    _todo_repository: TodoRepository
 
    def __init__(self, todo_repository: TodoRepository) -> None:
        self._todo_repository = todo_repository
 
    def get_todos(self):
        todos = self._todo_repository.get_todos()
        todos_schema = TodoSchema(many=True)
        output = todos_schema.dump(todos)
        return jsonify({"todos": output})