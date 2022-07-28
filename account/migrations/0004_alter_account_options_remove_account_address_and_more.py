# Generated by Django 4.0.6 on 2022-07-28 06:42

import account.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_first_name_account_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'アカウント', 'verbose_name_plural': 'アカウント'},
        ),
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.AddField(
            model_name='account',
            name='address1',
            field=models.CharField(blank=True, max_length=40, verbose_name='都道府県'),
        ),
        migrations.AddField(
            model_name='account',
            name='address2',
            field=models.CharField(blank=True, max_length=40, verbose_name='市区町村番地'),
        ),
        migrations.AddField(
            model_name='account',
            name='address3',
            field=models.CharField(blank=True, max_length=40, verbose_name='建物名'),
        ),
        migrations.AddField(
            model_name='account',
            name='self_introduction',
            field=models.TextField(blank=True, max_length=300, verbose_name='自己紹介'),
        ),
        migrations.AddField(
            model_name='account',
            name='zip_code',
            field=models.CharField(blank=True, max_length=8, verbose_name='郵便番号'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(verbose_name='アカウント作成日'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=10, verbose_name='名'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, verbose_name='最終ログイン日'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=10, verbose_name='姓'),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_icon',
            field=models.ImageField(blank=True, null=True, upload_to=account.models.upload_icon_path, verbose_name='アイコン'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator('^[a-zA-Z0-9]*$')], verbose_name='ユーザー名'),
        ),
    ]