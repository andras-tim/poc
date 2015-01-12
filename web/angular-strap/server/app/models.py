from flask import g
from wtforms.validators import Email
from .server import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, info={'validators': Email()})
    password = db.Column(db.String(80), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy='dynamic')
 
    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
 
    def __repr__(self):
        return '<User %r>' % self.email

    @classmethod
    def get_user(cls, email):
        return User.query.filter_by(email=email).first()

    # flask-loginmanager
    def is_authenticated(self):
        return True

    # flask-loginmanager
    def is_active(self):
        return True

    # flask-loginmanager
    def is_anonymous(self):
        return False

    # flask-loginmanager
    def get_id(self):
        return str(self.id)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())
 
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.user_id = g.user.id
 
    def __repr__(self):
        return '<Task %r>' % self.title
