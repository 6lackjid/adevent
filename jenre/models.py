from django.db import models
from django.forms import CharField

# Create your models here.
class Jenre(models.Model):
    id = models.IntegerField(primary_key=True)
    jenre = models.CharField(max_length=50, default='その他')
    
    
    class Meta:
        verbose_name = 'ジャンル'
        verbose_name_plural = 'ジャンル'
    
    
    def __str__(self):
        return self.jenre