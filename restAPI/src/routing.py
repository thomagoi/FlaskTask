from flask import Blueprint
import routes.todo_routes as todo_routes
import routes.tag_routes as tag_routes
import routes.project_routes as project_routes

from flask_swagger_ui import get_swaggerui_blueprint
from container.injector import Injecto

router = Blueprint("routing",__name__)

router.register_blueprint(todo_routes.blueprint, url_prefix="/todos")
router.register_blueprint(tag_routes.blueprint, url_prefix="/tags")
router.register_blueprint(project_routes.blueprint, url_prefix="/projects")

swaggerui_blueprint = get_swaggerui_blueprint("/swagger", "/documentation", config={'app_name': "FlaskTask"})
router.register_blueprint(swaggerui_blueprint)

di = Injecto()
di.wire(modules=[
    todo_routes,
    tag_routes,
    project_routes
])
