# Generated by Django 4.0.6 on 2022-07-27 01:39

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator('^[a-zA-Z0-9]*$')], verbose_name='username')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=60, verbose_name='パスワード')),
                ('address', models.CharField(max_length=100, verbose_name='住所')),
                ('phone_number', models.IntegerField(verbose_name='電話番号')),
                ('date_joined', models.DateTimeField()),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('is_authenticated', models.BooleanField(default=True)),
            ],
        ),
    ]
