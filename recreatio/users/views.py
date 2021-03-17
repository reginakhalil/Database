from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
        #'profile_form': profile_form
    }

    return render(request, 'users/profile.html',context)