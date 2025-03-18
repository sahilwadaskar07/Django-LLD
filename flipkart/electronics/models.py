from django.db import models

# Create your model here


class Product(models.Model): 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()