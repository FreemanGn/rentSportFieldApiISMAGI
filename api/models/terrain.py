from django.db import models

class Terrain(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    adresse = models.CharField(max_length=50)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name
    