from django.contrib.gis.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='places')
    location = models.PointField(srid=4326)  # lon/lat WGS84
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name
