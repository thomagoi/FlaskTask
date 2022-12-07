from models.database import db 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    completed = db.Column(db.Boolean, default=False)
    tag = db.Column(db.Integer, db.ForeignKey('tag.id',ondelete='SET NULL'))
    #TODO: add project foreign key
    project = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='SET NULL'))

    def __repr__(self):
        return f"#{self.id} Todo: {self.title}"

#has to be in the same file otherwise can't automatically connect
#TODO: maybe fix later 
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    todos = db.relationship('Todo', backref='given_tag', lazy=True)

    def __repr__(self):
        return f"#{self.id} Tag: {self.name}"

#TODO: add this also 
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(400))
    todos_of_project = db.relationship('Todo', backref='associated_project')

#TODO: add habits; repeating tasks
<<<<<<< HEAD
=======

import bcrypt

#TODO: add user management
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(256))

    def hash_password(self,password):
        password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        self.password_hash = hashed_password

    def verify_password(self,check_password):
        check_password = check_password.encode('utf-8')
        return bcrypt.checkpw(check_password, self.password_hash)
>>>>>>> fdd87e5 (changed url to better represent api)
