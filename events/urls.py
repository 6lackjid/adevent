from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, MyEventListView



app_name = 'events'

router = DefaultRouter()
router.register('event/', EventViewSet)


urlpatterns = [
    path('event/', MyEventListView.as_view(), name='event'),
    path('events/', include(router.urls))
    
]
