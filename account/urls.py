from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import models
import account
from .views import AccountViewSet, MyAccountListView, CreateAccountView
from rest_framework import routers



router = routers.DefaultRouter()
# router.register('accounts', AccountViewSet)



urlpatterns = [
    path('register/', CreateAccountView.as_view(), name='register'),
    path('myaccount/', MyAccountListView.as_view(), name='myaccount'),         #GET
    path('create/', CreateAccountView.as_view(), name='create'),               #POST
    
    
]







