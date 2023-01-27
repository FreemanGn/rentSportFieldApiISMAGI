from rest_framework.serializers import ModelSerializer

from api.models.reservation import Reservation
from .user_serializers import UserSerializer


class ReservationSerializer(ModelSerializer):
    # user = UserSerializer()
    
    class Meta:
        model = Reservation
        fields = '__all__'
        # depth = 1
        
        #fields = ['id','date','time_start','time_end','status','terrain','user']
       
    # def get_user(self,instance):
        
    #     queryset = instance.user.filter(status=True)
    #     serializer = UserSerializer(queryset,many=True)
        
    #     return serializer.data