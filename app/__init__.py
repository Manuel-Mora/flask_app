"""Init App file"""
from flask import Flask
from app.blueprints.employee import employee_bp

app = Flask(__name__)
app.register_blueprint(employee_bp)
