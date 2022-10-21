from django.core.validators  import MinValueValidator,MaxValueValidator

from django.db import models
from wsgiref.validate import validator

class Thing(models.Model):
    name=models.CharField(max_length=30,unique=True, blank=False, default='DEFAULT VALUE')
    description=models.CharField(max_length=120, blank=True)
    quantity=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
