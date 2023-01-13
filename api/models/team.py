from django.db import models
from .type import Type


class Team(models.Model):
    name = models.CharField(max_length=50)
    number_player = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name