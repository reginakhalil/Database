from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 40)
    last_name = forms.CharField(max_length = 40)
    organization = forms.ChoiceField(choices = [('0',"Parent"), ('1',"Grandparent"),('3',"Organization")],widget = forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1','password2']
        widgets = {'org'}



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

        