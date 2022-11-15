from services.todo_service import TodoClient, MockClient, TodoService
from dependency_injector import containers, providers

class Injecto(containers.DeclarativeContainer):
    todo_client = providers.Factory(MockClient)
    todo_service = providers.Factory(TodoService, todo_repository=todo_client)
