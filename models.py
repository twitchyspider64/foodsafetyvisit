from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class AuditSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_number = db.Column(db.String(20))
    manager_name = db.Column(db.String(100))
    date = db.Column(db.String(20))
    percentage = db.Column(db.Float)
    result = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
