from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=256)
    stock = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=32)
