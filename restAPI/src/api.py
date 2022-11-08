from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

""" render_as_batch makes a new copy of table with applied changes to work around the problem of altering
    the table, fix for working with sqlite
"""
migrate = Migrate(app,db,render_as_batch=True)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

