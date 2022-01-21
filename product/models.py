from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    quantity = models.IntegerField()