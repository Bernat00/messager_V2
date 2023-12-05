from flask import Blueprint
from io_blueprint import IOBlueprint

bp = Blueprint('chats', __name__)

io_bp = IOBlueprint()


@io_bp.on('connect')
def asd():
    print('aaaaaaaaa')


from app.chats import routes
from app.chats import events
