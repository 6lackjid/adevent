from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CreateEventView, EventDetailView



app_name = 'events'

router = DefaultRouter()
router.register('events', EventViewSet)  #ホーム画面でイベントの一覧取得


urlpatterns = [
    
    path('create/', CreateEventView.as_view(), name='create'),
    path('<id>/', EventDetailView.as_view(), name='detail'),
    path('', include(router.urls))
    
]
