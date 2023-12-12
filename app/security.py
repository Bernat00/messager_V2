import functools

from flask import redirect, g, url_for, session, request, abort

from app.models.user import User


def is_fully_authenticated(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.username is None or g.user_id is None:
            return redirect(url_for('user.login', redirect=request.path))

        return view(**kwargs)

    return wrapped_view


def has_role(role):
    def has_role_decorator(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if g.user is None:
                return redirect(url_for('pages.login', redirect=request.path))
            elif g.user.role.username.upper() != role.upper():
                abort(401)

            return view(**kwargs)

        return wrapped_view

    return has_role_decorator


def init_app(app):
    app.before_request(__load_current_user)
    app.jinja_env.globals['is_fully_authenticated'] = lambda: g.user
    app.jinja_env.globals['has_role'] = lambda role: g.user and g.user.role.username.upper() == role.upper()


def __load_current_user():
    user = User.find_by_id(session.get('user_id'))
    if user is None:
        g.username = None
        g.user_id = None
    else:
        user_id = session['user_id']
        g.username = User.find_by_id(user_id).username
        g.user_id = user_id
