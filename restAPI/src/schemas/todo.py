from schemas.schema import ma
from models.todo import Todo
from marshmallow_sqlalchemy import SQLAlchemySchema,auto_field

# class TodoSchema(ma.Schema):
#     class Meta: #options object for schema 
#         model = Todo

#         fields = ("id", "title", "description", "completed", "tag") #fields to include in serialized result
#         #exclude = () #fields to exclude

class TodoSchema(SQLAlchemySchema):
    class Meta: #options object for schema 
        model = Todo
        load_instance = True

    id = auto_field()
    title = auto_field()
    description = auto_field()
    completed = auto_field()
    tag = auto_field()


