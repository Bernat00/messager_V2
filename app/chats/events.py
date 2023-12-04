from flask import session, g
from flask_socketio import emit, join_room, leave_room
from app import socketio

from app.models.rooms import Room


"""@socketio.on('joined', namespace='/chat')
def joined(message):
    room = Room.find_by_id(session['room_id']).room_name
    join_room(room)
    emit('status', {'name': session['username'], 'event': 'join'})
"""


@socketio.on('get_rooms')
def get_rooms():
    rooms = Room.get_rooms_by_users(g.user['id'])
    room_dicts = []
    for room in rooms:
        room_dicts.append(room.to_dict())
    emit('got_rooms', room_dicts)


@socketio.on('get_chat')
def get_chat(room_id):
    room = Room.find_by_id(room_id)
    if session['user_id'] in room.members:
        emit('got_room', room.to_dict())


@socketio.on('connect')
def connect():
    print('connected')
