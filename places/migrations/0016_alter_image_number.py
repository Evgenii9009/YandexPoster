# Generated by Django 4.2 on 2025-04-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_alter_image_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Номер фото'),
        ),
    ]
