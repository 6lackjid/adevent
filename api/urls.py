from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CreateUserView
from account.views import AccountViewSet, MyAccountListView


app_name='api'

router = DefaultRouter()
router.register('accounts_list', AccountViewSet)

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('myaccount/', MyAccountListView.as_view(), name='myaccount'),
    path('', include(router.urls)),
    
    
]
