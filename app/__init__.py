from flask import Flask
from flask_socketio import SocketIO
from app.chats import io_bp

from app import security


def create_app(server=True):
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'secret!'
	security.init_app(app)

	from app.user import bp as user_bp
	app.register_blueprint(user_bp, url_prefix='/')

	from app.chats import bp as chats_bp
	app.register_blueprint(chats_bp, url_prefix='/chats')
	if server:
		socketio = SocketIO(app)
		io_bp.init_io(socketio)

	return app


def create_socket(app):
	socketio = SocketIO(app)
	io_bp.init_io(socketio)

	return socketio

