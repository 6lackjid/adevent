from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings






urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('api/', include('events.urls')),
    path('api-auth/', include('rest_framework.urls')),#'api'
    # path('events/', include('events.urls')),            #, 'events'
    path('api/users/', include('api.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api/rest-auth/', include('rest_auth.urls')),
    # path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
