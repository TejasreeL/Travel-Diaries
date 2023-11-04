from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]

        if User.objects.filter(username=username).exists():
            messages.success(request, "Username already exists, Try again!")
            return redirect('member-register')    

        my_user = User.objects.create_user(username=username, password=password)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        messages.success(request, "registered!")
        login(request, my_user)
        return redirect('user-home')
        
    
    else:
        return render(request, 'member_auth/member_register.html')


# def member_register(request):
#     if request.method == 'POST':
#         try:
#             username = request.POST["username"]
#             password = request.POST["password"]
#             fname = request.POST["fname"]
#             lname = request.POST["lname"]

#             if User.objects.filter(username=username).exists():
#                 messages.success(request, "User already exists, Login instead!")
#                 return redirect('member-register')
            
#             my_user = User.objects.create_user(username=username, password=password)
#             my_user.first_name = fname
#             my_user.last_name = lname
#             my_user.save()

#             messages.success(request, "Registered successfully!")
#             login(request, my_user)
#             return redirect('user-home')
        
#         except KeyError:
#             messages.error(request, "Missing required fields")
#             return redirect('member-register')

#     else:
#         return render(request, 'member_auth/member_register.html')


def member_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('landing_page')

