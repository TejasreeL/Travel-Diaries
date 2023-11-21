from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Diary

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

        context = {
            "pending_diaries": pending_diaries,
            "diaries": diaries,
            "user_diaries": user_diaries,
        }
        return render(request, 'base/user_home.html', context)
    messages.success(request, "You need to Login first.")
    return redirect('landing_page')