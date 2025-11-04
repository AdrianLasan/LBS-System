# places/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Place(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="places")
