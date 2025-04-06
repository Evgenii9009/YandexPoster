from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableStackedInline
from catalog.models import Event, Image
from django.utils.html import format_html


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('event_name', 'event_image', 'number')
    readonly_fields = ['event_image']
    def event_image(self, obj):
        image_height=obj.image.height if obj.image.height<=200 else 200
        image_width = obj.image.width if obj.image.height<200 else obj.image.width*200/obj.image.height
        return format_html('<img src="{url}" width="{width}" height={height} />',
            url = obj.image.url,
            width=image_width,
            height=image_height
            )


class ImageStackedInline(SortableStackedInline):
    model = Image
    


@admin.register(Event)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'longitude', 'latitude', 'id')
    inlines = [ImageStackedInline]


