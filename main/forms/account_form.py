from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Required, Length, Email, EqualTo, ValidationError
from mariaapi.models.user import User

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    pwd = PasswordField('Password', validators=[DataRequired()])
    confirm_pwd = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('pwd')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=2, max=20)])
    profile = FileField('Profile', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please choose a different one.')

    def validate_nickname(self, nickname):
        user = User.query.filter_by(nickname=nickname.data).first()
        if user:
            raise ValidationError('That nickname is already taken. Please choose a different one.')

    # https://stackoverflow.com/questions/52899084/flask-wtforms-why-is-my-post-request-to-upload-a-file-not-sending-the-file-data

class SigninForm(FlaskForm):
    pwd = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


