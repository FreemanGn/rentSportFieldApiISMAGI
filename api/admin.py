from django.contrib import admin

# Register your models here.

from .models import User, Reservation

class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'status')
    
    
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('user', 'date', 'time_start', 'time_end', 'status')
    

admin.site.register(User, UserAdmin)
admin.site.register(Reservation, ReservationAdmin)
