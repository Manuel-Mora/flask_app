"""Model for employee"""
from app.db import db

class Employee(db.Model):
    """Employee Model class"""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(60), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    rfc = db.Column(db.String(13), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    is_active = db.Column(db.Integer, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def get_all(self, params=None):
        """Get all employees that are not deleted"""
        return self.query.filter_by(deleted_at=None, **params).all()

    def get_one_by(self, params):
        """Get the first resource by the given params"""
        return self.query.filter_by(**params).first()

    def create(self):
        """Create a new employee in DB"""
        db.session.add(self)
        db.session.commit()

    def toggle_status(self, params):
        """Change an employee status by the given id"""
        employee = self.get_one_by(params)
        if employee:
            employee.is_active = int(not bool(employee.is_active))
            db.session.commit()
            return self.get_one_by(params)
        return None
