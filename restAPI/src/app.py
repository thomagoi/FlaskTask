from flask import Flask
from models.database import db 
from flask_migrate import Migrate
from flask_swagger import swagger 
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

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

import routing 
app.register_blueprint(routing.router,url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)

