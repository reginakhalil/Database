from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('page1/', views.page1, name='website-page1')
]