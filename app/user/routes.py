from urllib.parse import urlsplit

from flask import Flask, session, render_template, redirect, url_for, flash, request

from app.user import bp
from app.user.forms import LoginForm, RegisterForm
from app.models.user import User


# ide login, register, edit

@bp.route('/login', methods=('GET', 'POST'))
def login():
    username = None
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        user = User.find_by_username(username)
        if user is not None:
            if user.check_password(form.password.data):
                session['username'] = username
                session['user_id'] = user.user_id
                # redirecting after login
                if request.args.get('redirect') is not None \
                        and urlsplit(request.args.get('redirect')).netloc == '':
                    return redirect(request.args.get('redirect'))
                # just normal login
                return redirect(url_for('chats.chats'))
            else:
                flash('Password is incorrect!', 'warning')
        else:
            flash('Wrong username!', 'warning')

    return render_template('user/login.html', username=username, password=None, form=form)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    username = None
    email = None
    password = None

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(username, email, password=password)
        User.save(new_user)
        session['username'] = username
        session['user_id'] = User.find_by_username(username).user_id
        return redirect(url_for('chats.chats'))

    return render_template('user/register.html', username=username, email=email, password=password,
                           psw_again=None, form=form)


@bp.route('/logout')
def logout():
    session.clear()
    flash('Logout successful.')

    return redirect(url_for('user.login'))

# todo edit user stuff
