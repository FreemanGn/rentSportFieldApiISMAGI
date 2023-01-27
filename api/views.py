from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .models import User, Reservation, Team, Terrain, Type

from .serializers import UserSerializer, ReservationSerializer, TeamSerializer, TerainSerializer, TypeSerializer

from .permission import IsAdminAuthenticated;

# Create your views here.

class UserViewset(ModelViewSet):
    
    # permission_classes = [IsAdminAuthenticated]
    
    serializer_class = UserSerializer
     
    def get_queryset(self):
        return User.objects.all()
    
    
    # def get(self, *args, **kwargs):
        
    #     users = User.objects.all()
    #     serializer = UserSerializer(users,many=True)
        
    #     return Response( serializer.data, status=status.HTTP_200_OK)  
    
    
class ReservationViewset(ModelViewSet):
    
    serializer_class = ReservationSerializer
    
    # permission_classes = [IsAuthenticated]
     
    def get_queryset(self):
        queryset = Reservation.objects.filter(status=True)
        
        user_id = self.request.GET.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
    
class TeamViewset(ModelViewSet):
    
    serializer_class = TeamSerializer
    # permission_classes = [IsAdminAuthenticated]
     
    def get_queryset(self):
        return Team.objects.all()
    
    
class TerrainViewset(ModelViewSet):
    
    serializer_class = TerainSerializer
    # permission_classes = [IsAdminAuthenticated]
     
    def get_queryset(self):
        return Terrain.objects.all()
    
class TypeViewset(ModelViewSet):
    
    serializer_class = TypeSerializer
    # permission_classes = [IsAdminAuthenticated]
     
    def get_queryset(self):
        return Type.objects.all()