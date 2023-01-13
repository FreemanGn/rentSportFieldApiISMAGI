from django.contrib import admin

# Register your models here.

from .models import User, Reservation, Terrain, Type

class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'status')
    
    
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('user', 'terrain', 'date', 'time_start', 'time_end', 'status')
    
class TerrainAdmin(admin.ModelAdmin):

    list_display = ('name', 'type', 'size', 'adresse', 'capacity')

class TypeAdmin(admin.ModelAdmin):

    list_display = ('name',)
        

admin.site.register(User, UserAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Terrain, TerrainAdmin)
admin.site.register(Type, TypeAdmin)
