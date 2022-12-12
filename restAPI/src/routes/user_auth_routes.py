from flask import Blueprint, request, jsonify, g
from models.todo import User 
from models.database import db 

#TODO: use auth token instead of this variant 

blueprint = Blueprint('user_auth_routes', __name__)

@blueprint.route('/register', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        return 400 
    if User.query.filter_by(username = username).first() is not None:
        return 400 
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"User":user.username})

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username,password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user 
    return True

@blueprint.route('/test', )
@auth.login_required
def get_resource():
    return jsonify({"Auth": "Success"})


