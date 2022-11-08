from api import db 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    tag = db.Column(db.Integer, db.ForeignKey('tag.id'))
    #TODO: add project foreign key

    def __repr__(self):
        return f"Todo: {self.title}, assigned Tag: {self.tag}"

   