from django.contrib import admin
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'time', 'confirmed', 'key']

admin.site.register(Participant, ParticipantAdmin)
