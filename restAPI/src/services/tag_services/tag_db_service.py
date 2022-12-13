from .tag_repo import ITagRepository 
from models.todo import Tag
from models.database import db
from schemas.tag import TagSchema
from schemas.todo import TodoSchema

class TagClient(ITagRepository):
    def get_tags(self):
        tags = Tag.query.all()
        tags_schema = TagSchema(many=True)
        output = tags_schema.dump(tags)
        return output

    def get_tag(self,id):
        wanted_tag = Tag.query.filter_by(id=id).first()
        if wanted_tag is not None:
            tag_schema = TagSchema()
            wanted_tag = tag_schema.dump(wanted_tag)
            return wanted_tag
        else:
            return 404
    
    def get_todos_of_tag(self,id):
        tag = Tag.query.filter_by(id=id).first()
        if tag is not None:
            todos_schema = TodoSchema(many=True)
            todos = tag.todos 
            todos = todos_schema.dump(todos)
            return todos
        else:
            return 404
    
    def post_tag(self, new_tag):
        tag_schema = TagSchema()
        new_tag = tag_schema.load(new_tag,session=db.session)
        db.session.add(new_tag)
        db.session.commit()
        output = tag_schema.dump(new_tag)
        return output 

    def update_tag(self,id,update_tag):
        update_target = Tag.query.filter_by(id=id).first()
        if update_target is not None:
            filter_keys = ["name"]
            filter_dict = {filter_key: update_tag.get(filter_key) for filter_key in filter_keys}
            Tag.query.filter_by(id=id).update(filter_dict)
            db.session.commit()
            update_target = Tag.query.filter_by(id=id).first()
            tag_schema = TagSchema()
            output = tag_schema.dump(update_target)
            return output 
        else:
            return 404

    def delete_tag(self,id):
        delete_target = Tag.query.filter_by(id=id).first()
        if delete_target is not None:
            tag_schema = TagSchema()
            db.session.delete(delete_target)
            db.session.commit()
            delete_target = tag_schema.dump(delete_target)
            return delete_target
        else:
            return 404