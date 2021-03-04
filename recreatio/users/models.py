from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #org = models.Choices()
    #child = models.CharField(max_length=40, null=True)
    
    def __str__ (self):
        return f'{{ user.first_name }} Profile'

'''
class Child(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
'''