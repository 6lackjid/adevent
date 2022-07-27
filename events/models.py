
from django.db import models

from api.models import User
from jenre.models import Jenre

from datetime import datetime

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    jenre_id = models.ForeignKey(Jenre, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    
    time = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=150)
    over_view = models.TextField(max_length=1000)
    
    
    class Meta:
        verbose_name = 'イベント'
        verbose_name_plural = 'イベント'
        
    def __str__(self):
        return self.title  + ' | ' + str(self.time)
    
    
