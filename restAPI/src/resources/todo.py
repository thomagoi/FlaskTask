from flask_restful import Resource
from schemas.todo import TodoSchema
from models.todo import Todo
from flask import request
from models.database import db 

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

class TodoList(Resource):
    def get(self):
        todos = Todo.query.all()
        return todos_schema.dump(todos)
    
    def put(self):
        post_todo = Todo(
            title = request['title'],
            description = request.json['description'],
            completed = request.json['completed']
        )

        db.session.add(post_todo)
        db.session.commit()
        return todo_schema.dump(post_todo)