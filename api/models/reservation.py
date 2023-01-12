from django.db import models
from .user import User

class Reservation(models.Model):
    
    date = models.DateField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT) # Un utilisateur ne peut pas être supprimé sachant qu'il as une réservation
    
    def __str__(self):
        return self.user.first_name