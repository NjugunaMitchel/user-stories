from datetime import datetime
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


     
class User(UserMixin,db.Model):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column( db.String(20),unique = 1,nullable =0)
    email = db.Column(db.String(255), unique = True, nullable = False)
    profile_photo = db.Column(db.String(20),nullable =0,default="../download.jpeg")
    password = db.Column(db.String(40),nullable =0)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        pass_hash = generate_password_hash(password)
        self.password = pass_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User: {self.username}'


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Post Title: {self.title}"
