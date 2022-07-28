
from django.db import models

from api.models import User
import uuid

from datetime import datetime

class Event(models.Model):
    
    
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    jenre = models.CharField(max_length=50,verbose_name = 'ジャンル')
    title = models.CharField(max_length=100,verbose_name = 'タイトル')
    
    time = models.DateTimeField(default=datetime.now,verbose_name = '日時')
    location = models.CharField(max_length=150,verbose_name = '開催場所')
    over_view = models.TextField(max_length=1000, verbose_name = 'イベント概要')
    
    
    class Meta:
        verbose_name = 'イベント'
        verbose_name_plural = 'イベント'
        
    def __str__(self):
        return self.title  + ' | ' + str(self.time)
    


