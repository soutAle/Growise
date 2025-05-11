from flask import Blueprint, request, jsonify
from backend.services.user_service import get_all_users, get_user_by_id
from flask_jwt_extended import get_jwt_identity, jwt_required

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    if not users:
        return jsonify({"error": "No hay usuarios disponibles"}), 404
    return jsonify(users), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_User(user_id):
    current_user = get_jwt_identity()
    if current_user != user_id:
        return jsonify({'error':'No tienes permiso para acceder a este usuario'}),403
    
    if not current_user:
        return jsonify({'error':'No tienes permiso para acceder a este usuario'}),403
    
    validate_user = get_user_by_id(user_id)
    if not validate_user:
        return jsonify({'error':'Usuario no encontrado'}),404
