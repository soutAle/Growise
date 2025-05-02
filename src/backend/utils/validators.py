from backend.models.user import User
import re

def validate_signup_data(name, email, password):
    if not name or not email or not password:
        return "todos los campos son obligatorios"
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Formato de email inválido"

    if len(password) < 6:
        return "Introduzca una contraseña de al menos 6 caracteres"
    
    if User.query.filter_by(email=email).first():
        return "Este email ya está registrado"

    return None 

def validate_login_data(email, password):
    if not email or not password:
        return "todos los campos son obligatorios"
    
    return None 
 