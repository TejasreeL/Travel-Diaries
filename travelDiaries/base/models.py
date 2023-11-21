from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Diary(models.Model):
    diary_name = models.CharField("Diary",max_length= 100)
    users = models.ManyToManyField(User)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    desc = models.CharField(max_length=300, null=True, blank=True)
    destination = models.CharField(max_length=100, null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.diary_name
    
    class Meta:
        db_table = "Diary"


class Page(models.Model):
    page_template_num = models.IntegerField()
    home_diary = models.ManyToManyField(Diary)

    def __str__(self):
        pass

