from flask import Flask


def create_app():
    app = Flask(__name__)

    from controllers.character import app as char_app
    app.register_blueprint(char_app)

    from controllers.ship import app as ship_app
    app.register_blueprint(ship_app)

    from controllers.index import app as index_app
    app.register_blueprint(index_app)

    return app



