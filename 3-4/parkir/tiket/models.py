from django.db import models
# from time import time

# Create your models here.
class Park(models.Model):
    nopol=models.TextField(default='', max_length=10)

class Ket(models.Model):
    notempat=models.TextField(default='', max_length=5)
    dtg=models.TimeField(null=True, blank=True)
    klr=models.TimeField(null=True, blank=True)