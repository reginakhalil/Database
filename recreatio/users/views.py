from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AddChildForm, AddOrgForm, UpdateChildForm, ManageOrgForm, OrgAddActivites, EventForm, AddMemberForm
from .models import Child, Profile, Organization, Activities, Event, EventMember
from .tables import ActivityTable
from django_tables2 import RequestConfig
from .filters import ActivityFilter, ActivityFilterGeneric
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from datetime import datetime, date
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .utils import Calendar

def home(request): 
    context = {
        'activities': Activities.objects.all()
    }
    return render(request, 'web/home.html', context)


class ActivityListView(ListView): 
    model = Activities
    template_name = 'web/home.html' 
    context_object_name = 'activities'
    ordering = ['-date_posted'] #orders posts from newest to oldest

class ActivityDetailView(DetailView): 
    model = Activities

class ActivityCreateView(LoginRequiredMixin, CreateView): 
    model = Activities
    fields = ['title', 'organization', 'description', 'start_date', 'end_date', 'age_group_young', 'age_group_old', 'reg_start', 'reg_end', 'max_size']


    def form_valid(self, form): 
        form.instance.author = self.request.user #set the author of the post to the user currently logged in 
        return super().form_valid(form)


class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Activities
    fields = ['title', 'organization', 'description', 'start_date', 'end_date', 'age_group_young', 'age_group_old', 'reg_start', 'reg_end', 'max_size']

    def form_valid(self, form): 
        form.instance.author = self.request.user #set the author of the post to the user currently logged in 
        return super().form_valid(form)

    #this function is to make sure that only the author of a post is able to make updates 
    def test_func(self): 
        activity = self.get_object()
        #check if the user currenlty logged in is the author of the post
        return self.request.user == activity.author

#delete a post 
class ActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Activities
    success_url = '/'
   #this function is to make sure that only the author of a post is able to make updates 
    def test_func(self): 
        activity = self.get_object()
        #check if the user currenlty logged in is the author of the post
        return self.request.user == activity.author

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():       
            form.save()
            #username = form.cleaned_data.get("username")
            messages.success(request, f"Account created, please log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})

@login_required
def profile(request):

    parent = request.user   #extract the current user, can use this for multiple lookups

    parent_id = Profile.objects.get(user_id = parent.id)    #go to the profile objects and find ID
    parents = Child.objects.filter(parent__id = parent_id.id).order_by('first_name')   #use this ID to find my children
    
    org = Organization.objects.filter(leaders__id = parent_id.id).order_by('name')

    if request.method == "POST":
        update_form = UserUpdateForm(request.POST, instance=request.user)
    if request.method == "POST":
        profile_update_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_update_form.is_valid():# and profile_form.is_valid():
            profile_update_form.save()
            messages.success(request, f"Account updated")
            return redirect('profile')
    else:
        profile_update_form = UserUpdateForm(instance=request.user)
    context = {
        'profile_update_form': profile_update_form,
        'parents': parents,
        'org': org
    }

    return render(request, 'users/profile.html',context)

def profile_update(request):
    if request.method == "POST":
        profile_update_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_update_form.is_valid():# and profile_form.is_valid():
            profile_update_form.save()
            messages.success(request, f"Account updated")
            return redirect('profile')
    else:
        profile_update_form = UserUpdateForm(instance=request.user)
    context = {
        'profile_update_form': profile_update_form,
    }

    return render(request, 'users/profile_update.html',context)

def add_children(request):
    if request.method == "POST":
        add_children_form = AddChildForm(request.POST)
        if add_children_form.is_valid():# and profile_form.is_valid():
            new_child = add_children_form.save()
            messages.success(request, f"Account updated")
            return redirect('profile')
    else:
        add_children_form = AddChildForm()
    
    context = {
        'add_children_form': add_children_form,
    }

    return render(request, 'users/add_children.html',context)

def update_children(request, id):
    #capture the current child object
    obj = Child.objects.get(id=id)

    if request.method == "POST":
        update_children_form = UpdateChildForm(request.POST, instance = obj)
        if update_children_form.is_valid():# and profile_form.is_valid():
            new_child = update_children_form.save()
            messages.success(request, f"Child account updated")
            return redirect('profile')
    else:
        update_children_form = UpdateChildForm(instance = obj)

    context = {
        'update_children_form': update_children_form,
    }

    return render(request, 'users/update_children.html',context)

def my_organizations(request):
    profile = request.user   #extract the current user, can use this for multiple lookups
    profile_id = Profile.objects.get(user_id = profile.id)    #go to the profile objects and find ID
    org = Organization.objects.filter(leaders__id = profile_id.id).order_by('name')

    context = {
        'org': org
    }

    return render(request, 'users/my_organizations.html', context)


def add_organization(request):
    if request.method == "POST":
        add_org_form = AddOrgForm(request.POST)
        if add_org_form.is_valid():# and profile_form.is_valid():
            new_child = add_org_form.save()
            messages.success(request, f"Organization Added")
            return redirect('my_organizations')
    else:
        add_org_form = AddOrgForm()
    
    context = {
        'add_org_form': add_org_form,
    }

    return render(request, 'users/add_organization.html',context)

def manage_organization(request, id):
    obj = Organization.objects.get(id=id)

    if request.method == "POST":
        manage_org_form = ManageOrgForm(request.POST, instance = obj)
        if manage_org_form.is_valid():# and profile_form.is_valid():
            new_child = manage_org_form.save()
            messages.success(request, f"Organization Updated")
            return redirect('my_organizations')
    else:
        manage_org_form = ManageOrgForm(instance = obj)
    
    context = {
        'manage_org_form': manage_org_form,
        'obj': obj
    }

    return render(request, 'users/manage_organization.html',context)

def org_add_activities(request, id):
    obj = Organization.objects.get(id=id)

    if request.method == "POST":
        org_add_activities = OrgAddActivites(request.POST,instance = obj)
        if org_add_activities.is_valid():
            print("adding activity")
            org_add_activities.save()
            messages.success(request, f"Activity Added")
            return redirect('my_organizations')
    else:
        org_add_activities = OrgAddActivites(instance = obj)

    context = {
        'org_add_activities': org_add_activities,
        'obj': obj
    }

    return render(request, 'users/org_add_activities.html',context)

def org_view_activities(request, id):
    obj = Organization.objects.get(id=id)
    
    activities = Activities.objects.filter(organization__id = id)
    activities = activities.order_by("start_date")

    myFilter = ActivityFilter(request.GET, queryset=activities)
    activities = myFilter.qs

    table = ActivityTable(activities)
    table.columns["age_group_young"].header 
    'Young'
    RequestConfig(request).configure(table)

    

    context = {
        'obj': obj,
        'activities': activities,
        'table': table,
        'myFilter': myFilter,
    }

    return render(request, 'users/org_view_activities.html',context)

def sample_search(request):
    
    activities = Activities.objects.all()
    activities = activities.order_by("start_date")

    myFilter = ActivityFilterGeneric(request.GET, queryset=activities)
    activities = myFilter.qs

    table = ActivityTable(activities)
    RequestConfig(request).configure(table)

    context = {
        'activities': activities,
        'table': table,
        'myFilter': myFilter,
    }

    return render(request, 'users/sample_search.html',context)

def enrolled_children(request, pk):
    children = Child.objects.filter(activities__id = pk)
    children = children.order_by("first_name")

    context = {
        'children': children
    }

    return render(request, 'users/activities_detail_registered.html', context)

def parent_info(request, id):
    profile = Profile.objects.get(child__id = id)
    parent = Profile.objects.get(user__id = profile.user_id)
    user = User.objects.get(id = parent.user_id)

    children = Child.objects.filter(parent__id = parent.id).order_by('first_name')
    
    context = {
        'parent': user,
        'children': children
    }

    return render(request, 'users/parent_info.html', context)


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'signup'
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

@login_required(login_url='signup')
def create_event(request):    
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time
        )
        return HttpResponseRedirect(reverse('calendarapp:calendar'))
    return render(request, 'event.html', {'form': form})

class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'event.html'

@login_required(login_url='signup')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
        'eventmember': eventmember
    }
    return render(request, 'event-details.html', context)


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == 'POST':
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                user = forms.cleaned_data['user']
                EventMember.objects.create(
                    event=event,
                    user=user
                )
                return redirect('calendarapp:calendar')
            else:
                print('--------------User limit exceed!-----------------')
    context = {
        'form': forms
    }
    return render(request, 'add_member.html', context)

class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = 'event_delete.html'
    success_url = reverse_lazy('calendarapp:calendar')