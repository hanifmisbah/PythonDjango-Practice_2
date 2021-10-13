from django.db import models

# Create your models here.
class Makan(models.Model):
    item=models.CharField(default='', max_length=20)
    jenis=models.CharField(default='', max_length=20)
    harga=models.PositiveBigIntegerField(default=0)