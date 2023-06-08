from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    # Define the table name
    __tablename__ = 'users'
    
    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    lastLogin = db.Column(db.DateTime, default=datetime.utcnow) # -5 hours for EST


class Content(db.Model):
    __tablename__ = 'contents'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # -5 hours for EST
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Define the relationship to User model
    user = db.relationship('User', backref=db.backref('contents', lazy=True))
