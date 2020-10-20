from django.contrib import admin
from bookings.models import (Movie,UserProfile,Ticket,Payment)
# Register your models here.


admin.site.register(Movie)
admin.site.register(UserProfile)
admin.site.register(Ticket)
admin.site.register(Payment)
