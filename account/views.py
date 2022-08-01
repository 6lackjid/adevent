
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Account
from rest_framework import viewsets


class CreateAccountView(generics.CreateAPIView):
    serializer_class = serializers.AccountSerializer
    permission_classes = (AllowAny,)
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

class MyAccountListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer
    
    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
