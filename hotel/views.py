from django.shortcuts import render

# Create your views here.
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'hotel/index.html'


class RoomsView(generic.TemplateView):
    template_name = 'hotel/rooms.html'
