from django.contrib import admin
from django.urls import path
from scinet_app import views

urlpatterns = [
    path('main/', views.index),
    path('main/register', views.register),
    path('main/login', views.login)
]