from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Place, Category

@admin.register(Place)
class PlaceAdmin(GISModelAdmin):
    list_display = ('name', 'category')
    default_zoom = 13

admin.site.register(Category)
