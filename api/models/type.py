from django.db import models

class Type(models.Model):
    
    class Choise(models.TextChoices):
        FOOT_BALL = 'F'
        BASKET_BALL = 'B'
        TENNIS = 'T'
        HAND_BALL = 'H'
    
    name = models.fields.CharField(choices=Choise.choices, max_length=5,unique=True)
    
    def __str__(self):
        return self.name