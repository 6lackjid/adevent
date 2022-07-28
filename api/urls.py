from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CreateUserView
from account.views import AccountViewSet, MyAccountListView, CreateAccountView
from events.views import EventViewSet

app_name='api'

router = DefaultRouter()
router.register('accounts', AccountViewSet)
router.register('events', EventViewSet)

urlpatterns = [
    path('register/', CreateAccountView.as_view(), name='register'),
    path('myaccount/display', MyAccountListView.as_view(), name='myaccount'),
    path('', include(router.urls)),
    
    
]
