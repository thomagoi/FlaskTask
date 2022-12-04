from .project_repo import ProjectRepository
from flask import jsonify
from models.todo import Project 
from models.database import db 
from schemas.todo import TodoSchema
from schemas.project import ProjectSchema


class ProjectClient(ProjectRepository):
    def get_projects(self):
        projects = Project.query.all()
        projects_schema = ProjectSchema(many=True)
        output = projects_schema.dump(projects)
        return output 

    def get_project(self,id):
        wanted_project = Project.query.filter_by(id=id).first()
        if wanted_project is not None:
            project_schema = ProjectSchema()
            output = project_schema.dump(wanted_project)
            return output
        else:
            return jsonify({"Error":"could not find object with specified id"}),400

    def get_todos_of_project(self,id):
        project = Project.query.filter_by(id=id).first()
        if project is not None:
            todos_schema = TodoSchema(many=True)
            todos = project.todos_of_project
            todos = todos_schema.dump(todos)
            return todos
        else:
            return jsonify({"Error":"could not find the specified project to retrieve the Todos"}),400

    def post_project(self,new_project):
        project_schema = ProjectSchema()
        new_project = project_schema.load(new_project,session=db.session)
        db.session.add(new_project)
        db.session.commit()
        output = project_schema.dump(new_project)
        return output

    def update_project(self,id,update_project):
        update_target = Project.query.filter_by(id=id).first()
        if update_target is not None:
            filter_keys = ["title","description"]
            filter_dict = { filter_key: update_project.get(filter_key) for filter_key in filter_keys}
            filter_dict = {k:v for k,v in filter_dict.items() if v is not None}
            Project.query.filter_by(id=id).update(filter_dict)
            db.session.commit()
            update_target = Project.query.filter_by(id=id).first()
            project_schema = ProjectSchema()
            output = project_schema.dump(update_target)
            return output
        else:
            return jsonify({"Error":"object to update doesn't exist"}),400
    
    def delete_project(self,id):
        delete_target = Project.query.filter_by(id=id).first()
        if delete_target is not None:
            project_schema = ProjectSchema()
            db.session.delete(delete_target)
            db.session.commit()
            delete_target = project_schema.dump(delete_target)
            return delete_target
        else:
            return jsonify({"Error":"object to delete doesn't exist"}),400