from django.contrib import admin
from bookings.models import (Product,UserProfile,Ticket,Payment)
# Register your models here.


admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Ticket)
admin.site.register(Payment)
