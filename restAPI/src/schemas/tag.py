from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.todo import Tag

class TagSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        load_instance = True 

    id = auto_field()
    name = auto_field()
    todos = auto_field()