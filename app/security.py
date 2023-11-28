import functools

from flask import redirect, g, url_for, session, request, abort

from app.models.user import User


def is_fully_authenticated(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('pages.login', redirect=request.path))

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
    if session.get('user_id') is None:
        g.user = None
    else:
        user_id = session['user_id']
        g.username = User.find_by_id(user_id)
        g.user_id = user_id
