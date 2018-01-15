from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rooms/', views.RoomsView.as_view(), name='rooms'),
    path('room/<int:pk>/', views.RoomDetail.as_view(), name ='room'),
    path('contacts', views.contactsView, name ="contact")
]