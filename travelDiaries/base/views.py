from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Diary
from django.contrib.auth.models import User
from datetime import datetime
from django.db import IntegrityError


# Create your views here.
def landing_page(request):
    return render(request, 'base/landing_page.html')

def contact_us(request):
    return render(request, 'base/contact_us.html')

def user_home(request):
    if request.user.is_authenticated:
        diaries = Diary.objects.all()[:4]
        # user_diaries = [diary for diary in diaries if request.user in diary.users.all()]
        user_diaries = request.user.diary_set.all()
        pending_diaries = [diary for diary in user_diaries if diary.is_complete is False][:4]
        dates = [diary.start_date for diary in user_diaries]
        context = {
            "pending_diaries": pending_diaries,
            "diaries": diaries,
            "user_diaries": user_diaries,
            "dates": dates,
        }
        return render(request, 'base/user_home.html', context)
    messages.success(request, "You need to Login first.")
    return redirect('landing_page')

def convertDate(date: str) -> str:
    print("DDDDDD", type(date))
    date_obj = datetime.strptime(date, "%m/%d/%Y")
    print("BBBBBB", date_obj)
    corr_date = date_obj.strftime("%Y-%m-%d")
    print("CCCCCC", corr_date)
    return corr_date

def add_diary(request):
    
    diary_name = request.POST.get('diary_name')
    desc = request.POST.get('desc')
    destination = request.POST.get('destination')
    user1 = request.POST.get('author1')
    user2 = request.POST.get('author2')
    user3 = request.POST.get('author3')
    user4 = request.POST.get('author4')
    author = request.user.username
    new_diary = Diary()

   
    new_diary.diary_name = diary_name
    new_diary.author = author
    new_diary.desc = desc
    new_diary.destination = destination
    new_diary.is_complete = False

    
    try:
        new_diary.save()
        # new_diary.users.add(request.user)
        for username in [user1, user2, user3, user4]:
            try:
                if username != "None":
                    print("username is", username)
                    user = User.objects.get(username=username)
                    new_diary.users.add(user)
            except:
                print(username)
                messages.success(request, "One of the authors doesn't exist")
                return redirect('user-home')
        # usernames = [username.strip() for username in request.POST.getlist('authors') if username != None]

        # users = User.objects.filter(username__in=usernames)

        # Print statements for debugging
        # print('usernames:', usernames)
        # print('matching users:', users)

        

        # Adding other selected users
        # new_diary.users.add(*users)

        messages.success(request, "Diary Successfully Created!")
        return redirect('user-home')

    except IntegrityError:
        messages.success(request, "Diary name already exists!")
        return redirect('user-home')


def my_diary(request, d_id):
    my_diary = Diary.objects.get(id= d_id)

    context = {"my_diary": my_diary}

    return render(request, 'base/my_diary.html', context)




