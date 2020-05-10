from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    pass_code = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    blog = db.relationship('Blog', backref='user', lazy='dynamic')

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @property 
    def password(self):
        raise AttributeError('You cannot read password')

    @password.setter
    def password(self,password):
        self.pass_code = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_code,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')

    def __repr__(self):
        return f'Role : {self.name}'


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def display_blogs(cls):
        blogs = Blog.query.all()
        return blogs

    def __repr__(self):
        return f'Blog {self.title}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)

    def __repr__(self):
        return f'Comment {self.content}'


class Quote:
    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote
    
