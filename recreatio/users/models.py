from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
import datetime
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.user.first_name +' ' + self.user.last_name

class Organization(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    leaders = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name



class Activities(models.Model):
    start_date = models.DateField(verbose_name="Start Date (YYYY-MM-DD)")
    end_date = models.DateField(verbose_name="End Date (YYYY-MM-DD)")
    age_group_young = models.IntegerField(default = 0, verbose_name="Youngest Age") #flag year of birth
    age_group_old = models.IntegerField(default = 20, verbose_name="Oldest Age") #flag year of birth
    reg_start = models.DateTimeField(default = datetime.datetime.now(tz=timezone.utc), verbose_name="Registration Start Time")  #set up when registration is open
    reg_end = models.DateTimeField(default = datetime.datetime.now(tz=timezone.utc), verbose_name="Registration End Time")    #set up when registration is closed
    max_size = models.IntegerField(default = 0, verbose_name="Registration Maximum")    #set up the size of a class
    description = models.CharField(max_length=300)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    title = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self): 
        return self.title 

    def get_absolute_url(self): 
        return reverse('activity-detail', kwargs={'pk': self.pk})
    
class Child(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    parent = models.ManyToManyField(Profile)
    activities = models.ManyToManyField(Activities)
# list of their acvities

    def __str__(self):
        return self.first_name + " " + self.last_name


