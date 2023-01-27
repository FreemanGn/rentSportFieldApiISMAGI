from django.contrib import admin

# Register your models here.

from .models import User, Reservation, Terrain, Type, Team

class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'status')
    
    
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('user', 'terrain', 'date', 'time_start', 'time_end', 'status')
    
class TerrainAdmin(admin.ModelAdmin):

    list_display = ('name', 'type','price','size', 'adresse', 'capacity','image')

class TypeAdmin(admin.ModelAdmin):

    list_display = ('name','image')
        

class TeamAdmin(admin.ModelAdmin):

    list_display = ('name','type','number_player')
    

admin.site.register(User, UserAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Terrain, TerrainAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Team, TeamAdmin)
