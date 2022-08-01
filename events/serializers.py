from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format=" %Y年%m月%d日: %H時%M分 ")
    
    
    class Meta:
        model = Event
        fields = ('id', 'jenre', 'user_id','title', 'time', 'location', 'eventpics' , 'over_view')
        
        
        # extra_kwargs = {'id': {'read_only': True}}
        
#   

