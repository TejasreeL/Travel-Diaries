from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(request):
    return render(request, 'base/landing_page.html')

def contact_us(request):
    return render(request, 'base/contact_us.html')

def user_home(request):
    return render(request, 'base/user_home.html')