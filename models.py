# myapp/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)

    def __str__(self):
        return self.username


