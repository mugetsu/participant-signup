from django.contrib import admin
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'time', 'confirmed', 'key']

    def has_add_permission(self, request):
    	return False

admin.site.register(Participant, ParticipantAdmin)
