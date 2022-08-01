from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from . import serializers
from .models import User
from rest_framework import viewsets


class CreateUserView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes = (AllowAny,)
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
    