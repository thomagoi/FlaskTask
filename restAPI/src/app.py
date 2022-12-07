from flask import Flask
from models.database import db 
from flask_migrate import Migrate
from flask_swagger import swagger 
from flask import jsonify


import routing 
import yaml 



with open("config.yml","r") as ymlfile:
    config = yaml.safe_load(ymlfile)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['app']['db_uri']

db.init_app(app)

""" render_as_batch makes a new copy of table with applied changes to work around the problem of altering
    the table, fix for working with sqlite
"""
migrate = Migrate(app,db,render_as_batch=True)

@app.route("/documentation")
def documentation():
    swag = swagger(app)
    swag['info']['version'] = "1.0.0"
    swag['info']['title'] = "FlaskTask"
    return jsonify(swag)

app.register_blueprint(routing.router,url_prefix="/api")


if __name__ == "__main__":
    app.run(debug=True,port=config['app']['port'])

