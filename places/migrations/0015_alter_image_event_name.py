# Generated by Django 4.2 on 2025-04-07 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_alter_image_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='event_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.event', verbose_name='Событие'),
        ),
    ]
