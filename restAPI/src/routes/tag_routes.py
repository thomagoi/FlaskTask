from container.injector import Injecto
from flask import Blueprint,request
from dependency_injector.wiring import inject, Provide

blueprint = Blueprint('tag_routes',__name__)

#create 
@blueprint.route('/post',methods=['POST'])
@inject
def post_todo(tag_service=Provide[Injecto.tag_service]):
    output = tag_service.post_tag(request.json)
    return output,201

#read
@blueprint.route('/getAll', methods=['GET'])
@inject 
def get_tags(tag_service= Provide[Injecto.tag_service]):
    tags = tag_service.get_tags()
    return tags, 200


@blueprint.route('/tag/<int:id>', methods=['GET'])
@inject 
def get_tag(id,tag_service=Provide[Injecto.tag_service]):
    wanted_tag = tag_service.get_tag(id)
    return wanted_tag

@blueprint.route('/tag/<int:id>/todos',methods=['GET'])
@inject
def get_todos_of_tag(id,tag_service=Provide[Injecto.tag_service]):
    todos = tag_service.get_todos(id)
    return todos

#update
@blueprint.route('/tag/<int:id>',methods=['PUT'])
@inject
def update_tag(id,tag_service=Provide[Injecto.tag_service]):
    update_tag = tag_service.update_tag(id,request.json)
    return update_tag

#delete
@blueprint.route('/tag/<int:id>',methods=['DELETE'])
@inject
def delete_tag(id,tag_service=Provide[Injecto.tag_service]):
    delete_tag = tag_service.delete_tag(id)
    return delete_tag 

@blueprint.route('/deleteAll')
def deleteAll():
    from models.database import db
    from models.todo import Tag 
    db.session.query(Tag).delete()
    db.session.commit()
    return "Delete Tags Success"