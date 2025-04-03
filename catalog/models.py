from django.db import models


class Event(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото события',
        null=True, blank=True
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True,
    )
    long_description = models.TextField(
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