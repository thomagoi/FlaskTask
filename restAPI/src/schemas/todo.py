from schemas.schema import ma
from models.todo import Todo
#load (deserialization): takes db entry and creates the json object
#dump (serialization): transform object into bytes to store and transport them easily

class TodoSchema(ma.Schema):
    class Meta: #options object for schema 
        fields = ("id", "title", "description", "completed", "tag") #fields to include in serialized result
        #exclude = () #fields to exclude
        model = Todo

