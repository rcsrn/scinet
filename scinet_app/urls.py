from django.contrib import admin
from django.urls import path
from scinet_app import views

urlpatterns = [
    path('main/', views.index, name='index'),
    path('main/publication/<int:publication_id>/', views.publication, name='publication'),
    path('main/user/<int:user_id>/', views.user, name='user'),
    path('main/', views.index),
    path('main/register', views.register, name='register'),
    path('main/login', views.login, name='login'),
    path('main/topic/<int:topic_id>', views.topic, name='topic'),
    path('institution/<int:insti_id>', views.institution_info, name ='institution'),
    path('main/search', views.search, name='search'),
    path('main/logout', views.logout, name='logout'),
    path('main/researcher', views.newResearcher, name='researcher'),
    path('main/new-publication', views.newPublication, name='new-publication')
]