from flask import Blueprint, request, jsonify
from backend.services.user_service import get_all_users, get_user_by_id
from flask_jwt_extended import get_jwt_identity, jwt_required

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    if not users:
        return jsonify({"msg": "No hay usuarios disponibles"}), 404
    return jsonify(users), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_User(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify({'user': user}), 200
    return jsonify({'msg':'Usuario no encontrado'}),404
