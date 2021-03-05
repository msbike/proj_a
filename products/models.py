from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    valid_from = models.DateField(default=timezone.now)
