from rest_framework.serializers import ModelSerializer

from api.models.terrain import Terrain

class TerainSerializer(ModelSerializer):
    class Meta:
        model = Terrain
        fields = '__all__'