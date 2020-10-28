  def Validate_email(self,data_field):
        if email.data != current_user.email:
             user = User.query.filter_by(email = data_field.data).first()
             if user:
                  raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if username.data != current_user.username:
             user = User.query.filter_by(username = data_field.data).first()
             if user:
                  raise ValidationError('That username is taken')