from container.injector import Injecto
from flask import Blueprint,request
from dependency_injector.wiring import inject, Provide

blueprint = Blueprint('tag_routes',__name__)

#create 
@blueprint.route('/post',methods=['POST'])
@inject
def post_todo(tag_service=Provide[Injecto.tag_service]):
    """
    Create a new Tag
    --- 
    parameters:
        - in: body
          name: body
          schema:
            id: Tag
            properties:
              id: 
                type: int
                description: id of Tag
              name:
                type: string
                description: name of the Tag
              todos:
                type: list
                description: list of Todos with specific Tag
            required:
              - name
    """
    output = tag_service.post_tag(request.json)
    return output,201

#read
@blueprint.route('/getAll', methods=['GET'])
@inject 
def get_tags(tag_service= Provide[Injecto.tag_service]):
    """
    Get a list of all Tags
    ---
    response:
      200:
        description: returns list of Tags
    """
    tags = tag_service.get_tags()
    return tags, 200


@blueprint.route('/tag/<int:id>', methods=['GET'])
@inject 
def get_tag(id,tag_service=Provide[Injecto.tag_service]):
    """
    Get a specific Tag by ID
    --- 
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Tag
    responses:
      200:
        description: returns specified Tag
      400:
        description: could not find specified Tag
    """
    wanted_tag = tag_service.get_tag(id)
    return wanted_tag

@blueprint.route('/tag/<int:id>/todos',methods=['GET'])
@inject
def get_todos_of_tag(id,tag_service=Provide[Injecto.tag_service]):
    """
    Returns list of Todos for Tag specified by ID
    --- 
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Tag
    responses:
      200:
        description: return list of associated Todos
      400:
        description: could not find the specified Tag
    """
    todos = tag_service.get_todos(id)
    return todos

#update
@blueprint.route('/tag/<int:id>',methods=['PUT'])
@inject
def update_tag(id,tag_service=Provide[Injecto.tag_service]):
    """
    Update a specified Tag
    ---
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Tag
    responses:
        200:
          description: returns specific updated Tag
        400:
          description: could not find the specified Tag
    """
    update_tag = tag_service.update_tag(id,request.json)
    return update_tag

#delete
@blueprint.route('/tag/<int:id>',methods=['DELETE'])
@inject
def delete_tag(id,tag_service=Provide[Injecto.tag_service]):
    """
    Delete Tag by ID
    ---
    parameters:
      - in: path
        name: id
        required: true
        schema:
          id: Todo
    responses:
      200:
        description: returns deleted Tag
      400: 
        description: could not find specified Tag
    """
    delete_tag = tag_service.delete_tag(id)
    return delete_tag 

@blueprint.route('/deleteAll')
def deleteAll():
    from models.database import db
    from models.todo import Tag 
    db.session.query(Tag).delete()
    db.session.commit()
    return "Delete Tags Success"