# Generated by Django 4.0.6 on 2022-07-31 22:43

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_eventpics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventpics',
            field=models.ImageField(blank=True, null=True, upload_to=events.models.upload_eventpics_path, verbose_name='イベントイメージ'),
        ),
    ]
