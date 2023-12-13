import json

from flask import request

from app.security import session
from flask_socketio import emit, join_room, rooms
from app.chats import io_bp

from app.models.rooms import Room
from app.models.message import Message


# todo a joineddel valamit kezdeni
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
    chat_dict = {'room_id': room.room_id, 'my_name': session['username'], 'messages': []}

    if len(chat) == 0:
        chat_dict['messages'].append({'content': 'No messages yet!'})
    else:
        for message in chat:
            chat_message = message.to_dict()
            chat_message['sender_name'] = message.sender_name()
            chat_dict['messages'].append(chat_message)

    if session['user_id'] in Room.find_by_id(room_id).members:
        join_room(room.room_id)             # todo áááááááááááá mi van a room id-val?
        emit('got_chat', chat_dict, sid=request.sid)


@io_bp.on('new_message')
def new_message(msg):
    print(msg['room_id'])
    if len(rooms()) > 1:
        print(rooms())
        message = {
            'sender': session['user_id'],
            'room_id': msg['room_id'],
            'content': msg['content'],
            'sender_name': session['username']
        }
        Message.new_message(message)
        emit('got_new_message', message, room=message['room_id'])
    # todo else reload


@io_bp.on('connect')
def connect():
    print('connected')


@io_bp.on('disconnect')
def disconnect():
    print('disconnected')
