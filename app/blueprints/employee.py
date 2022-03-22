"""Employees module"""
import json
from flask import Blueprint, request
from app.models.employee_model import Employee
from app.schemas.employee_schema import EmployeeSchema
from app.responses.generic_responses import Responses

employee_bp = Blueprint('employee', __name__, url_prefix="/employee")

@employee_bp.get("")
def index():
    """Get all employees that are not deleted"""
    params = request.args
    employee_list = Employee().get_all(params)
    employees = EmployeeSchema(many=True).dump(employee_list)
    return Responses.index_response(employees)

@employee_bp.get("/<employee_id>")
def show(employee_id):
    """Get an employee by the given id"""
    employee = Employee().get_one_by({"id": employee_id})
    employee = EmployeeSchema(many=False).dump(employee)
    return Responses.show_response(employee)

@employee_bp.post("")
def create():
    """Create a new employee"""
    params = json.loads(request.data)
    employee = Employee(**params)
    employee.create()
    new_emp = EmployeeSchema(many=False).dump(employee.get_one_by(params))
    return Responses.create_response(new_emp)
