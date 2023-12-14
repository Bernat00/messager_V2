from flask_socketio import SocketIO

from app import create_app, io_bp

app = create_app()

socketio = SocketIO(app)

io_bp.init_io(socketio)

if __name__ == "__main__":
    socketio.run(app)



