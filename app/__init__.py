from flask import Flask

from app import security


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    security.init_app(app)

    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/')

    from app.chats import bp as chats_bp
    app.register_blueprint(chats_bp, url_prefix='/')

    return app

