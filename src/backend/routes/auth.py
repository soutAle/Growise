"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import request, jsonify, Blueprint
from backend.utils.validators import validate_signup_data, validate_login_data
from backend.services.auth_service import register_user, login_user

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    error = validate_signup_data(name, email, password)
    if error:
        return jsonify({"error": error}), 400

    return jsonify(*register_user(name, email, password))


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    error = validate_login_data(email, password)
    if error:
        return jsonify({"error": error}), 400

    return jsonify(*login_user(email, password))