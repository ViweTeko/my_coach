"""This script is the urls file of Members app"""
from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register_user"),
    path('athletes/', views.athletes, name="athletes"),
    path('add_athlete/', views.add_athlete, name="add_athlete"),
    path('view_athlete/', views.view_athlete, name="view_athlete"),
]
