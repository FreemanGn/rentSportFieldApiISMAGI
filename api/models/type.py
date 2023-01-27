from django.db import models

class Type(models.Model):
    
    class Choise(models.TextChoices):
        FOOTBALL = 'FB'
        BASKETBALL = 'BB'
        TENNIS = 'T'
        HANDBALL = 'HB'
        NATATION = 'N'
        SKATEPARK = 'SP'
        PATINOIRE = 'P'
        STREETGYM = 'SG'
        VOLLEYBALL = 'VB'
        
    
    name = models.fields.CharField(choices=Choise.choices, max_length=5,unique=True)
    image = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name