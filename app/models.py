from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    role_id = db.Column(db.Integer, db.Foreignkey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')

    def __repr__(self):
        return f'Role : {self.name}'



