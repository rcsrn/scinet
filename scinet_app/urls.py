from django.contrib import admin
from django.urls import path
from scinet_app import views

urlpatterns = [
    path('main/', views.index, name='index'),
    # path('publication/<int:publication_id>/', views.publication, name='publication'),
    # path('user/<int:user_id>/', views.user, name='user'),
    path('main/', views.index),
    path('main/register', views.register, name='register'),
    path('main/login', views.login, name='login'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    # path('institution/<int:insti_id>', views.institution_info, name ='institution'),
]