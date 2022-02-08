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

    def __init__(self):
        super().__init__()
        self.__tablename__ = "employee"

    def get_all(self, params=None):
        """Get all employees that are not deleted"""
        return self.query.filter_by(deleted_at=None, **params).all()
