from .todo_repo import ITodoRepository
from flask import jsonify

class TodoService:
    _todo_repository: ITodoRepository
 
    def __init__(self, todo_repository: ITodoRepository):
        self._todo_repository = todo_repository
 
    def get_todos(self):
        todos = self._todo_repository.get_todos()
        return todos

    def get_todo(self,search_id):
        if search_id is not None and isinstance(search_id,int):
            wanted_todo = self._todo_repository.get_todo(search_id)
            return wanted_todo
        else:
            error = {"Error": "need int for id"}
            return jsonify(error), 400

    def post_todo(self,new_todo):
        output =  self._todo_repository.post_todo(new_todo)
        return output
    
    def update_todo(self,id,new_data):
        output = self._todo_repository.update_todo(id,new_data)
        return output

    def delete_todo(self,search_id):
        if search_id is not None and isinstance(search_id,int):
            delete_todo = self._todo_repository.delete_todo(search_id)
            return delete_todo
        else:
            error = {"Error": "need int for id"}
            return jsonify(error), 400

