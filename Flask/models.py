class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Room:
    def __init__(self, name, type_, capacity, location, floor):
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.location = location
        self.floor = floor

class Event:
    def __init__(self, name, description, start_time, end_time, expected_attendance):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.expected_attendance = expected_attendance

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  

class Event(db.Model):  
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    event_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    room_id = db.Column(db.Integer, nullable=False)
    expected_attendance = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
