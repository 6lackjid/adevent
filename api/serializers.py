
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password 
from djoser.serializers import UserSerializer


class UserSerializer(serializers.ModelSerializer):
    # serializers.ModelSerializer
    # class Meta:
    #     model = get_user_model()
    #     fields = ('id', 'email', 'password')
    #     # extra_kwargs = {'password': {'write_only': True}}
        
    # def create(self, validated_data):
    #     user = get_user_model().objects.create_user(**validated_data)
        
    #     return user
    
    class Meta:
        model = User
        fields = '__all__'

# 追加
    def validate_password(self,value:str) ->str:
        """
        ハッシュ値に変換する
        """
        return make_password(value)
    
