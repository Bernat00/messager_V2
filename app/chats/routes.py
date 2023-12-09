import flask_socketio
from flask import Flask, session, render_template, request
from app.chats import bp
from app.security import is_fully_authenticated
from app.models.rooms import Room
from app.models.message import Message


@bp.route('')
def chats():
    rooms = Room.get_rooms_by_user_id(session['user_id'])
    return render_template('chats.html', rooms=rooms)
