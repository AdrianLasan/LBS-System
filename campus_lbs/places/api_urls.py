from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet, within_radius, nearest

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')

urlpatterns = [
    path('', include(router.urls)),
    path('places/within/', within_radius, name='within_radius'),
    path('places/nearest/', nearest, name='nearest'),
]
