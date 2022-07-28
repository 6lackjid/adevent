from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields =  ('id', 'username', 'email', 'last_name', 'first_name', 'password', 'zip_code', 'address1', 'address2', 'address3', 'phone_number', 'user_icon', 'self_introduction')
        extra_kwargs = {'username': {'read_only': True}}


#'__all__'

# 













