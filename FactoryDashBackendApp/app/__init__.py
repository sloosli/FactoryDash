from flask import Flask
from app.routes.api.machines_routes import api_bp as machines_bp


def create_app():
    main_app = Flask(__name__)
    main_app.register_blueprint(machines_bp, url_prefix='/api')

    return main_app
