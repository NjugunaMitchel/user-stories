from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
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
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')




class Login(FlaskForm):
    email = StringField('email', validators =[DataRequired(),Email()])
    Password = PasswordField('password',validators = [DataRequired()])
    submit = SubmitField('Login')
    

""" validations """
