from flask import Flask
from flask_restful import Api
from schemas.schema import ma 
from models.database import db 
from flask_migrate import Migrate

from resources.todo import TodoList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

api = Api(app)
db.init_app(app)


from flask_swagger import swagger 
from flask import jsonify

swag = swagger(app)

from flask_swagger_ui import get_swaggerui_blueprint
swaggerui_blueprint = get_swaggerui_blueprint("/swagger", "/documentation", config={'app_name': "FlaskTask"})

app.register_blueprint(swaggerui_blueprint)

@app.route("/documentation")
def documentation():
    swag = swagger(app)
    swag['info']['version'] = "1.0.0"
    swag['info']['title'] = "FlaskTask"
    return jsonify(swag)

""" render_as_batch makes a new copy of table with applied changes to work around the problem of altering
    the table, fix for working with sqlite
"""
migrate = Migrate(app,db,render_as_batch=True)

import routes.todo_routes as todo_routes
import routes.tag_routes as tag_routes
import routes.project_routes as project_routes

from container.injector import Injecto
app.register_blueprint(todo_routes.blueprint, url_prefix="/api/todos")
app.register_blueprint(tag_routes.blueprint, url_prefix="/api/tags")
app.register_blueprint(project_routes.blueprint, url_prefix="/api/projects")

if __name__ == "__main__":
    di = Injecto()
    di.wire(modules=[
        todo_routes,
        tag_routes,
        project_routes
    ])
    app.run(debug=True)

