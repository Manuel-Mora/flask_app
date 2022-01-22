"""Employees module"""
from flask import Blueprint
import json

employee_bp = Blueprint('employee', __name__)

@employee_bp.route("/")
def index():
    return json.dumps({
        "response": "blueprints working"
    })