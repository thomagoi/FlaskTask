from services.repos import TodoRepository
from models.todo import Todo
from models.database import db 
from flask import jsonify

from schemas.todo import TodoSchema

class TodoClient(TodoRepository):
    def get_todos(self):
        todos = Todo.query.all()
        return todos 

    def get_todo(self,id):
        wanted_todo = Todo.query.filter_by(id=id).first()
        if wanted_todo is not None:
            todo_schema = TodoSchema()
            wanted_todo = todo_schema.dump(wanted_todo)
            return wanted_todo
        else:
            return jsonify({"Error":"could not find specified id"}),400

    def post_todo(self,new_todo):
        todo_schema = TodoSchema()
        new_item = todo_schema.load(new_todo,session=db.session)
        db.session.add(new_item)
        db.session.commit()
        output = todo_schema.dump(new_item)
        return output

    def delete_todo(self,id):
        delete_target = Todo.query.filter_by(id=id).first()
        if delete_target is not None:
            todo_schema = TodoSchema()
            db.session.delete(delete_target)
            db.session.commit()
            delete_target = todo_schema.dump(delete_target)
            return delete_target
        else:
            return jsonify({"Error":"object to delete doesn't exist"}),400

    #TODO: implement Error handling like, if tag doesnt exist
    def update_todo(self,id,update_data):
        update_target = Todo.query.filter_by(id=id).first()
        if update_target is not None:
            filter_keys = ["title","description","completed","tag"]
            filter_dict = { filter_key: update_data.get(filter_key) for filter_key in filter_keys}
            filter_dict = {k:v for k,v in filter_dict.items() if v is not None}
            Todo.query.filter_by(id=id).update(filter_dict)
            db.session.commit()
            update_target = Todo.query.filter_by(id=id).first()
            todo_schema = TodoSchema()
            output = todo_schema.dump(update_target)
            return output
        else:
            return jsonify({"Error":"object to update doesn't exist"}),400

class MockClient(TodoRepository):
    todo_list = [Todo(title="todo1", completed=False), Todo(title="todo2", completed=False)]
    
    def get_todos(self):
        return self.todo_list


