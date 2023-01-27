from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from api.models.type import Type


class TypeSerializer(ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Type
        fields = '__all__'
        
    def get_name(self,obj):
        return obj.get_name_display()