"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask
from flask_migrate import Migrate
from backend.routes import all_blueprints
from backend.extensions import db, bcrypt, jwt
from flask_cors import CORS



ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
app = Flask(__name__)
app.url_map.strict_slashes = False

# CORS configuration
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# bcrypt config
bcrypt.init_app(app)


# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt.init_app(app)

# database condiguration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db, compare_type=True)
db.init_app(app)

# Add all endpoints form the API with a "api" prefix
for bp in all_blueprints:
    app.register_blueprint(bp, url_prefix='/api')
    


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
