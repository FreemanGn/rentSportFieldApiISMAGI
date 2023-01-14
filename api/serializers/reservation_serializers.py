from rest_framework.serializers import ModelSerializer

from api.models.reservation import Reservation


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        # depth = 2