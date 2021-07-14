from datetime import timezone
from django.db import models
import django.utils.timezone
from datetime import datetime

# Create your models here.
class Button(models.Model):
    name = models.CharField(max_length=100)
    state = models.BooleanField() 
    last_modification = models.DateTimeField()

    def __str__(self):
        return self.name

class RequiredButton(models.Model):
    name = models.CharField(max_length=100)
    state = models.BooleanField() 
    last_modification = models.DateTimeField()

    def __str__(self):
        return self.name



class DimmingButton(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.name