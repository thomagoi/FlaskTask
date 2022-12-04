from services.todo_service import TodoService
from services.todo_db_service import TodoClient
from services.tag_services.tag_db_service import TagClient
from services.tag_services.tag_service import TagService 
from services.project_services.project_db_service import ProjectClient
from services.project_services.project_service import ProjectService
from dependency_injector import containers, providers

class Injecto(containers.DeclarativeContainer):
    todo_client = providers.Factory(TodoClient)
    todo_service = providers.Factory(TodoService, todo_repository=todo_client)

    tag_client = providers.Factory(TagClient)
    tag_service = providers.Factory(TagService, tag_repository=tag_client)

    project_client = providers.Factory(ProjectClient)
    project_service = providers.Factory(ProjectService, project_repository=project_client)

    #habit_client
    #habit_service