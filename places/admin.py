from django.contrib import admin
from django.utils.html import format_html


from adminsortable2.admin import SortableAdminBase, SortableStackedInline


from places.models import Event, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ("event_name", "number")
    raw_id_fields = ["event_name"]


class ImageStackedInline(SortableStackedInline):
    model = Image
    readonly_fields = ("event_image", "event_name")
    def event_image(self, obj):
        return format_html(
            """<img style="max-width: 300px; max-height: 200px;"
            src="{url}"/>""",
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height
            )
    event_image.short_description = "Фото события"


@admin.register(Event)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("title", "longitude", "latitude", "id")
    inlines = [ImageStackedInline]
