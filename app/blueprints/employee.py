"""Employees module"""
from flask import Blueprint, request
from app.models.employee_model import Employee
from app.schemas.employee_schema import EmployeeSchema
from app.responses.generic_responses import Responses

employee_bp = Blueprint('employee', __name__, url_prefix="/employee")

@employee_bp.get("/")
def index():
    """Get all employees that are not deleted"""
    params = request.args
    employee_list = Employee().get_all(params)
    employees = EmployeeSchema(many=True).dump(employee_list)
    return Responses.index_response(employees)
