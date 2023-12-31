# Generated by Django 4.1 on 2023-10-29 07:59

import django.core.validators
from django.db import migrations, models
import emp.models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Invalid email format.')]),
        ),
        migrations.AlterField(
            model_name='emp',
            name='emp_id',
            field=models.CharField(default=emp.models.generate_unique_employee_id, editable=False, max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='first_name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[A-Za-z.]+$', message='Name can only contain letters and a dot (.).')]),
        ),
        migrations.AlterField(
            model_name='emp',
            name='last_name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[A-Za-z.]+$', message='Name can only contain letters and a dot (.).')]),
        ),
        migrations.AlterField(
            model_name='emp',
            name='phone',
            field=models.CharField(max_length=10, validators=[emp.models.validate_phone_number]),
        ),
    ]
