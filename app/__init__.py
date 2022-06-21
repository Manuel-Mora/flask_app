"""Init App file"""
from flask import Flask
from app.blueprints.employee import employee_bp
from app.db import db
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config())

app.register_blueprint(employee_bp)

db.init_app(app)
