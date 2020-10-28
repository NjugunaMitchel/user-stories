from datetime import datetime
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
     
class User(UserMixin,db.Model):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column( db.String(20),unique = 1,nullable =0)
    email = db.Column(db.String(255), unique = True, nullable = False)
    profile_photo = db.Column(db.String(20),nullable =0,default="../download.jpeg")
    password = db.Column(db.String(40),nullable =0)
    posts = db.relationship('Post', backref='author, lazy=True')

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.profile_photo}')"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)

    def __repr__(self):
        return f"User('{self.title}','{self.date}')"
