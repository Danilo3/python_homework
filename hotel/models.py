from django.db import models

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


