"""recreatio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from users.views import ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proj/', include('website.urls')),
    path("sample_search/",user_views.sample_search, name="sample_search"),
    path('', include('web.urls')),
    path("register/", user_views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path("profile/", user_views.profile, name="profile"), 
    path("profile_update/", user_views.profile_update, name="profile_update"),    
    path("add_children/",user_views.add_children, name="add_children"),
    path("add_organization/",user_views.add_organization, name="add_organization"),
    path("my_organizations/",user_views.my_organizations, name="my_organizations"),
    path("my_organizations/manage_organization/<int:id>",user_views.manage_organization, name="manage_organization"),
    path("my_organizations/org_add_activities/<int:id>",user_views.org_add_activities, name="org_add_activities"),
    path("my_organizations/org_view_activities/<int:id>",user_views.org_view_activities, name="org_view_activities"),
    path("profile/update_children/<int:id>/",user_views.update_children, name="update_children"),

    path('', ActivityListView.as_view(), name='web-home'),
    path('activity/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('activity/new/', ActivityCreateView.as_view(), name='activity-create'),
    path('activity/<int:pk>/update/', ActivityUpdateView.as_view(), name='activity-update'),
    path('activity/<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),

    ]
