from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def member_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('user-home')
            # Redirect to a success pa
        else:
            messages.success(request, "There was an error! Try again.")
            return redirect('member-login')
    else:
        return render(request, 'member_auth/member_login.html')

def member_register(request):
    return render(request, 'member_auth/member_register.html')

def member_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('landing_page')

