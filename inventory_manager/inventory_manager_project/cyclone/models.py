# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class arrays(models.Model):
    array_name = models.CharField('Array Name', max_length=100)
    array_status = models.BooleanField('Reserved', default=False)
    employee_array = models.ForeignKey('employees')

    def __str__(self):
        return str(self.array_name)

class employees(models.Model):
    employee_id = models.CharField('Employee ID', max_length=50)
    employee_name = models.CharField('Employee Full Name', max_length=100)
    employee_email = models.CharField('Employee Email ID', max_length=100)

    def __str__(self):
        return str(self.employee_id)
