from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField
    valid_from = models.DateField(default=timezone.now)
