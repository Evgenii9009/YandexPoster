from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        null=True,
        blank=True
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True,
    )
    long_description = HTMLField(
        verbose_name='Длинное описание',
        blank=True,
    )
    longitude = models.FloatField(
        verbose_name='долгота',
        null=True
    )
    latitude = models.FloatField(
        verbose_name='широта',
        null=True
    )

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.title
    

class Image(models.Model):

    image = models.ImageField(
        verbose_name='Фото события',
        null=True, blank=True
    )
    number = models.IntegerField(
        verbose_name='Номер фото',
        null=True
    )
    event_name = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Событие"
    )

    @property
    def get_absolute_image_url(self):
        return "{0}".format(self.image.url)

    class Meta:
        verbose_name = 'Фото события'
        verbose_name_plural = 'Фото событий'
        ordering = ('number',)