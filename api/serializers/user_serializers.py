from rest_framework.serializers import ModelSerializer

from gestionTerrain.api.models.user import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'