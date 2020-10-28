from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):

    username = StringField('username',validators = [DataRequired(),Length(min=3, max=15)])
    email = StringField('email', validators =[DataRequired(),Email()])
    Password = PasswordField('password',validators = [DataRequired()])
    confirm_password =PasswordField('password',validators = [DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign up')


class Login(FlaskForm):
    email = StringField('email', validators =[DataRequired(),Email()])
    Password = PasswordField('password',validators = [DataRequired()])
    submit = SubmitField('Login')
    

class updateAccount(FlaskForm):
    username = StringField('username',validators = [DataRequired(),Length(min=3, max=15)])
    email = StringField('email', validators =[DataRequired(),Email()])
    Password = PasswordField('password',validators = [DataRequired()])
    confirm_password =PasswordField('password',validators = [DataRequired(),EqualTo('password')])

    submit = SubmitField('update')

class postForm(FlaskForm):
    title = StringField('Title' , validators = [DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('post')

