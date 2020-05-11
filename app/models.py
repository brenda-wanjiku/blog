from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    bio = db.Column(db.String)
    profile_pic = db.Column(db.String)
    pass_code = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy='dynamic')

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
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref="blog", lazy ='dynamic')

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
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id = id).all()
        return comments


    def __repr__(self):
        return f'Comment {self.content}'

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),index = True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_subscribers(cls):
        return Subscriber.query.all()



class Quote:
    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote
    
