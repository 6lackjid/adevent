# Generated by Django 4.0.6 on 2022-07-28 21:37

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=150, verbose_name='開催場所'),
        ),
        migrations.AlterField(
            model_name='event',
            name='over_view',
            field=models.TextField(max_length=1000, verbose_name='イベント概要'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='日時'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
    ]
