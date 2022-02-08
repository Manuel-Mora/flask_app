"Schema for employee"
from app.ma import ma

class EmployeeSchema(ma.Schema):
    "Employee Schema"
    class Meta:
        "Class Meta with fields to convert to dict"
        fields = (
            "id",
            "first_name",
            "middle_name",
            "lasty_name",
            "birth_date",
            "rfc",
            "address",
            "city",
            "state",
            "zipcode",
            "is_active"
        )
