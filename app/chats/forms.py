from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class NewChatForm(FlaskForm):
    pass
    # todo select multiple vagy valami hasonló, youtube tutorial


