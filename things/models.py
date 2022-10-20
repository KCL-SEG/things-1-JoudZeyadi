from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model

class Thing(Model):
    name = models.CharField()
    description = models.TextField()
    quantity = models.IntegerField()



# Create your models here.
