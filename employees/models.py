from django.db import models
from django.utils import timezone


class Employees(models.Model):
    employee_id = models.CharField(max_length=50, default='NULL')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    salary = models.IntegerField()
    emp_id = models.CharField(max_length=10, default='NULL')

