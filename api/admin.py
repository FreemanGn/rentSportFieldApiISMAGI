from django.contrib import admin

# Register your models here.

from .models import User, Reservation,Terrain

class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'status')
    
    
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('user', 'terrain', 'date', 'time_start', 'time_end', 'status')
    
class TerrainAdmin(admin.ModelAdmin):

    list_display = ('name', 'size', 'adresse', 'capacity')
    

admin.site.register(User, UserAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Terrain, TerrainAdmin)
