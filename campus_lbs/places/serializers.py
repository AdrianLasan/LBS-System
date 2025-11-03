from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Place

class PlaceGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Place
        geo_field = 'location'
        fields = ('id', 'name', 'description', 'category')
