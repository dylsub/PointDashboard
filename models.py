from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, default=0)