from email.headerregistry import Address

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.forms import BooleanField




class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email: 
            raise ValueError('メールアドレスを入力してください')
        
        
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
            
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = MyUserManager()
     
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email

    