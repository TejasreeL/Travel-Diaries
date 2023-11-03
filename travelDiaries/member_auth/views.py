from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def member_login(request):
    return render(request, 'member_auth/member_login.html')

def member_register(request):
    return render(request, 'member_auth/member_register.html')

