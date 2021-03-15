from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #org = models.Choices()
    #child = models.CharField(max_length=40, null=True)
    #child = models.ManyToManyField(Child)
    def __str__ (self):
        #return f'{{ user.first_name }} Profile'
        return self.user.first_name +' ' + self.user.last_name

class Child(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    parent = models.ManyToManyField(Profile)

    def __str__(self):
        return self.first_name + " "+ self.last_name

class Activities(models.Model):
    activities = models.CharField(max_length=50)

    def __str__(self):
        return self.activities

class Organization(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    activities = models.ManyToManyField(Activities)

    def __str__(self):
        return self.name
