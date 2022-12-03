from .tag_repo import TagRepository

class TagService:
    _tag_repository: TagRepository

    def __init__(self, tag_repository: TagRepository):
        self._tag_repository = tag_repository

    def get_tags(self):
        tags = self._tag_repository.get_tags()
        return tags

    def get_tag(self,id):
        wanted_tag = self._tag_repository.get_tag(id)
        return wanted_tag

    def get_todos(self,tag_id):
        todos_of_tag = self._tag_repository.get_todos_of_tag(tag_id)
        return todos_of_tag

    def post_tag(self, new_tag):
        output = self._tag_repository.post_tag(new_tag)
        return output

    def update_tag(self,id,update_tag):
        output = self._tag_repository.update_tag(id,update_tag)
        return output 

    def delete_tag(self,id):
        output = self._tag_repository.delete_tag(id)
        return output