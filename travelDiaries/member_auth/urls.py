from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.member_login, name='member-login'),
    path('register', views.member_register, name='member-register'),
]