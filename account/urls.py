from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import models
import account
from .views import AccountViewSet, MyAccountListView, CreateAccountView


app_name = account

router = DefaultRouter()
router.register('accounts/', AccountViewSet)



urlpatterns = [
    
    path('myaccount/', MyAccountListView.as_view(), name='myaccount'),         #GET
    path('create/', CreateAccountView.as_view(), name='create'),                        #POST
    path('', include(router.urls))
    
]







