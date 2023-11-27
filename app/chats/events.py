from flask import session
from flask_socketio import emit, join_room, leave_room
from app import socketio

from app.models.rooms import Room


@socketio.on('joined', namespace='/chat')
def joined(message):
    room = Room.find_by_id(session['room_id']).room_name
    join_room(room)
    emit('status', {'name': session['username'], 'event': 'join'})
