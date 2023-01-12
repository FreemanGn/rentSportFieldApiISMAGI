from django.db import models

class User(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254) #utiliser email validator
    phone = models.PositiveBigIntegerField()
    adresse = models.CharField(max_length=100) 
    status = models.BooleanField(default=True)
    