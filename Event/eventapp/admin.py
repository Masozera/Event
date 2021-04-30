from django.contrib import admin
from .models import Speaker, Participant

# Register your models here.

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','Attendance', 'Nationality','Phone_number',]
    # list_filter = ['available', 'created', 'updated']
    
