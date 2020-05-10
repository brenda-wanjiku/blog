from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    blog = db.relationship('Blog', backref='user', lazy='dynamic')

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
    id = db.Column(db.Integer, primary_key = Role)
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



