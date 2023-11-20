from django.contrib import admin

# Register your models here.
from .models import Diary
from .models import Page

admin.site.register(Diary)
admin.site.register(Page)
