# backend/services/google_auth_service.py

from google.oauth2 import id_token
from google.auth.transport import requests
from backend.models.user import User, db
from flask_jwt_extended import create_access_token
import os


CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

def handle_google_login(token):
    try:
        # Verifica token directamente con Google
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        email = idinfo['email']
        name = idinfo.get('name', 'Usuario Google')

        # Buscar o crear usuario
        user = User.query.filter_by(email=email).first()
        if user and user.registerType != 'google':
            return {"error": "El usuario ya existe con otro método de registro"}

        if not user:
            user = User(email=email, name=name, is_active=True, registerType='google')
            db.session.add(user)
            db.session.commit()

        # Crear y devolver token interno
        access_token = create_access_token(identity=user.id)

        return {
            "access_token": access_token,
            "user": user.serialize()
        }

    except ValueError:
        return {"error": "Token de Google inválido o expirado"}, 400
    except Exception as e:
        print("Error inesperado:", str(e))
        return {"error": "Error interno del servidor"}, 500
