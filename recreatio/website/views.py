from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def page1(request):
    return render(request, 'website/page1.html')

