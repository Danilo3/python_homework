from django.contrib import admin

# Register your models here.
from hotel.models import Room, RoomFacility

admin.site.register(Room)
admin.site.register(RoomFacility)