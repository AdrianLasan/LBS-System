from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Place
from .serializers import PlaceGeoSerializer

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceGeoSerializer
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['name']

@api_view(['GET'])
def nearest(request):
    try:
        lat = float(request.query_params.get('lat'))
        lng = float(request.query_params.get('lng'))
        limit = int(request.query_params.get('limit', 10))
    except (TypeError, ValueError):
        return Response({'error': 'lat, lng (and optional limit) required'}, status=400)
    origin = Point(lng, lat, srid=4326)
    qs = Place.objects.annotate(distance=Distance('location', origin)).order_by('distance')[:limit]
    data = PlaceGeoSerializer(qs, many=True).data
    return Response({'type':'FeatureCollection','features':data})

@api_view(['GET'])
def within_radius(request):
    try:
        lat = float(request.query_params.get('lat'))
        lng = float(request.query_params.get('lng'))
        km = float(request.query_params.get('km', 1.0))
    except (TypeError, ValueError):
        return Response({'error': 'lat, lng (and optional km) required'}, status=400)
    origin = Point(lng, lat, srid=4326)
    qs = Place.objects.filter(location__distance_lte=(origin, D(km=km)))
    data = PlaceGeoSerializer(qs, many=True).data
    return Response({'type':'FeatureCollection','features':data})
