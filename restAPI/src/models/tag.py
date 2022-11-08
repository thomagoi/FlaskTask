from api import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    todos = db.relationship('Todo', backref='tag', lazy=True)

    def __repr__(self):
        return f"Tag: {self.name}"