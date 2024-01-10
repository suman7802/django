from sys import maxsize
from unittest.util import _MAX_LENGTH
from django.db import models

class Student(models.Model):
    roll_number = models.IntegerField()
    full_name = models.CharField(max_length = 30)
