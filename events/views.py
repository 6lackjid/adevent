from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Event
from rest_framework import viewsets
from .custompermissions import IsHostOrReadOnly

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    serializer_class = serializers.EventSerializer
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = (IsHostOrReadOnly,)
    serializer_class = serializers.EventSerializer
    
    lookup_field = 'id'       

# class MyEventListView(generics.ListAPIView):
#     queryset = Event.objects.all()
#     serializer_class = serializers.EventSerializer
    
#     def get_queryset(self):
#         return self.queryset.filter(user_id=self.request.user)
        
        
class CreateEventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer  
    
    
    def perform_create(self, serializer):
        serializer.save()
        
        
