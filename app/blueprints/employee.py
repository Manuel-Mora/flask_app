"""Employees module"""
import json
from flask import Blueprint, request
from datetime import datetime
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

@employee_bp.patch("/<employee_id>")
def toggle_active(employee_id):
    """Change the actual status of an employee"""
    employee = Employee().toggle_status({"id": employee_id})
    if employee:
        employee = EmployeeSchema(many=False).dump(employee)
        return Responses.update_response(employee)
    return Responses.not_found_response({"id": employee_id})

@employee_bp.put("/<employee_id>")
def update(employee_id):
    """Update the employee according to the given id"""
    body = json.loads(request.data)
    updated_emp = Employee().update(employee_id, body)
    if updated_emp:
        employee = EmployeeSchema(many=False).dump(updated_emp)
        return Responses.update_response(employee)
    return Responses.not_found_response({"id": employee_id})

@employee_bp.delete("/<employee_id>")
def logic_delete(employee_id):
    """Make a logical delete of an employee"""
    deleted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    employee = Employee().update(employee_id, {"deleted_at": deleted_at})
    if employee:
        employee = EmployeeSchema(many=False).dump(employee)
        return Responses.logical_delete(employee)
    return Responses.not_found_response({"id": employee_id})

@employee_bp.delete("/<employee_id>/destroy")
def destroy(employee_id):
    """Make a permanent delete of an employee"""
    response = Employee().destroy(employee_id)
    if response:
        return Responses.destroy_resource()
    return Responses.not_found_response({"id": employee_id})
