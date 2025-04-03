from django.contrib import admin
from catalog.models import Event, Image

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'longitude', 'latitude')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'number')
