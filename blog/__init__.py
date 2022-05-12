from flask import Flask
from flask_restx import Api
from .route.main import Main
from .route.user import User


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_namespace(Main, '/main')
    api.add_namespace(User, '/user')

    return app
