from django.contrib import admin
from catalog.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'longitude', 'latitude')
