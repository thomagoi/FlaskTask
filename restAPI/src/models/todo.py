from models.database import db 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    completed = db.Column(db.Boolean, default=False)
    tag = db.Column(db.Integer, db.ForeignKey('tag.id'))
    #TODO: add project foreign key

    def __repr__(self):
        return f"Todo: {self.title}, assigned Tag: {self.tag}"

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    todos = db.relationship('Todo', backref='given_tag', lazy=True)

    def __repr__(self):
        return f"Tag: {self.name}"
   