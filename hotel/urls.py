from . import views
from django.urls import path, include
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rooms/', views.RoomsView.as_view(), name='rooms'),
    path('room/<int:pk>/', views.RoomDetail.as_view(), name='room'),
    path('contacts', views.contactsView, name="contact"),
    # path('login/', views.user_login, name="login"),
    #path('register/', views.RegisterFormView.as_view(), name="register"),
    path('register/', views.register, name ="register"),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('dashboard/', views.dashboard,name='dashboard')
]