from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.member_login, name='member-login'),
    path('register_user', views.member_register, name='member-register'),
    path('logout_user', views.member_logout, name='member-logout'),
]