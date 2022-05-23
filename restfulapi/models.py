from audioop import maxpp
from django.db import models

# Create your models here.

class Commodity(models.Model):
    category = models.CharField(max_length=300)
    subcategory = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name