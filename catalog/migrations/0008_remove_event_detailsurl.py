# Generated by Django 4.2 on 2025-04-04 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_event_detailsurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='detailsUrl',
        ),
    ]
