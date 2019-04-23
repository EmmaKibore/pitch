from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.string(225),index = True)
    email = db.Colunm(db.string(225),unique = True,index = True)
    role_id = db.Column(db.integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.string(225))
    profile_pic_path = db.Column(db.string())
    password_hash = db.Column(db.String(225))

    pitchs = db.relationship('Pitch',backref='user',lazy='dynamic')
    comments = db.relationship('Comment', backref = 'comment', lazy= "dynamic")


    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.model):
    __tablename__ = 'pitch'


    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String())
    category = db.Column(db.String(255))

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.relationship('Comment', backref = 'comments', lazy= "dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):

    __tablename__ = 'Comments'

    id = db.Column(db.Integer,primary_key = True)
    comment_content = db.Column(db.String())
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

     def __repr__(self):
        return f'{self.comment}'  
