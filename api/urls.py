from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CreateUserView
from account.views import AccountViewSet, MyAccountListView, CreateAccountView
from api.views import UserDetail,CreateUserView
from events.views import EventViewSet

# app_name='api'

# router = DefaultRouter()
# router.register('accounts', AccountViewSet)


urlpatterns = [
    path('', CreateUserView.as_view(), name='users'),
    path('<id>/', UserDetail.as_view(), name='userdetail'),
    
    # path('', include(router.urls)),
    
    
]
