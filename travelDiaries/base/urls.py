from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page' ),
    path('contact-us', views.contact_us, name='contact-us'),
]