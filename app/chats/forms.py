from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length


class NewChatForm(FlaskForm):

    room_name = StringField('szoba neve', validators=[DataRequired(), Length(min=3, max=128)])
    selected_people = SelectMultipleField(coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create')


