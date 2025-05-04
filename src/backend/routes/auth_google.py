# backend/routes/auth_google.py

from flask import Blueprint, request, jsonify
from backend.services.auth_google_service import handle_google_login

auth_google_bp = Blueprint('auth_google_bp', __name__)

@auth_google_bp.route('/auth/google', methods=['POST'])
def google_login():
    data = request.get_json()
    token = data.get("token")

    result = handle_google_login(token)
    if "error" in result:
        return jsonify(result), 400
    return jsonify(result), 200
