from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
import random

# Custom function to generate a random employee ID
def generate_unique_employee_id():
    while True:
        employee_id = 'e' + str(random.randint(1, 100))
        if not Emp.objects.filter(emp_id=employee_id).exists():
            return employee_id

# Custom validator for a 10-digit phone number
def validate_phone_number(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("Phone number must be exactly 10 digits.")

class Emp(models.Model):
    first_name = models.CharField(max_length=200, validators=[RegexValidator(r'^[A-Za-z.]+$', message="First Name can only contain letters and a dot (.).")])
    last_name = models.CharField(max_length=200, validators=[RegexValidator(r'^[A-Za-z.]+$', message="Last Name can only contain letters and a dot (.).")])
    emp_id = models.CharField(max_length=3, unique=True, default=generate_unique_employee_id, editable=False)
    email = models.EmailField(validators=[EmailValidator(message="Invalid email format.")])
    phone = models.CharField(max_length=10, validators=[validate_phone_number])
    address = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.emp_id})"
