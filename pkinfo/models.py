from django.db import models

# Create your models here.

class Parking(models.Model):
    location = models.IntegerField(max_length=10, unique=True, null=False)
    isParked = models.BooleanField(default=False)
