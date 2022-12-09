from django.contrib import admin
from django.urls import path
from scinet_app import views

urlpatterns = [
    path('main/', views.index),
    path('main/register', views.register),
    path('publication/<int:publication_id>/', views.publication, name='publication'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('institution/<int:insti_id>', views.institution_info, name ='institution'),
]