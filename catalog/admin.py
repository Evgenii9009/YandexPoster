from django.contrib import admin
from catalog.models import Event, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'longitude', 'latitude', 'id')
    inlines = [
        ImageInline,
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'number')


