class IProjectRepository:
    def get_projects():
        raise NotImplementedError

    def get_project(id):
        raise NotImplementedError

    def get_todos_of_project(id):
        raise NotImplementedError

    def post_project():
        raise NotImplementedError

    def update_project():
        raise NotImplementedError

    def delete_project(id):
        raise NotImplementedError