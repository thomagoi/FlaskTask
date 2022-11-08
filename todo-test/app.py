from flask import Flask 
from todo import DI
import todo_routes

app = Flask(__name__)

app.register_blueprint(todo_routes.blueprint, url_prefix="/todo")

if __name__ == "__main__":
    di = DI()
    di.wire(modules=[
        todo_routes
    ])

    app.run(debug=True)
