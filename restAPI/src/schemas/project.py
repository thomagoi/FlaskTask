from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.todo import Project

class ProjectSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        load_instance = True

    id = auto_field()
    title = auto_field()
    description = auto_field()
    todos_of_project = auto_field()
