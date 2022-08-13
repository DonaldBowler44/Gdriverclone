from flask import Flask, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    data = db.Column(db.LargeBinary)

    def __repr__(self):
        return f"Upload: {self.filename}"
    
    def __init__(self, filename):
        self.filename = filename

# class Event(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(100), nullable=False)
#     created_At = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#         return f"Event: {self.description}"
    
#     def __init__(self, description):
#         self.description = description
