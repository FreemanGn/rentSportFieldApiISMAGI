from django.db import models

class Reservation(models.Model):
    
    date = models.DateField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    status = models.BooleanField(default=True)