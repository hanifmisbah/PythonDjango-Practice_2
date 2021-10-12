from django.db import models

# Create your models here.
class Kategori(models.Model):
    kate = models.CharField(default='', max_length=10)

class Makan(models.Model):
    nama = models.CharField(default='', max_length=10)
    ktgori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='kategori')
    nama = models.CharField(default='', max_length=10)