from django.contrib import admin

# Register your models here.
from hotel.models import Room, RoomFacility, Profile

admin.site.register(Room)
admin.site.register(RoomFacility)
admin.site.register(Profile)