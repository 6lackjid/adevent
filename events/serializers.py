from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    
    
    class Meta:
        model = Event
        fields =  ('id', 'user_id', 'title', 'time', 'location', 'over_view')
        extra_kwargs = {'id': {'read_only': True}}
        
# '__all__'

