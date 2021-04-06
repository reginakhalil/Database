from django.contrib import admin

from .models import Profile, Child, Organization, Activities, Event, EventMember

admin.site.register(Profile)
admin.site.register(Child)
admin.site.register(Organization)
admin.site.register(Activities)

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'participant']

admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)