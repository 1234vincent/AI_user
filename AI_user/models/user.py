__package__ = "models"
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Activity(db.Model):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
    activity_name = db.Column(db.String(255), nullable=False)
    activity_date = db.Column(db.Date, nullable=True)

class Membership(db.Model):
    __tablename__ = 'membership'
    
    membership_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
    level = db.Column(db.Enum('Bronze', 'Silver', 'Gold', 'Platinum'), nullable=False)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)

class Privilege(db.Model):
    __tablename__ = 'privileges'
    
    privilege_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    privilege_name = db.Column(db.String(255), nullable=False)
    remaining_uses = db.Column(db.Integer, default=0)
    is_enabled = db.Column(db.Boolean, default=False)
    conditions = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    membership_id = db.Column(db.Integer, db.ForeignKey('membership.membership_id'), nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

