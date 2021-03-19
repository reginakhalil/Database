from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Child, Organization, Activities
import datetime

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 40)
    last_name = forms.CharField(max_length = 40)
   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1','password2']
   
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 40)
    last_name = forms.CharField(max_length = 40)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user']

class AddChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name','birth_date','parent']
        widgets = {'birth_date': forms.SelectDateWidget(years=range(2000,2021,1))} 

class AddOrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'city','activities'] 