from flask import Flask, session, render_template, redirect, url_for, flash
from app.chats import bp
from app.security import is_fully_authenticated


@bp.route('/chats')
def chats():
    return render_template('chats.html')
