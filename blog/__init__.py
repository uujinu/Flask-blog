from flask import Flask


def create_app():
    app = Flask(__name__)

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, url_prifix='/')
    app.register_blueprint(views, url_prifix='/')

    return app
