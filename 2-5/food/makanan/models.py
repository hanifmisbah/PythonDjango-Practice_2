from django.db import models

# Create your models here.
class Makan(models.Model):
    jenis=models.CharField(default='', max_length=20)
    item=models.CharField(default='', max_length=20)
    harga=models.PositiveBigIntegerField(default='')