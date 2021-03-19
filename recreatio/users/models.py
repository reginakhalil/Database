from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.user.first_name +' ' + self.user.last_name


class Activities(models.Model):
    activities = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    age_group_young = models.IntegerField() #flag year of birth
    age_group_old = models.IntegerField() #flag year of birth
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.activities


class Child(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    parent = models.ManyToManyField(Profile)
#    parent = models.ManyToManyField(User)
    activity_list = models.ManyToManyField(Activities)
# list of their acvities

    def __str__(self):
        return self.first_name + " " + self.last_name

class Organization(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    activities = models.ManyToManyField(Activities)

    def __str__(self):
        return self.name