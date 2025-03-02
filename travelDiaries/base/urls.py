from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page' ),
    path('contact-us', views.contact_us, name='contact-us'),
    path('user-home', views.user_home, name='user-home'),
    path('user-home/add-diary', views.add_diary, name='add-diary'),
    path('user-home/my-diary/<int:d_id>/', views.my_diary, name="my-diary"),
]