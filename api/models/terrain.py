from django.db import models
from .type import Type

class Terrain(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    adresse = models.CharField(max_length=50)
    capacity = models.IntegerField()
    price = models.IntegerField()
    image = models.URLField(max_length=200)
    
    #FK Type
    
    type = models.ForeignKey(Type,on_delete=models.PROTECT) #A faire : Gerer la possibilité se supp un terrain
    
    def __str__(self):
        return self.name
    