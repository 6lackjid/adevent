# Generated by Django 4.0.6 on 2022-07-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jenre', '0002_alter_jenre_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jenre',
            name='jenre',
            field=models.CharField(default='その他', max_length=50),
        ),
    ]
