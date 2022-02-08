"""Employees module"""
from flask import Blueprint
import json
from app.models.employee_model import Employee
from app.schemas.employee_schema import EmployeeSchema

employee_bp = Blueprint('employee', __name__, url_prefix="/employee")

@employee_bp.get("/")
def index():
    """Get all employees that are not deleted"""
    employee_list = Employee().get_all()
    employees = EmployeeSchema(many=True).dump(employee_list)
    return json.dumps(employees, ensure_ascii=False), 200
