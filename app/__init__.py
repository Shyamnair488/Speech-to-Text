from flask import Flask


def create_app():
    app = Flask(__name__)
    with app.app_context():
        from .routes import app_routes
        app.register_blueprint(app_routes)
    return app
