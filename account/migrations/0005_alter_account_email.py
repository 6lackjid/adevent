# Generated by Django 4.0.6 on 2022-07-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_options_remove_account_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='メールアドレス'),
        ),
    ]
