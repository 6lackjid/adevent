from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . import serializers
from .models import User
from rest_framework import viewsets


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)
    
    