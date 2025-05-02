from backend.models.user import User
from flask_jwt_extended import create_access_token
from backend.extensions import bcrypt, db
from datetime import timedelta

def register_user(name, email, password):
    if User.query.filter_by(email=email).first():
        return {"error": "El email ya está registrado"}, 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(
        email=email,
        password=hashed_password,
        name=name,
        is_active=True
    )

    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=new_user.id, expires_delta=timedelta(days=1))

    return {
        "message": "Usuario creado exitosamente",
        "access_token": access_token,
        "user": new_user.serialize()
    }, 201

def login_user(email, password):
    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return {"msg": "Credenciales inválidas"}, 401

    access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))

    return {
        "msg": "Login exitoso",
        "access_token": access_token,
        "user": user.serialize()
    }, 200
