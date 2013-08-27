from django.contrib import admin
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'contact', 'time', 'birthday', 'age', 'participant_media', 'confirmed', ]

    def has_add_permission(self, request):
    	return False

    class Media:
    	css = { 'all': ('participant-signup/styles/lightbox-admin.css',) }
    	js = [ 'participant-signup/scripts/lightbox-admin.js', ]

admin.site.register(Participant, ParticipantAdmin)
