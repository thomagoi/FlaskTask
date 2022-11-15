from models.database import db
from models.todo import Todo
from schemas.todo import TodoSchema

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


class Todo_DB_Service():
    def get_todos():
        todos = Todo.query.all()
        return todos_schema.dump(todos)

    def post_todo(todo):
        db.session.add(todo)
        db.session.commit()
        return todo_schema.dump(todo) 
