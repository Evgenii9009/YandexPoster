# Generated by Django 4.2 on 2025-04-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_event_image_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
