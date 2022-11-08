from flask import Flask
from flask_restful import Api
from schemas.schema import ma 
from models.database import db 
from flask_migrate import Migrate

from resources.todo import TodoList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

api = Api(app)
ma.init_app(app)
db.init_app(app)

""" render_as_batch makes a new copy of table with applied changes to work around the problem of altering
    the table, fix for working with sqlite
"""
migrate = Migrate(app,db,render_as_batch=True)

api.add_resource(TodoList, "/todos")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
