from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(), Length(min=3, max=128)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=3, max=128)])
    psw_again = PasswordField('Confirm password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Login')
