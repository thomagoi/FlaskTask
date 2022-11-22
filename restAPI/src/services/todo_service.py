from .repos import TodoRepository
from models.todo import Todo
from models.database import db 
from flask import jsonify

class TodoClient(TodoRepository):
    def get_todos(self):
        todos = Todo.query.all()
        return todos 

    def post_todo(self,new_todo):
        db.session.add(new_todo)
        db.session.commit()

class MockClient(TodoRepository):
    todo_list = [Todo(title="todo1", completed=False), Todo(title="todo2", completed=False)]
    
    def get_todos(self):
        return self.todo_list

from schemas.todo import TodoSchema

class TodoService:
    _todo_repository: TodoRepository
 
    def __init__(self, todo_repository: TodoRepository):
        self._todo_repository = todo_repository
 
    def get_todos(self):
        todos = self._todo_repository.get_todos()
        todos_schema = TodoSchema(many=True)
        output = todos_schema.dump(todos)
        return output

    def post_todo(self,new_todo):
        todo_schema = TodoSchema()
        new_item = todo_schema.load(new_todo,session=db.session)
        self._todo_repository.post_todo(new_item)
        output = todo_schema.dump(new_item)
        return output


