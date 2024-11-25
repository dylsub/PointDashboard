from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, default=0)

@app.route('/')
def index():
    points = Point.query.all()
    return render_template('index.html', points=points)

@app.route('/add', methods=['POST'])
def add_point():
    user_name = request.form['user_name']
    point = Point(user_name=user_name, points=0)
    db.session.add(point)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_point(id):
    point = Point.query.get(id)
    if point:
        point.points += int(request.form['points'])
        db.session.commit()
    return redirect(url_for('index'))