from tinymce.models import HTMLField


from django.db import models


class Event(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    short_description = models.TextField(
        verbose_name="Краткое описание",
        blank=True,
    )
    long_description = HTMLField(
        verbose_name="Длинное описание",
        blank=True,
    )
    longitude = models.FloatField(
        verbose_name="долгота",
    )
    latitude = models.FloatField(
        verbose_name="широта",
    )

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.title


class Image(models.Model):

    image = models.ImageField(
        verbose_name="Фото события",
    )
    number = models.IntegerField(
        verbose_name="Номер фото",
        null=True,
        db_index=True, blank=True
    )
    event_name = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name="Событие", related_name="images"
    )

    class Meta:
        verbose_name = "Фото события"
        verbose_name_plural = "Фото событий"
        ordering = ("number",)

    @property
    def get_absolute_image_url(self):
        return "{0}".format(self.image.url)
