class Todo:
    id: int
    title: str 
    completed: bool

    def __init__(self,id: int, title: str, completed: bool) -> None:
        self.id = id 
        self.title = title 
        self.completed = completed 

    def json(self) -> dict:
        return {
            "id" : self.id,
            "title" : self.title,
            "completed" : self.completed
        }

#interface for the customer to use as a dependency
class TodoRepository:
    
    def get_todos() -> "list[Todo]":
        raise NotImplementedError

import requests

#implementation of Interface: TodoRepo 
class TodoApiClient(TodoRepository):
    def get_todos(self) -> "list[Todo]":
        response = requests.get("https://jsonplaceholder.typicode.com/todos") 
        todos_json = response.json()
        todos: "list[Todo]" = []
 
        for todo_data in todos_json:
            todo = Todo(id=todo_data["id"], title=todo_data["title"], completed=todo_data["completed"])
            todos.append(todo)
 
        return todos

#uses the API but doesnt care about the concrete implementation 
class TodoService:
    _todo_repository: TodoRepository
 
    def __init__(self, todo_repository: TodoRepository) -> None:
        self._todo_repository = todo_repository
 
    def get_todo(self, id: int) -> Todo:
        todos: "list[Todo]" = self._todo_repository.get_todos()
     
        todo: Todo = next((x for x in todos if x.id == id), None)
 
        return todo

from dependency_injector import containers, providers

#dependency injection container
""" takes care of creating the dependencies and providing them to the consumers
"""
class DI(containers.DeclarativeContainer):
    # creates new object of TodoApiClient
    todo_api_client = providers.Factory(TodoApiClient)
    # creates a Service object (needs a dependency of todoRepo); gives it the instance returned by provider todo_api_client
    todo_service = providers.Factory(TodoService, todo_repository = todo_api_client)
