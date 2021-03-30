from django.shortcuts import render



def about(request):
    return render(request, 'web/about.html', {'title': 'About'})

def login(request):
    return render(request, 'web/login.html', {'title': 'Login'})

