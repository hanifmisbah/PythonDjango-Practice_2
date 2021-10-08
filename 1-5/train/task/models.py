from django.db import models

# Create your models here.
class Task(models.Model):
    item = models.CharField(default="", max_length=30)
    nlatin = models.CharField(default="", max_length=50)
    rinci = models.TextField(default="")