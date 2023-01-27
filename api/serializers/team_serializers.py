from rest_framework.serializers import ModelSerializer

from api.models.team import Team

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'