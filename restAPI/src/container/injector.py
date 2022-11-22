from services.todo_service import TodoClient, MockClient, TodoService
from dependency_injector import containers, providers

class Injecto(containers.DeclarativeContainer):
    todo_client = providers.Factory(TodoClient)
    todo_service = providers.Factory(TodoService, todo_repository=todo_client)

    #tag_client
    #tag_service

    #project_client
    #project_service

    #habit_client
    #habit_service