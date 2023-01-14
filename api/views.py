from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import User, Reservation

from .serializers import UserSerializer, ReservationSerializer

# Create your views here.

class UserViewset(ModelViewSet):
    
    serializer_class = UserSerializer
     
    def get_queryset(self):
        return User.objects.all()
    
    
    # def get(self, *args, **kwargs):
        
    #     users = User.objects.all()
    #     serializer = UserSerializer(users,many=True)
        
    #     return Response( serializer.data, status=status.HTTP_200_OK)  
    
    
class ReservationViewset(ModelViewSet):
    
    serializer_class = ReservationSerializer
     
    def get_queryset(self):
        return Reservation.objects.all()
    