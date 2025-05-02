"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import datetime
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_cors import CORS
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required  
from backend.models import db, User
from flask_bcrypt import Bcrypt
import re


api = Blueprint('api', __name__)
bcrypt = Bcrypt()

# Allow CORS requests to this API
CORS(api)

@api.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "El email y la contraseña son requeridos"}), 400
    
    user_exist = User.query.filter_by(email=email).first()
    if user_exist:
        return jsonify({"error": "Usuario ya registrado"}), 400
    
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Formato de email inválido"}), 400

    if len(password) < 6:
        return jsonify({"error": "Contraseña muy corta"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Este email ya está registrado"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(email=email, password=hashed_password, name=name, is_active=True)
    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=new_user.id, expires_delta=datetime.timedelta(days=1))

    return jsonify({"message": "User created successfully",
                    "access_token": access_token,
                    "user": new_user.serialize()}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    if bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=1))

        return jsonify({
            "msg": "Login exitoso",
            "access_token": access_token,
            "user": user.serialize()
        }), 200
    else:
        return jsonify({"msg": "Contraseña incorrecta"}), 401