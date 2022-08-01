from distutils.command import upload
from tabnanny import verbose
from django.db import models
import uuid

from django.core.validators import MinLengthValidator, RegexValidator


def upload_icon_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['icons', str(instance.user_icon)+str(instance.username)+str(".")+str(ext)])



class Account(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(verbose_name='ユーザー名', max_length=20, unique=True, validators=[MinLengthValidator(5,), RegexValidator(r'^[a-zA-Z0-9]*$',)], )
    email = models.EmailField(verbose_name='メールアドレス', max_length=50, unique=True)
    
    last_name = models.CharField(max_length=10, verbose_name='姓')
    first_name = models.CharField(max_length=10, verbose_name='名')
    password = models.CharField(max_length=60, verbose_name='パスワード')
    zip_code = models.CharField(
        verbose_name='郵便番号',max_length=8,blank=True,
    )
    address1 = models.CharField(
        verbose_name='都道府県',max_length=40,blank=True,
    )
    address2 = models.CharField(
        verbose_name='市区町村番地',max_length=40,blank=True,
    )
    address3 = models.CharField(
        verbose_name='建物名',max_length=40,blank=True,
    )
    
    phone_number = models.IntegerField(verbose_name='電話番号')
    user_icon = models.ImageField(blank=True, null=True, upload_to=upload_icon_path, verbose_name='アイコン')
    # self_introduction = models.TextField(blank=True, max_length=300, verbose_name='自己紹介')
    
    
    # date_joined = models.DateTimeField(verbose_name='アカウント作成日')
    # last_login =models.DateTimeField(auto_now_add=True, verbose_name='最終ログイン日')
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    # is_superadmin = models.BooleanField(default=False)
    # is_anonymous = models.BooleanField(default=False)
    # is_authenticated = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'アカウント'
        verbose_name_plural = 'アカウント'
    
    def __str__(self):
        return str(self.id) + '  |  ' + self.last_name + self.first_name
    


















