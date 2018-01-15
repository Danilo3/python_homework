from django.db import models
from django.conf import settings
# Create your models here.


class RoomFacility(models.Model):
    name = models.CharField(max_length=20)
    icon_number = models.IntegerField(default=0)


class Room(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    amount = models.IntegerField()
    image_path = models.CharField(max_length=100, default="")
    facilities = models.ManyToManyField(RoomFacility)


class Booking(models.Model):
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank= True)
    adults_count = models.IntegerField(default=0)
    children_count = models.IntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='uploads/', blank=True)
    reservations = models.ManyToManyField(Booking)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


