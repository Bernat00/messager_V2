from flask import Flask, session, render_template, redirect, url_for, flash
from app.chats import bp
from app.security import is_fully_authenticated
from  app.models.rooms import Room


@bp.route('/chats')
def chats():
    rooms = Room.get_rooms_by_user_id(session['user_id'])
    return render_template('chats.html', rooms=rooms)
