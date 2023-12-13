from flask import session, render_template, redirect, url_for

from app.chats import bp

from app.security import is_fully_authenticated
from app.models.rooms import Room
from app.models.user import User

from app.chats.forms import NewChatForm


@bp.route('', methods=('GET', 'POST'))
@is_fully_authenticated
def chats():
    # todo form for new chat
    rooms = Room.get_rooms_by_user_id(session['user_id'])
    form = NewChatForm()
    form.selected_people.choices = User.get_all_tuple_incomplete()
    form.selected_people.choices.remove((session['user_id'], session['username']))

    if form.validate_on_submit():
        room_name = form.room_name.data

        members = form.selected_people.data
        members.append(session['user_id'])

        room = Room(room_name, members)
        room.save()

        return redirect(url_for('chats.chats'))

    return render_template('chats.html', rooms=rooms, form=form)
