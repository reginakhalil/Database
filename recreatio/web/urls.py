from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('about/', views.about, name='web-about'),
    path('login/', views.login, name='web-login'),
    
    ]