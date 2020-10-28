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

    def Validate_email(self,data_field):
        user = User.query.filter_by(email = data_field.data).first()
        if user:
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        user =  User.query.filter_by(username = data_field.data).first()
        if user:
            raise ValidationError('That username is taken')




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

    def Validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('There is an account with that email')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('That username is taken')

class postForm(FlaskForm):
    title = StringField('Title' , validators = [DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('post')

