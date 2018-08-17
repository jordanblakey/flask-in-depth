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
    EqualTo,
    ValidationError
)

from flaskblog.models import User


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

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('Account exists with that username.')

  def validate_email(self, email):
    email = User.query.filter_by(email=email.data).first()
    if email:
      raise ValidationError('Account exists with that email.')


class LoginForm(FlaskForm):
  email = StringField(
      'Email',
      validators=[DataRequired(), Email()])
  password = PasswordField(
      'Password',
      validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')
