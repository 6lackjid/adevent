# Generated by Django 4.0.6 on 2022-07-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='メールアドレス'),
        ),
    ]
