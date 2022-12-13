from .project_repo import IProjectRepository

class ProjectService:
    _project_repository: IProjectRepository 

    def __init__(self, project_repository: IProjectRepository):
        self._project_repository = project_repository

    def get_projects(self):
        projects = self._project_repository.get_projects()
        return projects

    def get_project(self,id):
        wanted_project = self._project_repository.get_project(id)
        return wanted_project 

    def get_todos(self,project_id):
        output = self._project_repository.get_todos_of_project(project_id)
        return output 

    def post_project(self,new_project):
        output = self._project_repository.post_project(new_project)
        return output

    def update_project(self,id,update_project):
        output = self._project_repository.update_project(id,update_project)
        return output

    def delete_project(self,id):
        output = self._project_repository.delete_project(id)
        return output