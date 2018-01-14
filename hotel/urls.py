from . import views
from django.urls import path


app_name = 'hotels'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]