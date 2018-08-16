from flask_wtf import FlaskForm  # Flask implementation of wtforms

# Classes/interfaces for form elements
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField
)

# Validators to be passed into wtforms classes
from wtforms.validators import(
    DataRequired,
    Length,
    Email,
    EqualTo
)


class RegistrationForm(FlaskForm):  # extend FlaskForm
  username = StringField(
      'Username',
      validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField(
      'Email',
      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField(
      'Confirm Password',
      validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
  email = StringField(
      'Email',
      validators=[DataRequired(), Email()])
  password = PasswordField(
      'Password',
      validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')
