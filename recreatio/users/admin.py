from django.contrib import admin

from .models import Profile, Child, Organization, Activities

admin.site.register(Profile)
admin.site.register(Child)
admin.site.register(Organization)
admin.site.register(Activities)
