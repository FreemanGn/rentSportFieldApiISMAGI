from django.db import models
from .user import User
from .terrain import Terrain

class Reservation(models.Model):
    
    date = models.DateField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    status = models.BooleanField(default=True)
    
    #FK USER
    user = models.ForeignKey(User, on_delete=models.PROTECT) # Un utilisateur ne peut pas être supprimé sachant qu'il as une réservation
    
    #FK TERRAIN
    terrain = models.ForeignKey(Terrain, on_delete=models.PROTECT)
    def __str__(self):
        return self.user.first_name