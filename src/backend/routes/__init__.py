from .auth import auth_bp
from .auth_google import auth_google_bp
from .user_routes import user_bp

all_blueprints = [auth_bp, auth_google_bp, user_bp]
