from django.db import models

# Create your models here.
class group2(models.Model):
    name =models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    price=models.FloatField()