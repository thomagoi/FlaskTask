# from api import db

# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(400))
#     todos = db.relationship('Todo', backref='project')