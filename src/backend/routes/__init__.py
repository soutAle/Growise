from .auth import auth_bp
from .auth_google import auth_google_bp

all_blueprints = [auth_bp, auth_google_bp]
