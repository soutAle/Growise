"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import datetime
from flask import request, jsonify, Blueprint
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from backend.models.user import db, User
from backend.extensions import bcrypt
from backend.utils.validators import validate_signup_data, validate_login_data

auth_bp = Blueprint('auth_bp', __name__)

CORS(auth_bp)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    error = validate_signup_data(name, email, password)
    if error: 
        return jsonify({"error": error}), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(email=email, password=hashed_password, name=name, is_active=True)
    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=new_user.id, expires_delta=datetime.timedelta(days=1))

    return jsonify({"message": "User created successfully",
                    "access_token": access_token,
                    "user": new_user.serialize()}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    error = validate_login_data(email, password)
    if error:
        return jsonify({"error": error}), 400
    
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    if bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=1))

        return jsonify({
            "msg": "Login successful",
            "access_token": access_token,
            "user": user.serialize()
        }), 200
    else:
        return jsonify({"msg": "Contraseña incorrecta"}), 401