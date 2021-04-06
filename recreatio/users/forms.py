from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Child, Organization, Activities, Event, EventMember
import datetime
from django.forms.widgets import NumberInput, TimeInput
from django.contrib.admin import widgets
from .MultiWidget import MinimalSplitDateTimeMultiWidget

from django.forms import ModelForm, DateInput
#not the sample brings in event member too... might have to look at changing the model

AGE_RANGE= [tuple([x,x]) for x in range(0,20)]
GROUP_RANGE= [tuple([x,x]) for x in range(0,100)]

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
        fields = ['first_name', 'last_name','birth_date','parent', 'activities']
        widgets = {'birth_date': forms.NumberInput(attrs={'type':'date'})}

class UpdateChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name','birth_date','parent', 'activities']
        widgets = {'birth_date': forms.NumberInput(attrs={'type':'date'})}

class AddOrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'city', 'leaders'] 
    
class ManageOrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'city', 'leaders'] 

class OrgAddActivites(forms.ModelForm):
    class Meta:
        model = Activities

        fields = ['start_date', 'end_date', 'age_group_young', 'age_group_old', 'reg_start','reg_end', 'max_size','description'] 
        widgets = {
            'age_group_young': forms.Select(choices=AGE_RANGE),
            'age_group_old': forms.Select(choices=AGE_RANGE),
            'max_size': forms.Select(choices=GROUP_RANGE),
            'start_date': forms.NumberInput(attrs={'type':'date'}),
            'end_date': forms.NumberInput(attrs={'type':'date'}),
            'reg_start': forms.NumberInput(attrs={'type':'date'}),
            'reg_end': forms.NumberInput(attrs={'type':'date'}),
        }
        labels = {
            'start_date': "Activity starting date", 
            'end_date': "Activity ending date",
            'age_group_young': "Younges age eligible for activity",
            'age_group_old': 'Oldest age eligible for activity',
            'reg_start': "Registration starting date",
            'reg_end': "Registration closing date", 
            'max_size': "Maximum number of registrants in the activity"
        }

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['participant']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class SignupForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class AddMemberForm(forms.ModelForm):
  class Meta:
    model = EventMember
    fields = ['participant']