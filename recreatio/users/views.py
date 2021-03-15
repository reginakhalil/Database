from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AddChildForm, AddOrgForm
from .models import Child, Profile, Organization

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

    parent_id = request.user.id
    parents = Child.objects.filter(parent__id = parent_id)
    

    if request.method == "POST":
        update_form = UserUpdateForm(request.POST, instance=request.user)
        #profile_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if update_form.is_valid():# and profile_form.is_valid():
            update_form.save()
        #    profile_form.save()
            messages.success(request, f"Account updated")
            return redirect('profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        #profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'update_form': update_form,
        'parents': parents
        #'profile_form': profile_form
    }

    return render(request, 'users/profile.html',context)


def profile_update(request):
    if request.method == "POST":
        profile_update_form = UserUpdateForm(request.POST, instance=request.user)
        #profile_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if profile_update_form.is_valid():# and profile_form.is_valid():
            profile_update_form.save()
        #    profile_form.save()
            messages.success(request, f"Account updated")
            return redirect('profile')
    else:
        profile_update_form = UserUpdateForm(instance=request.user)
        #profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'profile_update_form': profile_update_form,
        #'profile_form': profile_form
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

def add_organization(request):
    if request.method == "POST":
        add_org_form = AddOrgForm(request.POST)
        if add_org_form.is_valid():# and profile_form.is_valid():
            new_child = add_org_form.save()
            messages.success(request, f"Account updated")
            return redirect('profile')
    else:
        add_org_form = AddOrgForm()
    
    context = {
        'add_org_form': add_org_form,
    }

    return render(request, 'users/add_organization.html',context)