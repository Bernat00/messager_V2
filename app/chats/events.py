import json

from app.security import session
from flask_socketio import emit, join_room, leave_room
from app.chats import io_bp

from app.models.rooms import Room
from app.models.message import Message

"""@socketio.on('joined', namespace='/chat')
def joined(message):
    room = Room.find_by_id(session['room_id']).room_name
    join_room(room)
    emit('status', {'name': session['username'], 'event': 'join'})
"""


@io_bp.on('get_chat')
def get_chat(room_id):
    chat = Message.get_by_room(room_id)
    room = Room.find_by_id(room_id)
    chat_dict = []

    if chat is None:
        chat_dict = [{'content': 'No messages yet!'}]
    else:
        for message in chat:
            chat_dict.append(message.to_dict())

    if session['user_id'] in Room.find_by_id(room_id).members:
        join_room(room.room_name)
        emit('got_chat', chat_dict, room=room.room_name)  # ez így nem jó


@io_bp.on('new_message')
def new_message(msg):
    Message.new_message(msg)


@io_bp.on('connect')
def connect():
    print('connected')


@io_bp.on('disconnect')
def disconnect():
    print('disconnected')
