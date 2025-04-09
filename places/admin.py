from django.contrib import admin
from django.utils.html import format_html


from adminsortable2.admin import SortableAdminBase, SortableStackedInline


from places.models import Event, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ("event_name", "event_image", "number")
    readonly_fields = ["event_image"]
    raw_id_fields = ["event_name"]

    def event_image(self, obj):
        return format_html('<img style="max-width: 300px; max-height: 200px;" src="{url}" width="{width}" height={height} />',
                           url=obj.image.url,
                           width=obj.image.width,
                           height=obj.image.height)


class ImageStackedInline(SortableStackedInline):
    model = Image


@admin.register(Event)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("title", "longitude", "latitude", "id")
    inlines = [ImageStackedInline]
