# Generated by Django 4.2 on 2025-04-07 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_alter_image_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='event_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.event', verbose_name='Событие'),
        ),
    ]
