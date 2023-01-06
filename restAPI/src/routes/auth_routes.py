from flask import Blueprint, request, abort, jsonify, g 
from flask_httpauth import HTTPBasicAuth
from models.todo import User 
from models.database import db 

auth = HTTPBasicAuth()

blueprint = Blueprint('auth_routes',__name__)

@blueprint.route('/register', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first():
        abort(400)
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201

@blueprint.route('/auth')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!'} % g.user.username)

@auth.verify_password
def verify_password(username,password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True