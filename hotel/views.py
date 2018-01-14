from django.shortcuts import render

# Create your views here.
from django.views import generic

from hotel.models import Room


class IndexView(generic.TemplateView):
    template_name = 'hotel/index.html'


class RoomsView(generic.ListView):
    template_name = 'hotel/rooms.html'
    context_object_name = 'all_rooms_list'

    def get_queryset(self):
        return Room.objects.all()
