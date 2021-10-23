from flask import Flask
from app.routes.api_routes import api_bp


def create_app():
    main_app = Flask(__name__)
    main_app.register_blueprint(api_bp, url_prefix='/api')

    return main_app
