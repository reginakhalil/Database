from django.shortcuts import render


def home(request):
    return render(request, 'web/home.html')

def about(request):
    return render(request, 'web/about.html')

def login(request):
    return render(request, 'web/login.html')

